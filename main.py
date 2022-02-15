from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    description: str
    published_at: Optional[bool]


app = FastAPI()

@app.get('/')
def index():
    return 'hello'

@app.get('/blog')
def item(limit=10, published: bool = True):
    # return published

    if published:
        return {'data': f'{limit}件'}
    else:
        return {'data': '非公開'}

@app.get('/about')
def about():
    return {'data': {'about page'}}

@app.get('/blog/category')
def category():
    return {'data': 'all category'}

@app.get('/blog/{id}')
def show(id:int):
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id, limit: Optional[str] = None):
    return {'data': {id, limit, 'comments'}}

@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': blog}

# if __name__ == "__main__":
#     uvicorn.run(app, port=8080, host='0.0.0.0')