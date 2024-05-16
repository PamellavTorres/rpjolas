import pygame 
from rpjolas_config import *

# p - parede
# <space> - area em branco
mapa = [
         "pppppppppppppppppppppppppppppppppppppppp",
         "p                                      p",
         "p                                      p",
         "p                                      p",
         "p                                      p",
         "p                          p           p",
         "p                          p           p",
         "p                          p           p",
         "p                          p           p",
         "p                 pppppppppp           p",
         "p                 p                    p",
         "p                 p                    p",
         "p                 p                    p",
         "p                 p                    p",
         "p                 p                    p",
         "p                 p                    p",
         "p          pppppppp                    p",
         "p                                      p",
         "p                                      p",
         "pppppppppppppppppppppppppppppppppppppppp",
]

mapa_objs = [
        "                                         ",
        "               v                         ",
        "                                v        ",
        "                                         ",
        "                                         ",
        "                                         ",
        "                                         ",
        "              v                          ",
        "                                         ",
        "                                         ",
        "                                         ",
        "                                   v     ",
        "                                         ",
        "                                         ",
        "                                         ",
        "                                         ",
        "                                         ",
        "   v                                      ",
        "                                         ",                  
        "                                         ",
        "                                         ",
]


pygame.init()
tela = pygame.display.set_mode((TELA_WIDTH, TELA_HEIGHT))


    
tiles = pygame.image.load("./basictiles.png").convert_alpha()
caracters = pygame.image.load("./caracters.png").convert_alpha()

img_vaso = load_image(tiles, 48, 48)
img_grama = load_image(tiles, 16, 128)
img_parede = load_image(tiles, 48, 0)


def desenha_mapa(map, caracter_imagem):
        for id_linha, linha in enumerate(map): 
                for id_coluna, caracter in enumerate(linha):
                        if caracter in caracter_imagem:
                               x = id_coluna * BLK_WIDTH
                               y = id_linha * BLK_HEIGHT
                               img = caracter_imagem[caracter]
                               tela.blit(img, (x, y))

def teste_colisao_mapa(personagem, map, lista_caracteres):
        colisoes = []
        for id_linha, linha in enumerate(map):
                for id_coluna, caracter in enumerate(linha):
                        if caracter in lista_caracteres:
                                x = id_coluna * BLK_WIDTH
                                y = id_linha * BLK_HEIGHT
                                r = pygame.Rect((x, y), (BLK_WIDTH, BLK_HEIGHT))
                                r2 = personagem.rect.copy()
                                r2.move_ip(personagem.vel_x, personagem.vel_y)
                                if r.colliderect(r2):
                                        colisao = {"linha": id_linha, "coluna": id_coluna, "caracter": caracter}
                                        colisoes.append(colisao)         
        return colisoes 
class Personagem(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.vel_x = 0.0
                self.vel_y = 0.0
                car_img_1 = load_image(caracters, 48, 0)
                car_img_2 = load_image(caracters, 64, 0)
                car_img_3 = load_image(caracters, 80, 0)
                self.lista_imagens = [car_img_1, car_img_2, car_img_3]
                self.image_idx = 0
                self.image = car_img_1
                self.rect = pygame.Rect((32, 32), (BLK_WIDTH, BLK_HEIGHT))
       
         
        def update(self):
                self.image = self.lista_imagens[self.image_idx]
                self.image_idx += 1
                if self.image_idx >= len(self.lista_imagens):
                        self.image_idx = 0
                
                colisoes_movimento = teste_colisao_mapa(self, mapa, ["p"])
                if len(colisoes_movimento) == 0:
                        self.rect.move_ip(self.vel_x, self.vel_y)               
                                                 
        def processar_evento(self, e):
                if e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_d:
                                self.vel_x = 1.0 
                        if e.key == pygame.K_a:
                                self.vel_x = -1.0
                        if e.key == pygame.K_w:
                                self.vel_y = -1.0
                        if e.key == pygame.K_s:
                                self.vel_y = 1.0     
                if e.type == pygame.KEYUP:
                        if e.key in [pygame.K_a, pygame.K_d]:
                                self.vel_x = 0.0
                        if e.key in [pygame.K_w, pygame.K_s]:
                                self.vel_y = 0.0
               
heroi = Personagem()
grupo_heroi = pygame.sprite.Group(heroi)
      
while True:                  
        desenha_mapa(mapa, {"p": img_parede, " ": img_grama})
        desenha_mapa(mapa_objs, {"v": img_vaso})   
                        
        grupo_heroi.draw(tela)
        pygame.display.update()
       
        grupo_heroi.update()

        for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    exit()
                heroi.processar_evento(e)     
