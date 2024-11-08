import uvicorn # équivalent (plus ou moins) d'un serveur web 
from fastapi import FastAPI, Request # Outils pour API
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from fastapi.staticfiles import StaticFiles

app = FastAPI() #Créer une instance 

# Init request motor
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

# Créer une route 

@app.get("/home", response_class=HTMLResponse)
async def read_home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request" : request,
         "name": "Mario",
         "job": "Plombier",
         "brother": "Luigi",
         "friends" : ["Toad", "Peach", 
                      "Donkey Kong", "Yoshi"]
        }
    )


@app.get ("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/test")
async def read_test():
    return {"message" : "Hello Test"}

# Lancement du serveur
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)