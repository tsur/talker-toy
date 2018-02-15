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
        sprint_count = jiraClient.get_issues_number_in_sprint("169")
        return "Gentecilla, ahora puedo acceder a yira. Os informo de que os quedan {0} dias para terminar el sprint. Tenemos un total de {1} tareas, de las cuales {2} estan aun por hacer, {3} estan en progreso o siendo revisadas y {4} estan terminadas. {5}".format(days_remaining, sprint_count['total'], sprint_count['status']['To Do'], sprint_count['status']['In Progress'], sprint_count['status']['Done'],"Acordaos que al final siempre vais de culo, que si no os ha dado tiempo de probarlo todo, que si hay que hacer la integracion, que si un merje la ha liado parda. Solo os aviso, tenedlo en cuenta.")
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
