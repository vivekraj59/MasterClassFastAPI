from fastapi import APIRouter, status, Response, Depends
from enum import Enum
from typing import Optional
from router.blog_post import required_functionality

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


@router.get(
    '/all',
    summary='Retrieve all the blogs',
    description='This api simulates fetching all blogs.'
)
# Defining optional parameter in 2 diff way. these are called query parameter.
def get_all_blog(page=1, page_size: Optional[int] = None, req_parameter: dict = Depends(required_functionality)):
    return {'message': f'All {page_size} blogs on page {page}', 'req': req_parameter}


# In this example we are going to combine path parameter with query parameter
# Path parameter
@router.get('/{id}/comments/{comment_id}', tags=['comment'])
# Query parameter
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {'message': f'blog_id {id}, comment_id: {comment_id}, valid {valid}, username {username}'}


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@router.get('/type/{type}')
# Creating the method the handle the request.
def get_blog_type(type: BlogType):
    return {'message': f'Blog type {type}'}


# Path parameter with type int, fastapi uses pydantic to validate the parameter.
@router.get('/{id}', status_code=status.HTTP_200_OK)  # status code
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND  # Response code
    else:
        response.status_code = status.HTTP_200_OK
    return {'message': f'Blog with {id}'}
