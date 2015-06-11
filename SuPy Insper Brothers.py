import pygame
import sys
from pygame.locals import *
import os #Para importar arquivos de diferentes pastas
import time

pygame.init()

#Cores
white = (255,255,255)
black = (0,0,0)
black_creditos = (16,16,16)
red = (150,0,0)
bright_red = (255,0,0)
green = (0,150,0)
bright_green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
purple = (255,0,255)


#Configurações Gerais
fps = 100
dispWidth = 800
dispHeight = 600
pixMove = 10


#Posição inicial P1
p1_eixox = 370
p1_eixoy = 400

#Posicao inicial P2
p2_eixox = 500
p2_eixoy = 400

#Pastas
pasta_imagens = "Imagens"
pasta_musicas = "Musicas"
pasta_menu = "Menu"
pasta_credits = "IMG Credits"



#Ler Imagens
full_life = pygame.image.load(os.path.join(pasta_imagens,'full_life.png'))
img = pygame.image.load(os.path.join(pasta_imagens,'kirby.png'))
img2 = pygame.image.load(os.path.join(pasta_imagens,'fox.png'))
icon = pygame.image.load(os.path.join(pasta_imagens,'logo.png'))
p1_walkRight1 = pygame.image.load(os.path.join(pasta_imagens,'pedro_right1.png'))
p1_walkRight2 = pygame.image.load(os.path.join(pasta_imagens,'pedro_right2.png'))
p1_walkRight3= pygame.image.load(os.path.join(pasta_imagens,'pedro_right3.png'))
p1_walkLeft1= pygame.image.load(os.path.join(pasta_imagens,'pedro_left1.png'))
p1_walkLeft2= pygame.image.load(os.path.join(pasta_imagens,'pedro_left2.png'))
p1_walkLeft3= pygame.image.load(os.path.join(pasta_imagens,'pedro_left3.png'))
p1_punchLeft= pygame.image.load(os.path.join(pasta_imagens,'pedro_punch_left.png'))
p1_punchRight= pygame.image.load(os.path.join(pasta_imagens,'pedro_punch_right.png'))
p1_jumpRight = pygame.image.load(os.path.join(pasta_imagens,'pedro_jump_right.png'))
p1_jumpLeft = pygame.image.load(os.path.join(pasta_imagens,'pedro_jump_left.png'))

p2_walkRight1 = pygame.image.load(os.path.join(pasta_imagens,'Andar1_Right.png'))
p2_walkRight2 = pygame.image.load(os.path.join(pasta_imagens,'Andar2_Right.png'))
p2_walkRight3= pygame.image.load(os.path.join(pasta_imagens,'Andar3_Right.png'))
p2_walkLeft1= pygame.image.load(os.path.join(pasta_imagens,'Andar1_Left.png'))
p2_walkLeft2= pygame.image.load(os.path.join(pasta_imagens,'Andar2_Left.png'))
p2_walkLeft3= pygame.image.load(os.path.join(pasta_imagens,'Andar3_Left.png'))
p2_punchLeft= pygame.image.load(os.path.join(pasta_imagens,'Soco_Left.png'))
p2_punchRight= pygame.image.load(os.path.join(pasta_imagens,'Soco_Right.png'))
p2_jumpRight = pygame.image.load(os.path.join(pasta_imagens,'Pular_Right.png'))
p2_jumpLeft = pygame.image.load(os.path.join(pasta_imagens,'Pular_Left.png'))


p3_walkRight1 = pygame.image.load(os.path.join(pasta_imagens,'lourenco_right1.png'))
p3_walkRight2 = pygame.image.load(os.path.join(pasta_imagens,'lourenco_right2.png'))
p3_walkRight3= pygame.image.load(os.path.join(pasta_imagens,'lourenco_right3.png'))
p3_walkLeft1= pygame.image.load(os.path.join(pasta_imagens,'lourenco_left1.png'))
p3_walkLeft2= pygame.image.load(os.path.join(pasta_imagens,'lourenco_left2.png'))
p3_walkLeft3= pygame.image.load(os.path.join(pasta_imagens,'lourenco_left3.png'))
p3_punchLeft= pygame.image.load(os.path.join(pasta_imagens,'lourenco_punch_left.png'))
p3_punchRight= pygame.image.load(os.path.join(pasta_imagens,'lourenco_punch_right.png'))
p3_jumpRight = pygame.image.load(os.path.join(pasta_imagens,'lourenco_jump_right.png'))
p3_jumpLeft = pygame.image.load(os.path.join(pasta_imagens,'lourenco_jump_left.png'))

