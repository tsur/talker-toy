import subprocess
import boto3
import pygame
import os
import time
import io

class TextToSpeach():
    OUTPUT_FORMAT='mp3'

    def __init__(self):
        self.polly = boto3.client('polly') #access amazon web service
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.music.set_volume(1)

    def espeak(something, language='en', voice='f1'):
        subprocess.call(['espeak', '-v%s+%s' % (language, voice), something])

    def aws(self, textToSpeech, voice='Enrique'): #get polly response and play directly
        pollyResponse = self.polly.synthesize_speech(Text=textToSpeech, OutputFormat=self.OUTPUT_FORMAT, VoiceId=voice)
        
        # pygame.mixer.init()
        # pygame.init()  
        # this is needed for pygame.event.* and needs to be called after mixer.init() otherwise no sound is played 
        
        # if os.name != 'nt':
        #     pygame.display.set_mode((1, 1)) #doesn't work on windows, required on linux
            
        with io.BytesIO() as f: # use a memory stream
            f.write(pollyResponse['AudioStream'].read()) #read audiostream from polly
            f.seek(0)
            pygame.mixer.music.load(f)
            pygame.mixer.music.set_endevent(pygame.USEREVENT)
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