import pgzrun

WIDTH = 500 
HEIGHT = 500
def draw():
	screen.fill("black")
	r1 = Rect((10,10),(250,200))
	screen.draw.filled_rect(r1,"green")
	r2 = Rect((240,290),(250,200))
	screen.draw.filled_rect(r2,"red")
	r3 = Rect((290,10),(200,250))
	screen.draw.filled_rect(r3,"yellow")
	r4 = Rect((10,240),(200,250))
	screen.draw.filled_rect(r4,"blue")
	r5 = Rect((250,250),(25,25))
	r5.center = (250,250)
	screen.draw.filled_rect(r5,"white")
pgzrun.go()