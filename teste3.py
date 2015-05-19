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

p1_eixox = 370
p1_eixoy = 400

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

img = pygame.image.load('kirby.png')
img2 = pygame.image.load('fox.png')
p1_walkRight1 = pygame.image.load('Andar1_Right.png')
p1_walkRight2 = pygame.image.load('Andar2_Right.png')
p1_walkRight3= pygame.image.load('Andar3_Right.png')
p1_walkLeft1= pygame.image.load('Andar1_Left.png')
p1_walkLeft2= pygame.image.load('Andar2_Left.png')
p1_walkLeft3= pygame.image.load('Andar3_Left.png')
p1_punchLeft= pygame.image.load('Soco_Left.png')
p1_punchRight= pygame.image.load('Soco_Right.png')
p1_jumpRight = pygame.image.load('Pular_Right.png')
p1_jumpLeft = pygame.image.load('Pular_Left.png')



class Personagem(object):
	def __init__(self,eixox,eixoy,sprite1,sprite2,sprite3,sprite4,sprite5,sprite6,sprite7,sprite8,sprite9,sprite10):
		self.eixox = eixox
		self.eixoy = eixoy
		self.sprite_walkRight1 = sprite1
		self.sprite_walkRight2 = sprite2
		self.sprite_walkRight3 = sprite3
		self.sprite_walkLeft1 = sprite4
		self.sprite_walkLeft2 = sprite5
		self.sprite_walkLeft3 = sprite6
		self.sprite_punchRight = sprite7
		self.sprite_punchLeft = sprite8
		self.sprite_jumpRight = sprite9
		self.sprite_jumpLeft = sprite10

P1 = Personagem(p1_eixox,p1_eixoy,p1_walkRight1,p1_walkRight2,p1_walkRight3,p1_walkLeft1,p1_walkLeft2,p1_walkLeft3,p1_punchRight,p1_punchLeft,p1_jumpRight,p1_jumpLeft)


