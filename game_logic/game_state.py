import random
from .localization import get_text
from .config import (
    INITIAL_HEALTH, INITIAL_SUIT_CHARGE, INITIAL_FOOD, INITIAL_WATER,
    FOOD_PER_DAY, WATER_PER_DAY, SUIT_CHARGE_PER_OUTING, SUIT_CHARGE_RECOVERY_AMOUNT
)
from .events import GENERIC_OUTING_AI_EVENTS

class GameState:
    def __init__(self):
        self.reset_game_state()

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        gs = cls()
        gs.__dict__.update(data)
        return gs

    def reset_game_state(self):
        self.day = 1
        self.health = INITIAL_HEALTH
        self.suit_charge = INITIAL_SUIT_CHARGE
        self.food = INITIAL_FOOD
        self.water = INITIAL_WATER
        self.inventory = {}
        self.flags = {}
        self.active_quests = []
        self.completed_quests = []
        self.missed_storylines = []
        self.current_screen = "main_menu"
        self.ending = None
        self.is_dead = False
        self.messages = []
        self.language = "uk"
        self.current_event = None
        self.day_story = ""
        self.outing_result_text = ""

    def apply_daily_costs(self):
        self.food -= FOOD_PER_DAY
        self.water -= WATER_PER_DAY
        if self.food < 0:
            self.health -= 15
            self.add_message(get_text("no_food"))
            self.food = 0
        if self.water < 0:
            self.health -= 20
            self.add_message(get_text("no_water"))
            self.water = 0
        self.check_death()

    def go_on_outing(self):
        self.day += 1
        self.apply_daily_costs()
        if self.is_dead:
            return

        self.suit_charge -= SUIT_CHARGE_PER_OUTING
        if self.suit_charge <= 0:
            self.suit_charge = 0
            self.health = 0
            self.ending = "death_suit_charge"
            self.check_death()
            return

        weighted_events = (
            [GENERIC_OUTING_AI_EVENTS[0]] * 4 +
            [GENERIC_OUTING_AI_EVENTS[1]] * 4 +
            [GENERIC_OUTING_AI_EVENTS[2]] * 2 +
            [GENERIC_OUTING_AI_EVENTS[3]] * 1
        )
        outing_event = random.choice(weighted_events)
        self.apply_effect(outing_event.get('effect', {}))
        self.outing_result_text = get_text(outing_event.get('text_key', 'ai_find_nothing'))
        self.add_message(self.outing_result_text)
        self.check_death()

    def charge_suit(self):
        self.day += 1
        self.apply_daily_costs()
        if self.is_dead:
            return

        self.suit_charge = min(100, self.suit_charge + SUIT_CHARGE_RECOVERY_AMOUNT)
        self.outing_result_text = get_text("suit_charged_20")
        self.add_message(self.outing_result_text)
        self.check_death()

    def skip_day(self):
        self.day += 1
        self.apply_daily_costs()
        if self.is_dead:
            return
        self.outing_result_text = get_text("day_skipped")
        self.add_message(self.outing_result_text)
        self.check_death()

    def apply_effect(self, effect):
        if not effect:
            return
        self.health = min(100, self.health + effect.get('health', 0))
        self.food += effect.get('food', 0)
        self.water += effect.get('water', 0)
        self.suit_charge = min(100, self.suit_charge + effect.get('charge', 0))

        if 'set_flag' in effect:
            flag_name, value = effect['set_flag']
            self.flags[flag_name] = value
        
        self.check_death()

    def check_death(self):
        if self.health <= 0:
            self.health = 0
            self.is_dead = True
            if not self.ending:
                self.ending = "death_health"
            self.current_screen = "game_over"

    def add_message(self, text_key, **kwargs):
        message = get_text(text_key, **kwargs)
        self.messages.append(message)
        if len(self.messages) > 5:
            self.messages.pop(0)
