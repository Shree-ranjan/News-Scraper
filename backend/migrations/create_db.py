from db.database import Database
import db.models as models

print("Creating Database ................")
Base = models.Base
engine = Database().get_engine()
Base.metadata.create_all(engine)
