""" 
    Tile cost calculator
    Find out a cost of filling a floor with tiles.

    INPUT:
    1) Tile width [NUMBER]
    2) Tile height [NUMBER]
    3) Tile price [NUMBER]
    4) Floor width [NUMBER]
    5) Floor height [NUMBER]

    OUTPUT:
    Cost of the floor.
"""
from sys import argv
from math import ceil

if __name__ == "__main__":
    # Parse and check input
    tile_w, tile_h, tile_price, floor_w, floor_h = -1, -1, -1, -1, -1
    if len(argv) == 6:
            try:
                tile_w, tile_h, tile_price, floor_w, floor_h = [float(a) for a in argv[1:]]
            except ValueError:
                pass

    if tile_w <= 0 or tile_h <= 0 or tile_price <=0 or floor_w <= 0 or floor_h <= 0:
        print("Usage: tiles <tile width> <tile height> <tile price> <floor width> <floor height>")
    else:
        print("Calculated cost: ", tile_price * ceil((floor_h * floor_w) / (tile_w * tile_h)));
        