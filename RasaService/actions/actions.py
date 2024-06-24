# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.types import DomainDict
from rasa_sdk.executor import CollectingDispatcher
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from instances import buttons_main_json, buttons_docs_json, buttons_taxation, buttons_setup_company
from rasa_sdk.events import SlotSet


class ActionHandleGreet(Action):
    def name(self) -> Text:
        return "action_handle_greet"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_greet")
        dispatcher.utter_message(response="utter_suggesting_buttons", buttons=buttons_main_json)
        return []


class ActionHandleThanks(Action):
    def name(self) -> Text:
        return "action_handle_thanks"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> List[Dict[Text, Any]]:
        conversation_block = tracker.get_slot("conversation_block")
        print(f'{conversation_block=}')
        if conversation_block == "documents":
            dispatcher.utter_message(response="utter_thanks_from_docs")
            dispatcher.utter_message(response="utter_suggesting_buttons", buttons=buttons_main_json)
        else:
            dispatcher.utter_message(response="utter_thanks")
            dispatcher.utter_message(response="utter_thanks_tail")
            dispatcher.utter_message(response="utter_suggesting_buttons", buttons=buttons_main_json)
        return [SlotSet("conversation_block", "thanks")]


class ActionHandleHelp(Action):
    def name(self) -> Text:
        return "action_handle_help"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_help", buttons=buttons_main_json)
        return []


class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_default")
        return []


class ActionHandleDocuments(Action):
    def name(self) -> Text:
        return "action_handle_documents"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_documents")
        dispatcher.utter_message(response="utter_documents_tail", buttons=buttons_docs_json)
        return []


class ActionHandleVisasForEntry(Action):
    def name(self) -> Text:
        return "action_handle_visas_for_entry"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> List[Dict[Text, Any]]:
        buttons_docs2_json = [
            {"title": "Назад", "payload": "/go_back"},
            {"title": "Спасибо", "payload": "/thanks"},
        ]
        dispatcher.utter_message(response="utter_visas_for_entry", buttons=buttons_docs2_json)
        return [SlotSet("conversation_block", "documents")]


class ActionHandlePoliceClearanceCertificate(Action):
    def name(self) -> Text:
        return "action_handle_police_clearance_certificate"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> List[Dict[Text, Any]]:
        buttons_docs2_json = [
            {"title": "Назад", "payload": "/go_back"},
            {"title": "Спасибо", "payload": "/thanks"},
        ]
        dispatcher.utter_message(response="utter_police_clearance_certificate", buttons=buttons_docs2_json)
        return [SlotSet("conversation_block", "documents")]


class ActionHandleTranslationOfDocuments(Action):
    def name(self) -> Text:
        return "action_handle_translation_of_documents"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> List[Dict[Text, Any]]:
        buttons_docs2_json = [
            {"title": "Назад", "payload": "/go_back"},
            {"title": "Спасибо", "payload": "/thanks"},
        ]
        dispatcher.utter_message(response="utter_translation_of_documents", buttons=buttons_docs2_json)
        return [SlotSet("conversation_block", "documents")]


class ActionHandleAnotherQuestion(Action):
    def name(self) -> Text:
        return "action_handle_another_question"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_another_question")
        dispatcher.utter_message(response="utter_suggesting_buttons", buttons=buttons_main_json)

        return []


class ActionHandleSetupCompany(Action):
    def name(self) -> Text:
        return "action_handle_setup_company"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_setup_company", buttons=buttons_setup_company)
        return [SlotSet("conversation_block", "setup_company")]


class ActionHandleTaxation(Action):
    def name(self) -> Text:
        return "action_handle_taxation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_taxation", buttons=buttons_taxation)
        return []
