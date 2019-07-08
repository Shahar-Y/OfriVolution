from enum import Enum, auto


class TileType(Enum):
    Grass = auto()
    Pixel = auto()
    Cell = auto()
    Food = auto()
    Rock = auto()
    Antibiotics = auto()