import datetime
from typing import Annotated
from fastapi import APIRouter, HTTPException, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import select

from database import async_session_factory
from todo.models import Task

templates = Jinja2Templates(directory='templates')

router = APIRouter(
    prefix='/todo',
    tags=['todo']
)

@router.get('/{user_id}')
async def get_todo_app(request: Request, user_id: int):
    async with async_session_factory() as session:
        tasks = await session.execute(select(Task).where(Task.user_id == user_id))
        tasks = tasks.scalars().all()
    return templates.TemplateResponse('todo.html', {'request': request, 'user_id': user_id, 'tasks': tasks})


@router.post('/{user_id}/find_task')
async def find_task(request: Request, user_id: int, task_name: Annotated[str, Form()]):
    async with async_session_factory() as session:
        tasks = await session.execute(select(Task).where(Task.user_id == user_id).where(Task.task_name == task_name))
        tasks = tasks.scalars().all()
    return templates.TemplateResponse('todo.html', {'request': request, 'user_id': user_id, 'tasks': tasks})


@router.post('/{user_id}/add_task')
async def add_task(response: RedirectResponse, user_id: int, task_name: Annotated[str, Form()], creation_date: Annotated[datetime.datetime, Form()] = None):
    async with async_session_factory() as session:
        task = Task(task_name = task_name, user_id = user_id, creation_date = creation_date)
        session.add(task)
        await session.commit()
    return RedirectResponse(url=f"/todo/{user_id}", status_code=303)


@router.post('/{user_id}/delete_task')
async def delete_task(response: RedirectResponse, user_id: int, task_name: Annotated[str, Form()]):
    async with async_session_factory() as session:
        task = await session.execute(select(Task).where(Task.user_id == user_id, Task.task_name == task_name))
        task = task.scalar_one_or_none()    
        if task:
            await session.delete(task)
            await session.commit()
            return RedirectResponse(url=f"/todo/{user_id}", status_code=303)


