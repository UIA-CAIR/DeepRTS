import pygame
from .util import get_sprite, image_at
from DeepRTS.Constants import Unit, Direction, Tile
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

class Sprites:

    def __init__(self, gui):
        self.gui = gui

        self.peasant = self._load_sprite("data/textures/human/peasant.png")
        self.archer = self._load_sprite("data/textures/human/archer.png")
        self.footman = self._load_sprite("data/textures/human/footman.png")

        buildings = self._load_sprite("data/textures/human/buildings.png")
        self.town_hall = buildings
        self.barracks = buildings
        self.farm = buildings

    def load(self):
        return self.sprites(), self.tiles()

    def _load_sprite(self, path):
        sheet = pygame.image.load(path).convert_alpha()
        return sheet

    def tiles(self):
        tileset_path = os.path.join(dir_path, "..", "data", "textures", "tiles.png")
        sheet = pygame.image.load(tileset_path).convert()

        tile_types = [int(getattr(Tile, x)) for x in Tile.__dict__.keys() if not x.startswith("__")]

        tiles = {}
        for tile_type in tile_types:
            sprite = image_at(sheet, tile_type - 1, self.gui.map.tile_width).convert()  # -1 to account for index 0
            tiles[tile_type] = sprite

        return tiles

    def sprites(self):
        sprites = {
            int(Unit.Peasant):  {
                int(Direction.Left): [
                    get_sprite(self.peasant, 85, 4, 32, 32, 1, 1, True),
                    get_sprite(self.peasant, 85, 42, 32, 32, 1, 1, True),
                    get_sprite(self.peasant, 85, 82, 32, 32, 1, 1, True),
                    get_sprite(self.peasant, 85, 118, 32, 32, 1, 1, True),
                    get_sprite(self.peasant, 85, 155, 32, 32, 1, 1, True)
                ],
                int(Direction.Up): [
                    get_sprite(self.peasant, 15, 4, 32, 32, 1, 1),
                    get_sprite(self.peasant, 15, 42, 32, 32, 1, 1),
                    get_sprite(self.peasant, 15, 82, 32, 32, 1, 1),
                    get_sprite(self.peasant, 15, 118, 32, 32, 1, 1),
                    get_sprite(self.peasant, 15, 155, 32, 32, 1, 1)
                ],
                int(Direction.Right): [
                    get_sprite(self.peasant, 85, 4, 32, 32, 1, 1),
                    get_sprite(self.peasant, 85, 42, 32, 32, 1, 1),
                    get_sprite(self.peasant, 85, 82, 32, 32, 1, 1),
                    get_sprite(self.peasant, 85, 118, 32, 32, 1, 1),
                    get_sprite(self.peasant, 85, 155, 32, 32, 1, 1)
                ],
                int(Direction.Down): [
                    get_sprite(self.peasant, 164, 4, 32, 32, 1, 1),
                    get_sprite(self.peasant, 164, 42, 32, 32, 1, 1),
                    get_sprite(self.peasant, 164, 82, 32, 32, 1, 1),
                    get_sprite(self.peasant, 164, 118, 32, 32, 1, 1),
                    get_sprite(self.peasant, 164, 155, 32, 32, 1, 1)
                ],
                int(Direction.UpLeft): [
                    get_sprite(self.peasant, 50, 4, 32, 32, 1, 1, True),
                    get_sprite(self.peasant, 50, 42, 32, 32, 1, 1, True),
                    get_sprite(self.peasant, 50, 82, 32, 32, 1, 1, True),
                    get_sprite(self.peasant, 50, 118, 32, 32, 1, 1, True),
                    get_sprite(self.peasant, 50, 155, 32, 32, 1, 1, True)
                ],
                int(Direction.UpRight): [
                    get_sprite(self.peasant, 50, 4, 32, 32, 1, 1),
                    get_sprite(self.peasant, 50, 42, 32, 32, 1, 1),
                    get_sprite(self.peasant, 50, 82, 32, 32, 1, 1),
                    get_sprite(self.peasant, 50, 118, 32, 32, 1, 1),
                    get_sprite(self.peasant, 50, 155, 32, 32, 1, 1)
                ],
                int(Direction.DownLeft): [
                    get_sprite(self.peasant, 120, 4, 32, 32, 1, 1, True),
                    get_sprite(self.peasant, 120, 42, 32, 32, 1, 1, True),
                    get_sprite(self.peasant, 120, 82, 32, 32, 1, 1, True),
                    get_sprite(self.peasant, 120, 118, 32, 32, 1, 1, True),
                    get_sprite(self.peasant, 120, 155, 32, 32, 1, 1, True)
                ],
                int(Direction.DownRight): [
                    get_sprite(self.peasant, 120, 4, 32, 32, 1, 1),
                    get_sprite(self.peasant, 120, 42, 32, 32, 1, 1),
                    get_sprite(self.peasant, 120, 82, 32, 32, 1, 1),
                    get_sprite(self.peasant, 120, 118, 32, 32, 1, 1),
                    get_sprite(self.peasant, 120, 155, 32, 32, 1, 1)
                ]
            },
            int(Unit.Footman):  {
                int(Direction.Left): [
                    get_sprite(self.footman, 170, 7, 32, 32, 1, 1, True),
                    get_sprite(self.footman, 170, 56, 32, 32, 1, 1, True),
                    get_sprite(self.footman, 170, 99, 32, 32, 1, 1, True),
                    get_sprite(self.footman, 170, 138, 32, 32, 1, 1, True),
                    get_sprite(self.footman, 170, 176, 32, 32, 1, 1, True)
                ],
                int(Direction.Up): [
                    get_sprite(self.footman, 21, 7, 32, 32, 1, 1),
                    get_sprite(self.footman, 21, 56, 32, 32, 1, 1),
                    get_sprite(self.footman, 21, 99, 32, 32, 1, 1),
                    get_sprite(self.footman, 21, 138, 32, 32, 1, 1),
                    get_sprite(self.footman, 21, 176, 32, 32, 1, 1)
                ],
                int(Direction.Right): [
                    get_sprite(self.footman, 170, 7, 32, 32, 1, 1),
                    get_sprite(self.footman, 170, 56, 32, 32, 1, 1),
                    get_sprite(self.footman, 170, 99, 32, 32, 1, 1),
                    get_sprite(self.footman, 170, 138, 32, 32, 1, 1),
                    get_sprite(self.footman, 170, 176, 32, 32, 1, 1)
                ],
                int(Direction.Down): [
                    get_sprite(self.footman, 315, 7, 32, 32, 1, 1),
                    get_sprite(self.footman, 315, 56, 32, 36, 1, 1),
                    get_sprite(self.footman, 315, 99, 32, 32, 1, 1),
                    get_sprite(self.footman, 315, 138, 32, 36, 1, 1),
                    get_sprite(self.footman, 315, 176, 32, 32, 1, 1)
                ],
                int(Direction.UpLeft): [
                    get_sprite(self.footman, 96, 7, 32, 32, 1, 1, True),
                    get_sprite(self.footman, 96, 56, 32, 32, 1, 1, True),
                    get_sprite(self.footman, 96, 99, 32, 32, 1, 1, True),
                    get_sprite(self.footman, 96, 138, 32, 32, 1, 1, True),
                    get_sprite(self.footman, 96, 176, 32, 32, 1, 1, True)
                ],
                int(Direction.UpRight): [
                    get_sprite(self.footman, 96, 7, 32, 32, 1, 1),
                    get_sprite(self.footman, 96, 56, 32, 32, 1, 1),
                    get_sprite(self.footman, 96, 99, 32, 32, 1, 1),
                    get_sprite(self.footman, 96, 138, 32, 32, 1, 1),
                    get_sprite(self.footman, 96, 176, 32, 32, 1, 1)
                ],
                int(Direction.DownLeft): [
                    get_sprite(self.footman, 241, 7, 32, 32, 1, 1, True),
                    get_sprite(self.footman, 241, 56, 32, 32, 1, 1, True),
                    get_sprite(self.footman, 241, 99, 32, 32, 1, 1, True),
                    get_sprite(self.footman, 241, 138, 32, 32, 1, 1, True),
                    get_sprite(self.footman, 241, 176, 32, 32, 1, 1, True)
                ],
                int(Direction.DownRight): [
                    get_sprite(self.footman, 241, 7, 32, 32, 1, 1),
                    get_sprite(self.footman, 241, 56, 32, 32, 1, 1),
                    get_sprite(self.footman, 241, 99, 32, 32, 1, 1),
                    get_sprite(self.footman, 241, 138, 32, 32, 1, 1),
                    get_sprite(self.footman, 241, 176, 32, 32, 1, 1)
                ],

            },
            int(Unit.TownHall):  {
                int(Direction.UpLeft): [
                    get_sprite(self.town_hall, 270, 156, 111, 93, 3, 3),
                ],
                int(Direction.Up): [
                    get_sprite(self.town_hall, 270, 20, 111, 93, 3, 3)
                ]
            },
            int(Unit.Farm):  {
                int(Direction.UpLeft): [
                    get_sprite(self.farm, 398, 70, 66, 66, 2, 2)
                ],
                int(Direction.Up): [
                    get_sprite(self.farm, 398, 1, 66, 66, 2, 2),
                ]
            },
            int(Unit.Barracks):  {
                int(Direction.UpLeft): [
                    get_sprite(self.barracks, 304, 560, 102, 102, 3, 3)
                ],
                int(Direction.Up): [
                    get_sprite(self.barracks, 304, 457, 102, 102, 3, 3),
                ]
            }
        }
        return sprites