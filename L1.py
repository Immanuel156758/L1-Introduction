import pgzrun

WIDTH = 500
HEIGHT = 500
def draw():
	screen.fill("blue")
	r1 = Rect((10,10),(200,200))
	r1.center = (250,250)
	screen.draw.filled_rect(r1,"black")
pgzrun.go()