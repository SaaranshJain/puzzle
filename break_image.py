from pil import Image
from numpy import asarray

im = asarray(Image.open("Pic3.png"))
M = im.shape[0]//4
N = im.shape[1]//4
tiles = [im[x:x+M, y:y+N]
         for x in range(0, im.shape[0], M) for y in range(0, im.shape[1], N)]

for index, tile in enumerate(tiles):
    data = Image.fromarray(tile)
    data.save(f"Piece{index}.png")
