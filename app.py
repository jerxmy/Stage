import uvicorn # équivalent (plus ou moins) d'un serveur web 
from fastapi import FastAPI, Request # Outils pour API
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from fastapi.middleware.cors import CORSMiddleware
from project_routes import router as projet_routes
from stage_routes import router as stage_routes

app = FastAPI() #Créer une instance 

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(projet_routes)
app.include_router(stage_routes)

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
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)