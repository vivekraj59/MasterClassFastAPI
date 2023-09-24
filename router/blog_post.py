from fastapi import APIRouter, Query, Path, Body
from pydantic import BaseModel
from typing import Optional, List, Dict

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


class Image(BaseModel):
    url: str
    alias: str


class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] = {'key1': 'value1'}
    image: Optional[Image] = None


@router.post('/new/{id}')
# here BlogModel is the body parameter.
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'id': id,
        'data': blog,
        'version': version
    }


@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog: BlogModel, id: int,
                   comment_title: int = Query(None,
                                              title='Title of the comment',
                                              description='Some description for comment_title ',
                                              alias='commentTitle',
                                              deprecated=True
                                              ),
                   content: str = Body(...,
                                       min_length=10,
                                       max_length=50,
                                       regex='^[a-z\s]*$'
                                       ),
                   v: Optional[List[str]] = Query(
                       ['1.0', '1.1', '1.2']),  # multiple values
                   comment_id: int = Path(gt=5, le=10)
                   ):
    return {
        'blog': blog,
        'id': id,
        'comment_title': comment_title,
        'content': content,
        'version': v,
        'comment_id': comment_id
    }


def required_functionality():
    return {'message': 'Learning FastAPI is important'}
