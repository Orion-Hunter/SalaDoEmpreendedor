from databases.database import SessionLocal, engine
import models.model as model

model.Base.metadata.create_all(bind=engine)


def get_db():
    try:
            db = SessionLocal()
            yield db
    finally:
            db.close()   
