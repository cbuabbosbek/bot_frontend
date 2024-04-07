from telebot import types
from Models.main import Option

# Helper function to generate inline keyboard markup
def generate_markup_languages():
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(f"O'zbek Tili", callback_data=f"uzlatin")
    btn2 = types.InlineKeyboardButton(f"Ўзбек тили", callback_data=f"uzkiril")
    btn3 = types.InlineKeyboardButton(f"Русский язык", callback_data=f"ru")
    markup.add(btn1, btn2, btn3)
    return markup

# Helper function to generate inline keyboard markup
def generate_option_markup(options: list[Option], question_number: int) -> types.InlineKeyboardMarkup:
    select_symbol = "⚪️"
    markup = types.InlineKeyboardMarkup(row_width=2)
    for option in options:
        markup.add(types.InlineKeyboardButton(text=f"{select_symbol} {option.option_text}", callback_data=f"{question_number}_{option.id}_none"))
    return markup
