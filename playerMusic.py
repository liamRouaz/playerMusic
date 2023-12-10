import pygame
from tkinter import Tk, filedialog

# Initialisation de Pygame
pygame.init()

# Définition de la fenêtre
screen = pygame.display.set_mode((400, 300))
done = False
white = (255, 255, 255)
pygame.display.set_caption("Cliquez sur l'image pour jouer de la musique")


# Chargement de la police
font = pygame.font.SysFont("Arial", 14)

# Boutons
text_play = font.render(" PLAY ", True, white)
text_pause = font.render(" PAUSE ", True, white)
text_stop = font.render(" STOP ", True, white)
text_select = font.render(" FICHIER ", True, white)
text_volume_up = font.render(" VOLUME + ", True, white)
text_volume_down = font.render(" VOLUME - ", True, white)
text_toggle_loop = font.render(" LOOP ", True, white)

# Cadres des boutons
rect_play = text_play.get_rect(topleft=(10, 240))
rect_pause = text_pause.get_rect(topleft=(120, 240))
rect_stop = text_stop.get_rect(topleft=(230, 240))
rect_select = text_select.get_rect(topleft=(340, 240))
rect_volume_up = text_volume_up.get_rect(topleft=(10, 270))
rect_volume_down = text_volume_down.get_rect(topleft=(160, 270))
rect_toggle_loop = text_toggle_loop.get_rect(topleft=(310, 270))

# Image de fond
image = pygame.image.load("pochette/A82V.gif")  # Remplacez par le chemin de votre image

# Chargement initial d'une musique
current_file = "music/Werenoi - La League (Clip Officiel).mp3"
pygame.mixer.music.load(current_file)

# Volume initial
volume = 0.5  # Valeur entre 0.0 et 1.0 (0 pour muet, 1 pour le volume maximal)
pygame.mixer.music.set_volume(volume)

# État de la boucle
looping = False

# Boucle principale
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect_play.collidepoint(event.pos):
                pygame.mixer.music.load(current_file)
                pygame.mixer.music.play(loops=-1 if looping else 0)  # -1 pour boucler, 0 pour ne pas boucler
            elif rect_pause.collidepoint(event.pos):
                if pygame.mixer.music.get_busy() and pygame.mixer.music.get_pos() > 0:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif rect_stop.collidepoint(event.pos):
                pygame.mixer.music.stop()
            elif rect_select.collidepoint(event.pos):
                Tk().withdraw()  # Hide the main window
                file_path = filedialog.askopenfilename(initialdir="/Users/rouaz/Desktop/player/music")
                if file_path:
                    current_file = file_path
            elif rect_volume_up.collidepoint(event.pos):
                volume = min(1.0, volume + 0.1)  # Augmente le volume (limité à 1.0)
                pygame.mixer.music.set_volume(volume)
            elif rect_volume_down.collidepoint(event.pos):
                volume = max(0.0, volume - 0.1)  # Diminue le volume (limité à 0.0)
                pygame.mixer.music.set_volume(volume)
            elif rect_toggle_loop.collidepoint(event.pos):
                looping = not looping  # Inverse l'état de la boucle

    # Affichage de l'image de fond
    screen.blit(image, (-45, 0))

    # Affichage de la bannière grise en bas
    pygame.draw.rect(screen, (128, 128, 128), (0, 230, 400, 70))

    # Affichage des boutons
    screen.blit(text_play, rect_play)
    pygame.draw.rect(screen, white, rect_play, 2)

    screen.blit(text_pause, rect_pause)
    pygame.draw.rect(screen, white, rect_pause, 2)

    screen.blit(text_stop, rect_stop)
    pygame.draw.rect(screen, white, rect_stop, 2)

    screen.blit(text_select, rect_select)
    pygame.draw.rect(screen, white, rect_select, 2)

    screen.blit(text_volume_up, rect_volume_up)
    pygame.draw.rect(screen, white, rect_volume_up, 2)

    screen.blit(text_volume_down, rect_volume_down)
    pygame.draw.rect(screen, white, rect_volume_down, 2)

    screen.blit(text_toggle_loop, rect_toggle_loop)
    pygame.draw.rect(screen, white, rect_toggle_loop, 2)

    pygame.display.update()

pygame.quit()
