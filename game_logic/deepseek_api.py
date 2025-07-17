from .config import DEFAULT_LANGUAGE
from .localization import get_text
import logging
logger = logging.getLogger(__name__)

API_URL = "https://api.deepseek.com/v1/chat/completions"

placeholder_events = [
    {'id': 'ai_find_food_placeholder', 'text_key': 'ai_find_food_placeholder', 'effect': {'food': 1}},
    {'id': 'ai_find_water_placeholder', 'text_key': 'ai_find_water_placeholder', 'effect': {'water': 1}},
    {'id': 'ai_minor_danger_placeholder', 'text_key': 'ai_minor_danger_placeholder', 'effect': {'health': -3}},
    {'id': 'ai_find_nothing_placeholder', 'text_key': 'ai_find_nothing_placeholder', 'effect': {}},
    {'id': 'ai_find_scrap_placeholder', 'text_key': 'ai_find_scrap_placeholder', 'effect': {'found_item': 'scrap_metal'}},
]

def get_random_placeholder_event():
    chosen_event = random.choice(placeholder_events)
    return {
        'id': chosen_event['id'],
        'text': get_text(chosen_event['text_key']),
        'options': [{'text': get_text('ok'), 'effect': chosen_event.get('effect', {})}]
     }

def get_ai_event():
    
    logger.warning("DeepSeek API integration is disabled in this version. Using placeholder event.")
    return get_random_placeholder_event()
