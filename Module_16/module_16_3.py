from typing import Annotated

import uvicorn
from fastapi import FastAPI, Path

app = FastAPI()

users = {1: "Имя: Example, возраст: 18"}

@app.get("/users")
def get_all_users() -> dict:
    return users

@app.post("/user/{username}/{age}")
def create_user(
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
) -> dict:
    current_id = max(users.keys(), default=0) + 1
    users[current_id] = f"Имя: {username}, возраст: {age}"
    return {"message": f"User {current_id} is registered"}

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
) -> dict:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return {"message": f"User {user_id} has been updated"}

@app.delete("/user/{user_id}")
def update_user(
        user_id: Annotated[
            int,
            Path(
                ge=1,
                le=100,
                description="Enter User ID",
                examples=[15]
            )
        ]
) -> dict:
    users.pop(user_id)
    return {"message": f"User {user_id} has been updated"}


if __name__ == '__main__':
    uvicorn.run(app)
