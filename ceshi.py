import pygame
import sys

def run_game():
	pygame.init()
	screen=pygame.display.set_mode((200,200))
	pygame.display.set_caption("测试")
	bg_color=(220,240,200)
	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
		screen.fill(bg_color)
		pygame.display.flip()
	
run_game()