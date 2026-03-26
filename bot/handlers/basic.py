from services.lms_api import get_health_text, get_labs_text, get_scores_text


def handle_command(text: str) -> str:
    text = (text or "").strip()

    if text == "/start":
        return (
            "Welcome to the LMS bot.\n"
            "I can show backend status, labs, and scores.\n"
            "Use /help to see available commands."
        )

    if text == "/help":
        return (
            "Available commands:\n"
            "/start - welcome message\n"
            "/help - show this help\n"
            "/health - backend status and item count\n"
            "/labs - list available labs\n"
            "/scores <lab> - show pass rates for a lab"
        )

    if text == "/health":
        return get_health_text()

    if text == "/labs":
        return get_labs_text()

    if text.startswith("/scores"):
        parts = text.split(maxsplit=1)
        lab = parts[1] if len(parts) > 1 else ""
        return get_scores_text(lab)

    if text.startswith("/"):
        return f"Unknown command: {text}\nUse /help to see available commands."

    return "Use /help to see available commands."
