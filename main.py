
from fastapi import FastAPI
from mylib.logic import wiki as wikilogic
from mylib.logic import search_wiki
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Wikipedai api. Call /search or /wiki"}

@app.get("/search/{value}")
async def search(value : str):
    """Page to search in wikipedia"""
    result = search_wiki(value)
    return {"results" : result}

@app.get("wiki/{name}")
async def wiki(name : str):
    """Retrieve wikipedia page"""
    result = wikilogic(name)
    return {"result" : result}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')