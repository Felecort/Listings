import pygame

class Snake:
	def __init__(self):
		# Создание тела и головы змейки
		self.head = [45, 45]
		self.body = [[45, 45], [34, 45], [23,45]]
	
	# Движение змеи в зависимости от направления  
	def move (self, control):
		if control.flag_direction == "RIGHT":
			self.head[0] += 11
		elif control.flag_direction == "LEFT":
			self.head[0] -= 11
		elif control.flag_direction == "UP":
			self.head[1] -= 11
		elif control.flag_direction == "DOWN":
			self.head[1] += 11
	
	# Анимация перемещения тела и головы
	def Animation(self):
		self.body.insert(0, list(self.head))
		self.body.pop()
	
	# Отрисовка анимации 
	def Draw_Snake(self, win):
		for segment in self.body:
			pygame.draw.rect(win, pygame.Color("Green"), 
pygame.Rect(segment[0], segment[1], 10, 10))
	
	# Отслеживание касаний барьера
	def Check_End_Win(self):
		if self.head[0] == 419:
			self.head[0] = 23
		elif self.head[0] == 12:
			self.head[0] = 419
		elif self.head[1] == 23:
			self.head[1] = 419
		elif self.head[1] == 419:
			self.head[1] = 34
	
	# Создание еды и поедание
	def Eat(self, Food, GUI):
		if self.head == Food.food_position:
			self.body.append(Food.food_position)
			Food.Get_Food_Position(GUI)
			GUI.Get_New_Indicator()
	
	# Удаление элементов при касании барьера
	def Check_Barrier(self, GUI):
		if self.head in GUI.barrier:
			self.body.pop()
			GUI.indicator.pop()
		if self.head in self.body[1:]:
			self.body.pop()
			GUI.indicator.pop()
