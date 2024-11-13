from sqlmodel import SQLModel, Field
from faker import Faker
from typing import Optional

class Stage(SQLModel, table=True):
    # Definition de la structure de la table = une classe
    __tablename__ = "Stages"
    id: Optional[int] = Field(default=None, primary_key=True)
    poste : str
    entreprise : str
    expedition : str
    url : Optional[str] = None

def fake_stage():
    fake = Faker("fr_FR")
    return Stage(
        poste=fake.job(),
        entreprise=fake.company(),
        expedition=fake.date_this_month().isoformat(),
        url=fake.url()
    )