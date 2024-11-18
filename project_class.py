from sqlmodel import SQLModel, Field
from typing import Optional

class Project(SQLModel, table=True):
    # Definition de la structure de la table = une classe
    __tablename__ = "Projects"
    id: Optional[int] = Field(default=None, primary_key=True)
    rubrique : str
    nom : str
    image : str
    rendu : str 
    url : Optional[str] = None

    @classmethod
    def get_all(cls) -> list[dict]:
        pass

    @classmethod
    def get_one(cls, id: int) -> Optional[dict]:
        pass

    @classmethod
    def insert (cls,
                rubrique : str,
                nom : str,
                image : str,
                rendu : str,
                ) -> dict :
        pass
    
    @classmethod
    def update (cls,
                id: int,
                rubrique : Optional[str] = None,
                nom : Optional[str] = None,
                image : Optional[str] = None,
                rendu : Optional[str] = None,
                ) -> Optional[dict] :
        pass

    @classmethod
    def update (cls, id: int) -> bool:
        pass