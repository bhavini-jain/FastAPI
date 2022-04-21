import email
import json
from uuid import UUID
from fastapi import FastAPI
from typing import Optional, List
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from fastapi import Query, Path, FastAPI

app = FastAPI()

with open('data.json' , 'r') as f:
    var = json.load(f)


@app.get('/')
def home():
    return{'Hello....'};

@app.get('/query1')
def query1(page_no : int = Query(None,description='page number', le = 2 , gt = 0)):
    for i  in var:
        if i ['page'] == page_no:
            return i

        

@app.get('/query2')
def query2(uid : int = Query(None, description='User Id', le=12 , gt=7)):
    for i in var:
        for j in i['data']:
            if j['id'] == uid:
                return j , i['support']
         
    
            

