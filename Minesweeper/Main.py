import pygame
import Board
import Player
import math
import sys



screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

texture_lib = {
    '0': 'textures/mine1.png',
    '1': 'textures/mine2.png',
    '2': 'textures/mine3.png',
    '3': 'textures/mine4.png',
    '4': 'textures/mine5.png',
    '5': 'textures/mine6.png',
    '6': 'textures/mine7.png',
    '7': 'textures/mine8.png',
    '8': 'textures/mine9.png',
    'M': 'textures/blank.png',
    ' ': 'textures/blank.png',
    'F': 'textures/flag.png'
}


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(
            'textures/blank.png').convert(), (tilesize, tilesize))
        self.rect = self.image.get_rect(topleft=pos)


def init(Length: int, Height: int,Mines:int) -> None:
    global tiles, tile_grid, length, height,tilesize
    sys.setrecursionlimit(Length*Height)
    Board.init(Length, Height, Mines)

    base = max(Length,Height)
    
    tilesize = math.floor(600/base)
    length, height = Length, Height
    tiles = pygame.sprite.Group()

    tile_grid = []
    for h in range(height):
        for l in range(length):
            tile_grid.append(Tile((l*tilesize, h*tilesize)))
    tiles.add(tile_grid)


#init(int(input('Board Height -> ')),int(input('Board With -> ')),int(input('Mines -> ')),int(input('Tile Size -> ')))
init(20,20,40)

def convert_pos(pos: int) -> tuple:
    global length, height
    return (math.floor(pos/length), pos % length)


def convert_mouse_pos(pos: tuple) -> tuple:
    return (math.floor(pos[1]/tilesize), math.floor(pos[0]/tilesize))


while True:
    global length, height
    # event loop
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_key = pygame.mouse.get_pressed()

        if event.type == pygame.MOUSEBUTTONUP:
            pos = convert_mouse_pos(pygame.mouse.get_pos())
            if mouse_key == (True, False, False):
                Player.guess(pos[0], pos[1])
            else:
                Player.flag(pos[0], pos[1])

    # update
    for tile in range(length*height):
        tile_grid[tile].image = pygame.transform.scale(pygame.image.load(
            texture_lib[Board.board[convert_pos(tile)[0]][convert_pos(tile)[1]]]).convert(), (tilesize, tilesize))

    # render
    tiles.draw(screen)
    # display
    pygame.display.update()
    clock.tick(60)
