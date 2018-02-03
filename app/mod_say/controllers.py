# Import flask dependencies
from flask import Blueprint, request, abort
from say import Say
import json

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_say = Blueprint('say', __name__)
ttsEngine = Say()

# Set the route and accepted methods
@mod_say.route('/say', methods=['POST'])
def say():
    if not request.json:
        abort(400)
    textToSay = request.json['text']
    lang = request.json['lang']
    ttsEngine.aws(textToSay, voice=lang)
    return json.dumps({'status': 200})
