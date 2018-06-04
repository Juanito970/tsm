import pygame, sys, math, random
from pygame.locals import *
from processing import *

x=800
y=600
vel=50
pygame.init()
win = pygame.display.set_mode((x,y))
pygame.display.set_caption("Radar")
blue=(0,0,255)
white = (255,255,255)
negro=(0,0,0)

#Arcos
def dashedArc(n, r):
    delta = (math.pi)/(2*n - 1)
    for i in range(0,2*n):
        if i%2 == 0:
            pygame.draw.arc(win,blue,(x/2-r,y-r,2*r,2*r),delta*i,delta*(i+1),4)


#Lineas
def lineas():
	pygame.draw.line(win,blue,(x/2,100),(x/2,y),4)
	pygame.draw.line(win,blue,(200,142),(x/2,y),4)
	pygame.draw.line(win,blue,(600,142),(x/2,y),4)
	pygame.draw.line(win,blue,(0,y/2),(x/2,y),4)
	pygame.draw.line(win,blue,(x,y/2),(x/2,y),4)

#Nubes
cloudPos=[]
for i in range(5):
	PosX=random.randrange(0,x)
	PosY=random.randrange(-800, 0)
	r=random.randrange(4, 20)
	cloudPos.append([[PosX,PosY],r])

def drawCloud():
	for i in range(1,16):
		size=randint(20,70)
		xOffset=randint(-40,40)
		yOffset=randint(-30,30)
		ellipse(100+Offset, 100+Offset, size, size)
#Time
clk=pygame.time.Clock()


while True:
    win.fill(negro)
    for i in range(0,3):
        dashedArc(15+5*i, ((i+1)*(y-100))/3)
    lineas()
    for i in range(len(cloudPos)):
	pygame.draw.circle(win, white, cloudPos[i][0],cloudPos[i][1])
	cloudPos[i][0][1]+=5
	if cloudPos[i][0][1]>(y+20):
		PosY=random.randrange(-800,0)
		cloudPos[i][0][1]=PosY
		PosX=random.randrange(0,x)
		cloudPos[i][0][0]=PosX
		r=random.randrange(4,20)
		cloudPos[i][1]=r
    drawCloud()
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clk.tick(vel)
