import random   
EVENTS = {
    "tadmavriel_1": { 
        "id": "tadmavriel_1",
        "text_key": "tadmavriel_1_text",
        "options": [
            {"text_key": "tadmavriel_1_opt1", "next_event": "tadmavriel_2"},
            {"text_key": "tadmavriel_1_opt2", "effect": {"set_flag": ["tadmavriel_declined_initial", True]}}
        ],
        "condition_day_gte": 10,
        "condition_flag_false": "tadmavriel_storyline_started",
        "repeatable": False 
    },
    "tadmavriel_2": {
        "id": "tadmavriel_2",
        "text_key": "tadmavriel_2_text",
        "options": [
            {"text_key": "tadmavriel_2_opt1", "effect": {"set_flag": ["tadmavriel_quest_accepted", True]}, "next_event": "find_blood_bottle_1"},
            {"text_key": "tadmavriel_2_opt2", "effect": {"set_flag": ["tadmavriel_quest_accepted", False]}}
        ]
    },
    "find_blood_bottle_1": {
        "id": "find_blood_bottle_1",
        "text_key": "find_blood_bottle_1_text",
        "options": [
            {"text_key": "find_blood_bottle_1_opt1", "effect": {"health": -5, "set_flag": ["blood_bottle_found", True]}, "next_event": "tadmavriel_3"},
            {"text_key": "find_blood_bottle_1_opt2"}
        ],
        "condition_flag_true": "tadmavriel_quest_accepted"
    },
    "tadmavriel_3": {
        "id": "tadmavriel_3",
        "text_key": "tadmavriel_3_text",
        "options": [
            {"text_key": "tadmavriel_3_opt1", "effect": {"set_flag": ["ritual_ready", True]}}
        ],
        "condition_flag_true": "blood_bottle_found",
        "repeatable": False
    },
    "tadmavriel_4": {
        "id": "tadmavriel_4",
        "text_key": "tadmavriel_4_text",
        "options": [
            {"text_key": "tadmavriel_4_opt1", "effect": {"set_flag": ["entered_portal_with_tadmavriel", True], "ending": "ending_tadmavriel_escape"}},
            {"text_key": "tadmavriel_4_opt2", "effect": {"set_flag": ["refused_portal_tadmavriel", True]}}
        ],
        "condition_flag_true": "ritual_ready",
        "condition_day_gte": 12
    },
    "org_1": { 
        "id": "org_1",
        "text_key": "org_1_text",
        "options": [
            {"text_key": "org_1_opt1", "next_event": "org_2"},
            {"text_key": "org_1_opt2", "effect": {"set_flag": ["org_declined_initial", True]}}
        ],
        "condition_day_gte": 7,
        "condition_flag_false": "org_storyline_started"
    },
    "org_2": {
        "id": "org_2",
        "text_key": "org_2_text",
        "options": [
            {"text_key": "org_2_opt1", "effect": {"set_flag": ["org_quest_accepted", True]}, "next_event": "find_seal_1"},
            {"text_key": "org_2_opt2", "effect": {"set_flag": ["org_quest_accepted", False]}}
        ]
    },
    "find_seal_1": {
        "id": "find_seal_1",
        "text_key": "find_seal_1_text",
        "options": [
            {"text_key": "find_seal_1_opt1", "effect": {"set_flag": ["seal_found", True]}, "next_event": "org_3"},
            {"text_key": "find_seal_1_opt2"}
        ],
        "condition_flag_true": "org_quest_accepted"
    },
    "org_3": {
        "id": "org_3",
        "text_key": "org_3_text",
        "options": [
            {"text_key": "org_3_opt1", "next_event": "org_4"}
        ],
        "condition_flag_true": "seal_found"
    },
    "org_4": {
        "id": "org_4",
        "text_key": "org_4_text",
        "options": [
            {"text_key": "org_4_opt1", "effect": {"set_flag": ["joined_organization", True], "ending": "ending_joined_organization"}}
        ],
        "condition_flag_true": "seal_found"
    },
    "reject_1": {
        "id": "reject_1",
        "text_key": "reject_1_text",
        "options": [
            {"text_key": "reject_1_opt1", "next_event": "reject_2"},
            {"text_key": "reject_1_opt2", "effect": {"set_flag": ["org_reject_path", True]}}
        ],
        "condition_flag_true": "org_declined_initial",
        "condition_day_gte": 6
    },
    "reject_2": {
        "id": "reject_2",
        "text_key": "reject_2_text",
        "options": [
            {"text_key": "reject_2_opt1", "next_event": "reject_3"}
        ],
        "condition_flag_true": "org_reject_path"
    },
    "reject_3": {
        "id": "reject_3",
        "text_key": "reject_3_text",
        "options": [
            {"text_key": "reject_3_opt1", "effect": {"health": -999, "ending": "ending_death"}}
        ],
        "condition_day_gte": 8,
        "condition_flag_true": "org_reject_path"
    }
}

GENERIC_OUTING_AI_EVENTS = [
    {"text_key": "ai_outing_found_food_small", "effect": {"food": 2}},
    {"text_key": "ai_outing_found_water_small", "effect": {"water": 2}},
    {"text_key": "ai_outing_minor_hazard", "effect": {"health": -5}},
    {"text_key": "ai_outing_nothing_significant", "effect": {}},
]

STORY_EVENT_IDS = [
    "tadmavriel_1", "org_1", "reject_1"
]

def get_event_details(event_id):
    return EVENTS.get(event_id)

def check_event_conditions(event_details, game_state):
    if not event_details:
        return False
    
    event_id = event_details.get("id")
    if event_id and game_state.flags.get(f"event_{event_id}_done"):
        return False

    min_day_inclusive = event_details.get("condition_day_gte")
    if min_day_inclusive is not None and game_state.day < min_day_inclusive:
        return False

    required_flag_true = event_details.get("condition_flag_true")
    if required_flag_true and not game_state.flags.get(required_flag_true, False):
        return False

    required_flag_false = event_details.get("condition_flag_false")
    if required_flag_false and game_state.flags.get(required_flag_false, False):
        return False
        
    return True

def check_for_new_story_event(game_state):
    if game_state.current_event:
        return None

    possible_events = []
    for event_id in STORY_EVENT_IDS:
        event_details = get_event_details(event_id)
        if check_event_conditions(event_details, game_state):
            possible_events.append(event_id)
    
    if possible_events:
        return random.choice(possible_events)
    return None
