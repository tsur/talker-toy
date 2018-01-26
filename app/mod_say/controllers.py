# Import flask dependencies
from flask import Blueprint, request, abort
import json

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_say = Blueprint('say', __name__)

# Set the route and accepted methods
@mod_say.route('/say', methods=['POST'])
def say():
    if not request.json:
        abort(400)
    textToSay = request.json['text']
    return json.dumps({'status': 200})
