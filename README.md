# CodeAtlas

AI-powered documentation generator for source code.

## Features

- Generate documentation from pasted code
- Upload source code files
- AI-powered documentation using Google Gemini
- Automatic programming language detection
- MongoDB storage
- FastAPI REST API
- Interactive Swagger UI

## Tech Stack

- FastAPI
- MongoDB
- Google Gemini API
- Python
- Pydantic

## Future Roadmap

- Upload entire project folders
- GitHub repository documentation
- React frontend
- Markdown rendering
- Search & filtering
- Export as PDF/Markdown

## Run locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload