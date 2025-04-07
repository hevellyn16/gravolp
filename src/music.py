import pygame as pg

class MusicPlayer:
    def __init__(self):
        pg.init()

    def play_music(self, music_file):
        pg.mixer.music.load(music_file)
        pg.mixer.music.play()
