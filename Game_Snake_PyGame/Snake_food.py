import pygame
import random

class Food:

	# Заполнение позиций еды
	def __init__(self):
		self.food_position = []
	
	# Рандомное местоположение еды
	def Get_Food_Position(self, gui):
		self.food_position = random.choice(gui.field)
	
	# Отрисовка эл-тов еды 
	def Draw_Food(self, win):
		pygame.draw.rect(win,pygame.Color("Red"), pygame.Rect(self.food_position[0],
		 self.food_position[1], 10, 10))
