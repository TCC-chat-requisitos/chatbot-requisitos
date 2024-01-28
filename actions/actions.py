from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

# rasa run actions

class ActionResetUserStoryTitle(Action):
    def name(self) -> Text:
        return "action_reset_user_story_title"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("user_story_title", None)]

class ActionResetUserStoryDescription(Action):
    def name(self) -> Text:
        return "action_reset_user_story_description"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("user_story_description", None)]
    
class ActionResetUserStoryAcceptanceCriteria(Action):
    def name(self) -> Text:
        return "action_reset_user_story_acceptance_criteria"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("user_story_acceptance_criteria", None)]
