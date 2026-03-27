from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

MAIN_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="What labs are available?",
                callback_data="labs"
            ),
            InlineKeyboardButton(
                text="Show me scores for lab 4",
                callback_data="scores_lab_04"
            ),
        ],
        [
            InlineKeyboardButton(
                text="How many students are enrolled?",
                callback_data="learners"
            ),
            InlineKeyboardButton(
                text="Which lab has the lowest pass rate?",
                callback_data="lowest_pass_rate"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Sync the data",
                callback_data="sync_data"
            ),
        ],
    ]
)
