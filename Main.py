import sys
import pygame
from Settings import *
from Game_objects2 import *
from pygame.locals import *
from Projective import *

class Main():
	def __init__(self, screen):
		self.screen = screen
		self.player = Player(self)
		self.player2 = Player2(self)
		self.projective = []
		self.mobs = []
		self.background = pygame.image.load('assets/background.jpg')
		self.running = True
		self.timer = pygame.time.Clock()
		self.main_loop()

	# def handle_events(self):
	# 	for event in pygame.event.get():
	# 		if event.type == QUIT:
	# 			self.running = False
	# 			#MOOVING PLAYER
	# 		elif event.type == USEREVENT+1:
	# 			self.player.tick()
	# 		elif event.type == KEYDOWN:

	# 			if event.key == K_RIGHT:
	# 				self.player.mooving = [1,0,0,0]
	# 				#print(self.player)

	# 			if event.key == K_DOWN:
	# 				self.player.mooving = [0,1,0,0]

	# 			if event.key == K_LEFT:
	# 				self.player.mooving = [0,0,1,0]

	# 			if event.key == K_UP:
	# 				self.player.mooving = [0,0,0,1]

	# 			if event.key == K_SPACE:
	# 				if self.player.state != DEAD:
	# 					self.player.die()
	# 				else:
	# 					self.player.state = ALIVE

	# 			if event.key == K_z:
	# 				self.player.shoot_z()
	# 			#print(self.player)

	# 		#KEY OTZHATIE
	# 		elif event.type == KEYUP:
	# 			# if event.key == K_z:
	# 			# 	self.player.state = ALIVE

	# 			if event.key == K_UP:
	# 				self.player.mooving[UP] = 0
	# 			if event.key == K_DOWN:
	# 				self.player.mooving[DOWN] = 0
	# 			if event.key == K_RIGHT:
	# 				self.player.mooving[RIGHT] = 0
	# 			if event.key == K_LEFT:
	# 				self.player.mooving[LEFT] = 0
	# 			#print(self.player)

	def handle_events(self, player):
		self.player = player
		for event in pygame.event.get():
			if event.type == QUIT:
				self.running = False
				#MOOVING PLAYER
			elif event.type == USEREVENT+1:
				self.player.tick()
			elif event.type == KEYDOWN:

				if event.key == K_RIGHT:
					self.player.mooving = [1,0,0,0]
					#print(self.player)

				if event.key == K_DOWN:
					self.player.mooving = [0,1,0,0]

				if event.key == K_LEFT:
					self.player.mooving = [0,0,1,0]

				if event.key == K_UP:
					self.player.mooving = [0,0,0,1]

				if event.key == K_SPACE:
					if self.player.state != DEAD:
						self.player.die()
					else:
						self.player.state = ALIVE

				if event.key == K_z:
					self.player.shoot_z()
				#print(self.player)

			#KEY OTZHATIE
			elif event.type == KEYUP:
				# if event.key == K_z:
				# 	self.player.state = ALIVE

				if event.key == K_UP:
					self.player.mooving[UP] = 0
				if event.key == K_DOWN:
					self.player.mooving[DOWN] = 0
				if event.key == K_RIGHT:
					self.player.mooving[RIGHT] = 0
				if event.key == K_LEFT:
					self.player.mooving[LEFT] = 0
				#print(self.player)

	def render(self):
		self.screen.blit(self.background, (0, 0))
		self.player.render(screen)
		self.player2.render(screen)
		# self.player.render_ui(screen)
		for i in self.projective:
			i.render(screen)
		pygame.display.flip()

	def main_loop(self):
		#self.player = self.player
		pygame.time.set_timer(USEREVENT+1, 100)
		while self.running == True:
			self.timer.tick(33)
			self.player.moove()
			for i in self.projective:
				i.moove()
			if len(self.projective) != 0:   #чтобы не молотило вечно
				print(self.projective[0])   #сам проджект это список, элемент списка это объект
			self.render()
			self.handle_events(self.player)



pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
game = Main(screen)
