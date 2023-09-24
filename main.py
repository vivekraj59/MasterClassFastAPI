from fastapi import FastAPI
from router import blog_get, blog_post
from db import database, models
from db.database import engine


app = FastAPI()  # Create a instance with name app
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get('/hello')  # Creating a endpoints
def index():
    return {'message': 'Hello World'}


models.Base.metadata.create_all(engine)