p4_walkRight1 = pygame.image.load(os.path.join(pasta_imagens,'miranda_right1.png'))
p4_walkRight2 = pygame.image.load(os.path.join(pasta_imagens,'miranda_right2.png'))
p4_walkRight3= pygame.image.load(os.path.join(pasta_imagens,'miranda_right3.png'))
p4_walkLeft1= pygame.image.load(os.path.join(pasta_imagens,'miranda_left1.png'))
p4_walkLeft2= pygame.image.load(os.path.join(pasta_imagens,'miranda_left2.png'))
p4_walkLeft3= pygame.image.load(os.path.join(pasta_imagens,'miranda_left3.png'))
p4_punchLeft= pygame.image.load(os.path.join(pasta_imagens,'miranda_punch_left.png'))
p4_punchRight= pygame.image.load(os.path.join(pasta_imagens,'miranda_punch_right.png'))
p4_jumpRight = pygame.image.load(os.path.join(pasta_imagens,'miranda_jump_right.png'))
p4_jumpLeft = pygame.image.load(os.path.join(pasta_imagens,'miranda_jump_left.png'))

#Imagens Menu
background_menu = pygame.image.load(os.path.join(pasta_menu,'background_menu.png'))
background_character = pygame.image.load(os.path.join(pasta_menu,'choose_character.png'))
bg = pygame.image.load(os.path.join(pasta_imagens,'background.png'))
p1_select = pygame.image.load(os.path.join(pasta_menu,'select_p1.png'))
p2_select = pygame.image.load(os.path.join(pasta_menu,'select_p2.png'))
start_1 = pygame.image.load(os.path.join(pasta_menu,'start_1.png'))
start_2 = pygame.image.load(os.path.join(pasta_menu,'start_2.png'))
close_1 = pygame.image.load(os.path.join(pasta_menu,'close_1.png'))
close_2 = pygame.image.load(os.path.join(pasta_menu,'close_2.png'))
credits1 = pygame.image.load(os.path.join(pasta_menu,'credits1.png'))
credits2 = pygame.image.load(os.path.join(pasta_menu,'credits2.png'))


#Wins
p1_wins = pygame.image.load(os.path.join(pasta_imagens,'player1_wins.png'))
p2_wins = pygame.image.load(os.path.join(pasta_imagens,'player2_wins.png'))

#Ninja
movie = pygame.movie.Movie(os.path.join(pasta_credits,'ninja.mpg'))
creditos = pygame.image.load(os.path.join(pasta_credits,'creditos.jpg'))



#Classe Personagens
class Personagem(object):
	def __init__(self,eixox,eixoy,sprite1,sprite2,sprite3,sprite4,sprite5,sprite6,sprite7,sprite8,sprite9,sprite10,altura_hitbox):
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
		self.altura_hitbox = altura_hitbox



#Função Menu
def Menu():
	pygame.mixer.music.load(os.path.join(pasta_musicas,'quimica-do-amor.wav'))
	pygame.mixer.music.play(-1)
	button_pressed = False	
	i = 0
	while not button_pressed:
		setDisplay.blit(background_menu,(0,0))
		for event in pygame.event.get():
			mouse_pos = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		if 300 > mouse_pos[0] > 100 and 500 > mouse_pos[1] > 400:
			setDisplay.blit(start_2,(100,400))
			if click[0] == 1:
				button_pressed = True
				#pygame.mixer.music.stop()
		else:
			setDisplay.blit(start_1,(100,400))
		if 700 > mouse_pos[0] > 500 and 500 > mouse_pos[1] > 400:
			setDisplay.blit(close_2,(500,400))
			if click[0] == 1:
				pygame.quit()
				sys.exit()
		else:
			setDisplay.blit(close_1,(500,400))
		if 120 > mouse_pos[0] > 0 and 23 > mouse_pos[1] > 0:
			if i == 0:
				setDisplay.blit(credits1,(5,5))
				i+=1
			elif i == 1:
				setDisplay.blit(credits2,(5,5))
				i-=1
			if click[0] == 1:
				button_pressed = "Creditos"
				pygame.mixer.music.stop()
				return button_pressed
		pygame.display.update()


