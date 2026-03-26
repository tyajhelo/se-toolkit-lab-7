def handle_command(text: str) -> str:
    text = (text or "").strip()

    if text == "/start":
        return (
            "Welcome to the LMS bot.\n"
            "Use /help to see available commands."
        )

    if text == "/help":
        return (
            "Available commands:\n"
            "/start - welcome message\n"
            "/help - show this help\n"
            "/health - backend health placeholder\n"
            "/labs - list labs placeholder"
        )

    if text == "/health":
        return "Health check is not implemented yet."

    if text == "/labs":
        return "Labs list is not implemented yet."

    if text.startswith("/"):
        return f"Unknown command: {text}\nUse /help to see available commands."

    return "Send /help to see available commands."
