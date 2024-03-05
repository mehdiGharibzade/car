import pgzrun
import os
os.environ["SDL_VIDEO_CENTERED"] = "1"
WIDTH = 1000
HEIGHT = 700

backgrond = Actor ("back")
road = Actor("road",(500,350))
ball = Actor("car")
df = Actor("car",(500,350))
ball.x = 500
ball.y = 300
x = 10
speedCar = 0
ballshotR = False
ballshotL = False
endbackgrond = False


def draw():
    screen.clear()
    road.draw()
    
    ball.draw()

      
def update():

    ball.x += speedCar

    if ball.x > WIDTH :
        print("right",speedCar)
        ball.x = 0
    elif ball.x < 0:
        ball.x = WIDTH 
        print("left",speedCar)   
            
def on_mouse_down(pos,button):
    global ballshotR , speedCar , ballshotL

    if ball.collidepoint(pos) and button == mouse.LEFT:
        speedCar -= 2
    if ball.collidepoint(pos) and button == mouse.RIGHT:
        speedCar += 2


pgzrun.go()
