import os, sys
from random import randint

import pygame
from pygame import font

from player import Player
from enemy import Enemy

def run_game():
	# screen & color data
	SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
	BG_COLOR = 255, 255, 255
	FONT_COLOR = 0, 0, 0

	# Generic non-object game data
	hits = 0	# Keeps track of total hits
	playerInvincibility = 0		# Keeps track of invincibility interval
	flash_state = 0				# Keeps track of if the player should be drawn (0, 1 = drawn.  2, 3 = not drawn)

	# initalize the libraries
	pygame.init()
	font.init()

	outputFont = font.Font(None, 44)

	# set up the display
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
	pygame.display.set_caption('Dodge the Angry People!!!')

	clock = pygame.time.Clock()

	# create the player object
	playerObj = Player(screen, 'images/player1.png', (300, 300), 350)

	# Generate enemies
	enemies = []
	for x in range(4):
		temp = None
		valid = False

		# randomly place enemies
		while valid == False:
			valid = True
			temp = Enemy(screen, 'images/enemy.png', (randint(0, SCREEN_WIDTH - 50), randint(0, SCREEN_HEIGHT - 50)), 350)

			for y in enemies:
				tempRect = temp.getHitbox();
				enemyRect = y.getHitbox();

				if tempRect.y >= enemyRect.y and tempRect.y <= enemyRect.y + enemyRect.height:
					valid = False

		enemies.append(temp)

	# The main game loop
	while True:
		# Limit frame speed to a glorious 60 FPS
		time_passed = clock.tick(60)

		# Event loop to catch if the user has quit
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit_game()
        
		# Redraw the background
		screen.fill(BG_COLOR)

		# Keep track of player flashing state
		# Only advance flash state if player is currently invincible, otherwise just set it to zero
		if playerInvincibility > 0:
			flash_state += 1
			if flash_state >= 4:
				flash_state = 0
		else:
			flash_state = 0

		# Update and display game objects

		playerObj.update(float(time_passed))
		if(flash_state == 0 or flash_state == 1): # The player object will flash if you hit an enemy
			playerObj.draw()

		for enemy in enemies:
			enemy.update(float(time_passed))
			enemy.draw()

		# Now if the player has no more i-frames calculate hitboxes
		if playerInvincibility <= 0:
			playerInvincibility = 0
			for enemy in enemies:
				playerRect = playerObj.getHitbox()
				if playerRect.colliderect(enemy.getHitbox()):
					hits += 1
					playerInvincibility = 1500
		else: # Otherwise deduct from the invincibility time
			playerInvincibility -= time_passed

		# Display the hit counter
		fontOut = outputFont.render("Hits: " + str(hits), True, FONT_COLOR)
		screen.blit(fontOut, (275, 10))

		pygame.display.flip()


def exit_game():
	sys.exit()

run_game()