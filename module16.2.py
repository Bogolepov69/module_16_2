from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/")
async def root():
  return dict(message="Hello World")

@app.get("/user/{username}/{user_id}")
async def user_page(
  user_id: Annotated[int, Path(gt=0, le=100, description='Enter User ID', example='1')],
  username: str = Path(..., description='Enter Username', example='Username')
) -> dict:
  return {"message": f"Вы вошли как пользователь {username}:{user_id}"}

@app.get("/user/{username}/{age}")
async def user_info(
  username: Annotated[str, Path(min_length=3, max_length=15, description='Enter username', example='UrbanUser')],
  age: Annotated[int, Path(gt=18, le=120, description='Enter age', example='24')]
):
  return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

@app.get("/user/admin")
async def admin_page():
  return {"message": "Вы вошли как администратор"}