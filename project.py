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