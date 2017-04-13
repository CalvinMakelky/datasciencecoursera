import math

import pygame
from pygame.sprite import Sprite
from pygame import Rect
from pygame import key
from pygame import display

from vec2d import vec2d

class Player(Sprite):
	def __init__(self, screen, img_filename, init_position, speed):
		Sprite.__init__(self)

		self.screen = screen
		self.speed = speed

		self.base_image = pygame.image.load(img_filename).convert_alpha()
		self.image = self.base_image

		self.image_w, self.image_h = self.image.get_size()

		self.pos = vec2d(init_position)

	def update(self, time_passed):
		pressed = key.get_pressed()

		dx = 0
		dy = 0
		diagonal = False

		# Take the keypresses and move character accordingly
		# Checks for diagonals and correct accordingly
		if pressed[pygame.K_UP]:
			if pressed[pygame.K_LEFT]:
				diagonal = True
				dx -= self.speed / math.sqrt(2) * (time_passed / 1000)
			if pressed[pygame.K_RIGHT]:
				diagonal = True
				dx += self.speed / math.sqrt(2) * (time_passed / 1000)

			if not diagonal or pressed[pygame.K_LEFT] and pressed[pygame.K_RIGHT]:
				dy -= self.speed * (time_passed / 1000)
			else:
				dy -= self.speed / math.sqrt(2) * (time_passed / 1000)

		if pressed[pygame.K_DOWN]:
			if pressed[pygame.K_LEFT]:
				diagonal = True
				dx -= self.speed / math.sqrt(2) * (time_passed / 1000)
			if pressed[pygame.K_RIGHT]:
				diagonal = True
				dx += self.speed / math.sqrt(2) * (time_passed / 1000)

			if not diagonal or pressed[pygame.K_LEFT] and pressed[pygame.K_RIGHT]:
				dy += self.speed * (time_passed / 1000)
			else:
				dy += self.speed / math.sqrt(2) * (time_passed / 1000)

		if not diagonal:
			if pressed[pygame.K_LEFT]:
				dx -= self.speed * (time_passed / 1000)
			if pressed[pygame.K_RIGHT]:
				dx += self.speed * (time_passed / 1000)
		elif pressed[pygame.K_UP] and pressed[pygame.K_DOWN]:
			if pressed[pygame.K_LEFT]:
				dx = -1 * self.speed * (time_passed / 1000)
			if pressed[pygame.K_RIGHT]:
				dx = self.speed * (time_passed / 1000)

		result = self.pos + vec2d(dx, dy)

		#check to see if you're hitting the walls, if so correct your movement
		gameScreen = display.get_surface();

		if result.x < 0:
			result.x = 0
		if result.x + self.image_w > gameScreen.get_width():
			result.x = gameScreen.get_width() - self.image_w
		if result.y < 0:
			result.y = 0
		if result.y + self.image_h > gameScreen.get_height():
			result.y = gameScreen.get_height() - self.image_h

		self.pos = result

	def getHitbox(self):
		return Rect(self.pos.x, self.pos.y, self.image_w, self.image_h)

	def draw(self):
		draw_pos = self.image.get_rect().move(self.pos.x,  self.pos.y)
		self.screen.blit(self.image, draw_pos)