
""" ЕСЛИ ЧТО-ТО РАБОТАЕТ НЕ ТАК КАК ДОЛЖНО - ЭТО НЕ БАГ, А ФИЧА"""

""" Из-за привязки к частоте кадров, управление может не успевать за юзверем, 
по этому змейка, двигаясь вправо, может мнгновенно повернуть влево 
(UP/DPWN + LEFT и  др стороны, если успеть попасть в 0,1 сек, т к анимация 
привязана к частоте кадров) и ударится в саму себя"""

# Импортирование модулей
import pygame
import random
from pygame.locals import *

class Control:
	def __init__(self):
		# Флаги для управления
		self.flag_game = True
		self.flag_direction = "RIGHT"
		self.flag_pause = True

	# Управление в зависимости от флага
	def control(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.flag_game = False	
			elif event.type == KEYDOWN:
				if event.key == K_RIGHT and self.flag_direction != "LEFT":
					self.flag_direction = "RIGHT"
				elif event.key == K_LEFT and self.flag_direction != "RIGHT":
					self.flag_direction = "LEFT"
				elif event.key == K_DOWN and self.flag_direction != "UP":
					self.flag_direction = "DOWN"
				elif event.key == K_UP and self.flag_direction != "DOWN":
					self.flag_direction = "UP"

				# Условия при паузе
				elif event.key == K_ESCAPE:
					if self.flag_pause:
						self.flag_pause = False
					else:
						self.flag_pause = True

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
			pygame.draw.rect(win, pygame.Color("Green"), pygame.Rect(segment[0], segment[1], 10, 10))

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

class GUI:
	# Графикеский интерфейс, 0 - барьер, 1 - поле 10*10 пикселей
	def __init__(self):
		self.level = [
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
            0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
        ]

        # Загрузка графики
		self.gui_image = pygame.image.load("images/GUI.png")
		self.victory = pygame.image.load("images/win.jpg")
		self.lose = pygame.image.load("images/lose.jpg")

		# Создание условий
		self.barrier = []
		self.field = []
		self.indicator = [[12, 12]]
		self.game = "GAME"

	def Create_Image(self):
		# Заполнение массива и построение изображения GUI
		screen = pygame.Surface((441,441), pygame.SRCALPHA, 32)
		x = 1
		y = 1
		for i in self.level:
			if i == 0:
				pygame.draw.rect(screen, pygame.Color("Grey"), pygame.Rect(x, y, 10, 10))
			x += 11
			if x == 441:
				y += 11
				x = 1
		pygame.image.save(screen, "images/GUI.png")

	# Отрисовка GUI
	def Draw_Level(self, win):
		win.blit(self.gui_image, (0, 0))

	# Заполнение барьеров и поля
	def Init_Field(self):
		x = 1
		y = 1
		for i in self.level:
			if i == 0:
				self.barrier.append([x, y])
			elif i == 1 and y != 12:
				self.field.append([x, y])
			x += 11
			if x == 441:
				y += 11
				x = 1

	# Добаление элемента к текущему индикатору
	def Get_New_Indicator(self):
		self.indicator.append([self.indicator[-1][0] +11, 12])

	# Отрисовка индикатора
	def Draw_Indicator(self, win):
		for i in self.indicator:
			pygame.draw.rect(win, pygame.Color("Blue"), pygame.Rect(i[0], i[1], 10, 10))

	# Отрисовка победного окна
	def Draw_Victory(self, win):
		win.blit(self.victory, (0, 96))

	# Отрисовка окна поражения 
	def Draw_Lose(self, win):
		win.blit(self.lose, (0, 0))

	# Проверка на победу / поражение 
	def Check_Victory_Lose(self):
		if len(self.indicator) == 0:
			self.game = "LOSE"
		elif len(self.indicator) == 37: #кол-во единиц  еды,  которое необходимо достичь для победы
			self.game = "Victory" 

# Инициализация модуля
pygame.init()

clock = pygame.time.Clock()

# Создание окна х на у пикселей
win = pygame.display.set_mode((441, 441))

# Добавление иконки окна 
pygame.display.set_icon(pygame.image.load("images/icon.jpg"))

# Название окна
pygame.display.set_caption("Snake")

# Инициализация классов
snake = Snake()
gui = GUI()
food = Food()
gui.Init_Field()
food.Get_Food_Position(gui)
gui.Create_Image()
control = Control()

# Основной цикл логики игры
while control.flag_game:
	# Фрэймрейт
	clock.tick(9)

	# Проверка условий касания барьеров
	gui.Check_Victory_Lose()

	# Проверка нажатия клавиш
	control.control()

	# Отрисовка графики
	win.fill(pygame.Color("black"))
	gui.Draw_Indicator(win)
	gui.Draw_Level(win)

	# Условия флагов
	if gui.game == "GAME":
		snake.Draw_Snake(win)
		food.Draw_Food(win)
	elif gui.game == "Victory":
		win.fill(pygame.Color("black"))
		gui.Draw_Victory(win)
	elif gui.game == "LOSE":
		win.fill(pygame.Color("black"))
		gui.Draw_Lose(win)
	elif gui.game == "LOSE":
		win.fill(pygame.Color("black"))
		gui.Draw_Lose(win)

	# Условия паузы + логика происходящего
	if control.flag_pause and gui.game == "GAME":
		snake.move(control)
		snake.Check_Barrier(gui)
		snake.Eat(food, gui)
		snake.Check_End_Win()
		snake.Animation()

	# Обновление экрана
	pygame.display.flip()
