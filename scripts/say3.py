import subprocess

def say(something, language='en', voice='f2'):
    subprocess.call(['espeak', '-v%s+%s' % (language, voice), something])