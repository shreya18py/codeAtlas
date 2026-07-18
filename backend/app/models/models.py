from pydantic import BaseModel

class Documentation(BaseModel):
    title: str
    language: str
    difficulty: str
    content: str

class CodeInput(BaseModel):
    code: str

class GeneratedDocumentation(BaseModel):
    filename: str
    language: str
    documentation: str
    source: str