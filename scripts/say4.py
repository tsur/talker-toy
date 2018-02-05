import boto3
import pygame
import os
import time
import io

class Polly():
    OUTPUT_FORMAT='mp3'

    def __init__(self, voiceId=''):
        self.polly = boto3.client('polly') #access amazon web service
        self.VOICE_ID = voiceId

    def say(self, textToSpeech, voice='Enrique'): #get polly response and play directly
        pollyResponse = self.polly.synthesize_speech(Text=textToSpeech, OutputFormat=self.OUTPUT_FORMAT, VoiceId=voice if not self.VOICE_ID else self.VOICE_ID)
        
        pygame.mixer.init()
        pygame.init()  # this is needed for pygame.event.* and needs to be called after mixer.init() otherwise no sound is played 
            
        with io.BytesIO() as f: # use a memory stream
            f.write(pollyResponse['AudioStream'].read()) #read audiostream from polly
            f.seek(0)
            pygame.mixer.music.load(f)
            pygame.mixer.music.set_endevent(pygame.USEREVENT)
            pygame.mixer.music.set_volume(1)
            pygame.event.set_allowed(pygame.USEREVENT)
            pygame.mixer.music.play()
            pygame.event.wait() # play() is asynchronous. This wait forces the speaking to be finished before closing
            
        while pygame.mixer.music.get_busy() == True:
            pass

    def saveToFile(self, textToSpeech, fileName): #get polly response and save to file
        pollyResponse = self.polly.synthesize_speech(Text=textToSpeech, OutputFormat=self.OUTPUT_FORMAT, VoiceId=self.VOICE_ID)
        
        with open(fileName, 'wb') as f:
            f.write(pollyResponse['AudioStream'].read())
            f.close()

ttsEngine=Polly('Enrique')
ttsEngine.say('Hola. Soy Flafy tu nuevo manager. Aún no puedo hacer muchas tareas, dado que solo tengo algunos commits de vida. Sin embargo, pronto seré capaz de realizar tareas mas complejas como avisaros de historias de usuarios que no avanzan, de pull ricues que no tienen revision en varios días o de facilitar vuestras reuniones creando automáticamente historias de usuarios o haciendo las estimaciones por vosotros. Por si fuera poco, también puedo contar chistes malos. ¿Sabes cómo se despiden los químicos? Ácido un placer. Ja ja ja. Y para terminar, también puedo decir groserías, improperios y exabruptos, entre otras declaraciones de amor. ¡hay hija!, ¡te comía to la cosa!')