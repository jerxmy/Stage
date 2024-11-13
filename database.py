from sqlmodel import SQLModel, create_engine, Session

file_name = "database.sqlite"

# Initialiser le moteur 
engine = create_engine(f"sqlite:///{file_name}")

# Créer tables si nécessaire 
SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)