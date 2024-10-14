import pgzrun
import random

HEIGHT = 600
WIDTH = 600

TITLE = "tom and jerry"

tom = Actor("tom")
tom.pos = (WIDTH//2,HEIGHT//2)
jerry = Actor("jerry")
jerry.pos = (random.randint(0,WIDTH),random.randint(0,HEIGHT))
def draw():
    pass

pgzrun.go()