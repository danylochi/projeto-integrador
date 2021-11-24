#from typing import Optional
import os
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
import pandas
import mysql.connector
from fastapi.encoders import jsonable_encoder
import io
from fastapi.middleware.cors import CORSMiddleware

#cria conexão com o banco de dados mysql
conexion = mysql.connector.connect(user=os.environ.get('HRK_DB_USER', None), 
                              password=os.environ.get('HRK_DB_PASS', None),
                              host=os.environ.get('HRK_DB_HOST', None),
                              database=os.environ.get('HRK_DB_NAME', None))
#conexion.close()



app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/downloadfile/")
async def download_caed(recuperacao:str, ano: int, materia: str, turma: str, serie: int, bimestre: int, vazia: int = 0):
#prepara query de consulta 
    query_consulta=conexion.cursor()

    #cria string com comando de consulta 
    string_consulta= ("SELECT "
        " recuperacao_continuada AS `RECUPERACAO CONTINUADA`, "
        " ano AS `ano`, "
        " materia AS `materia`, "
        " turma AS `turma`, "
        " serie AS `serie`, "
        " bimestre AS `Bimestre`, "
        " estudante AS `ESTUDANTE`, "
        " participacao AS `PARTICIPAÇÃO`, "
        " numero_itens_respondidos AS `Nº DE ITENS RESPONDIDOS`, "
        " porcento_acertos AS `% ACERTOS`, "
        " categoria_desempenho AS `CATEGORIA DE DESEMPENHO`, "
        " tipo_intervencao AS `TIPO DE INTERVENÇÃO`, "
        " itens_acertados AS `ITENS ACERTADOS`, "
        " h_01, "
        " h_02, "
        " h_03, "
        " h_04, "
        " h_05, "
        " h_06, "
        " h_07, "
        " h_08, "
        " h_09, "
        " h_10, "
        " h_11, "
        " h_12, "
        " h_13, "
        " h_14, "
        " h_15, "
        " h_16, "
        " h_17, "
        " h_18, "
        " h_19, "
        " h_20, "
        " h_21, "
        " h_22, "
        " h_23, "
        " h_24, "
        " h_25, "
        " h_26, "
        " h_27, "
        " h_28, "
        " h_29, "
        " h_30 "    
        " FROM consulta_caed "
        " WHERE recuperacao_continuada = %(recuperacao)s"
        " AND ano = %(ano)s"
        " AND UPPER(materia) = UPPER(%(materia)s)"
        " AND UPPER(turma) = UPPER(%(turma)s)"
        " AND serie = %(serie)s"
        " AND bimestre = %(bimestre)s")

    if vazia == 1:
        string_consulta += " AND 1=2 "    

    #cria dados de aluno com o conteúdo da linha para consulta  
    data_consulta = {
        'recuperacao': recuperacao,
        'ano': ano, 'materia': materia, 'turma': turma, 'serie': serie, 'bimestre': bimestre
    }
        
    #executa a consulta   
    query_consulta.execute(string_consulta, data_consulta)

    #força carregar todos os dados da consulta, ignora modo lazy            
    results= query_consulta.fetchall()

    #------------------BUSCAR CÓDIGO DA HABILIDADE-----------------------------------#
    query_habilidade=conexion.cursor()

    #cria string com comando de consulta 
    string_habilidade= ("SELECT * FROM habilidade_caed "
        " WHERE ano = %(ano)s"
        " AND UPPER(materia) = UPPER(%(materia)s)"
        " AND UPPER(turma) = UPPER(%(turma)s)"
        " AND serie = %(serie)s"
        " AND bimestre = %(bimestre)s")

    #cria dados de aluno com o conteúdo da linha para consulta  
    data_habilidade = {
        'ano': ano, 'materia': materia, 'turma': turma, 'serie': serie, 'bimestre': bimestre
    }
        
    #executa a consulta   
    query_habilidade.execute(string_habilidade, data_habilidade)

    #força carregar todos os dados da consulta, ignora modo lazy            
    results_habilidade= query_habilidade.fetchall()
    #-----------------------------------------------------#

    #extrai cabeçalho da linha
    row_headers=[x[0] for x in query_consulta.description]

    for i in range(len(row_headers)):
        for row in results_habilidade:
            if (row[6] == row_headers[i] and row[7] != None):
                row_headers[i] = row[7]
            else:
                row_headers[i] = row_headers[i].upper().replace("_", " ")

    data_frame = pandas.DataFrame(results, columns = row_headers)

    output = io.BytesIO()
    writer = pandas.ExcelWriter(output, engine = 'xlsxwriter')

    data_frame.to_excel(writer, index=False, sheet_name='Sheet1')

    # Auto-adjust columns' width
    for column in data_frame:
        column_width = max(data_frame[column].astype(str).map(len).max(), len(column))
        col_idx = data_frame.columns.get_loc(column)
        writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width+4)

    writer.close()

    #go back to the beginning of the stream
    output.seek(0)


    headers = {
        'Content-Disposition': 'attachment; filename="file.xlsx"'
    }
    return StreamingResponse(output, headers=headers,media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

   


@app.get("/consultacaed/")
def consulta_caed(recuperacao:str, ano: int, materia: str, turma: str, serie: int, bimestre: int):
    #prepara query de consulta 
    query_consulta=conexion.cursor()

    #cria string com comando de consulta 
    string_consulta= ("SELECT * FROM consulta_caed "
        " WHERE recuperacao_continuada = %(recuperacao)s"
        " AND ano = %(ano)s"
        " AND UPPER(materia) = UPPER(%(materia)s)"
        " AND UPPER(turma) = UPPER(%(turma)s)"
        " AND serie = %(serie)s"
        " AND bimestre = %(bimestre)s")

    #cria dados de aluno com o conteúdo da linha para consulta  
    data_consulta = {
        'recuperacao': recuperacao,
        'ano': ano, 'materia': materia, 'turma': turma, 'serie': serie, 'bimestre': bimestre
    }

        
    #executa a consulta   
    query_consulta.execute(string_consulta, data_consulta)

    #força carregar todos os dados da consulta, ignora modo lazy            
    results= query_consulta.fetchall()

    #------------------BUSCAR CÓDIGO DA HABILIDADE-----------------------------------#
    query_habilidade=conexion.cursor()

    #cria string com comando de consulta 
    string_habilidade= ("SELECT * FROM habilidade_caed "
        " WHERE ano = %(ano)s"
        " AND UPPER(materia) = UPPER(%(materia)s)"
        " AND UPPER(turma) = UPPER(%(turma)s)"
        " AND serie = %(serie)s"
        " AND bimestre = %(bimestre)s")

    #cria dados de aluno com o conteúdo da linha para consulta  
    data_habilidade = {
        'ano': ano, 'materia': materia, 'turma': turma, 'serie': serie, 'bimestre': bimestre
    }
        
    #executa a consulta   
    query_habilidade.execute(string_habilidade, data_habilidade)

    #força carregar todos os dados da consulta, ignora modo lazy            
    results_habilidade= query_habilidade.fetchall()
    #-----------------------------------------------------#
    #extrai cabeçalho da linha
    row_headers = [x[0] for x in query_consulta.description]
    
    row_header_table = [x for x in row_headers if x.find("h_") > -1]
    
    for i in range(len(row_header_table)):
        alterou = False
        for row in results_habilidade:
            if (row[6] == row_header_table[i] and row[7] != None):
                row_header_table[i] = row[7]
                alterou = True
        
        if (not(alterou)):
            row_header_table[i] = row_header_table[i].upper().replace("_"," ")

    #inicializa a array de json
    json_array=[]


    #percorre dados da query de consulta e insere no json
    for row in results:
        json_array.append(dict(zip(row_headers,row)))

    json_data = {'dataCaed':json_array, 'table_header': row_header_table}   
    
    #converte para json
    json_compatible_item_data = jsonable_encoder(json_data)

    return json_compatible_item_data
#-----------------------------------------------------------------------------------------
@app.get("/habilidadecaed/")
def habilidade_caed(ano: int, materia: str, turma: str, serie: int, bimestre: int):
    #prepara query de consulta 
    query_consulta=conexion.cursor()

    #cria string com comando de consulta 
    string_consulta= ("SELECT * FROM habilidade_caed "
        " WHERE ano = %(ano)s"
        " AND UPPER(materia) = UPPER(%(materia)s)"
        " AND UPPER(turma) = UPPER(%(turma)s)"
        " AND serie = %(serie)s"
        " AND bimestre = %(bimestre)s")

    #cria dados de aluno com o conteúdo da linha para consulta  
    data_consulta = {
        'ano': ano, 'materia': materia, 'turma': turma, 'serie': serie, 'bimestre': bimestre
    }
        
    #executa a consulta   
    query_consulta.execute(string_consulta, data_consulta)

    #força carregar todos os dados da consulta, ignora modo lazy            
    results= query_consulta.fetchall()

    #extrai cabeçalho da linha
    row_headers=[x[0] for x in query_consulta.description]

    #inicializa a array de json
    json_data=[]

    #percorre dados da query de consulta e insere no json
    for row in results:
        json_data.append(dict(zip(row_headers,row)))
    
    #converte para json
    json_compatible_item_data = jsonable_encoder(json_data)

    return json_compatible_item_data
#-------------------------------------------------------------------------------------------------
@app.put("/habilidadecaed/{id}")
def atualizar_habilidade(id: int, cod_da_habilidade: str):

    #prepara query de consulta 
    query_update=conexion.cursor()

    #cria string com comando de consulta 
    string_update= ("UPDATE habilidade_caed "
        " SET cod_da_habilidade = %(cod_da_habilidade)s"
        " WHERE id = %(id)s")
       
    #cria dados de aluno com o conteúdo da linha para consulta  
    data_update = {
        'cod_da_habilidade': cod_da_habilidade, 'id': id
    }
        
    #executa a consulta   
    query_update.execute(string_update, data_update)

    #força carregar todos os dados da consulta, ignora modo lazy            
    query_update.fetchall()

    #prepara query de consulta 
    query_consulta=conexion.cursor()

    #cria string com comando de consulta 
    string_consulta= ("SELECT * FROM habilidade_caed "
        " WHERE id = %(id)s"
    )

    #cria dados de aluno com o conteúdo da linha para consulta  
    data_consulta = {
        'id': id
    }
        
    #executa a consulta   
    query_consulta.execute(string_consulta, data_consulta)

    #força carregar todos os dados da consulta, ignora modo lazy            
    result= query_consulta.fetchone()

    #extrai cabeçalho da linha
    row_headers=[x[0] for x in query_consulta.description]

    #inicializa a array de json
    json_data=dict(zip(row_headers,result))

    #percorre dados da query de consulta e insere no json
    
    #json_data.append(dict(zip(row_headers,result)))
    
    #converte para json
    json_compatible_item_data = jsonable_encoder(json_data)

    conexion.commit()

    query_update.close()
    query_consulta.close()

    return json_compatible_item_data

#-------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
@app.post("/uploadfile/")
async def create_upload_file(content: UploadFile = File(...)):
    
    #ler o arquivo e armazenar o conteúdo na memória 
    content_in_memory = content.file.read()

    #ler conteúdo da memória e converter para data frame 
    data_frame = pandas.read_excel(content_in_memory)

    data_frame.fillna("-", inplace = True)
    
    #conexion.open() 

    #---------------------------------COMANDOS TABELA CONSULTA CAED------------------------------------------------------
    # prepara query de insert 
    query_insert= conexion.cursor()

    #cria string com comando de insert 
    string_insert= ("INSERT INTO consulta_caed (recuperacao_continuada, ano, materia, turma, serie, bimestre, estudante, participacao, numero_itens_respondidos, "
        " porcento_acertos, categoria_desempenho, tipo_intervencao, itens_acertados, "
        " h_01, h_02, h_03, h_04, h_05, h_06, h_07, h_08, h_09, h_10, h_11, "
        " h_12, h_13, h_14, h_15, h_16, h_17, h_18, h_19, h_20, h_21, h_22, "
        " h_23, h_24, h_25, h_26, h_27, h_28, h_29, h_30) "
        " VALUES (%(recuperacao)s, %(ano)s, %(materia)s,%(turma)s,%(serie)s,%(bimestre)s,%(estudante)s,%(participacao)s,%(numero_itens_respondidos)s,"
        " %(porcento_acertos)s,%(categoria_desempenho)s,%(tipo_intervencao)s,%(itens_acertados)s,"
        " %(h_01)s,%(h_02)s,%(h_03)s,%(h_04)s,%(h_05)s,%(h_06)s,%(h_07)s,%(h_08)s,%(h_09)s,%(h_10)s,%(h_11)s,"
        " %(h_12)s,%(h_13)s,%(h_14)s,%(h_15)s,%(h_16)s,%(h_17)s,%(h_18)s,%(h_19)s,%(h_20)s,%(h_21)s,%(h_22)s,"
        " %(h_23)s,%(h_24)s,%(h_25)s,%(h_26)s,%(h_27)s,%(h_28)s,%(h_29)s,%(h_30)s )")

    #prepara query de consulta 
    query_consulta=conexion.cursor()

    #cria string com comando de consulta 
    string_consulta= ("SELECT * FROM consulta_caed "
        " WHERE recuperacao_continuada = %(recuperacao)s"
        " AND ano = %(ano)s"
        " AND UPPER(materia) = UPPER(%(materia)s)"
        " AND UPPER(turma) = UPPER(%(turma)s)"
        " AND serie = %(serie)s"
        " AND bimestre = %(bimestre)s"
        " AND UPPER(estudante) = UPPER(%(estudante)s)")         

    #prepara query de update 
    query_update=conexion.cursor()

    #cria string com comando de update 
    string_update= ("UPDATE consulta_caed SET participacao = %(participacao)s, numero_itens_respondidos = %(numero_itens_respondidos)s, "
         " porcento_acertos = %(porcento_acertos)s, categoria_desempenho = %(categoria_desempenho)s, "
         " tipo_intervencao = %(tipo_intervencao)s, itens_acertados = %(itens_acertados)s, "
         " h_01 = %(h_01)s, h_02 = %(h_02)s, h_03 = %(h_03)s, h_04 = %(h_04)s, h_05 = %(h_05)s, h_06 = %(h_06)s, "
         " h_07 = %(h_07)s, h_08 = %(h_08)s, h_09 = %(h_09)s, h_10 = %(h_10)s, h_11 = %(h_11)s, h_12 = %(h_12)s, "
         " h_13 = %(h_13)s, h_14 = %(h_14)s, h_15 = %(h_15)s, h_16 = %(h_16)s, h_17 = %(h_17)s, h_18 = %(h_18)s, "
         " h_19 = %(h_19)s, h_20 = %(h_20)s, h_21 = %(h_21)s, h_22 = %(h_22)s, h_23 = %(h_23)s, h_24 = %(h_24)s, "
         " h_25 = %(h_25)s, h_26 = %(h_26)s, h_27 = %(h_27)s, h_28 = %(h_28)s, h_29 = %(h_29)s, h_30 = %(h_30)s "        
         " WHERE ano = %(ano)s"
         " AND materia = %(materia)s"
         " AND turma = %(turma)s"
         " AND serie = %(serie)s"
         " AND bimestre = %(bimestre)s" 
         " AND estudante = %(estudante)s") 
    #-----------------------------------------------------------------------------------------------------     

    #---------------------------------COMANDOS TABELA HABILIDADE CAED------------------------------------------------------
    # prepara query de insert 
    query_insert_hab= conexion.cursor()

    #cria string com comando de insert 
    string_insert_hab= ("INSERT INTO habilidade_caed (ano, materia, turma, serie, bimestre, questao) "
        " VALUES (%(ano)s, %(materia)s,%(turma)s,%(serie)s,%(bimestre)s,%(questao)s )")

    #prepara query de consulta 
    query_consulta_hab=conexion.cursor()

    #cria string com comando de consulta 
    string_consulta_hab= ("SELECT * FROM habilidade_caed "
        " WHERE ano = %(ano)s"
        " AND materia = %(materia)s"
        " AND turma = %(turma)s"
        " AND serie = %(serie)s"
        " AND bimestre = %(bimestre)s" 
        " AND questao = %(questao)s")  

    #-----------------------------------------------------------------------------------------------------     
    
    
    #---------------------------------EXECUÇÃO TABELA CONSULTA CAED------------------------------------------------------
    #percorre planilha linha a linha através do data frame 
    for index, row in data_frame.iterrows(): 

        #cria dados de aluno com o conteúdo da linha para insert/update 
        data_aluno = {
        'recuperacao': row['RECUPERACAO CONTINUADA'],'ano': row['ano'], 'materia': row['materia'], 'turma': row['turma'], 'serie': row['serie'], 'bimestre': row['Bimestre'], 
        'estudante': row['ESTUDANTE'], 'participacao': row['PARTICIPAÇÃO'], 'numero_itens_respondidos': row['Nº DE ITENS RESPONDIDOS'], 
        'porcento_acertos': row['% ACERTOS'], 'categoria_desempenho': row.get('CATEGORIA DE DESEMPENHO', '-'), 
        'tipo_intervencao': row['TIPO DE INTERVENÇÃO'], 'itens_acertados': row['ITENS ACERTADOS'], 
        'h_01': row.get('H 01', '-'), 'h_02': row.get('H 02', '-'), 'h_03': row.get('H 03', '-'), 'h_04': row.get('H 04', '-'), 'h_05': row.get('H 05', '-'), 'h_06': row.get('H 06', '-'), 
        'h_07': row.get('H 07', '-'), 
        'h_08': row.get('H 08', '-'), 'h_09': row.get('H 09', '-'), 'h_10': row.get('H 10', '-'), 'h_11': row.get('H 11', '-'), 'h_12': row.get('H 12', '-'), 'h_13': row.get('H 13', '-'), 
        'h_14': row.get('H 14', '-'), 
        'h_15': row.get('H 15', '-'), 'h_16': row.get('H 16', '-'), 'h_17': row.get('H 17', '-'), 'h_18': row.get('H 18', '-'), 'h_19': row.get('H 19', '-'), 'h_20': row.get('H 20', '-'), 
        'h_21': row.get('H 21', '-'), 
        'h_22': row.get('H 22', '-'), 'h_23': row.get('H 23', '-'), 'h_24': row.get('H 24', '-'), 'h_25': row.get('H 25', '-'), 'h_26': row.get('H 26', '-'), 'h_27': row.get('H 27', '-'), 
        'h_28': row.get('H 28', '-'), 
        'h_29': row.get('H 29', '-'), 'h_30': row.get('H 30', '-')
        } 

        #cria dados de aluno com o conteúdo da linha para consulta  
        data_consulta = {
        'recuperacao': row['RECUPERACAO CONTINUADA'],
        'ano': row['ano'], 'materia': row['materia'], 'turma': row['turma'], 'serie': row['serie'], 'bimestre': row['Bimestre'], 
        'estudante': row['ESTUDANTE']
        }
        
        #executa a consulta   
        query_consulta.execute(string_consulta, data_consulta)

        #força carregar todos os dados da consulta, ignora modo lazy 
        query_consulta.fetchall()

        #verifica se linha já foi inserida 
        if query_consulta.rowcount > 0:
            #se rowcount>0 significa que linha já foi inserida e devemos atualizá-la 
            query_update.execute(string_update, data_aluno)
            query_update.fetchall()
        else:
            #se rowcount=0 significa que linha não foi inserida e devemos inseri-la 
            query_insert.execute(string_insert, data_aluno)
            query_insert.fetchall()
    #-----------------------------------------------------------------------------------------------------     

    #---------------------------------EXECUÇÃO TABELA HABILIDADE CAED------------------------------------------------------
        
    row_one=next(data_frame.iterrows())[1]


    #percorre planilha linha a linha através do data frame 
    for i in range(1,31):

        #cria dados de aluno com o conteúdo da linha para insert/update 
        data_hab = {
            'ano': row_one['ano'], 'materia': row_one['materia'], 'turma': row_one['turma'], 'serie': row_one['serie'], 'bimestre': row_one['Bimestre'], 
            'questao': 'h_'+f'{i:02}'
        }

        #executa a consulta   
        query_consulta_hab.execute(string_consulta_hab, data_hab)

        #força carregar todos os dados da consulta, ignora modo lazy 
        query_consulta_hab.fetchall()

        #verifica se linha já foi inserida 
        if query_consulta_hab.rowcount == 0:
            #se rowcount=0 significa que linha não foi inserida e devemos inseri-la 
            query_insert_hab.execute(string_insert_hab, data_hab)
            query_insert_hab.fetchall()

    #-----------------------------------------------------------------------------------------------------            

    #efetiva todas as transações no banco 
    conexion.commit()

    #fecha as querys
    query_insert.close()
    query_consulta.close()
    query_update.close()
    query_insert_hab.close()
    query_consulta_hab.close()    

    #conexion.close()


    


    return {"filename": content.filename}


@app.get("/resultadocaed/")
def resultado_caed(ano: int, materia: str, turma: str, serie: int, bimestre: int):
    #prepara query de consulta 
    query_consulta=conexion.cursor()

    #cria string com comando de consulta 
    string_consulta= ("SELECT 'NÃO' AS RC, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_01, 1, POSITION('/' IN H_01)-1)) / SUM(SUBSTRING(H_01, POSITION('/' IN H_01)+1, LENGTH(H_01)))) *100,0)) AS H_01, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_02, 1, POSITION('/' IN H_02)-1)) / SUM(SUBSTRING(H_02, POSITION('/' IN H_02)+1, LENGTH(H_02)))) *100,0)) AS H_02, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_03, 1, POSITION('/' IN H_03)-1)) / SUM(SUBSTRING(H_03, POSITION('/' IN H_03)+1, LENGTH(H_03)))) *100,0)) AS H_03, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_04, 1, POSITION('/' IN H_04)-1)) / SUM(SUBSTRING(H_04, POSITION('/' IN H_04)+1, LENGTH(H_04)))) *100,0)) AS H_04, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_05, 1, POSITION('/' IN H_05)-1)) / SUM(SUBSTRING(H_05, POSITION('/' IN H_05)+1, LENGTH(H_05)))) *100,0)) AS H_05, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_06, 1, POSITION('/' IN H_06)-1)) / SUM(SUBSTRING(H_06, POSITION('/' IN H_06)+1, LENGTH(H_06)))) *100,0)) AS H_06, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_07, 1, POSITION('/' IN H_07)-1)) / SUM(SUBSTRING(H_07, POSITION('/' IN H_07)+1, LENGTH(H_07)))) *100,0)) AS H_07, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_08, 1, POSITION('/' IN H_08)-1)) / SUM(SUBSTRING(H_08, POSITION('/' IN H_08)+1, LENGTH(H_08)))) *100,0)) AS H_08, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_09, 1, POSITION('/' IN H_09)-1)) / SUM(SUBSTRING(H_09, POSITION('/' IN H_09)+1, LENGTH(H_09)))) *100,0)) AS H_09, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_10, 1, POSITION('/' IN H_10)-1)) / SUM(SUBSTRING(H_10, POSITION('/' IN H_10)+1, LENGTH(H_10)))) *100,0)) AS H_10, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_11, 1, POSITION('/' IN H_11)-1)) / SUM(SUBSTRING(H_11, POSITION('/' IN H_11)+1, LENGTH(H_11)))) *100,0)) AS H_11, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_12, 1, POSITION('/' IN H_12)-1)) / SUM(SUBSTRING(H_12, POSITION('/' IN H_12)+1, LENGTH(H_12)))) *100,0)) AS H_12, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_13, 1, POSITION('/' IN H_13)-1)) / SUM(SUBSTRING(H_13, POSITION('/' IN H_13)+1, LENGTH(H_13)))) *100,0)) AS H_13, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_14, 1, POSITION('/' IN H_14)-1)) / SUM(SUBSTRING(H_14, POSITION('/' IN H_14)+1, LENGTH(H_14)))) *100,0)) AS H_14, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_15, 1, POSITION('/' IN H_15)-1)) / SUM(SUBSTRING(H_15, POSITION('/' IN H_15)+1, LENGTH(H_15)))) *100,0)) AS H_15, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_16, 1, POSITION('/' IN H_16)-1)) / SUM(SUBSTRING(H_16, POSITION('/' IN H_16)+1, LENGTH(H_16)))) *100,0)) AS H_16, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_17, 1, POSITION('/' IN H_17)-1)) / SUM(SUBSTRING(H_17, POSITION('/' IN H_17)+1, LENGTH(H_17)))) *100,0)) AS H_17, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_18, 1, POSITION('/' IN H_18)-1)) / SUM(SUBSTRING(H_18, POSITION('/' IN H_18)+1, LENGTH(H_18)))) *100,0)) AS H_18, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_19, 1, POSITION('/' IN H_19)-1)) / SUM(SUBSTRING(H_19, POSITION('/' IN H_19)+1, LENGTH(H_19)))) *100,0)) AS H_19, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_20, 1, POSITION('/' IN H_20)-1)) / SUM(SUBSTRING(H_20, POSITION('/' IN H_20)+1, LENGTH(H_20)))) *100,0)) AS H_20, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_21, 1, POSITION('/' IN H_21)-1)) / SUM(SUBSTRING(H_21, POSITION('/' IN H_21)+1, LENGTH(H_21)))) *100,0)) AS H_21, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_22, 1, POSITION('/' IN H_22)-1)) / SUM(SUBSTRING(H_22, POSITION('/' IN H_22)+1, LENGTH(H_22)))) *100,0)) AS H_22, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_23, 1, POSITION('/' IN H_23)-1)) / SUM(SUBSTRING(H_23, POSITION('/' IN H_23)+1, LENGTH(H_23)))) *100,0)) AS H_23, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_24, 1, POSITION('/' IN H_24)-1)) / SUM(SUBSTRING(H_24, POSITION('/' IN H_24)+1, LENGTH(H_24)))) *100,0)) AS H_24, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_25, 1, POSITION('/' IN H_25)-1)) / SUM(SUBSTRING(H_25, POSITION('/' IN H_25)+1, LENGTH(H_25)))) *100,0)) AS H_25, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_26, 1, POSITION('/' IN H_26)-1)) / SUM(SUBSTRING(H_26, POSITION('/' IN H_26)+1, LENGTH(H_26)))) *100,0)) AS H_26, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_27, 1, POSITION('/' IN H_27)-1)) / SUM(SUBSTRING(H_27, POSITION('/' IN H_27)+1, LENGTH(H_27)))) *100,0)) AS H_27, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_28, 1, POSITION('/' IN H_28)-1)) / SUM(SUBSTRING(H_28, POSITION('/' IN H_28)+1, LENGTH(H_28)))) *100,0)) AS H_28, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_29, 1, POSITION('/' IN H_29)-1)) / SUM(SUBSTRING(H_29, POSITION('/' IN H_29)+1, LENGTH(H_29)))) *100,0)) AS H_29, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_30, 1, POSITION('/' IN H_30)-1)) / SUM(SUBSTRING(H_30, POSITION('/' IN H_30)+1, LENGTH(H_30)))) *100,0)) AS H_30  "
        "  FROM consulta_caed "
        "         WHERE ano = %(ano)s "
        "         AND UPPER(materia) = UPPER(%(materia)s) "
        "         AND UPPER(turma) = UPPER(%(turma)s) "
        "         AND serie = %(serie)s "
        "         AND bimestre = %(bimestre)s "
        "    AND participacao = 'SIM' "
        "    AND recuperacao_continuada  = 'NÃO' "
        "UNION ALL "
        "SELECT 'SIM' AS RC, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_01, 1, POSITION('/' IN H_01)-1)) / SUM(SUBSTRING(H_01, POSITION('/' IN H_01)+1, LENGTH(H_01)))) *100,0)) AS H_01, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_02, 1, POSITION('/' IN H_02)-1)) / SUM(SUBSTRING(H_02, POSITION('/' IN H_02)+1, LENGTH(H_02)))) *100,0)) AS H_02, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_03, 1, POSITION('/' IN H_03)-1)) / SUM(SUBSTRING(H_03, POSITION('/' IN H_03)+1, LENGTH(H_03)))) *100,0)) AS H_03, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_04, 1, POSITION('/' IN H_04)-1)) / SUM(SUBSTRING(H_04, POSITION('/' IN H_04)+1, LENGTH(H_04)))) *100,0)) AS H_04, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_05, 1, POSITION('/' IN H_05)-1)) / SUM(SUBSTRING(H_05, POSITION('/' IN H_05)+1, LENGTH(H_05)))) *100,0)) AS H_05, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_06, 1, POSITION('/' IN H_06)-1)) / SUM(SUBSTRING(H_06, POSITION('/' IN H_06)+1, LENGTH(H_06)))) *100,0)) AS H_06, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_07, 1, POSITION('/' IN H_07)-1)) / SUM(SUBSTRING(H_07, POSITION('/' IN H_07)+1, LENGTH(H_07)))) *100,0)) AS H_07, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_08, 1, POSITION('/' IN H_08)-1)) / SUM(SUBSTRING(H_08, POSITION('/' IN H_08)+1, LENGTH(H_08)))) *100,0)) AS H_08, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_09, 1, POSITION('/' IN H_09)-1)) / SUM(SUBSTRING(H_09, POSITION('/' IN H_09)+1, LENGTH(H_09)))) *100,0)) AS H_09, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_10, 1, POSITION('/' IN H_10)-1)) / SUM(SUBSTRING(H_10, POSITION('/' IN H_10)+1, LENGTH(H_10)))) *100,0)) AS H_10, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_11, 1, POSITION('/' IN H_11)-1)) / SUM(SUBSTRING(H_11, POSITION('/' IN H_11)+1, LENGTH(H_11)))) *100,0)) AS H_11, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_12, 1, POSITION('/' IN H_12)-1)) / SUM(SUBSTRING(H_12, POSITION('/' IN H_12)+1, LENGTH(H_12)))) *100,0)) AS H_12, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_13, 1, POSITION('/' IN H_13)-1)) / SUM(SUBSTRING(H_13, POSITION('/' IN H_13)+1, LENGTH(H_13)))) *100,0)) AS H_13, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_14, 1, POSITION('/' IN H_14)-1)) / SUM(SUBSTRING(H_14, POSITION('/' IN H_14)+1, LENGTH(H_14)))) *100,0)) AS H_14, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_15, 1, POSITION('/' IN H_15)-1)) / SUM(SUBSTRING(H_15, POSITION('/' IN H_15)+1, LENGTH(H_15)))) *100,0)) AS H_15, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_16, 1, POSITION('/' IN H_16)-1)) / SUM(SUBSTRING(H_16, POSITION('/' IN H_16)+1, LENGTH(H_16)))) *100,0)) AS H_16, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_17, 1, POSITION('/' IN H_17)-1)) / SUM(SUBSTRING(H_17, POSITION('/' IN H_17)+1, LENGTH(H_17)))) *100,0)) AS H_17, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_18, 1, POSITION('/' IN H_18)-1)) / SUM(SUBSTRING(H_18, POSITION('/' IN H_18)+1, LENGTH(H_18)))) *100,0)) AS H_18, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_19, 1, POSITION('/' IN H_19)-1)) / SUM(SUBSTRING(H_19, POSITION('/' IN H_19)+1, LENGTH(H_19)))) *100,0)) AS H_19, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_20, 1, POSITION('/' IN H_20)-1)) / SUM(SUBSTRING(H_20, POSITION('/' IN H_20)+1, LENGTH(H_20)))) *100,0)) AS H_20, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_21, 1, POSITION('/' IN H_21)-1)) / SUM(SUBSTRING(H_21, POSITION('/' IN H_21)+1, LENGTH(H_21)))) *100,0)) AS H_21, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_22, 1, POSITION('/' IN H_22)-1)) / SUM(SUBSTRING(H_22, POSITION('/' IN H_22)+1, LENGTH(H_22)))) *100,0)) AS H_22, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_23, 1, POSITION('/' IN H_23)-1)) / SUM(SUBSTRING(H_23, POSITION('/' IN H_23)+1, LENGTH(H_23)))) *100,0)) AS H_23, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_24, 1, POSITION('/' IN H_24)-1)) / SUM(SUBSTRING(H_24, POSITION('/' IN H_24)+1, LENGTH(H_24)))) *100,0)) AS H_24, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_25, 1, POSITION('/' IN H_25)-1)) / SUM(SUBSTRING(H_25, POSITION('/' IN H_25)+1, LENGTH(H_25)))) *100,0)) AS H_25, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_26, 1, POSITION('/' IN H_26)-1)) / SUM(SUBSTRING(H_26, POSITION('/' IN H_26)+1, LENGTH(H_26)))) *100,0)) AS H_26, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_27, 1, POSITION('/' IN H_27)-1)) / SUM(SUBSTRING(H_27, POSITION('/' IN H_27)+1, LENGTH(H_27)))) *100,0)) AS H_27, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_28, 1, POSITION('/' IN H_28)-1)) / SUM(SUBSTRING(H_28, POSITION('/' IN H_28)+1, LENGTH(H_28)))) *100,0)) AS H_28, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_29, 1, POSITION('/' IN H_29)-1)) / SUM(SUBSTRING(H_29, POSITION('/' IN H_29)+1, LENGTH(H_29)))) *100,0)) AS H_29, "
        "       ROUND(COALESCE((SUM(SUBSTRING(H_30, 1, POSITION('/' IN H_30)-1)) / SUM(SUBSTRING(H_30, POSITION('/' IN H_30)+1, LENGTH(H_30)))) *100,0)) AS H_30  "
        "  FROM consulta_caed "
        "         WHERE ano = %(ano)s "
        "         AND UPPER(materia) = UPPER(%(materia)s) "
        "         AND UPPER(turma) = UPPER(%(turma)s) "
        "         AND serie = %(serie)s "
        "         AND bimestre = %(bimestre)s "
        "    AND participacao = 'SIM' "
        "    AND recuperacao_continuada  = 'SIM' ")

    #cria dados de aluno com o conteúdo da linha para consulta  
    data_consulta = {
        'ano': ano, 'materia': materia, 'turma': turma, 'serie': serie, 'bimestre': bimestre
    }   
    
    query_consulta.execute(string_consulta, data_consulta)

    #força carregar todos os dados da consulta, ignora modo lazy            
    results= query_consulta.fetchall()

    #------------------BUSCAR CÓDIGO DA HABILIDADE-----------------------------------#
    query_habilidade=conexion.cursor()

    #cria string com comando de consulta 
    string_habilidade= ("SELECT h.*, "
        " coalesce(concat(replace(upper(h.questao), '_', ' '),' (', h.cod_da_habilidade ,')'), replace(upper(h.questao), '_', ' ')) as label "
        " FROM habilidade_caed h "
        " WHERE ano = %(ano)s"
        " AND UPPER(materia) = UPPER(%(materia)s)"
        " AND UPPER(turma) = UPPER(%(turma)s)"
        " AND serie = %(serie)s"
        " AND bimestre = %(bimestre)s")

    #cria dados de aluno com o conteúdo da linha para consulta  
    data_habilidade = {
        'ano': ano, 'materia': materia, 'turma': turma, 'serie': serie, 'bimestre': bimestre
    }
        
    #executa a consulta   
    query_habilidade.execute(string_habilidade, data_habilidade)

    #força carregar todos os dados da consulta, ignora modo lazy            
    results_habilidade= query_habilidade.fetchall()
    #-----------------------------------------------------#

    #print(results_habilidade)

    #extrai cabeçalho da linha
    row_headers=[x[0] for x in query_consulta.description]
    row_headers_table = [x for x in row_headers if x.find("H_") > -1]

    for i in range(len(row_headers_table)):
        for row in results_habilidade:
            if (row[6].upper() == row_headers_table[i].upper()):
                row_headers_table[i] = row[8]

    #inicializa a array de json
    json_array=[]


    #percorre dados da query de consulta e insere no json
    for row in results:
        json_array.append(dict(zip(row_headers,row)))

    json_data = {'resultadoCaed':json_array, 'table_header': row_headers_table}   
    
    #converte para json
    json_compatible_item_data = jsonable_encoder(json_data)

    return json_compatible_item_data