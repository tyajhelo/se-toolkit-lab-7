def handle_command(text: str) -> str:
    text = (text or "").strip()

    if text == "/start":
        return "Welcome! Use /help to see commands."

    if text == "/help":
        return "Commands: /start, /help, /health, /labs"

    if text == "/health":
        return "Health check not implemented."

    if text == "/labs":
        return "Labs not implemented."

    if text.startswith("/"):
        return f"Unknown command: {text}"

    return "Use /help"
