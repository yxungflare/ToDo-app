from fastapi import APIRouter, Request, Form, Response
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import select

from typing import Annotated

from database import async_session_factory
from auth.models import User

templates = Jinja2Templates(directory='templates')

router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)


async def get_db():
    async with async_session_factory() as session:
        yield session


@router.get('/registration')
async def get_auth_page(request: Request):
    return templates.TemplateResponse('registration.html', {'request': request})


@router.post('/register')
async def user_register(request: Request, username: Annotated[str, Form()], email: Annotated[str, Form()], password: Annotated[str, Form()]):
    async with async_session_factory() as session:
        user = User(username = username, email = email, hashed_password = password)
        session.add(user)
        await   session.commit()
    return templates.TemplateResponse('login.html', {'request': request})


@router.get('/login')
async def get_auth_page(request: Request):
    return templates.TemplateResponse('login.html', {'request': request})


@router.post('/login')
async def user_login(response: Response, email: Annotated[str, Form()], password: Annotated[str, Form()]):
    async with async_session_factory() as session:
        user = await session.execute(select(User).where(User.email == email).where(User.hashed_password == password))
        user = user.scalar_one_or_none()

        if not user:
            return {"Error": "User not found or wrong password"}
        return RedirectResponse(url=f"/todo/{user.id}", status_code=303)