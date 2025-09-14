from fastapi import FastAPI
from . import routes, models, database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)
app.include_router(routes.router)
