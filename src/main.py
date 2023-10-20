from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import uvicorn
    
from auth.router import router as auth_router
from todo.router import router as app_router

app = FastAPI(title='todo')

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(auth_router)
app.include_router(app_router)

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)