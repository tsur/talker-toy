import subprocess

def say(something, language='en', voice='f1'):
    subprocess.call(['espeak', '-v%s+%s' % (language, voice), something])

say('hola', language='es')