# -*- coding: utf-8 -*-

import pygame
from Settings import *
from Projective import *

class Game_objects():
	def __init__(self, game, direction, start_x, start_y, name, hp, mp, image_pack):
		self.game = game
		self.direction = direction
		self.state = ALIVE
		self.x = start_x
		self.y = start_y
		self.name = name
		self.hp = hp
		self.mp = mp
		self.image_pack = image_pack
		self.images = []
		self.spell_casted = 0
		for image in self.image_pack:
			temp = pygame.image.load(image).convert_alpha()
			i = []
			i.append(temp.subsurface(0,0,64,64))
			i.append(temp.subsurface(64,0,64,64))
			i.append(temp.subsurface(128,0,64,64))
			self.images.append(i)
		#self.dots = [[self.x, self.y],[self.x+64, self.y], [self.x, self.y+64], [self.x+64, self.y+64]]
		#self.coordination = [w_r = , w_l, ]
		self.mooving = [0,0,0,0]
		self.blocked = [0,0,0,0]
		self.size = 40

	def die(self):
		self.hp = 0
		self.state = DEAD


	def tick(self):
		if self.state != DEAD:
			if self.hp >= MAX_HP:
				self.hp = MAX_HP
			if self.mp >= MAX_MP:
				self.mp = MAX_MP
			self.hp += HP_REG
			self.mp += MP_REG
			if pygame.time.get_ticks() > self.spell_casted + 1000:
				self.state = ALIVE
			if self.hp <= 0:
				self.die()

	def shoot_z(self):
		if self.mp >= SKILL1_COST and self.state != SHOOT:
			self.mp -= SKILL1_COST
			self.state = SHOOT
			#self.spell_casted = pygame.time.get_ticks()
			if self.direction == RIGHT:
				self.__shoot__(8, 18)
			elif self.direction == DOWN:
				self.__shoot__(18, 0)
			elif self.direction == LEFT:
				self.__shoot__(-16, 16)
			else:
				self.__shoot__(18, 0)

	def __shoot__(self, x, y):
		self.game.projective.append(Arrow(self.game, self.x + x, self.y + y, self.direction))

	def block_check(self):
		self.blocked = [0,0,0,0]
		#for i in self.mobs:
		self.contact_check(self.game.player2)

		if self.x <= 0: self.blocked[LEFT] = 1
		if self.y <= 0: self.blocked[UP] = 1
		if self.x >= WIDTH - 60: self.blocked[RIGHT] = 1
		if self.y >= HEIGHT - 64: self.blocked[DOWN] = 1


	def contact_check(self, obj):
		# self.wx 
		# self.wy
		
		wall = obj.x - obj.size
		wall_1 = obj.y + obj.size
		wall_2 = obj.y - obj.size
		w_zh = obj.x
		right = [wall, wall_1, wall_2, w_zh]
		#print(right)
		if w_zh >= self.x >= wall and wall_2 <= self.y <= wall_1:
			self.blocked[RIGHT] = 1
		if self.x <= wall:
			self.blocked[LEFT] = 1


	# def contact_check(self, obj):
	# 	if self.x >= obj.x - self.size and self.y <= obj.y + obj.size and self.y >= obj.y - obj.size and self.x <= obj.x:# + obj.size/2:
	# 		self.blocked[RIGHT] = 1
		

	def moove(self):
		self.block_check()
		if self.state != DEAD:
			if self.mooving[RIGHT] == 1:
				self.direction = RIGHT
				if self.blocked[RIGHT] == 0:
					self.x += PLAYER_SPEED
					
				
			if self.mooving[DOWN] == 1 and self.blocked[DOWN] == 0:
				self.direction = DOWN
				self.y += PLAYER_SPEED
			if self.mooving[LEFT] == 1 and self.blocked[LEFT] == 0:
				self.direction = LEFT
				self.x -= PLAYER_SPEED
			if self.mooving[UP] == 1 and self.blocked[UP] == 0:
				self.direction = UP
				self.y -= PLAYER_SPEED


			# if self.x <= 0: self.x = 0
			# if self.y <= 0: self.y = 0
			# if self.x >= WIDTH - 60: self.x = WIDTH - 60
			# if self.y >= HEIGHT - 64: self.y = HEIGHT - 64

	# def render_ui(self, screen):
	# 	screen.blit(pygame.image.load('assets/hp.png'), (self.x+12, self.y+58))
	# 	screen.blit(pygame.image.load('assets/mp.png'), (self.x+12, self.y+62))
	# 	m = 1
	# 	z = self.hp // 5
	# 	while m <= z:
	# 		screen.blit(pygame.image.load('assets/thp.png'), (self.x+11+m*2, self.y+58))
	# 		m += 1

	# 	m = 1
	# 	z = self.mp // 5
	# 	while m <= z:
	# 		screen.blit(pygame.image.load('assets/tmp.png'), (self.x+11+m*2, self.y+62))
	# 		m += 1


	def render(self, screen):
		screen.blit(self.images[self.direction][self.state], (self.x, self.y))
		screen.blit(pygame.image.load('assets/hp.png'), (self.x+12, self.y+58))
		screen.blit(pygame.image.load('assets/mp.png'), (self.x+12, self.y+62))
		m = 1
		z = self.hp // 5
		while m <= z:
			screen.blit(pygame.image.load('assets/thp.png'), (self.x+11+m*2, self.y+58))
			m += 1

		m = 1
		z = self.mp // 5
		while m <= z:
			screen.blit(pygame.image.load('assets/tmp.png'), (self.x+11+m*2, self.y+62))
			m += 1

	


	def __str__(self):
		return '({}, {})'.format(self.x, self.y)

class Player(Game_objects):
	def __init__(self, game):
		self.direction = RIGHT
		self.state = ALIVE
		self.x = START_X
		self.y = START_Y
		self.name = 'sasa'
		self.hp = MAX_HP
		self.mp = MAX_MP
		self.image_pack = ['assets/archerr.png','assets/archerd.png','assets/archerl.png','assets/archeru.png',]
		Game_objects.__init__(self, game, self.direction, self.x, self.y, self.name, self.hp, self.mp, self.image_pack)

class Player2(Game_objects):
	def __init__(self, game):
		self.direction = LEFT
		self.state = ALIVE
		self.x = START_X + 300
		self.y = START_Y
		self.name = 'sasa'
		self.hp = MAX_HP
		self.mp = MAX_MP
		self.image_pack = ['assets/skeletonr.png','assets/skeletond.png','assets/skeletonl.png','assets/skeletonu.png',]
		Game_objects.__init__(self, game, self.direction, self.x, self.y, self.name, self.hp, self.mp, self.image_pack)