from pathlib import Path
import os


def load_env_file(path: str) -> None:
    p = Path(path)
    if not p.exists():
        return
    for raw in p.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


load_env_file("../.env.bot.secret")
load_env_file(".env.bot.secret")

LMS_API_BASE_URL = os.getenv("LMS_API_BASE_URL", "http://localhost:42002").rstrip("/")
LMS_API_KEY = os.getenv("LMS_API_KEY", "my-secret-api-key")
