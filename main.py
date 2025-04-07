from src.music import MusicPlayer
from src.intro import Introduction
from src.interaction import Interaction
from src.interaction1 import Interaction2

import time


def main():
    music_player = MusicPlayer()
    introduction = Introduction()
    interaction = Interaction()
    interaction1 = Interaction2()

    music_player.play_music("background1.mp3")
    time.sleep(3)

    introduction.display_intro()
    interaction.start_game()
    interaction.conversa_inicial()
    interaction.conversa_1()
    interaction1.conversa_2()


if __name__ == "__main__":
    main()
