#import pygame, sys
#from pygame.locals import *

#def main():
	#pygame.init()
	#screen = pygame.display.set_mode((400, 400))
	#while True:
		#for event in pygame.event.get():
			#if event.type == QUIT:
				#sys.exit()

#if __name__ == '__main__':
	#main()

#def draw_gallows(screen):
	#pygame.draw.rect(screen, PURPLE, (450, 350, 100, 10)) # BOTTOM 
	#pygame.draw.rect(screen, PURPLE, (495, 250, 10, 100)) # SUPPORT
	#pygame.draw.rect(screen, PURPLE, (450, 250, 50, 10))  #crossbar
	#pygame.draw.rect(screen, PURPLE, (450, 250, 10, 25)) #noose

#def draw_word(screen, spaces):
	#x = 10
	#for i in range(spaces):
		#pygame.draw.line(screen, YELLOW, (x, 350), (x+20, 350), 3)

#def draw_letter(screen, font, word, guess):
	#x = 10 
	#for letter in word:
		#if letter == guess:
			#letter = font.render(letter, 3, (255,255,255))
			#screen.blit(letter, (x, 300))
		#x += 30

#def draw_man(screen, body_part):
	#if body_part == "head":
		#pygame.draw.circle(screen, RED, (455, 270), 10) #head
	#if body_part == "body":
		#pygame.draw.line(screen, RED, (455, 280), (455, 320), 3) #body
	#if body_part == "l_arm":
		#pygame.draw.line(screen, RED, (455, 300), (445, 285), 3) #arm
	#if body_part == "r_arm":
		#pygame.draw.line(screen, RED, (455, 300), (465, 330), 3) #arm
	#if body_part == "l_leg":
		#pygame.draw.line(screen, RED, (455, 320), (445, 330), 3) #l_leg
	#if body_part == "r_leg":
		#pygame.draw.line(screen, RED, (455, 320), (465, 330), 3) #leg

import pygame
import sys
from random import choice

from pygame.locals import * 

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 100, 0)
PURPLE = (100, 0, 255)

def get_words():
	f = open("words.txt")
	temp = f.readlines()
	words = []
	for word in temp:
		words.append(word.strip())
	return words

def draw_gallows(screen):
	pygame.draw.rect(screen, PURPLE, (450, 350, 100, 10)) # BOTTOM 
	pygame.draw.rect(screen, PURPLE, (495, 250, 10, 100)) # SUPPORT
	pygame.draw.rect(screen, PURPLE, (450, 250, 50, 10))  #crossbar
	pygame.draw.rect(screen, PURPLE, (450, 250, 10, 25)) #noose

def draw_man(screen, body_part):
	if body_part == "head":
		pygame.draw.circle(screen, RED, (455, 270), 10) #head
	if body_part == "body":
		pygame.draw.line(screen, RED, (455, 280), (455, 320), 3) #body
	if body_part == "l_arm":
		pygame.draw.line(screen, RED, (455, 300), (445, 285), 3) #arm
	if body_part == "r_arm":
		pygame.draw.line(screen, RED, (455, 300), (465, 330), 3) #arm
	if body_part == "l_leg":
		pygame.draw.line(screen, RED, (455, 320), (445, 330), 3) #l_leg
	if body_part == "r_leg":
		pygame.draw.line(screen, RED, (455, 320), (465, 330), 3) #leg


def draw_word(screen, spaces):
	x = 10
	for i in range(spaces):
		pygame.draw.line(screen, YELLOW, (x, 350), (x+20, 350), 3)
		x += 30
def draw_letter(screen, font, word, guess):
	x = 10 
	for letter in word:
		if letter == guess:
			letter = font.render(letter, 3, (255,255,255))
			screen.blit(letter, (x, 300))
		x += 30

def main():
	pygame.init()
	screen = pygame.display.set_mode((600, 400))
	font = pygame.font.SysFont("monospace", 30)
	draw_gallows(screen)
	draw_man(screen, body_part="head")

	words = get_words()
	word = choice(words)
	draw_word(screen, len(word))
	pygame.display.update()

	body = ['r_leg', 'l_leg', 'r_arm', 'l_arm', 'body', 'head']

	while body:
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
			if event .type == KEYDOWN:
				if event.unicode.isalpha():
					guess = event.unicode
					if guess in word:
						draw_letter(screen, font, word, guess)
						pygame.display.update()
					else:
						body_part = body.pop()
						draw_man(screen, body_part)
						pygame.display.update()

if __name__ == '__main__':
	main()
