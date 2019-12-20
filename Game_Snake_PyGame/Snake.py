""" ЕСЛИ ЧТО-ТО РАБОТАЕТ НЕ ТАК КАК ДОЛЖНО - ЭТО НЕ БАГ, А ФИЧА"""

""" Из-за привязки к частоте кадров, управление может не успевать за юзверем, 
по этому змейка, двигаясь вправо, может мнгновенно повернуть влево 
(UP/DPWN + LEFT и  др стороны, если успеть попасть в 0,1 сек, т к анимация 
привязана к частоте кадров) и ударится в саму себя"""

# Импортирование модулей и классов
import pygame

from Snake_control import Control 
from Snake_direction import Snake
from Snake_GUI import GUI
from Snake_food import Food

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
control = Control()
snake = Snake()
gui = GUI()
food = Food()
gui.Init_Field()
food.Get_Food_Position(gui)
gui.Create_Image()

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
