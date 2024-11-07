import uvicorn
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def main_page():
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin_page():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user_page(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user")
async def user_info_page(user_name: str = "Test User", user_age: int = 18):
    return {"message": f"Информация о пользователе. Имя: {user_name}, Возраст: {user_age}"}


if __name__ == '__main__':
    uvicorn.run(app)