#Função escolher personagem
def Character():
	personagem = [0]*2
	button_pressed_p1 = False	
	button_pressed_p2 = False
	#Escolher P1
	while not button_pressed_p1:
		setDisplay.blit(background_character,(0,0))
		for event in pygame.event.get():
			mouse_pos = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if 165 > mouse_pos[0] > 66 and 233 > mouse_pos[1] > 133:
				setDisplay.blit(p1_select,(65,130))
				if click[0] == 1:
					personagem[0] = "Pedro"
					button_pressed_p1 = True
			if 306 > mouse_pos[0] > 207 and 233 > mouse_pos[1] > 133:
				setDisplay.blit(p1_select,(207,130))
				if click[0] == 1:
					personagem[0] = "PixelGuy"
					button_pressed_p1 = True
			if 446 > mouse_pos[0] > 347 and 233 > mouse_pos[1] > 133:
				setDisplay.blit(p1_select,(349,130))
				if click[0] == 1:
					personagem[0] = "Lourenco"
					button_pressed_p1 = True
			if 586 > mouse_pos[0] > 487 and 233 > mouse_pos[1] > 133:
				setDisplay.blit(p1_select,(491,130))
				if click[0] == 1:
					personagem[0] = "Miranda"
					button_pressed_p1 = True
			#Adicionar novos personagens aqui.
			#
			#
			#

			pygame.display.update()
	#Escolher P2
	click_continuo = False
	while not click_continuo:
		for event in pygame.event.get():
			click = pygame.mouse.get_pressed()
			if click[0] == 0:
				click_continuo = True
	while not button_pressed_p2:
		setDisplay.blit(background_character,(0,0))
		for event in pygame.event.get():
			mouse_pos = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if 165 > mouse_pos[0] > 66 and 233 > mouse_pos[1] > 133:
				setDisplay.blit(p2_select,(65,130))
				if click[0] == 1:
					personagem[1] = "Pedro"
					button_pressed_p2 = True
			if 306 > mouse_pos[0] > 207 and 233 > mouse_pos[1] > 133:
				setDisplay.blit(p2_select,(207,130))
				if click[0] == 1:
					personagem[1] = "PixelGuy"
					button_pressed_p2 = True
			if 446 > mouse_pos[0] > 347 and 233 > mouse_pos[1] > 133:
				setDisplay.blit(p2_select,(349,130))
				if click[0] == 1:
					personagem[1] = "Lourenco"
					button_pressed_p2 = True
			if 586 > mouse_pos[0] > 487 and 233 > mouse_pos[1] > 133:
				setDisplay.blit(p2_select,(491,130))
				if click[0] == 1:
					personagem[1] = "Miranda"
					button_pressed_p2 = True
			#Adicionar novos personagens aqui.
			#
			#
			#
			
			pygame.display.update()
	return personagem

def PlayerWin(win):
	setDisplay.blit(bg,(0,0))
	if win == "p1":	
		setDisplay.blit(p1_wins,(0,0))
	if win == "p2":
		setDisplay.blit(p2_wins,(0,0))
	pygame.display.update()
	time.sleep(3)

def Credits():
	FPS = 60
	credits_x = 500
	credits_y = 600
	pygame.mixer.music.load(os.path.join(pasta_musicas,'sandstorm.mp3'))
	pygame.mixer.music.play(-1)
	clock = pygame.time.Clock()
	movie = pygame.movie.Movie(os.path.join(pasta_credits,'ninja.mpg'))
	movie_screen = pygame.Surface(movie.get_size()).convert()
	movie.set_display(movie_screen)
	movie.play()

	playing = True
	while playing:
		credits_y -= 1
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				movie.stop()
				playing = False
		setDisplay.fill(black_creditos)
		setDisplay.blit(movie_screen,(50,200))
		setDisplay.blit(creditos,(credits_x,credits_y))
		pygame.display.update()
		clock.tick(FPS)

	pygame.quit()
