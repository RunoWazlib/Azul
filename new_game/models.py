from django.db import models

# Create your models here.
# Bag of tiles to play
class TileBag(models.Model):
    number_of_blue_tiles = models.SmallIntegerField()
    number_of_orange_tiles = models.SmallIntegerField()
    number_of_red_tiles = models.SmallIntegerField()
    number_of_black_tiles = models.SmallIntegerField()
    number_of_white_tiles = models.SmallIntegerField()

# Individual tiles
class Tile(TileBag):
    TileBag
    for i in range(number_of_blue_tiles):
        Tile("black")
    for i in TileBag.number_of_orange_tiles:
        Tile("black")
    for i in TileBag.number_of_red_tiles:
        Tile("black")
    for i in TileBag.number_of_black_tiles:
        Tile("black")
    for i in TileBag.number_of_white_tiles:
        Tile("black")