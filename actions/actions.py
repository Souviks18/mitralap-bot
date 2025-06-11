from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

def is_bengali(text):
    for ch in text:
        if '\u0980' <= ch <= '\u09FF':
            return True
    return False

class ActionDepressionSupport(Action):
    def name(self):
        return "action_depression_support_lang"

    def run(self, dispatcher, tracker, domain):
        msg = tracker.latest_message.get("text", "")
        if is_bengali(msg):
            dispatcher.utter_message(response="utter_depression_support_bn")
        else:
            dispatcher.utter_message(response="utter_depression_support")
        return []

class ActionStressSupport(Action):
    def name(self):
        return "action_stress_support_lang"

    def run(self, dispatcher, tracker, domain):
        msg = tracker.latest_message.get("text", "")
        if is_bengali(msg):
            dispatcher.utter_message(response="utter_stress_support_bn")
        else:
            dispatcher.utter_message(response="utter_stress_support")
        return []

class ActionAnxietySupport(Action):
    def name(self):
        return "action_anxiety_support_lang"

    def run(self, dispatcher, tracker, domain):
        msg = tracker.latest_message.get("text", "")
        if is_bengali(msg):
            dispatcher.utter_message(response="utter_anxiety_support_bn")
        else:
            dispatcher.utter_message(response="utter_anxiety_support")
        return []
