from typing import Optional
from fastapi import FastAPI, File, UploadFile
import pandas
import mysql.connector

conexion = mysql.connector.connect(user='root', password='root',
                              host='localhost',
                              database='educacaodb')
#conexion.close()



app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}



@app.post("/uploadfile/")
async def create_upload_file(content: UploadFile = File(...)):
    
    content_in_memory = content.file.read()

    data_frame = pandas.read_excel(content_in_memory)

    #conexion.open() 
    query_insert= conexion.cursor()
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

    query_consulta=conexion.cursor()
    string_consulta= ("SELECT * FROM educacaodb.consulta_caed "
        " WHERE ano = %(ano)s"
        " AND materia = %(materia)s"
        " AND turma = %(turma)s"
        " AND serie = %(serie)s"
        " AND bimestre = %(bimestre)s" 
        " AND estudante = %(estudante)s") 

    query_update=conexion.cursor()
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

    for index, row in data_frame.iterrows(): 
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

        data_consulta = {
        'ano': row['ano'], 'materia': row['materia'], 'turma': row['turma'], 'serie': row['serie'], 'bimestre': row['Bimestre'], 
        'estudante': row['ESTUDANTE']
        }
           
        query_consulta.execute(string_consulta, data_consulta)
        query_consulta.fetchall()

        if query_consulta.rowcount > 0:
            query_update.execute(string_update, data_aluno)
            query_update.fetchall()
        else:
            query_insert.execute(string_insert, data_aluno)
            query_insert.fetchall()

    conexion.commit()
    query_insert.close()
    query_consulta.close()
    query_update.close()

    #conexion.close()


    


    return {"filename": content.filename}


