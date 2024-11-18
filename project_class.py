# projet_class.py
from sqlmodel import SQLModel, Field
from typing import Optional, List
from database import get_session
from sqlmodel import select


class Projet(SQLModel, table=True):
    # Définition de la structure de la table = une classe
    __tablename__ = "Projects"
    id: Optional[int] = Field(default=None, primary_key=True)
    rubrique: str
    nom: str
    image: str
    rendu: str
    url: Optional[str]

    @classmethod
    def get_all(cls) -> List[dict]:
        with get_session() as session:
            statement = select(cls)
            results = session.exec(statement).all()
            return [  projet.model_dump() for projet in results  ]

    @classmethod
    def get_one (cls, id: int) -> Optional[dict] :
        with get_session() as session:
            statement = select(cls).where(cls.id == id)
            result = session.exec(statement).first()
            return result.model_dump() if result else None
        

    @classmethod
    def insert (cls, rubrique: str, nom : str, image: str, rendu: str) -> dict:
        with get_session() as session:
            item = cls(rubrique=rubrique, nom=nom, image=image, rendu=rendu)
            session.add(item)
            session.commit()
            session.refresh(item)
            return item.model_dump()



    @classmethod
    def update (cls, id: int) -> bool:
        pass



if __name__ == '__main__':
    projets = Projet.get_all()
    print(projets)

    projet = Projet.get_one(id=1)
    print(projet)

    projet = Projet.insert(
        rubrique="retardataire",
        nom="Quentin",
        image="image.jpg",
        rendu="2024-12-24"
    )

    