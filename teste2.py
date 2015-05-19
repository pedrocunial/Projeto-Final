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

fps = 100
dispWidth = 800
dispHeight = 600
pixMove = 10

def runGame():
	global imgx
	global imgy
	global alive
	global pressed_up
	global g
	global jump_count
	global pixFall
	global pixAir

	imgx = 300
	imgy = 400
	alive = True
	pressed_up = False
	g = 0.5
	jump_count = 0
	pygame.mixer.music.load('fdmusic.mp3')
	pygame.mixer.music.play(-1)
	pixFall = 0
	pixAir = False

	while True:     #main loop
		delay = 100
		interval = 10
		pygame.key.set_repeat(delay, interval)
		
		while alive == True:
			
			#imgx, pixAir, jump_count, pressed_up = movement()

			for event in pygame.event.get():	#event handling loop
				pressed_left = False
				pressed_right = False
				pressed_down = False
				bug = False
				
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

				elif event.type == KEYDOWN:
					if event.key == K_LEFT:
						pressed_left = True
					elif event.key == K_RIGHT:
						pressed_right = True
					elif event.key == K_DOWN:
						pressed_down = True
					elif event.key == K_UP and jump_count == 0 and imgy <= 400:
						pressed_up = True
						jump_count = 38
						pixFall = 0
						pixJump = pixMove
						pixAir = True

				if pressed_left:
					imgx -= pixMove
				elif pressed_right:
					imgx += pixMove

			if jump_count > 0 and imgy <= 400:  #jump
			
				if pressed_left:
					imgx -= pixMove/5  #ITS A FEATURE!!
				elif pressed_right:
					imgx += pixMove/5  #IT IS STILL A FEATURE!!

				if pixJump > 0: #UP WE GO!
					pixJump = pixJump - g
					if pixJump < 0: #falls
						pixJump = 0
					imgy -= pixJump

				elif pixJump <= 0:
					pixFall += g
					imgy += pixFall
					if imgy >= 400:
						pixJump = pixMove
						pixFall = 0
						pressed_up = False

				if pygame.key.get_pressed()[K_DOWN]:
					if pressed_left:
						imgx -= 10*pixMove
						imgy = 400
						jump_count = 0

					elif pressed_right:
						imgx += 10*pixMove
						imgy = 400
						jump_count = 0
						
				if jump_count == 1:
					imgy = 400
				
				jump_count -= 1
				
				if jump_count <= 0:
					pixAir = False
					jump_count = 0
					pixGround = True

			if imgx < 205 or imgx > 620 or imgy > 400:
				if pixAir == False:
					pixFall += g
					imgy += pixFall				
				
			img = pygame.image.load('kirby.png')
			img2 = pygame.image.load('fox.png')
			imgWidth = 30
			imgHeight = 30
			img = pygame.transform.scale(img,(imgWidth,imgHeight))
			img2 = pygame.transform.scale(img2,(imgWidth, 2*imgHeight))
			bg = pygame.image.load('fdbackground.jpg')
			bg = pygame.transform.scale(bg,(dispWidth,dispHeight))
			setDisplay.blit(bg,(0,0))
			setDisplay.blit(img,(imgx - imgWidth,imgy - imgHeight))
			setDisplay.blit(img2,(400 + imgWidth, 400 - 2*imgHeight))
			fase = pygame.draw.rect(setDisplay, purple, (200, 400, 400, 20))
			pygame.display.update()


			if (imgx < 0 or imgy < 0 or imgx > (dispWidth - imgWidth) or imgy > (dispHeight - imgHeight)):
				#kills
				alive = False
				print('You Died')
				pygame.quit()
				sys.exit()

# def movement():
# 	for event in pygame.event.get():	#event handling loop
# 				pressed_left = False
# 				pressed_right = False
# 				pressed_down = False
# 				bug = False
				
# 				if event.type == QUIT:
# 					pygame.quit()
# 					sys.exit()

# 				elif event.type == KEYDOWN:
# 					if event.key == K_LEFT:
# 						pressed_left = True
# 					elif event.key == K_RIGHT:
# 						pressed_right = True
# 					elif event.key == K_DOWN:
# 						pressed_down = True
# 					elif event.key == K_UP and jump_count == 0 and imgy <= 400:
# 						pressed_up = True
# 						jump_count = 38
# 						pixFall = 0
# 						pixJump = pixMove
# 						pixAir = True

# 				if pressed_left:
# 					imgx -= pixMove
# 				elif pressed_right:
# 					imgx += pixMove
# 	return imgx, pixAir, jump_count, pressed_up
				
while True:
	global fpsTime
	global setDisplay

	fpsTime = pygame.time.Clock()
	setDisplay = pygame.display.set_mode((dispWidth,dispHeight))
	pygame.display.set_caption('kirby\'s controlled adventure')
	runGame()
			