#Função Principal - Rodar Jogo
def runGame():


	#Definindo personagens
	if personagem[0] == "Pedro":
		P1 = Personagem(p1_eixox,p1_eixoy,p1_walkRight1,p1_walkRight2,p1_walkRight3,p1_walkLeft1,p1_walkLeft2,p1_walkLeft3,p1_punchRight,p1_punchLeft,p1_jumpRight,p1_jumpLeft,42)
	if personagem[0] == "PixelGuy":
		P1 = Personagem(p1_eixox,p1_eixoy,p2_walkRight1,p2_walkRight2,p2_walkRight3,p2_walkLeft1,p2_walkLeft2,p2_walkLeft3,p2_punchRight,p2_punchLeft,p2_jumpRight,p2_jumpLeft,20)
	if personagem[0] == "Lourenco":
		P1 = Personagem(p1_eixox,p1_eixoy,p3_walkRight1,p3_walkRight2,p3_walkRight3,p3_walkLeft1,p3_walkLeft2,p3_walkLeft3,p3_punchRight,p3_punchLeft,p3_jumpRight,p3_jumpLeft,42)
	if personagem[0] == "Miranda":
		P1 = Personagem(p1_eixox,p1_eixoy,p4_walkRight1,p4_walkRight2,p4_walkRight3,p4_walkLeft1,p4_walkLeft2,p4_walkLeft3,p4_punchRight,p4_punchLeft,p4_jumpRight,p4_jumpLeft,42)
	if personagem[1] == "Pedro":
		P2 = Personagem(p2_eixox,p2_eixoy,p1_walkRight1,p1_walkRight2,p1_walkRight3,p1_walkLeft1,p1_walkLeft2,p1_walkLeft3,p1_punchRight,p1_punchLeft,p1_jumpRight,p1_jumpLeft,42)
	if personagem[1] == "PixelGuy":
		P2 = Personagem(p2_eixox,p2_eixoy,p2_walkRight1,p2_walkRight2,p2_walkRight3,p2_walkLeft1,p2_walkLeft2,p2_walkLeft3,p2_punchRight,p2_punchLeft,p2_jumpRight,p2_jumpLeft,20)
	if personagem[1] == "Lourenco":
		P2 = Personagem(p1_eixox,p1_eixoy,p3_walkRight1,p3_walkRight2,p3_walkRight3,p3_walkLeft1,p3_walkLeft2,p3_walkLeft3,p3_punchRight,p3_punchLeft,p3_jumpRight,p3_jumpLeft,42)
	if personagem[1] == "Miranda":
		P2 = Personagem(p1_eixox,p1_eixoy,p4_walkRight1,p4_walkRight2,p4_walkRight3,p4_walkLeft1,p4_walkLeft2,p4_walkLeft3,p4_punchRight,p4_punchLeft,p4_jumpRight,p4_jumpLeft,42)



	global img2
	imgx = 300
	if personagem[0] == "Pedro":
		imgy = 308
		imgy_original = 308
	if personagem[0] == "PixelGuy":
		imgy = 330
		imgy_original = 330
	if personagem[1] == "Pedro":
		imgy2 = 308
		imgy2_original = 308
	if personagem[1] == "PixelGuy":
		imgy2 = 330
		imgy2_original = 330
	if personagem[0] == "Lourenco":
		imgy = 308
		imgy_original = 308
	if personagem[1] == "Lourenco":
		imgy2 = 308
		imgy2_original = 308
	if personagem[0] == "Miranda":
		imgy = 308
		imgy_original = 308
	if personagem[1] == "Miranda":
		imgy2 = 308
		imgy2_original = 308

	alive = True
	pressed_up = False
	g = 0.5
	p1_jump_count = 0
	p2_jump_count = 0

	pygame.mixer.music.load(os.path.join(pasta_musicas,'fd_8bits.mp3'))
	pygame.mixer.music.set_volume(0.6)
	pygame.mixer.music.play(-1)

	p1_pixFall = 0
	p2_pixFall = 0
	p1_pixAir = False
	p2_pixAir = False
	p1_aux_lado = "right"
	p2_aux_lado = "left"
	p1_aux = 0
	p2_aux = 0
	p1_sprite = 1
	p2_sprite = 4
	imgx2 = 430
	game = True
	p1_hitstun = 0
	p2_hitstun = 0
	hitstun = 7
	knockback = 25
	hit1 = 0
	hit2 = 0
	while game:     #main loop
		delay = 20
		interval = 30
		pygame.key.set_repeat(delay, interval)
		#Consertar erro (????)
		pressed_rctrl = False
		pressed_tab = False
		win = False

		while alive:
			for event in pygame.event.get():	#event handling loop
				pressed_left = False
				pressed_right = False
				pressed_down = False
				pressed_rctrl = False
				
				pressed_d = False
				pressed_a = False
				pressed_s = False
				pressed_tab = False
				bug = False
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

				#Verificar qual tecla foi pressionada
				keys = pygame.key.get_pressed()
				#P1
				if p1_hitstun <= 0:		#personagem só poderá atacar se não estiver em hitstun
					if keys[K_RCTRL]:
						pressed_rctrl = True
					if keys[K_LEFT]:
						pressed_left = True
						pressed_rctrl = False
						p1_aux_lado = "left"
					if keys[K_RIGHT]:
						pressed_right = True
						pressed_rctrl = False
						p1_aux_lado = "right"
					if keys[K_DOWN]:
						pressed_down = True
					if keys[K_UP] and p1_jump_count == 0  and imgy <= imgy_original:
						pressed_up = True
						p1_jump_count = 38
						p1_pixFall = 0
						p1_pixJump = pixMove
						p1_pixAir = True
				p1_hitstun -= 1 	#subtrai valores da hitstun até zerar e o jogador poder controlar seu personagem novamente

				if p2_hitstun <= 0: 	#personagem só poderá atacar e não estiver em hitstun (ver código mais abaixo, na parte de colisões)
				

				#P2
					if keys [K_TAB]:
						pressed_tab = True
					if keys[K_d]:
						pressed_d = True
						pressed_tab = False
						p2_aux_lado = "right"
					if keys[K_w] and p2_jump_count == 0 and imgy2 <= imgy2_original:
						pressed_w = True
						p2_jump_count = 38
						p2_pixFall = 0
						p2_pixJump = pixMove
						p2_pixAir = True
					if keys[K_a]:
						pressed_a = True
						pressed_tab = False
						p2_aux_lado = "left"
					if keys [K_s]:
						pressed_s = True
				p2_hitstun -= 1 	#subtrai valores da hitstun até zerar e o jogador poder controlar seu personagem novamente


				# Andar Esquerda_P1
				if pressed_left: 
					imgx -= pixMove
					if p1_jump_count == 0:# posicao das pernas ao andar
						if p1_aux <= 3:
							p1_sprite = 4
							p1_aux += 1
						elif p1_aux <= 6:
							p1_sprite = 5
							p1_aux += 1
						elif p1_aux <= 9:
							p1_sprite = 6
							p1_aux += 1
						elif p1_aux <= 12:
							p1_sprite = 5
							p1_aux += 1
							if p1_aux == 12:
								p1_aux = 0

				# Andar Direita_P1
				elif pressed_right:
					imgx += pixMove
					if p1_jump_count == 0:# posicao das pernas ao andar
						if p1_aux <=3:
							p1_sprite = 1
							p1_aux += 1
						elif p1_aux <=6:
							p1_sprite = 2
							p1_aux += 1
						elif p1_aux <=9:
							p1_sprite = 3
							p1_aux += 1
						elif p1_aux <=12:
							p1_sprite = 2
							p1_aux += 1
							if p1_aux == 12:
								p1_aux = 0




				# Andar Esquerda_P2
				if pressed_a: 
					imgx2 -= pixMove
					if p2_jump_count == 0:# posicao das pernas ao andar
						if p2_aux <= 3:
							p2_sprite = 4
							p2_aux += 1
						elif p2_aux <= 6:
							p2_sprite = 5
							p2_aux += 1
						elif p2_aux <= 9:
							p2_sprite = 6
							p2_aux += 1
						elif p2_aux <= 12:
							p2_sprite = 5
							p2_aux += 1
							if p2_aux == 12:
								p2_aux = 0

				# Andar Direita_P2
				elif pressed_d:
					imgx2 += pixMove
					if p2_jump_count == 0:# posicao das pernas ao andar
						if p2_aux <=3:
							p2_sprite = 1
							p2_aux += 1
						elif p2_aux <=6:
							p2_sprite = 2
							p2_aux += 1
						elif p2_aux <=9:
							p2_sprite = 3
							p2_aux += 1
						elif p2_aux <=12:
							p2_sprite = 2
							p2_aux += 1
							if p2_aux == 12:
								p2_aux = 0
			#Soco_P1
			if pressed_rctrl:
				if p1_aux_lado == "right":
					p1_sprite = 7
					p1_punch_aux = 10
				elif p1_aux_lado =="left":
					p1_sprite = 8
					p1_punch_aux = 10


			#Soco_P2
			if pressed_tab:
				if p2_aux_lado == "right":
					p2_sprite = 7
					p2_punch_aux = 10
				elif p2_aux_lado =="left":
					p2_sprite = 8
					p2_punch_aux = 10

			# Pular_P1
			if p1_jump_count > 0 and imgy <= 330: 
				p1_aux = 0
				if pressed_left:
					imgx -= pixMove/5  #ITS A FEATURE!!
					p1_sprite = 10
				elif pressed_right:
					imgx += pixMove/5  #IT IS STILL A FEATURE!!
					p1_sprite = 9
				else:			
					if p1_aux_lado == "right":
						p1_sprite = 9
					elif p1_aux_lado == "left":
						p1_sprite = 10
				if p1_pixJump > 0: #UP WE GO!
					p1_pixJump = p1_pixJump - g
					if p1_pixJump < 0: #falls
						p1_pixJump = 0
					imgy -= p1_pixJump

				elif p1_pixJump <= 0:
					p1_pixFall += g
					imgy += p1_pixFall
					if imgy >= 400:
						p1_pixJump = pixMove
						p1_pixFall = 0
						pressed_up = False


				# Wave Dash_P1
				if pygame.key.get_pressed()[K_DOWN]:
					if pressed_left:
						imgx -= 3*pixMove
						imgy = imgy_original
						p1_jump_count = 0
						if p1_aux_lado == "right":
							p1_sprite = 1
						elif p1_aux_lado =="left":
							p1_sprite = 4

					elif pressed_right:
						imgx += 3*pixMove
						imgy = imgy_original
						p1_jump_count = 0
						p1_sprite = 1
						if p1_aux_lado == "right":
							p1_sprite = 1
						elif p1_aux_lado =="left":
							p1_sprite = 4

				#Cair na plataforma/Mudar sprite para andando_P1
				if p1_jump_count == 1:
					imgy = imgy_original
					if p1_aux_lado == "right":
						p1_sprite = 1
					elif p1_aux_lado == "left":
						p1_sprite = 4

				#Frames Pulo - 1_P1
				p1_jump_count -= 1
				
				if p1_jump_count <= 0:
					p1_pixAir = False
					p1_jump_count = 0


			#Fora da Plataforma/Gravidade_P1
			if imgx < 180 or imgx > 605 or imgy > 330:
				if not p1_pixAir:
					p1_pixFall += g
					imgy += p1_pixFall				
			
			imgWidth = 50
			imgHeight = 40

			# Pular_P2
			if p2_jump_count > 0 and imgy2 <= 330: 
				p2_aux = 0
				if pressed_a:
					imgx2 -= pixMove/5  #ITS A FEATURE!!
					p2_sprite = 10
				elif pressed_d:
					imgx2 += pixMove/5  #IT IS STILL A FEATURE!!
					p2_sprite = 9
				else:			
					if p2_aux_lado == "right":
						p2_sprite = 9
					elif p2_aux_lado == "left":
						p2_sprite = 10
				if p2_pixJump > 0: #UP WE GO!
					p2_pixJump = p2_pixJump - g
					if p2_pixJump < 0: #falls
						p2_pixJump = 0
					imgy2 -= p2_pixJump

				elif p2_pixJump <= 0:
					p2_pixFall += g
					imgy2 += p2_pixFall
					if imgy2 >= 400:
						p2_pixJump = pixMove
						p2_pixFall = 0
						pressed_w = False


				# Wave Dash_P2
				if pygame.key.get_pressed()[K_s]:
					if pressed_a:
						imgx2 -= 3*pixMove
						imgy2 = imgy2_original
						p2_jump_count = 0
						if p2_aux_lado == "right":
							p2_sprite = 1
						elif p2_aux_lado =="left":
							p2_sprite = 4

					elif pressed_d:
						imgx2 += 3*pixMove
						imgy2 = imgy2_original
						p2_jump_count = 0
						p2_sprite = 1
						if p2_aux_lado == "right":
							p2_sprite = 1
						elif p2_aux_lado =="left":
							p2_pixFall_sprite = 4

				#Cair na plataforma/Mudar sprite para andando_P2
				if p2_jump_count == 1:
					imgy2 = imgy2_original
					if p2_aux_lado == "right":
						p2_sprite = 1
					elif p2_aux_lado == "left":
						p2_sprite = 4

				#Frames Pulo - 1_P2
				p2_jump_count -= 1
				
				if p2_jump_count <= 0:
					p2_pixAir = False
					p2_jump_count = 0


			#Fora da Plataforma/Gravidade_P2
			if imgx2 < 180 or imgx2 > 605 or imgy2 > 330:
				if not p2_pixAir:
					p2_pixFall += g
					imgy2 += p2_pixFall	




			setDisplay.blit(bg,(0,0))
			fase = pygame.draw.rect(setDisplay, purple, (200, 400, 400, 20))
			life1 = pygame.draw.rect(setDisplay, red, (23, 13, 298-hit1, 58))
			life2 = pygame.draw.rect(setDisplay, red, (471, 13, 300-hit2, 58))
			setDisplay.blit(full_life,(0,0))


			#Desenhar Sprites
			#
			#sprite1 = Andar Direita 1
			#sprite2 = Andar Direita 2
			#sprite3 = Andar Direita 3
			#sprite4 = Andar Esquerda 1
			#sprite5 = Andar Esquerda 2
			#sprite6 = Andar Esquerda 3
			#sprite7 = Soco Direita
			#sprite8 = Soco Esquerda
			#sprite9 = Pulo Direita
			#sprite10 = Pulo Esquerda 

			#P1-Sprites
			if p1_sprite == 1: #p1_sprite do personagem em relacao a sua posicao
				setDisplay.blit(P1.sprite_walkRight1,(imgx,imgy))
			if p1_sprite == 2:
				setDisplay.blit(P1.sprite_walkRight2,(imgx,imgy))
			if p1_sprite == 3:
				setDisplay.blit(P1.sprite_walkRight3,(imgx,imgy))
			if p1_sprite == 4:
				setDisplay.blit(P1.sprite_walkLeft1,(imgx,imgy))
			if p1_sprite == 5:
				setDisplay.blit(P1.sprite_walkLeft2,(imgx,imgy))
			if p1_sprite == 6:
				setDisplay.blit(P1.sprite_walkLeft3,(imgx,imgy))
			if p1_sprite == 7 and p1_punch_aux > 0:
				setDisplay.blit(P1.sprite_punchRight,(imgx,imgy))
				p1_punch_aux -=1
				if p1_punch_aux == 0:
					p1_sprite = 1
			if p1_sprite == 8 and p1_punch_aux > 0:
				setDisplay.blit(P1.sprite_punchLeft,(imgx,imgy))
				p1_punch_aux -=1
				if p1_punch_aux == 0:
					p1_sprite = 4
			if p1_sprite == 9:
				setDisplay.blit(P1.sprite_jumpRight,(imgx,imgy))
			if p1_sprite == 10:
				setDisplay.blit(P1.sprite_jumpLeft,(imgx,imgy))


			# Teste Impacto
			if p1_sprite == 7 or p1_sprite == 8:
				if imgx in range(int(imgx2)-38,int(imgx2)+38) and imgy+P1.altura_hitbox in range(int(imgy2)+P2.altura_hitbox -10,int(imgy2)+P2.altura_hitbox+10):
					if imgx >= imgx2:
						imgx2 -= knockback + hit2/5 	#knockback (recuo do personagem ao ser atacado) aumenta conforme ele toma mais dano
					if imgx < imgx2:
						imgx2 += knockback + hit2/5
					p2_hitstun = hitstun 	#hitstun (personagem atacado não poderá atacar por um "breve" periodo)
					hit2+=10

			if p2_sprite == 7 or p2_sprite == 8:
				if imgx2 in range(int(imgx)-38,int(imgx)+38) and imgy2+P2.altura_hitbox in range(int(imgy)+P1.altura_hitbox -10,int(imgy)+P1.altura_hitbox+10):
					if imgx2 >= imgx:
						imgx -= knockback + hit1/5
					if imgx2 < imgx:
						imgx += knockback + hit1/5
					p1_hitstun = hitstun 	#hitstun (personagem atacada não poderá atacar por um 'x' número de frames)
					hit1+=10

			#P2-Sprites
			#setDisplay.blit(img,(imgx - imgWidth,imgy - imgHeight))
			#setDisplay.blit(img2,(imgx2 + imgWidth, imgy2 - 2*imgHeight))
			if p2_sprite == 1: #p2_sprite do personagem em relacao a sua posicao
				setDisplay.blit(P2.sprite_walkRight1,(imgx2,imgy2))
			if p2_sprite == 2:
				setDisplay.blit(P2.sprite_walkRight2,(imgx2,imgy2))
			if p2_sprite == 3:
				setDisplay.blit(P2.sprite_walkRight3,(imgx2,imgy2))
			if p2_sprite == 4:
				setDisplay.blit(P2.sprite_walkLeft1,(imgx2,imgy2))
			if p2_sprite == 5:
				setDisplay.blit(P2.sprite_walkLeft2,(imgx2,imgy2))
			if p2_sprite == 6:
				setDisplay.blit(P2.sprite_walkLeft3,(imgx2,imgy2))
			if p2_sprite == 7 and p2_punch_aux > 0:
				setDisplay.blit(P2.sprite_punchRight,(imgx2,imgy2))
				p2_punch_aux -=1
				if p2_punch_aux == 0:
					p2_sprite = 1
			if p2_sprite == 8 and p2_punch_aux > 0:
				setDisplay.blit(P2.sprite_punchLeft,(imgx2,imgy2))
				p2_punch_aux -=1
				if p2_punch_aux == 0:
					p2_sprite = 4
			if p2_sprite == 9:
				setDisplay.blit(P2.sprite_jumpRight,(imgx2,imgy2))
			if p2_sprite == 10:
				setDisplay.blit(P2.sprite_jumpLeft,(imgx2,imgy2))

			pygame.display.update()

			#Cair da plataforma
			if (imgx < 0 or imgy < 0 or imgx > (dispWidth - imgWidth) or imgy > (dispHeight - imgHeight)):
				#kills
				alive = False
				game = False
				win = "p2"
				pygame.mixer.music.stop()
				return win
			if (imgx2 < 0 or imgy2 < 0 or imgx2 > dispWidth or imgy2 > dispHeight):
				#kills
				alive = False
				game = False
				win = "p1"
				pygame.mixer.music.stop()
				return win
			if hit1 == 300 or hit2 == 300:
				if hit1 == 300:
					win = "p2"
				if hit2 == 300:
					win = "p1"
				alive = False
				game = False
				pygame.mixer.music.stop()
				return win



while True:
	global fpsTime
	global setDisplay
	fpsTime = pygame.time.Clock()
	setDisplay = pygame.display.set_mode((dispWidth,dispHeight))
	pygame.display.set_icon(icon)
	pygame.display.set_caption('SuPy Insper Brothers')
	while True:
		button_pressed = Menu()
		if button_pressed == "Creditos":
			Credits()
		personagem = Character()
		win = runGame()
		PlayerWin(win)	