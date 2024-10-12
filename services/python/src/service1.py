from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def status():
    return {
        'name': 'service1',
        'status': 'ok'
        }
