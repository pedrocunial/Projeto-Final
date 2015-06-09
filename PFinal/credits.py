import pygame
import sys
from pygame.locals import *
import time

pygame.init()

black = (0,0,0)
background = black
white = (255,255,255)
dispLarg = 800
dispAlt = 600
FPS = 60
cellSize = 10
pixMove = 5
imgx = 10
imgy = 10
cagar2 = 0
cord = [0]*2
penis = 0

UP = "up"
DOWN = "down"
RIGHT = "right"
LEFT = "left"

setDisplay = pygame.display.set_mode((dispLarg,dispAlt))
pygame.display.set_caption("Dickbutt Cagao")
img = pygame.image.load("dickbutt.png")
img2 = pygame.image.load("sperm.png")
bd = pygame.image.load("background.png")
fpsTime = pygame.time.Clock()

img2 = pygame.transform.scale(img2,(12,37))
img2 = pygame.transform.rotate(img2,-30)

img3 = pygame.image.load("shit.png")
img3 = pygame.transform.scale(img3,(50,50))

direction = 0
def sperm():
	global img2
	global cagar2
	global cord
	global ponto
	img5 = img2
	penis = 0
	x=1.15
	k=5
	z=2
	for i in range (20):
		setDisplay.fill(black)
		setDisplay.blit(bd,(0,0))
		setDisplay.blit(img,(imgx,imgy))
		cord_sperm_x = imgx + 130 + k
		cord_sperm_y = imgy - k/x
		setDisplay.blit(img5,(cord_sperm_x,cord_sperm_y))
		if cagar2 == 1:
			setDisplay.blit(img3,(cord[0],cord[1]))
		if cord_sperm_x in range (cord[0]-15,cord[0]+15) and int(cord_sperm_y) in range (cord[1]-15,cord[1]+15):
			penis = 1
		pygame.display.update()
		time.sleep(0.025)
		img5 = pygame.transform.rotate(img5,-5.5)
		k+=15
		x=x*1.07
	return penis
	
def cagar():
	global img3
	global imgx,imgy
	xcago = imgx+120
	ycago = imgy+120
	cago = setDisplay.blit(img3,(xcago,ycago))
	return xcago,ycago

def girar():
	global img,img3,imgx,imgy,cord
	img6 = [0]*10
	for i in range (10):
		img6[i] = img
	for i in range (10):
		setDisplay.fill(black)
		setDisplay.blit(bd,(0,0))
		setDisplay.blit(img3,(cord[0],cord[1]))
		img6[i] = pygame.transform.rotate(img,-36*i)
		setDisplay.blit(img6[i],(imgx,imgy))
		pygame.display.update()
		time.sleep(0.1)


while True:
	penis = 0
	setDisplay.fill(black)
	cagando = False
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_LEFT:
				direction = LEFT
			if event.key == K_RIGHT:
				direction = RIGHT
			if event.key == K_DOWN:
				direction = DOWN
			if event.key == K_UP:
				direction = UP
			if event.key == K_SPACE:
				penis = sperm()
			if event.key == K_k:
				cagando = True
				cagar2 = 1
		elif event.type == KEYUP:
				direction = 0
	if penis == 1:
		cagar2 = 0
	if direction == DOWN:
		imgy += pixMove
	if direction == RIGHT:
		imgx += pixMove
	if direction == UP:
		imgy -= pixMove
	if direction == LEFT:
		imgx -= pixMove
	setDisplay.blit(bd,(0,0))
	setDisplay.blit(img,(imgx,imgy))
	if cagando == True:
		cord = cagar()
	if cagar2 == 1 and cagando == False:
		setDisplay.blit(img3,(cord[0],cord[1]))
	if (imgx in range (cord[0]-20,cord[0]+20) and (imgy+110) in range (cord[1]-20,cord[1]+20) and cord!=(0,0) and cagar2 == 1):
		girar()
		cagar2 = 0
	pygame.display.update()
	fpsTime.tick(FPS)
