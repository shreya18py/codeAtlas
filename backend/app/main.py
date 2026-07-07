from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to CodeAtlas"}


@app.get("/about")
def about():
    return {
        "project": "CodeAtlas",
        "version": "1.0"
    }


@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id
    }


@app.get("/search")
def search(topic: str = "all"):
    return {
        "topic": topic
    }