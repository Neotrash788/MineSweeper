import pygame
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600,600))

while True:
    #Event loop
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    
    #Update

    #Render

    #Draw
    pygame.display.update()
    clock.tick(60)
