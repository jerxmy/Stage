import uvicorn # équivalent (plus ou moins) d'un serveur web 
from fastapi import FastAPI, Request # Outils pour API
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI() #Créer une instance 

# Créer une route 

@app.get ("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/test")
async def read_test():
    return {"message" : "Hello Test"}

# Lancement du serveur
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)