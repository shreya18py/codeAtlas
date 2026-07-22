from git import Repo
import tempfile


def clone_repo(repo_url: str):

    temp_dir = tempfile.mkdtemp()

    Repo.clone_from(repo_url, temp_dir)

    return temp_dir