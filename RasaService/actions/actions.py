# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.types import DomainDict
from rasa_sdk.executor import CollectingDispatcher
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from instances import phrazes
from helpers import get_random_object


class ActionHandleGreet(Action):

    def name(self) -> Text:
        return "action_handle_greet"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> List[Dict[Text, Any]]:
        buttons = [
            {"title": "Документы", "payload": "/documents"},
            {"title": "Set up your company", "payload": "/setup_company"},
            {"title": "Taxation", "payload": "/taxation"}
        ]
        dispatcher.utter_message(response="utter_greet")
        # dispatcher.utter_message(text=get_random_object(phrazes.get('start_tails')), buttons=buttons)
        dispatcher.utter_message(response="utter_suggesting_buttons", buttons=buttons)
        return []


class ActionHandleThanks(Action):

    def name(self) -> Text:
        return "action_handle_thanks"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> List[Dict[Text, Any]]:
        buttons = [
            {"title": "Документы", "payload": "/documents"},
            {"title": "Set up your company", "payload": "/setup_company"},
            {"title": "Taxation", "payload": "/taxation"}
        ]
        dispatcher.utter_message(response="utter_thanks")
        dispatcher.utter_message(response="utter_thanks_tail")
        dispatcher.utter_message(response="utter_suggesting_buttons", buttons=buttons)
        return []


# class ActionHandleGoodbye(Action):
#
#     def name(self) -> Text:
#         return "action_handle_goodbye"
#
#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         message = tracker.latest_message.get('text', '')
#         if any(word in message.lower() for word in ['goodbye', 'bye', 'see you', 'catch you later']):
#             dispatcher.utter_message(response="utter_goodbye")
#         else:
#             dispatcher.utter_message(response="utter_goodbye")
#         return []
#
# class ActionHandleMoodGreat(Action):
#
#     def name(self) -> Text:
#         return "action_handle_mood_great"
#
#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         message = tracker.latest_message.get('text', '')
#         if any(word in message.lower() for word in ['great', 'well', 'amazing', 'happy']):
#             dispatcher.utter_message(response="utter_mood_great")
#         else:
#             dispatcher.utter_message(response="utter_mood_great")
#         return []
#
# class ActionHandleMoodUnhappy(Action):
#
#     def name(self) -> Text:
#         return "action_handle_mood_unhappy"
#
#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         message = tracker.latest_message.get('text', '')
#         if any(word in message.lower() for word in ['sad', 'not feeling well', 'unhappy', 'bad']):
#             dispatcher.utter_message(response="utter_mood_unhappy")
#         else:
#             dispatcher.utter_message(response="utter_mood_unhappy")
#         return []

class ActionDefaultFallback(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_default")
        return []
