from fastapi import Request, APIRouter, HTTPException
from stage_model import Stage
from typing import List, Optional

router = APIRouter()

@router.get("/stage", response_model=List[Stage])
def get_all_stage():
    results = Stage.get_all()
    return results

@router.get("/stage/{id}", response_model=Stage)
def get_one_stage(id : int):
    result = Stage.get_one(id=id)
    if result is None:
        raise HTTPException(status_code=404, detail="Not Found... Try again")
    return result

@router.post("/stage", response_model=Stage)
async def create_stage(request: Request):
    body = await request.json()
    poste = body.get("poste")
    entreprise = body.get("entreprise")
    expedition = body.get("expedition")
    url = body.get("url")

    if not poste or not entreprise or not url:
        raise HTTPException(status_code=400, detail="Missing required fields")
    
    result = Stage.insert(
        poste= poste,
        entreprise= entreprise,
        expedition= expedition,
        url= url
    )
    return result

@router.delete("/stage/{id}", response_model=bool)
def delete_stage(id : int):
    sucess = Stage.delete(id)
    if not sucess:
         raise HTTPException(status_code=404, detail="Not Found... Try again")
    
    raise HTTPException(status_code=204, detail="Deleted")

@router.put("/stage/{id}", response_model=Stage)
async def update_stage(id : int, request : Request):
    try:
        body = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Data missing")
    poste = body.get("poste")
    entreprise = body.get("entreprise")
    expedition = body.get("expedition"
                          )
    url = body.get("url")
    if not any([poste, entreprise, expedition, url]):
        raise HTTPException(status_code=400, detail="Data missing")
    
    result = Stage.update(
        id= id,
        poste= poste,
        entreprise= entreprise,
        expedition= expedition,
        url= url
    )
    if result is None:
        raise HTTPException(status_code=404, detail="Not Found... Try again")
    return result