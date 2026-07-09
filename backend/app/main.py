from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

docs = []

class Documentation(BaseModel):
    title: str
    language: str
    difficulty: str
    content: str

#routes

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

@app.post("/docs", status_code=201)
def create_documentation(doc: Documentation):
    docs.append(doc)
    return {
        "message": "Documentation created successfully!",
        "documentation": doc
    }

@app.get("/documentations")
def get_all_documentation():
    return docs

@app.get("/documentations/{doc_id}", response_model=Documentation)
def get_udocs(doc_id: int):

    if doc_id < 0 or doc_id >= len(docs):
        raise HTTPException(
        status_code=404,
        detail="Documentation not found"
    )

    return docs[doc_id]

@app.delete("/documentations/{doc_id}")
def delete_doc(doc_id:int):
    if doc_id < 0 or doc_id >= len(docs):
        raise HTTPException(
        status_code=404,
        detail="Documentation not found"
    )
    docs.pop(doc_id)
    return {
        "message": "Documentation deleted successfully!"
    }

@app.put("/documentations/{doc_id}")
def update_doc(doc: Documentation, doc_id: int):
    if doc_id < 0 or doc_id >= len(docs):
        raise HTTPException(
        status_code=404,
        detail="Documentation not found"
    )
    docs[doc_id]=doc
    return {
        "message": "Documentation updated successfully!"
    }
