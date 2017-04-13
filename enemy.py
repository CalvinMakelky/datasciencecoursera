import pygame
from pygame.sprite import Sprite
from pygame import Rect
from pygame import display

from vec2d import vec2d

class Enemy(Sprite):
	def __init__(self, screen, img_filename, init_position, speed):
		Sprite.__init__(self)

		# set your own screen output
		self.screen = screen

		# set your image and image information
		self.base_image = pygame.image.load(img_filename).convert_alpha()
		self.image = self.base_image
		self.image_w, self.image_h = self.image.get_size()

		#set your inital position and speed
		self.pos = vec2d(init_position)
		self.dx = speed

	def update(self, time_passed):
		result = self.pos + vec2d(self.dx * (time_passed / 1000), 0)

		gameScreen = display.get_surface()

		if(result.x < 0):
			result.x = 0
			self.dx *= -1
		if(result.x + self.image_w > gameScreen.get_width()):
			result.x = gameScreen.get_width() - self.image_w
			self.dx *= -1

		self.pos = result

	def getHitbox(self):
		return Rect(self.pos.x, self.pos.y, self.image_w, self.image_h)

	def draw(self):
		draw_pos = self.image.get_rect().move(self.pos.x,  self.pos.y)
		self.screen.blit(self.image, draw_pos)