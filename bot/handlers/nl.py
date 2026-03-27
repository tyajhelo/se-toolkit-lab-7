from services.router import route

def handle_natural_language(text: str) -> str:
    return route(text)
