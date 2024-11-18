from sqlmodel import SQLModel, Field, select
from faker import Faker
from typing import Optional, List
from database import get_session


def fake_stage():
    fake = Faker("fr_FR")
    return Stage(
        poste=fake.job(),
        entreprise=fake.company(),
        expedition=fake.date_this_month().isoformat(),
        url=fake.url()
    )


class Stage(SQLModel, table=True):
    # Definition de la structure de la table = une classe
    __tablename__ = "Stages"
    id: Optional[int] = Field(default=None, primary_key=True)
    poste : str
    entreprise : str
    expedition : str
    url : Optional[str] = None


    @classmethod
    def get_all(cls) -> List[dict]:
        with get_session() as session:
            statement = select(cls)
            results = session.exec(statement).all()
            return [  stage.model_dump() for stage in results  ]

    @classmethod
    def get_one (cls, id: int) -> Optional[dict] :
        with get_session() as session:
            statement = select(cls).where(cls.id == id)
            result = session.exec(statement).first()
            return result.model_dump() if result else None
        

    @classmethod
    def insert (cls, poste: str, entreprise : str, expedition: str, url: str) -> dict:
        with get_session() as session:
            item = cls(poste=poste, entreprise=entreprise, expedition=expedition, url=url)
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
                poste: Optional[str] = None,
                entreprise : Optional[str] = None,
                expedition : Optional[str] = None,
                url : Optional[str] = None,
                ) -> Optional[dict]:
         with get_session() as session:
            statement = select(cls).where(cls.id == id)
            result = session.exec(statement).first()
            if result : 
                if poste is not None:
                    result.poste = poste
                if entreprise is not None:
                    result.entreprise = entreprise
                if expedition is not None:
                    result.expedition = expedition
                if url is not None:
                    result.url = url
                session.add(result)
                session.commit()
                session.refresh(result)
                return result.model_dump()
            return None

if __name__ == '__main__':
    stages = Stage.get_all()
    print(stages)

    stage = Stage.update(id=1000, entreprise="Richnou")

    stage = Stage.get_one(id=1000)
    print(stage)

    stage = Stage.insert(
        poste="",
        entreprise="",
        expedition="",
        url=""
    )

    ok = Stage.delete(id=6)
    print(ok)