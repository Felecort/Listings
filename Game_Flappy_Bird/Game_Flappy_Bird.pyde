
        # Flappy Bird V 1.7 #

# Импортирование библиотеки
add_library('sound')

# Установка флагов
first_click = False
gamestate = True
sound_theme_flaf = True

# Установка начальных перепенных
bird_y = 400        # Координата птицы по Oy
x = -200            # Координата заднего фона по Ox
speed = 1           # Скорость падения птицы

wall_x = [0,0]      # Создание массива координат труб
wall_y = [0,0]

score = 0           # Добавление счётчика
high_score = 0      # Добавление переменной максимального значения счётчика

def setup():
    global start, back, bird_fly, bird_down, pipe_up, pipe_down, font, bird_y, theme, flip, die, point1
    
    # Создание основного окна
    size(680, 800)

    # Инициализация аудиофайлов
    theme = SoundFile(this, "theme.mp3")
    flip = SoundFile(this, "flip.wav")
    die = SoundFile(this, "die.wav")
    point1 = SoundFile(this, "point.wav")

    # Инициализация изображений
    pipe_up = loadImage("pipe_up.png")
    pipe_down = loadImage("pipe_down.png")
    back = loadImage("back.png")
    bird_fly = loadImage("bird__1.png")
    bird_down = loadImage("bird__2.png")
    font = loadFont("AgencyFB-Bold-70.vlw")

    # Отрисовка начального рабочего фона
    image(back, 0 , 0)                  # Отрисовка заднего фона 
    imageMode(CENTER)
    image(bird_fly, 220, bird_y )       # Отрисовка птицы

    textFont(font, 70)                  # Параметры текста
    text("Flappy Bird", 120, 300)       
    textFont(font, 50)
    text("Click to start", 400, 600)

def draw():
    global gamestate, bird_y, x, speed, wall_y, wall_x, score, high_score, first_click, sound_theme_flaf
    if not gamestate:

        # Условия запуска музыкальной темы
        if sound_theme_flaf:
            theme.loop(1, 0.6)
            sound_theme_flaf = False

        first_click = True

        # Создание иллюзии движения заднего фона
        imageMode(CORNER)
        image(back, x, 0)
        image(back, x + back.width, 0)
        if x < -back.width:
            x = 0

        # Анимация птицы
        imageMode(CENTER)
        image(bird_fly, 220, bird_y )

        # Изменение координат птицы ( скорость падения )
        x -= 1
        speed += 1
        bird_y += speed

        # Главный цикл 
        for i in range(2):

            # Отрисовка двух пар труб
            imageMode(CORNER)
            image(pipe_down, wall_x[i], wall_y[i] - pipe_down.height/2 - 100)
            image(pipe_up, wall_x[i], wall_y[i] + pipe_up.height/2 + 100)

            # Создание пары труб, после перехода однорй из пар за координату -65 Ох
            if wall_x[i] < -65:
                wall_y[i] = round(random(-180, 370))  # Рандомные координаты в пределе -180, 370 Ох
                wall_x[i] = width  

            # Добавление очков после преодаления 218 координаты Ох
            # Число должно быть кратным 6, на столько перемещается труба каждый кадр                    
            if wall_x[i] == 218:
                point1.play(1, 0.35)
                score += 1
                high_score = max(score, high_score)

            # Условия проигрыша (Сложная математика из-за отрисовки от угла, размера изображения и т д. Лучше не менять ничего)
            if bird_y > height-15 or bird_y < 0 or abs(220 - wall_x[i]) < 30 and abs(bird_y-(wall_y[i]+pipe_down.height/2))>70:
                gamestate = True 
                theme.stop()
                die.play()
            wall_x[i] -= 6

        # Отрисовка счёта во время игры
        text("Score: " + str(score), width/2+100, 750)    

    # Отрисовка графики во время проигрышей
    if first_click and gamestate:

        # Отрисока заднего фона без анимации
        imageMode(CORNER)
        image(back, x, 0)
        image(back, x + back.width, 0)

        # Создание 2х пар труб
        for i in range(2):
            image(pipe_down, wall_x[i], wall_y[i] - pipe_down.height/2 - 100)
            image(pipe_up, wall_x[i], wall_y[i] + pipe_up.height/2 + 100)

        # Анимация падения птицы
        image(bird_down, 220, bird_y)

        # Изменение координаты птицы во время падения 
        if bird_y < 800:
            bird_y += 10
        else:
            first_click = False

        # Аннулирование счётчика
        score = 0

        # Отрисовка "меню"
        textFont(font, 70)
        text("Flappy Bird", 120, 300)
        textFont(font, 50)
        text("Click to start", 400, 600)
        text("High score: " + str(high_score), 50, width)
        text("Score: " + str(score), width/2+100, 750)  

def mousePressed():
    global speed, wall_y, wall_x, gamestate, bird_y, sound_theme_flaf

    # Изменение скорости птицы после нажатия 
    speed = -17

    # Звук взмаха крыльями
    flip.play()

    # Создание изначальных условий 
    if gamestate:

        # Отрисовка заднего фона
        imageMode(CORNER)
        image(back, 0, 0)

        # Создание 2х пар труб с расстоянием 1082-782
        # При нулевой разности координат трубы будут отрисовываться друг в друге
        # Числа должны быть кратны 6, иначе счётчик не будет работать на первых двух препятствиях
        wall_x[0] = 782
        wall_y[0] = round(random(-180, 370))
        wall_x[1] = 1082
        wall_y[1] = round(random(-180, 370))

        # Начальные  параметры птицы
        bird_y = 400
        score = 0

        gamestate = False
        sound_theme_flaf = True

# Как-то так ¯\_(ツ)_/¯
