import pygame
import sys
from pygame.locals import *

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
purple = (255,0,255)

bg = black

fps = 30
dispWidth = 800
dispHeight = 600
pixMove = 10

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def runGame():
	global imgy
	global pulos

	imgx = 400
	imgy = 380
	direction = RIGHT
	alive = True
	pulos = 0
	STANDING = True
	JUMPING = False
	FALL = False
	g = 0.5
	pixFall = 0
	pixJump = pixMove
	jump_count = 0

	while True:     #main loop
		delay = 100
		interval = 50
		pygame.key.set_repeat(delay, interval)
		
		while alive == True:
			for event in pygame.event.get():	#event handling loop
				pressed_up = False
				pressed_left = False
				pressed_right = False
				pressed_down = False
				
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

				if event.type == KEYDOWN:
					if event.key == K_LEFT:
						pressed_left = True
					elif event.key == K_RIGHT:
						pressed_right = True
					elif event.key == K_DOWN:
						pressed_down = True
					elif event.key == K_UP:
						pressed_up = True
						jump_count = 38

				if jump_count > 0:
					if pixJump > 0:
						print(pixJump)
						pixJump = pixJump - g
						if pixJump < 0:
							pixJump = 0
						imgy -= pixJump

					if pixJump <= 0:
						pixFall += g
						imgy += pixFall
						if imgy >= 380:
							imgy = 380
							pixJump = pixMove
							pixFall = 0

					jump_count -= 1

				#elif pressed_up:
				#	imgy -= pixMove
				#elif pressed_down:
					#imgy += pixMove    #tentando fazer pulos
				if pressed_left:
					imgx -= pixMove
				elif pressed_right:
					imgx += pixMove


				setDisplay.fill(bg)
				img = pygame.image.load('kirby.png')
				fase = pygame.draw.rect(setDisplay, purple, (200, 400, 400, 20))
				imgWidth = 20
				imgHeight = 20
				img = pygame.transform.scale(img, (imgWidth,imgHeight))
				setDisplay.blit(img,(imgx,imgy))
				pygame.display.update()

				if (imgx < 0 or imgy < 0 or imgx > (dispWidth - imgWidth) or imgy > (dispHeight - imgHeight)):
					#kills
					alive = False
					print('You Died')
					pygame.quit()
					sys.exit()

#def pulo():
#	global pulos
#	global imgy
#
#		if pulos < 3:
#			imgy -= pixMove
#		elif pulos < 5:
#			imgy -= pixMove
#		else:
#			pulos = 0




while True:
	global fpsTime
	global setDisplay

	fpsTime = pygame.time.Clock()
	setDisplay = pygame.display.set_mode((dispWidth,dispHeight))
	pygame.display.set_caption('kirby\'s controlled adventure')
	runGame()
			