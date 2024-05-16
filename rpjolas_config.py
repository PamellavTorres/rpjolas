import pygame
AMARELO =(0xFF, 0xFF, 0x00)
PRETO =(0x00, 0x00, 0x00)
TELA_WIDTH = 800
TELA_HEIGHT = 600

BLK_WIDTH = TELA_WIDTH / 40
BLK_HEIGHT = TELA_HEIGHT / 20

def load_image(img_set, x, y):
    img_orig = img_set.subsurface((x, y), (16, 16))
    img_scaled = pygame.transform.scale(img_orig, (BLK_WIDTH, BLK_HEIGHT))
    return img_scaled 