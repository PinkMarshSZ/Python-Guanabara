#Faça um programa em python que abra e reproduza o áudio de um arquivo MP3

import pygame
import time # Usaremos 'time.sleep' para uma alternativa mais simples ao pygame.time.Clock()

# 1. Inicializa o Pygame
pygame.init()

# 2. Inicializa o módulo do mixer do Pygame
# Boas configurações para áudio em geral: 44.1KHz, 16-bit estéreo
pygame.mixer.init(44100, -16, 2, 4096)

# 3. Carrega a música MP3
# Certifique-se de que 'True Stories.mp3' está na mesma pasta do seu script.
pygame.mixer.music.load('True Stories.mp3')

# 4. Toca a música (0 significa tocar uma vez)
print("Tocando a música 'True Stories.mp3'...")
pygame.mixer.music.play(0) 

# 5. Mantém o programa ativo enquanto a música toca
# pygame.mixer.music.get_busy() retorna True enquanto a música está tocando.
while pygame.mixer.music.get_busy():
    time.sleep(1) # Espera 1 segundo e verifica novamente para não consumir muita CPU

print("Reprodução de música concluída.")

# 6. Desinicializa o mixer e o Pygame ao final
pygame.mixer.quit()
pygame.quit()