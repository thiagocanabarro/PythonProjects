# Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3

import pygame

pygame.mixer.init()
pygame.mixer.music.load('leguas.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass