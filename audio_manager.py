import pygame


class AudiManager:
    def __init__(self):
        pygame.mixer.init()

    def play(self, file):
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        
