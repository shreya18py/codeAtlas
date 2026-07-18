import os

ALLOWED_EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".cpp",
    ".c",
    ".java",
    ".go",
    ".rs",
    ".cs"
}


def get_source_files(folder_path):
    source_files = []

    for root, dirs, files in os.walk(folder_path):

        dirs[:] = [
            d for d in dirs
            if d not in {
                "venv",
                "__pycache__",
                ".git",
                "node_modules"
            }
        ]

        for file in files:
            extension = os.path.splitext(file)[1]

            if extension in ALLOWED_EXTENSIONS:
                source_files.append(
                    os.path.join(root, file)
                )

    return source_files