# Import flask dependencies
from flask import Blueprint, request, abort
from tts import TextToSpeach
from jira_client import JiraClient
import json

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_say = Blueprint('say', __name__)
ttsEngine = TextToSpeach()
jiraClient = JiraClient()

def textResponse(text):
    if ":sprint" in text.lower():
        days_remaining = jiraClient.get_remaining_days("169")
        return "Gentecilla, ahora puedo acceder a yira. Os informo de que os quedan {0} dias para terminar el sprint. {1}".format(days_remaining, "Acordaos que al final siempre vais de culo, que si no os ha dado tiempo de probarlo todo, que si la integracion, que si un merje la ha liado parda. Tenedlo en cuenta.")
    return text

# Set the route and accepted methods
@mod_say.route('/say', methods=['POST'])
def say():
    if not request.json:
        return abort(400)
    textToSay = textResponse(request.json['text'])
    lang = request.json['lang']
    ttsEngine.aws(textToSay, voice=lang)
    return json.dumps({'status': 200})
