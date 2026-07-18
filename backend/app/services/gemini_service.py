from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def generate_documentation(code: str):

    prompt = f"""
You are an expert software engineer.

Generate professional documentation for the following code.

Include:
1. Title
2. Purpose
3. Functions
4. Inputs
5. Outputs
6. Explanation

Code:
{code}
"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    return response.text

def detect_language(filename: str):

    extension = filename.split(".")[-1].lower()

    languages = {
        "py": "Python",
        "cpp": "C++",
        "c": "C",
        "java": "Java",
        "js": "JavaScript",
        "ts": "TypeScript",
        "html": "HTML",
        "css": "CSS",
        "go": "Go",
        "rs": "Rust",
        "php": "PHP",
        "rb": "Ruby"
    }

    return languages.get(extension, "Unknown")