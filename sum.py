import pygame
import random
import os
import time

os.system('cls' if os.name == 'nt' else 'clear')
print("start xocxoc...")
# start
pygame.init()

screen = pygame.display.set_mode((750, 500))
pygame.display.set_caption('SUM68CLUB - Game Bai Chien Pham')

img1 = pygame.image.load('sum_img.png').convert_alpha()

BLACK = (0, 0, 0)
WHITE = (255,255,255)
o_cuoc1 = pygame.Rect(105, 310, 150, 35)
o_cuoc2 = pygame.Rect(487, 310, 150, 35)

font = pygame.font.Font(None, 25)
font2 = pygame.font.Font(None, 25)

text_cuoc1 = font.render("Dat Cuoc", True, BLACK)
text_cuoc2 = font2.render("Dat Cuoc", True, BLACK)

def draw_background():
	screen.fill(BLACK)

def draw_sum68():
	sum68_img = pygame.transform.scale(img1, (750, 500))
	screen.blit(sum68_img, (0, 0))

rect_dat_cuoc = pygame.Rect(100, 400, 100, 25)
rect_all_in = pygame.Rect(325, 400, 100, 25)
rect_huy = pygame.Rect(550, 400, 100, 25)
	# text dat cuoc
font_dat_cuoc = pygame.font.Font(None, 30)
text_dat_cuoc = font_dat_cuoc.render(
	"Dat Cuoc",
	True,
	WHITE
)
font_all_in = pygame.font.Font(None, 30)
text_all_in = font_all_in.render(
	"All In",
	True,
	BLACK
)
font_huy = pygame.font.Font(None, 30)
text_huy = font_huy.render(
	"Huy",
	True,
	BLACK
)

session = True
while session:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			session = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if o_cuoc1.collidepoint(event.pos):
				print("Cuoc Tai")
			if o_cuoc2.collidepoint(event.pos):
				print("Cuoc Xiu")

			if rect_all_in.collidepoint(event.pos):
				print("Dat Cuoc")
			if rect_dat_cuoc.collidepoint(event.pos):
				print("ALL In")
			if rect_huy.collidepoint(event.pos):
				print("huy cuoc")

	draw_background()
	draw_sum68()

	pygame.draw.rect(screen, (255,255,255), o_cuoc1)
	pygame.draw.rect(screen, (255,255,255), o_cuoc2)

	screen.blit(text_cuoc1, (140, 320))
	screen.blit(text_cuoc1, (515, 320))


	pygame.draw.rect(screen, (0,255,0), rect_dat_cuoc)
	pygame.draw.rect(screen, (0,0,255), rect_all_in)
	pygame.draw.rect(screen, (255,0,0), rect_huy)

	screen.blit(text_all_in, (120, 400))
	screen.blit(text_dat_cuoc, (330, 400))
	screen.blit(text_huy, (580, 400))

	pygame.display.flip()