def runGame():

	global img, img2

	imgx = 300
	imgy = 330
	alive = True
	pressed_up = False
	g = 0.5
	jump_count = 0
	pygame.mixer.music.load('fdmusic.mp3')
	pygame.mixer.music.play(-1)
	pixFall = 0
	pixAir = False
	aux_lado = "right"
	aux = 0
	p1_sprite = 1
	imgx2 = 400
	imgy2 = 400

	while True:     #main loop
		delay = 100
		interval = 30
		pygame.key.set_repeat(delay, interval)
		
		while alive == True:
			for event in pygame.event.get():	#event handling loop
				pressed_left = False
				pressed_right = False
				pressed_down = False
				pressed_space = False
				bug = False
				
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

				elif event.type == KEYDOWN:
					if event.key == K_LEFT:
						pressed_left = True
						aux_lado = "left"
					elif event.key == K_RIGHT:
						pressed_right = True
						aux_lado = "right"
					elif event.key == K_DOWN:
						pressed_down = True
					elif event.key == K_UP and jump_count == 0 and imgy <= 400:
						pressed_up = True
						jump_count = 38
						pixFall = 0
						pixJump = pixMove
						pixAir = True
					elif event.key == K_SPACE:
						pressed_space = True

				if pressed_left:
					imgx -= pixMove
					if jump_count == 0:# posicao das pernas ao andar
						if aux <= 3:
							p1_sprite = 4
							aux += 1
						elif aux <= 6:
							p1_sprite = 5
							aux += 1
						elif aux <= 9:
							p1_sprite = 6
							aux += 1
						elif aux <= 12:
							p1_sprite = 5
							aux += 1
							if aux == 12:
								aux = 0
				elif pressed_right:
					imgx += pixMove
					if jump_count == 0:# posicao das pernas ao andar
						if aux <=3:
							p1_sprite = 1
							aux += 1
						elif aux <=6:
							p1_sprite = 2
							aux += 1
						elif aux <=9:
							p1_sprite = 3
							aux += 1
						elif aux <=12:
							p1_sprite = 2
							aux += 1
							if aux == 12:
								aux = 0

			if jump_count > 0 and imgy <= 400:  #jump
				aux = 0
				if pressed_left:
					imgx -= pixMove/5  #ITS A FEATURE!!
					p1_sprite = 10
				elif pressed_right:
					imgx += pixMove/5  #IT IS STILL A FEATURE!!
					p1_sprite = 9
				else:			
					if aux_lado == "right":
						p1_sprite = 9
					elif aux_lado == "left":
						p1_sprite = 10
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
						imgx -= 3*pixMove
						imgy = 330
						jump_count = 0
						if aux_lado == "right":
							p1_sprite = 1
						elif aux_lado =="left":
							p1_sprite = 4

					elif pressed_right:
						imgx += 3*pixMove
						imgy = 330
						jump_count = 0
						p1_sprite = 1
						if aux_lado == "right":
							p1_sprite = 1
						elif aux_lado =="left":
							p1_sprite = 4

				if jump_count == 1:
					imgy = 330
					if aux_lado == "right":
						p1_sprite = 1
					elif aux_lado == "left":
						p1_sprite = 4
				
				jump_count -= 1
				
				if jump_count <= 0:
					pixAir = False
					jump_count = 0
					pixGround = True

			if imgx < 180 or imgx > 605 or imgy > 330:
				if pixAir == False:
					pixFall += g
					imgy += pixFall				
			imgWidth = 50
			imgHeight = 40
			if pressed_space:
				if aux_lado == "right":
					p1_sprite = 7
					punch_aux = 10
				elif aux_lado =="left":
					p1_sprite = 8
					punch_aux = 10
			#img = pygame.transform.scale(img,(imgWidth,imgHeight))
			img2 = pygame.transform.scale(img2,(imgWidth, 2*imgHeight))
			bg = pygame.image.load('fdbackground.jpg')
			bg = pygame.transform.scale(bg,(dispWidth,dispHeight))
			setDisplay.blit(bg,(0,0))
			if p1_sprite == 1: #p1_sprite do personagem em relacao a sua posicao
				setDisplay.blit(p1_walkRight1,(imgx,imgy))
			if p1_sprite == 2:
				setDisplay.blit(p1_walkRight2,(imgx,imgy))
			if p1_sprite == 3:
				setDisplay.blit(p1_walkRight3,(imgx,imgy))
			if p1_sprite == 4:
				setDisplay.blit(p1_walkLeft1,(imgx,imgy))
			if p1_sprite == 5:
				setDisplay.blit(p1_walkLeft2,(imgx,imgy))
			if p1_sprite == 6:
				setDisplay.blit(p1_walkLeft3,(imgx,imgy))
			if p1_sprite == 7 and punch_aux > 0:
				setDisplay.blit(p1_punchRight,(imgx,imgy))
				punch_aux -=1
				if punch_aux == 0:
					p1_sprite = 1
			if p1_sprite == 8 and punch_aux > 0:
				setDisplay.blit(p1_punchLeft,(imgx,imgy))
				punch_aux -=1
				if punch_aux == 0:
					p1_sprite = 4
			if p1_sprite == 9:
				setDisplay.blit(p1_jumpRight,(imgx,imgy))
			if p1_sprite == 10:
				setDisplay.blit(p1_jumpLeft,(imgx,imgy))
			if p1_sprite == 7 or p1_sprite == 8:#impacto teste
				if imgx - 57 in range(imgx2-38,imgx2+38) and imgy+70 in range(imgy2-5,imgy2+5):
					if imgx - 57 >= imgx2:
						imgx2-=10
					if imgx - 57 < imgx2:
						imgx2+=10
			#setDisplay.blit(img,(imgx - imgWidth,imgy - imgHeight))
			setDisplay.blit(img2,(imgx2 + imgWidth, imgy2 - 2*imgHeight))
			fase = pygame.draw.rect(setDisplay, purple, (200, 400, 400, 20))
			pygame.display.update()
			print(imgx)
			print(imgx2)


			if (imgx < 0 or imgy < 0 or imgx > (dispWidth - imgWidth) or imgy > (dispHeight - imgHeight)):
				#kills
				alive = False
				print('You Died')
				pygame.quit()
				sys.exit()

while True:
	global fpsTime
	global setDisplay

	fpsTime = pygame.time.Clock()
	setDisplay = pygame.display.set_mode((dispWidth,dispHeight))
	pygame.display.set_caption('kirby\'s controlled adventure')
	runGame()
			