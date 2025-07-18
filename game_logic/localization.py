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
    "found_scrap": "Ви знайшли металобрухт під час вилазки.",
    "scrap_count": "Металобрухт: {}",

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
    "search_result_found": "Знайдено людину в паралельній реальності.\n\nСтатус \"Вознесіння\": Активний суб'єктом\n\nРекомендовані дії: Перейти до світу \"Misr\" (координати світу: \"Y:#14^3 X:34.4^0 Z:34d^1x\") та активувати вознесіння",

    # --- Modules ---
    "modules": "Модулі",
    "medical_module": "Медичний модуль",
    "food_module": "Харчовий модуль",
    "water_module": "Модуль фільтрації води",
    "craft": "Створити",
    "use": "Використати",
    "module_crafted_medical": "Медичний модуль створено",
    "module_crafted_food": "Харчовий модуль створено",
    "module_crafted_water": "Модуль фільтрації води створено",
    "module_used_medical": "Медичний модуль використано. Здоров'я відновлено",
    "module_used_food": "Харчовий модуль виробив {} банок супу",
    "module_used_water": "Модуль фільтрації виробив {} пляшок води",
    "module_cooldown": "Модуль можна використати через {} днів",
    "not_enough_scrap": "Недостатньо металобрухту",
    "medical_module_desc": "Лікує рани кожні 2 дні (25 металобрухту)",
    "food_module_desc": "Виробляє 1-3 банки супу кожні 2 дні (17 металобрухту)",
    "water_module_desc": "Фільтрує 1-3 пляшки води кожні 2 дні (17 металобрухту)",
    "suit_no_charge": "Недостатньо заряду костюма для вилазки! Спочатку зарядіть його.",

    # --- Outing Narrative Texts ---
    "outing_narrative_food_1": "Повільно крокуючи порожніми вулицями, я помітив закинуту будівлю зі стертою вивіскою. Це виявився старий магазин, двері якого скрипнули під моїм натиском. Усередині — тиша, запах пилу й розбиті полиці. Проте, оглянувшись, я знайшов консерви.",
    "outing_narrative_food_2": "У підвалі напівзруйнованого будинку я натрапив на старий бункер. Двері були відчинені, всередині — сліди поспішної евакуації. На полицях збереглися кілька банок з їжею.",
    "outing_narrative_water_1": "Серед руїн я знайшов стару аптеку. У задній кімнаті виявився автомат з водою, в якому досі зберігалося кілька пляшок.",
    "outing_narrative_water_2": "Під час обстеження підземного паркінга я помітив склад з припасами. Більшість була зіпсована, але кілька пляшок води залишились придатними.",
    "outing_narrative_danger_1": "Прокрадаючись повз завалений міст, я не помітив нестабільну конструкцію. Частина балки впала, ледь не зачепивши мене. Я встиг відскочити, але при цьому пошкодив скафандр.",
    "outing_narrative_danger_2": "У пошуках припасів я забрів в радіаційну зону. Лічильник Гейгера запищав занадто пізно. Я швидко покинув небезпечну територію, але доза опромінення вже вплинула на моє здоров'я.",
    "outing_narrative_scrap_1": "Під час обстеження старої фабрики я знайшов склад запчастин. Більшість деталей заіржавіла, але деякі металеві компоненти ще можна використати.",
    "outing_narrative_scrap_2": "У гаражному комплексі я натрапив на автомайстерню. Серед розкиданих інструментів та деталей вдалося знайти придатний для переробки металобрухт.",
    "outing_narrative_nothing_1": "Години пошуків у зруйнованому торговому центрі не принесли результатів. Все цінне давно розграбовано.",
    "outing_narrative_nothing_2": "Я обстежив житловий комплекс, але знайшов лише порожні квартири та розбиті меблі. Нічого корисного не вдалося виявити.",

    # --- Diary ---
    "diary": "Щоденник",
    "diary_title": "Записи в щоденнику",
    "no_diary_entries": "Поки що немає записів у щоденнику..."
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
    "found_scrap": "You found some scrap metal during the outing.",
    "scrap_count": "Scrap: {}",


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
    "search_result_found": "A person in a parallel reality has been found.\n\nStatus \"Ascension\": Active by subject\n\nRecommended actions: Go to the world \"Misr\" (world coordinates: \"Y:#14^3 X:34.4^0 Z:34d^1x\") and activate the ascent",

    # --- Modules ---
    "modules": "Модулі",
    "medical_module": "Медичний модуль",
    "food_module": "Харчовий модуль",
    "water_module": "Модуль фільтрації води",
    "craft": "Створити",
    "use": "Використати",
    "module_crafted_medical": "Медичний модуль створено",
    "module_crafted_food": "Харчовий модуль створено",
    "module_crafted_water": "Модуль фільтрації води створено",
    "module_used_medical": "Медичний модуль використано. Здоров'я відновлено",
    "module_used_food": "Харчовий модуль виробив {} банок супу",
    "module_used_water": "Модуль фільтрації виробив {} пляшок води",
    "module_cooldown": "Модуль можна використати через {} днів",
    "not_enough_scrap": "Недостатньо металобрухту",
    "medical_module_desc": "Лікує рани кожні 2 дні (25 металобрухту)",
    "food_module_desc": "Виробляє 1-3 банки супу кожні 2 дні (17 металобрухту)",
    "water_module_desc": "Фільтрує 1-3 пляшки води кожні 2 дні (17 металобрухту)",
    "suit_no_charge": "Недостатньо заряду костюма для вилазки! Спочатку зарядіть його.",

    # --- Outing Narrative Texts ---
    "outing_narrative_food_1": "Повільно крокуючи порожніми вулицями, я помітив закинуту будівлю зі стертою вивіскою. Це виявився старий магазин, двері якого скрипнули під моїм натиском. Усередині — тиша, запах пилу й розбиті полиці. Проте, оглянувшись, я знайшов консерви.",
    "outing_narrative_food_2": "У підвалі напівзруйнованого будинку я натрапив на старий бункер. Двері були відчинені, всередині — сліди поспішної евакуації. На полицях збереглися кілька банок з їжею.",
    "outing_narrative_water_1": "Серед руїн я знайшов стару аптеку. У задній кімнаті виявився автомат з водою, в якому досі зберігалося кілька пляшок.",
    "outing_narrative_water_2": "Під час обстеження підземного паркінга я помітив склад з припасами. Більшість була зіпсована, але кілька пляшок води залишились придатними.",
    "outing_narrative_danger_1": "Прокрадаючись повз завалений міст, я не помітив нестабільну конструкцію. Частина балки впала, ледь не зачепивши мене. Я встиг відскочити, але при цьому пошкодив скафандр.",
    "outing_narrative_danger_2": "У пошуках припасів я забрів в радіаційну зону. Лічильник Гейгера запищав занадто пізно. Я швидко покинув небезпечну територію, але доза опромінення вже вплинула на моє здоров'я.",
    "outing_narrative_scrap_1": "Під час обстеження старої фабрики я знайшов склад запчастин. Більшість деталей заіржавіла, але деякі металеві компоненти ще можна використати.",
    "outing_narrative_scrap_2": "У гаражному комплексі я натрапив на автомайстерню. Серед розкиданих інструментів та деталей вдалося знайти придатний для переробки металобрухт.",
    "outing_narrative_nothing_1": "Години пошуків у зруйнованому торговому центрі не принесли результатів. Все цінне давно розграбовано.",
    "outing_narrative_nothing_2": "Я обстежив житловий комплекс, але знайшов лише порожні квартири та розбиті меблі. Нічого корисного не вдалося виявити.",

    # --- Diary ---
    "diary": "Щоденник",
    "diary_title": "Записи в щоденнику",
    "no_diary_entries": "Поки що немає записів у щоденнику..."
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
    "found_scrap": "You found some scrap metal during the outing.",
    "scrap_count": "Scrap: {}",


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
    "search_result_found": "A person in a parallel reality has been found.\n\nStatus \"Ascension\": Active by subject\n\nRecommended actions: Go to the world \"Misr\" (world coordinates: \"Y:#14^3 X:34.4^0 Z:34d^1x\") and activate the ascent",

    # --- Modules ---
    "modules": "Модулі",
    "medical_module": "Медичний модуль",
    "food_module": "Харчовий модуль",
    "water_module": "Модуль фільтрації води",
    "craft": "Створити",
    "use": "Використати",
    "module_crafted_medical": "Медичний модуль створено",
    "module_crafted_food": "Харчовий модуль створено",
    "module_crafted_water": "Модуль фільтрації води створено",
    "module_used_medical": "Медичний модуль використано. Здоров'я відновлено",
    "module_used_food": "Харчовий модуль виробив {} банок супу",
    "module_used_water": "Модуль фільтрації виробив {} пляшок води",
    "module_cooldown": "Модуль можна використати через {} днів",
    "not_enough_scrap": "Недостатньо металобрухту",
    "medical_module_desc": "Лікує рани кожні 2 дні (25 металобрухту)",
    "food_module_desc": "Виробляє 1-3 банки супу кожні 2 дні (17 металобрухту)",
    "water_module_desc": "Фільтрує 1-3 пляшки води кожні 2 дні (17 металобрухту)",
    "suit_no_charge": "Недостатньо заряду костюма для вилазки! Спочатку зарядіть його.",

    # --- Outing Narrative Texts ---
    "outing_narrative_food_1": "Walking slowly through empty streets, I noticed an abandoned building with a faded sign. It turned out to be an old store, its door creaking under my push. Inside - silence, smell of dust and broken shelves. However, looking around, I found some canned food.",
    "outing_narrative_food_2": "In the basement of a half-destroyed house, I stumbled upon an old bunker. The door was open, inside - signs of hasty evacuation. A few cans of food remained on the shelves.",
    "outing_narrative_water_1": "Among the ruins, I found an old pharmacy. In the back room was a water dispenser that still contained a few bottles.",
    "outing_narrative_water_2": "While examining an underground parking lot, I noticed a supply storage. Most was spoiled, but several bottles of water remained usable.",
    "outing_narrative_danger_1": "Sneaking past a collapsed bridge, I didn't notice an unstable structure. Part of the beam fell, barely missing me. I managed to jump away, but damaged my suit in the process.",
    "outing_narrative_danger_2": "Searching for supplies, I wandered into a radiation zone. The Geiger counter beeped too late. I quickly left the dangerous area, but the radiation dose had already affected my health.",
    "outing_narrative_scrap_1": "While examining an old factory, I found a parts warehouse. Most parts were rusty, but some metal components could still be used.",
    "outing_narrative_scrap_2": "In a garage complex, I came across an auto repair shop. Among scattered tools and parts, I managed to find scrap metal suitable for recycling.",
    "outing_narrative_nothing_1": "Hours of searching in a destroyed mall yielded no results. Everything valuable was looted long ago.",
    "outing_narrative_nothing_2": "I examined a residential complex but found only empty apartments and broken furniture. Nothing useful was discovered.",

    # --- Diary ---
    "diary": "Щоденник",
    "diary_title": "Записи в щоденнику",
    "no_diary_entries": "Поки що немає записів у щоденнику..."
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
