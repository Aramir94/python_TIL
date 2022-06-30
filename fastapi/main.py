#pip install python-multipart
from fastapi import FastAPI, File, UploadFile
import pandas as pd
import os
from sqlalchemy import create_engine

conn_string = 'postgresql://postgres:dataint@192.168.192.40:5432/marketing'
db = create_engine(conn_string)
conn = db.connect()

app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    contents = await file.read()
    UPLOAD_DIRECTORY = "./"
    with open(os.path.join(UPLOAD_DIRECTORY, file.filename), "wb") as fp:
            fp.write(contents)

    data = pd.read_excel(file.filename)
    data.to_sql('guud', con=conn, if_exists='append', index=False)
    os.remove(file.filename)
    return { "file upload Done " "filename": file.filename}
    
# uvicorn main:app --reload