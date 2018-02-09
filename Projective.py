import pygame
from Settings import *

class Projective():
	def __init__(self, game, x_start, y_start, dire, image_pack):
			self.game = game
			self.x = x_start
			self.y = y_start
			self.direction = dire
			self.image = pygame.image.load(image_pack).convert_alpha()
			self.images = []
			self.images.append(self.image.subsurface(45,0,45,45))
			self.images.append(self.image.subsurface(90,0,45,45))
			self.images.append(self.image.subsurface(135,0,43,45))
			self.images.append(self.image.subsurface(0,0,45,45))

			
			
	def render(self, screen):
		screen.blit(self.images[self.direction], (self.x, self.y))


	def moove(self):
		if self.direction == RIGHT:
			self.x += self.speed
		elif self.direction == DOWN:
			self.y += self.speed
		elif self.direction == LEFT:
			self.x -= self.speed
		else:
			self.y -= self.speed

		if self.x > WIDTH or self.x < -32 or self.y > HEIGHT or self.y <-32:
			self.remove()

	def remove(self):
		self.game.projective.remove(self)

	def __str__(self):
		return '({}, {})'.format(self.x, self.y)


class Arrow(Projective):
	def __init__(self, game, x_start, y_start, dire):
		self.image = 'assets/arrow.png'
		self.speed = 25
		Projective.__init__(self, game, x_start, y_start, dire, self.image)

