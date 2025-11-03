import pygame , pathlib

pygame.init()

def main(): pygame.mixer.Sound(pathlib.Path(__file__).resolve().parent / "ineedthis.mp3").play()
