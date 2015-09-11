import pygame
import math
pygame.init()
SIZE = (400,400)
BLACK = (0,0,0)
WHITE = (255,255,255)
EXIT_GAME = False
sc = pygame.display.set_mode(SIZE)
bg = pygame.Surface(sc.get_size()).convert()
degree = 90
class Cannon:
    def __init__(self,bg):
        self.base_x = 70
	self.base_y = 10
	self.base_size = (70,10)
	self.cannon_x = 7
	self.cannon_y = 55
	self.cannon_size = (7,55)
	self.angle = 90
	self.speed = 5
    def draw(self):
	pygame.draw.rect(bg, BLACK, (200 - self.base_x/2, 400 - self.base_y, self.base_x, self.base_y)) 
	pygame.draw.rect(bg, BLACK, (200 - self.cannon_x/2, 400 - self.cannon_y, self.cannon_x, self.cannon_y))
    def update(self, cor_x, cor_y):
	self.cannon_x = cor_x
	self.cannon_y = cor_y
	 

while not EXIT_GAME:
	bg.fill(WHITE)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			EXIT_GAME = True
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_RIGHT:
			degree +=5

	bigger = pygame.Rect(200, 200, 50, 50)
	pygame.draw.rect(bg, BLACK, bigger).center
	centerCube = pygame.draw.rect(bg, BLACK, bigger).center
	rotatedSurf = pygame.transform.rotate(bg, degree)
	rotRect = rotatedSurf.get_rect()
	rotRect.center = centerCube
	
	print centerCube
	sc.blit(bg,(0,0))
	sc.blit(rotatedSurf, rotRect)
	pygame.display.flip()
pygame.quit()
