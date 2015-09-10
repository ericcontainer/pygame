import pygame
pygame.init()
SIZE = (400,400)
BLACK = (0,0,0)
WHITE = (255,255,255)
EXIT_GAME = False
sc = pygame.display.set_mode(SIZE)
bg = pygame.Surface(sc.get_size()).convert()
size = 10
while not EXIT_GAME:
    bg.fill(WHITE)
    for event in pygame.event.get():
	if event.type == pygame.QUIT:
		EXIT_GAME = True
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_RIGHT:
			size += 5
    pygame.draw.rect(bg, BLACK, (200,200,size,10))

    sc.blit(bg,(0,0))
    pygame.display.flip()
pygame.quit()
