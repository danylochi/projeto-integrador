#from typing import Optional
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
import pandas
import mysql.connector
from fastapi.encoders import jsonable_encoder
import io

#cria conexão com o banco de dados mysql
conexion = mysql.connector.connect(user='root', password='root',
                              host='localhost',
                              database='educacaodb')
#conexion.close()



app = FastAPI()



@app.get("/downloadfile/")
async def download_caed(ano: int, materia: str, turma: str, serie: int, bimestre: int):
#prepara query de consulta 
    query_consulta=conexion.cursor()

    #cria string com comando de consulta 
    string_consulta= ("SELECT * FROM educacaodb.consulta_caed "
        " WHERE ano = %(ano)s"
        " AND materia = %(materia)s"
        " AND turma = %(turma)s"
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

    print(results)

    data_frame = pandas.DataFrame(results, columns = row_headers)

    output = io.BytesIO()
    writer = pandas.ExcelWriter(output, engine = 'xlsxwriter')

    data_frame.to_excel(writer, index=False)

    writer.close()

    #go back to the beginning of the stream
    output.seek(0)


    headers = {
        'Content-Disposition': 'attachment; filename="file.xlsx"'
    }
    return StreamingResponse(output, headers=headers,media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

   


@app.get("/consultacaed/")
def consulta_caed(ano: int, materia: str, turma: str, serie: int, bimestre: int):
#prepara query de consulta 
    query_consulta=conexion.cursor()

    #cria string com comando de consulta 
    string_consulta= ("SELECT * FROM educacaodb.consulta_caed "
        " WHERE ano = %(ano)s"
        " AND materia = %(materia)s"
        " AND turma = %(turma)s"
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

@app.post("/uploadfile/")
async def create_upload_file(content: UploadFile = File(...)):
    
    #ler o arquivo e armazenar o conteúdo na memória 
    content_in_memory = content.file.read()

    #ler conteúdo da memória e converter para data frame 
    data_frame = pandas.read_excel(content_in_memory)

    #data_frame['H 01'] = data_frame['H 01'].dt.strftime('%d/%m')
    #data_frame['H 01'] = data_frame['H 01'].astype(str)
    #print(data_frame['H 01'])
    #conexion.open() 

    #---------------------------------COMANDOS TABELA CONSULTA CAED------------------------------------------------------
    # prepara query de insert 
    query_insert= conexion.cursor()

    #cria string com comando de insert 
    string_insert= ("INSERT INTO consulta_caed (ano, materia, turma, serie, bimestre, estudante, participacao, numero_itens_respondidos, "
        " porcento_acertos, categoria_desempenho, tipo_intervencao, itens_acertados, "
        " h_01, h_02, h_03, h_04, h_05, h_06, h_07, h_08, h_09, h_10, h_11, "
        " h_12, h_13, h_14, h_15, h_16, h_17, h_18, h_19, h_20, h_21, h_22, "
        " h_23, h_24, h_25, h_26, h_27, h_28, h_29, h_30) "
        " VALUES (%(ano)s, %(materia)s,%(turma)s,%(serie)s,%(bimestre)s,%(estudante)s,%(participacao)s,%(numero_itens_respondidos)s,"
        " %(porcento_acertos)s,%(categoria_desempenho)s,%(tipo_intervencao)s,%(itens_acertados)s,"
        " %(h_01)s,%(h_02)s,%(h_03)s,%(h_04)s,%(h_05)s,%(h_06)s,%(h_07)s,%(h_08)s,%(h_09)s,%(h_10)s,%(h_11)s,"
        " %(h_12)s,%(h_13)s,%(h_14)s,%(h_15)s,%(h_16)s,%(h_17)s,%(h_18)s,%(h_19)s,%(h_20)s,%(h_21)s,%(h_22)s,"
        " %(h_23)s,%(h_24)s,%(h_25)s,%(h_26)s,%(h_27)s,%(h_28)s,%(h_29)s,%(h_30)s )")

    #prepara query de consulta 
    query_consulta=conexion.cursor()

    #cria string com comando de consulta 
    string_consulta= ("SELECT * FROM educacaodb.consulta_caed "
        " WHERE ano = %(ano)s"
        " AND materia = %(materia)s"
        " AND turma = %(turma)s"
        " AND serie = %(serie)s"
        " AND bimestre = %(bimestre)s" 
        " AND estudante = %(estudante)s") 

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
    string_consulta_hab= ("SELECT * FROM educacaodb.habilidade_caed "
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
        'ano': row['ano'], 'materia': row['materia'], 'turma': row['turma'], 'serie': row['serie'], 'bimestre': row['Bimestre'], 
        'estudante': row['ESTUDANTE'], 'participacao': row['PARTICIPAÇÃO'], 'numero_itens_respondidos': row['Nº DE ITENS RESPONDIDOS'], 
        'porcento_acertos': row['% ACERTOS'], 'categoria_desempenho': row['CATEGORIA DE DESEMPENHO'], 
        'tipo_intervencao': row['TIPO DE INTERVENÇÃO'], 'itens_acertados': row['ITENS ACERTADOS'], 
        'h_01': row['H 01'], 'h_02': row['H 02'], 'h_03': row['H 03'], 'h_04': row['H 04'], 'h_05': row['H 05'], 'h_06': row['H 06'], 
        'h_07': row['H 07'], 
        'h_08': row['H 08'], 'h_09': row['H 09'], 'h_10': row['H 10'], 'h_11': row['H 11'], 'h_12': row['H 12'], 'h_13': row['H 13'], 
        'h_14': row['H 14'], 
        'h_15': row['H 15'], 'h_16': row['H 16'], 'h_17': row['H 17'], 'h_18': row['H 18'], 'h_19': row['H 19'], 'h_20': row['H 20'], 
        'h_21': row['H 21'], 
        'h_22': row['H 22'], 'h_23': row['H 23'], 'h_24': row['H 24'], 'h_25': row['H 25'], 'h_26': row['H 26'], 'h_27': row['H 27'], 
        'h_28': row['H 28'], 
        'h_29': row['H 29'], 'h_30': row['H 30']
        } 

        #cria dados de aluno com o conteúdo da linha para consulta  
        data_consulta = {
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


