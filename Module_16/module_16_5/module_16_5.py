from typing import Annotated, List

import uvicorn
from fastapi import FastAPI, HTTPException, Path, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

templates = Jinja2Templates(directory="templates")
users = []

class User(BaseModel):
    id : int
    username : str
    age: int


def find_user(user_id: int) -> int | None:
    """
    Находит пользователя по id, и возвращает его индекс в списке
    :param user_id: int
    :return: User
    """
    for idx, user in enumerate(users):
        if user.id == user_id:
            return idx
    return None


@app.get("/")
def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get("/user/{user_id}")
def get_user(
        request: Request,
        user_id: Annotated[
            int,
            Path(
                ge=1,
                le=100,
                description="Enter User ID",
                examples=[15]
            )
        ]
)-> HTMLResponse:
    current_idx = find_user(user_id)
    if current_idx is None:
        raise HTTPException(status_code=404, detail="User not found")
    return templates.TemplateResponse("users.html", {"request": request, "user": users[current_idx]})


@app.post("/user/{username}/{age}")
def create_user(
        request: Request,
        username: Annotated[
            str,
            Path(
                min_length=5,
                max_length=20,
                description="Enter Username",
                examples=["UrbanUser"]
            )
        ],
        age: Annotated[
            int,
            Path(
                ge=18,
                le=120,
                description="Enter age",
                examples=[19]
            )
        ],
)-> HTMLResponse:
    current_id = users[-1].id + 1 if users else 1
    new_user = User(id=current_id, username=username, age=age)
    users.append(new_user)
    return templates.TemplateResponse("users.html", {"request": request, "user": new_user})

@app.put("/user/{user_id}/{username}/{age}")
def update_user(
        user_id: Annotated[
            int,
            Path(
                ge=1,
                le=100,
                description="Enter User ID",
                examples=[15]
            )
        ],
        username: Annotated[
            str,
            Path(
                min_length=5,
                max_length=20,
                description="Enter Username",
                examples=["UrbanUser"]
            )
        ],
        age: Annotated[
            int,
            Path(
                ge=18,
                le=120,
                description="Enter age",
                examples=[19]
            )
        ]
) -> User:

    current_idx = find_user(user_id)
    if current_idx is None:
        raise HTTPException(status_code=404, detail="User not found")
    users[current_idx].username = username
    users[current_idx].age = age
    return users[current_idx]

@app.delete("/user/{user_id}")
def delete_user(
        user_id: Annotated[
            int,
            Path(
                ge=1,
                le=100,
                description="Enter User ID",
                examples=[15]
            )
        ]
) -> User:
    current_idx = find_user(user_id)
    if current_idx is None:
        raise HTTPException(status_code=404, detail="User not found")
    return users.pop(current_idx)


if __name__ == '__main__':
    uvicorn.run(app)