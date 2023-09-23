import pygame

audio_file = "mario_star_song.mp3"

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load(audio_file)
pygame.mixer.music.play()
pygame.mixer.music.set_volume(1000)

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

pygame.quit()