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
    "laptop_options": "Ноутбук",
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

    # --- Intro Dialogue ---
    "intro_dialogue_1": "Щ-що?",
    "intro_dialogue_2": "Де я?",
    "intro_dialogue_3": "коли я?",
    "intro_dialogue_4": "Де Джон?",
    "intro_dialogue_5": "Ми ж бігли разом?",

    # --- Story Events: Tadmavriel ---
    "tadmavriel_1_text": "Дивний сигнал лунає з вашого радіо. Голос, що називає себе Тадмавріель, пропонує вам порятунок від самотності. Він каже, що знає вихід.",
    "tadmavriel_1_opt1": "Відповісти на сигнал.",
    "tadmavriel_1_opt2": "Ігнорувати його.",
    "tadmavriel_2_text": "Тадмавріель розповідає про портал, який може перенести вас у безпечне місце. Але для його активації потрібен ритуал, що вимагає краплі вашої крові.",
    "tadmavriel_2_opt1": "Погодитись на ритуал.",
    "tadmavriel_2_opt2": "Відмовитись.",
    "find_blood_bottle_1_text": "Вам потрібно знайти щось, щоб зібрати кров. Стара медична аптечка може містити потрібне. Це буде коштувати вам трохи здоров'я.",
    "find_blood_bottle_1_opt1": "Взяти кров (-5 здоров'я).",
    "find_blood_bottle_1_opt2": "Передумати.",
    "tadmavriel_3_text": "Ви зібрали кров. Тадмавріель каже, що ритуал майже готовий. Він зв'яжеться з вами, коли настане час.",
    "tadmavriel_3_opt1": "Чекати.",
    "tadmavriel_4_text": "Портал відкрито. Тадмавріель кличе вас. Це ваш шанс.",
    "tadmavriel_4_opt1": "Увійти в портал.",
    "tadmavriel_4_opt2": "Відмовитись в останню мить.",
    "ending_tadmavriel_escape": "Ви ступаєте в портал і опиняєтеся в дивному, але мирному місці. Ви врятовані... мабуть.",

    # --- Story Events: Organization ---
    "org_1_text": "На ваш комп'ютер надходить зашифроване повідомлення. Невідома 'Організація' пропонує вам приєднатися до них для відновлення цивілізації.",
    "org_1_opt1": "Прийняти пропозицію.",
    "org_1_opt2": "Відхилити.",
    "org_2_text": "Організація просить вас довести свою вірність, знайшовши для них старий артефакт - 'Печатку Порядку', заховану десь у руїнах.",
    "org_2_opt1": "Погодитись на пошуки.",
    "org_2_opt2": "Відмовитись від завдання.",
    "find_seal_1_text": "Ви шукаєте Печатку Порядку. Це небезпечно, але ви знаєте, де шукати.",
    "find_seal_1_opt1": "Почати пошуки.",
    "find_seal_1_opt2": "Відкласти це.",
    "org_3_text": "Ви знайшли Печатку. Організація вражена вашими здібностями і запрошує вас на зустріч.",
    "org_3_opt1": "Передати Печатку.",
    "org_4_text": "Ви передали Печатку. Організація приймає вас у свої лави. Нове майбутнє чекає.",
    "org_4_opt1": "Приєднатися до Організації.",
    "ending_joined_organization": "Ви стали частиною Організації. Ваша самотність закінчилася, але почалася нова, сповнена праці та дисципліни, ера.",

    # --- Story Events: Rejection ---
    "reject_1_text": "Після вашої відмови Організації, ви помічаєте, що за вами стежать. Дивні шуми лунають біля бункера.",
    "reject_1_opt1": "Зміцнити оборону.",
    "reject_1_opt2": "Ігнорувати.",
    "reject_2_text": "Напруга зростає. Ви відчуваєте, що не самі. Хтось намагається проникнути всередину.",
    "reject_2_opt1": "Підготуватися до гіршого.",
    "reject_3_text": "Двері бункера вибухають. Агенти Організації вриваються всередину. Вони не приймають 'ні' як відповідь.",
    "reject_3_opt1": "Це кінець.",
    "ending_death": "Ваш опір був марним. Організація не терпить непокори.",

    # --- Additional Search Protocol Strings ---
    "search_button": "Шукати",
    "search_protocol_start": "Щоб активувати протокол \"S.F.P.A.I.\", напишіть \"/start\"",
    "search_result_not_found": "Нікого не знайдено... Ви самі. Ніхто не прийде до вас.",
    "search_result_found": "Знайдено людину в паралельній реальності.\n\nСтатус \"Вознесіння\": Активний суб'єктом\n\nРекомендовані дії: Перейти до світу \"Misr\" (координати світу: \"Y:#14^3 X:34.4^0 Z:34d^1x\") та активувати вознесіння"
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
    "laptop_options": "Laptop",
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


        # --- Introductory dialog ---
    "intro_dialogue_1": "W-what?",
    "intro_dialogue_2": "Where am I?",
    "intro_dialogue_3": "When am I?",
    "intro_dialogue_4": "Where is John?",
    "intro_dialogue_5": "We were running together?",
    
    # --- Story Events: Tadmavriel ---
    "tadmavriel_1_text": "A strange signal comes from your radio. A voice calling itself Tadmavriel offers you salvation from loneliness. He says he knows the way out.",
    "tadmavriel_1_opt1": "Answer the signal.",
    "tadmavriel_1_opt2": "Ignore it.",
    "tadmavriel_2_text": "Tadmavriel tells you about a portal that can take you to a safe place. But to activate it, a ritual is required, demanding a drop of your blood.",
    "tadmavriel_2_opt1": "Agree to the ritual.",
    "tadmavriel_2_opt2": "Refuse.",
    "find_blood_bottle_1_text": "You need to find something to collect the blood. An old first-aid kit might contain what you need. It will cost you some health.",
    "find_blood_bottle_1_opt1": "Draw blood (-5 health).",
    "find_blood_bottle_1_opt2": "Reconsider.",
    "tadmavriel_3_text": "You have collected the blood. Tadmavriel says the ritual is almost ready. He will contact you when the time comes.",
    "tadmavriel_3_opt1": "Wait.",
    "tadmavriel_4_text": "The portal is open. Tadmavriel is calling you. This is your chance.",
    "tadmavriel_4_opt1": "Enter the portal.",
    "tadmavriel_4_opt2": "Refuse at the last moment.",
    "ending_tadmavriel_escape": "You step into the portal and find yourself in a strange but peaceful place. You are saved... probably.",

    # --- Story Events: Organization ---
    "org_1_text": "An encrypted message arrives on your computer. An unknown 'Organization' offers you to join them to restore civilization.",
    "org_1_opt1": "Accept the offer.",
    "org_1_opt2": "Decline.",
    "org_2_text": "The Organization asks you to prove your loyalty by finding an old artifact for them - the 'Seal of Order', hidden somewhere in the ruins.",
    "org_2_opt1": "Agree to search.",
    "org_2_opt2": "Refuse the task.",
    "find_seal_1_text": "You are searching for the Seal of Order. It's dangerous, but you know where to look.",
    "find_seal_1_opt1": "Start the search.",
    "find_seal_1_opt2": "Postpone it.",
    "org_3_text": "You have found the Seal. The Organization is impressed with your abilities and invites you to a meeting.",
    "org_3_opt1": "Hand over the Seal.",
    "org_4_text": "You have handed over the Seal. The Organization accepts you into its ranks. A new future awaits.",
    "org_4_opt1": "Join the Organization.",
    "ending_joined_organization": "You have become part of the Organization. Your loneliness is over, but a new era of work and discipline has begun.",

    # --- Story Events: Rejection ---
    "reject_1_text": "After you refused the Organization, you notice that you are being watched. Strange noises are heard near the bunker.",
    "reject_1_opt1": "Strengthen defenses.",
    "reject_1_opt2": "Ignore.",
    "reject_2_text": "The tension is rising. You feel that you are not alone. Someone is trying to get inside.",
    "reject_2_opt1": "Prepare for the worst.",
    "reject_3_text": "The bunker door explodes. Agents of the Organization burst in. They don't take 'no' for an answer.",
    "reject_3_opt1": "This is the end.",
    "ending_death": "Your resistance was futile. The Organization does not tolerate disobedience.",

    # --- Additional Search Protocol Strings ---
    "search_button": "Search",
    "search_protocol_start": "To activate the \"S.F.P.A.I.\" protocol, write \"/start\"",
    "search_result_not_found": "No one was found... You're all alone. No one is coming to accompany you",
    "search_result_found": "A person in a parallel reality has been found.\n\nStatus \"Ascension\": Active by subject\n\nRecommended actions: Go to the world \"Misr\" (world coordinates: \"Y:#14^3 X:34.4^0 Z:34d^1x\") and activate the ascent"
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
