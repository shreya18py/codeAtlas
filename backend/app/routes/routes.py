from fastapi import APIRouter, HTTPException, UploadFile, File
from bson import ObjectId
from pymongo import ASCENDING


from app.database.database import docs_collection
from app.models.models import Documentation, CodeInput
from app.services.gemini_service import (
    generate_documentation,
    detect_language
)

router = APIRouter()

# routes

@router.get("/")
def home():
    return {"message": "Welcome to CodeAtlas"}


@router.get("/about")
def about():
    return {
        "project": "CodeAtlas",
        "version": "1.0"
    }


@router.get("/user/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id
    }

# CREATE
@router.post("/docs", status_code=201)
def create_documentation(doc: Documentation):

    result = docs_collection.insert_one(doc.model_dump())

    return {
        "message": "Documentation created successfully!",
        "id": str(result.inserted_id)
    }


# READ ALL
@router.get("/documentations")
def get_all_documentation():

    documents = []

    for doc in docs_collection.find():
        doc["id"] = str(doc["_id"])
        del doc["_id"]
        documents.append(doc)

    return documents


# READ ONE
@router.get("/documentations/{doc_id}", response_model=Documentation)
def get_documentation(doc_id: str):

    document = docs_collection.find_one(
        {"_id": ObjectId(doc_id)}
    )

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Documentation not found"
        )

    return document


# DELETE
@router.delete("/documentations/{doc_id}")
def delete_doc(doc_id: str):

    result = docs_collection.delete_one(
        {"_id": ObjectId(doc_id)}
    )

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Documentation not found"
        )

    return {
        "message": "Documentation deleted successfully!"
    }


# UPDATE
@router.put("/documentations/{doc_id}")
def update_doc(doc: Documentation, doc_id: str):

    result = docs_collection.update_one(
        {"_id": ObjectId(doc_id)},
        {"$set": doc.model_dump()}
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Documentation not found"
        )

    return {
        "message": "Documentation updated successfully!"
    }


# TEST DATABASE
@router.get("/test-db")
def test_db():

    docs_collection.insert_one({
        "message": "MongoDB Connected!"
    })

    return {
        "message": "Inserted successfully!"
    }

#search
@router.get("/search")
def search(
    language: str = None,
    difficulty: str = None,
    title: str = None,
    sort: str = None
):
    query = {}

    if language:
        query["language"] = language

    if difficulty:
        query["difficulty"] = difficulty

    if title:
        query["title"] = {
        "$regex": title,
        "$options": "i"
    }

    documents = []

    for doc in docs_collection.find(query):
        doc["id"] = str(doc["_id"])
        del doc["_id"]
        documents.append(doc)

    return documents

#api recieves code
@router.post("/generate-docs")
def generate_docs(data: CodeInput):

    documentation = generate_documentation(data.code)

    return {
        "documentation": documentation
    }

#upload file
@router.post("/upload-file")
async def upload_file(file: UploadFile = File(...)):

    code = await file.read()
    code = code.decode("utf-8")

    language = detect_language(file.filename)

    documentation = generate_documentation(code)

    docs_collection.insert_one({
        "filename": file.filename,
        "language": language,
        "documentation": documentation,
        "source": "upload"
    })

    return {
    "filename": file.filename,
    "language": language,
    "documentation": documentation
}