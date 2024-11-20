from fastapi import Request, APIRouter, HTTPException
from project_model import Projet
from typing import List, Optional

router = APIRouter()

@router.get("/projets", response_model=List[Projet])
def get_all_projets():
    results = Projet.get_all()
    return results

@router.get("/projets/{id}", response_model=Projet)
def get_one_projet(id : int):
    result = Projet.get_one(id=id)
    if result is None:
        raise HTTPException(status_code=404, detail="Not Found... Try again")
    return result

@router.post("/projets", response_model=Projet)
async def create_projet(request: Request):
    body = await request.json()
    rubrique = body.get("rubrique")
    nom = body.get("nom")
    image = body.get("image", "default.jpg")
    rendu = body.get("rendu")

    if not rubrique or not nom or not rendu:
        raise HTTPException(status_code=400, detail="Missing required fields")
    
    result = Projet.insert(
        rubrique= rubrique,
        nom= nom,
        image= image,
        rendu= rendu
    )
    return result

@router.delete("/projets/{id}", response_model=bool)
def delete_projet(id : int):
    sucess = Projet.delete(id)
    if not sucess:
         raise HTTPException(status_code=404, detail="Not Found... Try again")
    
    raise HTTPException(status_code=204, detail="Deleted")