import logging
logger = logging.getLogger(__name__)

LANGUAGES = {"uk": {}, "en": {}}
CURRENT_LANGUAGE = "uk"

LANGUAGES["uk"] = {
    "bunker_survival": "Виживання в бункері",
    "play": "Грати",
    "settings": "Налаштування",
    "quit": "Вийти",
    "language": "Мова",
    "ukrainian": "Українська",
    "english": "English",
    "back": "Назад",
    "exit_to_menu": "Вийти в меню",
    "game_over": "Гру закінчено",
    "day": "День",
    "health": "Здоров'я",
    "suit_charge": "Заряд костюма",
    "food": "Їжа",
    "water": "Вода",
    "character": "Персонаж",
    "laptop_options": "Інтерфейс Ноутбука",
    "go_on_outing": "Піти на вилазку",
    "charge_suit": "Зарядити скафандр",
    "skip_day": "Пропустити день",
    "last_action_result": "Результат останньої дії",
    "day_skipped": "День минув спокійно.",
    "no_food": "Немає їжі! (-15 здоров'я)",
    "no_water": "Немає води! (-20 здоров'я)",
    "suit_charged_20": "Скафандр заряджено на 20%. День минув за обслуговуванням обладнання.",
    "ai_outing_found_food_small": "Ви знайшли трохи їжі під час вилазки.",
    "ai_outing_found_water_small": "Ви знайшли трохи води під час вилазки.",
    "ai_outing_minor_hazard": "Ви зіткнулися з невеликою небезпекою, але вижили. (-5 здоров'я)",
    "ai_outing_nothing_significant": "Вилазка не принесла результатів.",
    "death_health": "Здоров'я на нулі. Кінець.",
    "death_suit_charge": "Заряд костюма вичерпано. Кінець.",
    "ending_generic_death": "Ви не змогли вижити. Кінець.",
    "ok": "Гаразд",
    "ai_find_food_placeholder": "ШІ: Знайдено їжу (placeholder).",
    "ai_find_water_placeholder": "ШІ: Знайдено воду (placeholder).",
    "ai_minor_danger_placeholder": "ШІ: Невелика небезпека (placeholder).",
    "ai_find_nothing_placeholder": "ШІ: Нічого не знайдено (placeholder).",
    "ai_find_scrap_placeholder": "ШІ: Знайдено металобрухт (placeholder).",
}

LANGUAGES["en"] = {
    "bunker_survival": "Bunker Survival",
    "play": "Play",
    "settings": "Settings",
    "quit": "Quit",
    "language": "Language",
    "ukrainian": "Українська",
    "english": "English",
    "back": "Back",
    "exit_to_menu": "Exit to Menu",
    "game_over": "Game Over",
    "day": "Day",
    "health": "Health",
    "suit_charge": "Suit Charge",
    "food": "Food",
    "water": "Water",
    "character": "Character",
    "laptop_options": "Laptop Interface",
    "go_on_outing": "Go on Outing",
    "charge_suit": "Charge Suit",
    "skip_day": "Skip Day",
    "last_action_result": "Last Action Result",
    "day_skipped": "The day passed peacefully.",
    "no_food": "No food! (-15 health)",
    "no_water": "No water! (-20 health)",
    "suit_charged_20": "Suit charged by 20%. The day was spent on maintenance.",
    "ai_outing_found_food_small": "You found some food during the outing.",
    "ai_outing_found_water_small": "You found some water during the outing.",
    "ai_outing_minor_hazard": "You encountered a minor hazard but survived. (-5 health)",
    "ai_outing_nothing_significant": "The outing yielded nothing significant.",
    "death_health": "Health reached zero. The end.",
    "death_suit_charge": "Suit charge depleted. The end.",
    "ending_generic_death": "You could not survive. The end.",
    "ok": "OK",
    "ai_find_food_placeholder": "AI: Found food (placeholder).",
    "ai_find_water_placeholder": "AI: Found water (placeholder).",
    "ai_minor_danger_placeholder": "AI: Minor danger (placeholder).",
    "ai_find_nothing_placeholder": "AI: Found nothing (placeholder).",
    "ai_find_scrap_placeholder": "AI: Found scrap metal (placeholder).",
}

def set_language(lang_code):
    global CURRENT_LANGUAGE
    if lang_code in LANGUAGES:
        CURRENT_LANGUAGE = lang_code
    else:
        CURRENT_LANGUAGE = "uk"

def get_text(key, **kwargs):
    lang_dict = LANGUAGES.get(CURRENT_LANGUAGE, LANGUAGES["en"])
    text_template = lang_dict.get(key)

    if text_template is None:
        logger.error(f"Localization key '{key}' not found in '{CURRENT_LANGUAGE}'.")
        return f"ERR_NO_TXT_{key}"

    try:
        return text_template.format(**kwargs)
    except KeyError as e:
        logger.error(f"Formatting error for key '{key}': Missing argument {e}")
        return text_template
