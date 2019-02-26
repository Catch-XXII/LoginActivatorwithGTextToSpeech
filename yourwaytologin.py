#Don't forget to install pygame if you don't have the module you are not going to be able to import it.
# --> pip install pygame

import pygame

pygame.mixer.init()
pygame.mixer.music.load("question.mp3")
pygame.mixer.music.play(1)

def main():
    password = "123qwe"
    answer = input("Enter the passcode: ")
    if answer == password:
        pygame.mixer.music.load("success.mp3")
        pygame.mixer.music.play(1)
    else:
        pygame.mixer.music.load("fail.mp3")
        pygame.mixer.music.play(1)

if __name__ == "__main__":
    main()
