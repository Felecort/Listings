""" Управление на w a s d,  выпуск снаряда - Space"""

# Добавление и инициализация модулей
import pygame 
pygame.init()

# Создание окна х на у пикселей
win = pygame.display.set_mode((1000,750))

# Название окна и иконка
pygame.display.set_caption("Ani Trump")
pygame.display.set_icon(pygame.image.load("images/pygame_idle.png"))

# Импортирование спрайтов
walk_right = [pygame.image.load('images/pygame_right_1.png'), 
pygame.image.load('images/pygame_right_2.png'), pygame.image.load('images/pygame_right_3.png'), 
pygame.image.load('images/pygame_right_4.png'), pygame.image.load('images/pygame_right_5.png'), 
pygame.image.load('images/pygame_right_6.png')] 
walk_left = [pygame.image.load('images/pygame_left_1.png'), 
pygame.image.load('images/pygame_left_2.png'), pygame.image.load('images/pygame_left_3.png'), 
pygame.image.load('images/pygame_left_5.png'), pygame.image.load('images/pygame_left_4.png'), 
pygame.image.load('images/pygame_left_6.png')]
player_stand = pygame.image.load('images/pygame_idle.png')
background = pygame.image.load('images/WH2.jpg')

# Добавление счётчика
clock = pygame.time.Clock()

# Параметpы положения игрока
x = 50
y = 650

# Параметры размеров игрока
widht = 60
height = 71

# Скорость игрока
speed = 10

# Параметры для прыжка
is_jump = False
jump_count = 10

# Параметры для анимаций
left = False
right = False
anim_count = 0

# Определение направления игрока во время движения 
last_move = "right"

# Создание класса для снарядов
class Shell():

    # Параметры снарядов
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 30 * facing
    
    # Создание снарядов
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), 
        self.radius)

# Обновление экрана
def draw_window():
    global anim_count
    win.blit(background, (0, 0))
    
    # Счётчкик для анимаций
    if anim_count + 1 >= 30:
        anim_count = 0
    
    # Анимации для движения в соответствующие стороны
    if left:
        win.blit(walk_left[anim_count // 5], (x, y))
        anim_count += 1
    elif right:
        win.blit(walk_right[anim_count // 5], (x, y))
        anim_count += 1
    else:
        win.blit(player_stand, (x, y))
    
    # Рисование снарядов
    for bullet in bullets:
        bullet.draw(win)
    
    # Обновление дисплея
    pygame.display.update()
run = True

# Создание массива для количества выпущенных снарядов
bullets = []

# Основной цикл
while run:
    clock.tick(30)
    
    # Условия при закрытии окна
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # Перемещение снарядов
    for bullet in bullets:
        if bullet.x < 1000 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    
    # Программирование ключей(клавиш)
    keys = pygame.key.get_pressed()
    
    # Програмирование логики снарядов
    if keys[pygame.K_SPACE]:
        if last_move == "right":
            facing = 1
        else:
            facing = -1
        if len(bullets) < 20:
            bullets.append(Shell(round(x + widht // 2),
            round(y + height // 2), 5, (255, 0, 0), facing))
    if keys[pygame.K_a] and x > 5:
        x -= speed 
        left = True
        right = False
        last_move = "left"
    elif keys[pygame.K_d] and x < 1000 - widht - 5:
        x += speed
        left = False
        right = True
        last_move = "right"
    else:
        left = False
        right = False
        anim_count = 0
    if not(is_jump):
    
    # Программироване прыжка
        if keys[pygame.K_w]:
            is_jump = True
    else:
        if jump_count >= -10:
            if jump_count < 0:
                y += (jump_count ** 2) / 3
            else:
                y -= (jump_count ** 2) / 3
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10
    draw_window()
pygame.quit()
