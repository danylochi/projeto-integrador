from typing import Optional
from fastapi import FastAPI, File, UploadFile
import pandas as pd
import xlrd


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    book = xlrd.open_workbook(file_contents=file.file.read())
    df = pd.read_excel(book,engine='xlrd')
    print(df.head())
    return {"filename": file.filename}


