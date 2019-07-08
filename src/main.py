import random as random
import pygame as pygame
from typing import List
from enums import TileType
import time

pygame.init()                                 # start up dat pygame
clock = pygame.time.Clock()                   # for frame-rate or something? still not very sure
Screen = pygame.display.set_mode([1000, 1000])  # making the window
Done = False                                  # variable to keep track if window is open
MapSize = 25                                  # how many tiles in either direction of grid

TileWidth = 20                                # pixel sizes for grid squares
TileHeight = 20
TileMargin = 4

BLACK = (0, 0, 0)                             # some color definitions
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


# The main class for stationary things that inhabit the grid ... grass, trees, rocks and stuff.
class MapTile(object):
    def __init__(self, name, column, row, tile_type):
        self.Type = tile_type
        self.Name = name
        self.Column = column
        self.Row = row


# Characters can move around and do cool stuff
class Character(object):
    def __init__(self, name, hp, column, row):
        self.Name = name
        self.HP = hp
        self.Column = column
        self.Row = row

    def handle_step(self, col_advance, row_advance):
        new_col = self.Column + col_advance
        new_row = self.Row + row_advance
        print("Advancing to " + str(new_col) + "," + str(new_row))
        if Map.Grid[new_col][new_row].Type == TileType.Food:
            print("TODO1: stepped on food!")
            # what to do?
            print("TODO2: making a step: replacing the hero tile with the grass and moving the hero to the next tile!")

    # This function implements how a character moves around in a certain direction
    def move(self, direction):

        if direction == "UP":
            if not(self.collides("UP")):
                self.handle_step(0, -1)

        elif direction == "LEFT":
            if not(self.collides("LEFT")):
                self.handle_step(-1, 0)

        elif direction == "RIGHT":
            if not(self.collides("RIGHT")):
                self.handle_step(1, 0)

        elif direction == "DOWN":
            if not(self.collides("DOWN")):
                self.handle_step(0, 1)

    def collides(self, direction):
        # check if the cell collides in its current direction
        print("TODO3: checking collision while going " + direction)
        return False


# The main class; where the action happens
class Map(object):
    global MapSize

    Grid: List[List[MapTile]] = []*(MapSize*MapSize)

    # Creating grid
    empty_tile = MapTile("", 0, 0, TileType.Pixel)
    for Row in range(MapSize*MapSize):
        Grid.append([empty_tile])
        for Column in range(MapSize):
            Grid[Row].append(empty_tile)

    # Filling grid with grass
    for Row in range(MapSize):
        for Column in range(MapSize):
            TempTile = MapTile("Grass", Column, Row, TileType.Grass)
            Grid[Column][Row] = TempTile

    # creating the Hero cell and putting it on the map
    Hero = Character("Hero", 0, 0, 0)
    Cells: List[Character] = [Hero]
    Grid[0][0] = MapTile("Hero", 0, 0, TileType.Cell)

    def spread_food(self, num):
        print("TODO4: this function should spread food on the map!")


Map = Map()
Map.spread_food(150)


def run_game():
    done = False
    while not done:     # Main pygame loop

        for event in pygame.event.get():         # catching events
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (TileWidth + TileMargin)  # Translating mouse position into rows and columns
                row = pos[1] // (TileHeight + TileMargin)
                print(str(row) + ", " + str(column))
                print(str(Map.Grid[column][row].Name))  # print stuff that inhabits that square

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Map.Hero.move("LEFT")
                if event.key == pygame.K_RIGHT:
                    Map.Hero.move("RIGHT")
                if event.key == pygame.K_UP:
                    Map.Hero.move("UP")
                if event.key == pygame.K_DOWN:
                    Map.Hero.move("DOWN")

        color = BLACK
        Screen.fill(color)
        # Drawing grid
        for Row in range(MapSize):
            for Column in range(MapSize):
                if Map.Grid[Column][Row].Type == TileType.Grass:
                    color = WHITE
                if Map.Grid[Column][Row].Type == TileType.Cell:
                    color = BLUE
                if Map.Grid[Column][Row].Type == TileType.Food:
                    color = RED

                pygame.draw.rect(Screen, color, [(TileMargin + TileWidth) * Column + TileMargin,
                                                 (TileMargin + TileHeight) * Row + TileMargin,
                                                 TileWidth,
                                                 TileHeight])

        clock.tick(60)      # Limit to 60 fps or something

        pygame.display.flip()     # Honestly not sure what this does, but it breaks if I remove it


run_game()
pygame.quit()