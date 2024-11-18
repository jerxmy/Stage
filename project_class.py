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
    def delete (cls, id: int) -> bool:
        with get_session() as session:
            statement = select(cls).where(cls.id == id)
            result = session.exec(statement).first()
            if result:
                session.delete(result)
                session.commit()
                return True
            return False


    @classmethod
    def update (cls, 
                id: int,
                rubrique: Optional[str] = None,
                nom : Optional[str] = None,
                image : Optional[str] = None,
                rendu : Optional[str] = None,
                ) -> Optional[dict]:
         with get_session() as session:
            statement = select(cls).where(cls.id == id)
            result = session.exec(statement).first()
            if result : 
                if rubrique is not None:
                    result.rubrique = rubrique
                if nom is not None:
                    result.nom = nom
                if image is not None:
                    result.image = image
                if rendu is not None:
                    result.rendu = rendu
                session.add(result)
                session.commit()
                session.refresh(result)
                return result.model_dump()
            return None

if __name__ == '__main__':
    projets = Projet.get_all()
    print(projets)

    projet = Projet.update(id=1, nom="Richnou")

    projet = Projet.get_one(id=1)
    print(projet)

    # projet = Projet.insert(
    #     rubrique="retardataire",
    #     nom="Quentin",
    #     image="image.jpg",
    #     rendu="2024-12-24"
    # )

    ok = Projet.delete(id=6)
    print(ok)

    