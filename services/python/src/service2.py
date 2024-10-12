from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def status():
    return {
        'name': 'service2',
        'status': 'ok'
        }
