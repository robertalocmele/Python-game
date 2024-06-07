import pygame
import sys

#Инициализируем Pygame
#это библиотека для создания игр и мультимедийных приложений на Python
#Pygame обрабатывает графику, анимацию и многое другое, что необходимо для создания игры
pygame.init()

# Константы
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600  # Размеры экрана
BACKGROUND_COLOR = (255, 255, 255)  # Цвет фона (белый)
FONT = pygame.font.SysFont(None, 36)  # Шрифт и размер текста (36)
QUALITY_SIZE = (100, 100)  # Размер каждого изображения
GAP = 40  # Расстояние между изображениями и элементами
QUALITIES_PER_ROW = 5  # Количество качеств на строку в сетке
GLASS_WIDTH, GLASS_HEIGHT = 100, 300  # Размеры стакана

# Цвета
WHITE = (255, 255, 255)  # Бе́лый
BLACK = (0, 0, 0)  # Черный
GOOD_COLORS = [  # Цвета, связанные с хорошими качествами
    (37, 64, 154),  # kindness
    (69, 159, 216),  # honesty
    (255, 222, 89),  # generosity
    (126, 217, 87),  # patience
    (255, 145, 77)   # humility
]
BAD_COLORS = [  # Цвета, связанные с плохими качествами
    (84, 84, 84),     # greed
    (82, 41, 16),    # dishonesty
    (132, 125, 95),    # impatience
    (51, 68, 43),   # pride
    (60, 90, 109)       # cruelty
]

# Загрузка изображений (заменить на фактические пути к файлам)
good_qualities_images = [
    pygame.image.load('kindness.png'),  # Загрузка изображения для доброты
    pygame.image.load('honesty.png'),   # Загрузка изображения для честности
    pygame.image.load('generosity.png'),  
    pygame.image.load('patience.png'),  
    pygame.image.load('humility.png')  
]

bad_qualities_images = [
    pygame.image.load('greed.png'),  # Загрузка изображения для жадности
    pygame.image.load('dishonesty.png'),  
    pygame.image.load('impatience.png'),  
    pygame.image.load('pride.png'),  
    pygame.image.load('cruelty.png')  
]

all_qualities_images = good_qualities_images + bad_qualities_images  # Объединение всех изображений качеств в один список
quality_names = ["Kindness", "Honesty", "Generosity", "Patience", "Humility",  # Названия качеств
                 "Greed", "Dishonesty", "Impatience", "Pride", "Cruelty"]

# Изменение размера изображения до нужного размера
all_qualities_images = [pygame.transform.scale(img, QUALITY_SIZE) for img in all_qualities_images]

# Инициализация экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Установка размера экрана
pygame.display.set_caption("Quality Selection Game")  # Установка заголовка окна

def draw_text(text, position, color=BLACK):
    """
    Отображает текст на экране в указанной позиции с заданным цветом

    """
    img = FONT.render(text, True, color)  # Отрисовка текста
    screen.blit(img, position)  # Отображение текста на экране

def determine_person_type(good_count, bad_count):
    """
     Определяет тип человека на основе количества выбранных хороших и плохих качеств
    """
    if good_count == 5:
        return "Excellent person"
    elif good_count == 4 and bad_count == 1:
        return "Awesome person"
    elif good_count == 3 and bad_count == 2:
        return "Great person"
    elif good_count == 2 and bad_count == 3:
        return "Normal person"
    elif good_count == 1 and bad_count == 4:
        return "Bad person"
    else:  # good_count == 0 and bad_count == 5
        return "Awful person"

def draw_glass_fill(selected_qualities):
    """
    Рисует стакан и заполняет его цветами, соответствующими выбранным качествам
    """
    glass_rect = pygame.Rect(SCREEN_WIDTH - GLASS_WIDTH - GAP, SCREEN_HEIGHT // 2 - GLASS_HEIGHT // 2, GLASS_WIDTH, GLASS_HEIGHT)
    pygame.draw.rect(screen, BLACK, glass_rect, 2)  # Рисование границы стакана

    fill_height = GLASS_HEIGHT // 5  # Высота каждого сегмента заполнения
    for idx, quality_idx in enumerate(selected_qualities):
        if quality_idx < 5:
            fill_color = GOOD_COLORS[quality_idx]  # Получение цвета для хорошего качества
            
        else:
            fill_color = BAD_COLORS[quality_idx - 5]  # Получение цвета для плохого качества

        fill_rect = pygame.Rect(glass_rect.left, glass_rect.bottom - (idx + 1) * fill_height, GLASS_WIDTH, fill_height)
        pygame.draw.rect(screen, fill_color, fill_rect)  # Рисование сегмента заполнения
   
def main():
    selected_qualities = []  # Список для отслеживания выбранных качеств
    running = True  # Флаг для управления циклом игры

    while running:
        screen.fill(BACKGROUND_COLOR)  # Заполнение фона указанным цветом


        # Отображение качеств в виде изображений
        for i, img in enumerate(all_qualities_images):
            row = i // QUALITIES_PER_ROW  # Определение позиции строки
            col = i % QUALITIES_PER_ROW  # Определение позиции столбца
            x = GAP + col * (QUALITY_SIZE[0] + GAP)  # Вычисление координаты X
            y = GAP + row * (QUALITY_SIZE[1] + GAP)  # Вычисление координаты Y
            screen.blit(img, (x, y))  # Отображение изображения качества

            draw_text(quality_names[i], (x, y + QUALITY_SIZE[1] + 5), BLACK)  # Отображение имени качества

        # Отображение заполнения стакана
        draw_glass_fill(selected_qualities)

        # Отображение выбранных качеств и результата
        if len(selected_qualities) == 5:
            good_count = sum(1 for i in selected_qualities if i < 5)  # Подсчет количества хороших качеств
            bad_count = 5 - good_count  # Подсчет количества плохих качеств
            result = determine_person_type(good_count, bad_count)  # Определение типа человека
            draw_text(result, (GAP, SCREEN_HEIGHT - 50), BLACK)  # Отображение результата


        pygame.display.flip()  # Обновление экрана

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  #  Выход из игры
            elif event.type == pygame.MOUSEBUTTONDOWN and len(selected_qualities) < 5:
                x, y = event.pos  # Получение позиции щелчка мыши
                for i, img in enumerate(all_qualities_images):
                    row = i // QUALITIES_PER_ROW  # Определение позиции строки
                    col = i % QUALITIES_PER_ROW  # Определение позиции столбца
                    img_x = GAP + col * (QUALITY_SIZE[0] + GAP)  # ычисление координаты X
                    img_y = GAP + row * (QUALITY_SIZE[1] + GAP)  # Вычисление координаты Y
                    if img_x <= x <= img_x + QUALITY_SIZE[0] and img_y <= y <= img_y + QUALITY_SIZE[1]:
                        if i not in selected_qualities:  # Проверка, не выбрано ли качество уже
                            selected_qualities.append(i)  # Добавление в список выбранных качеств

    pygame.quit()  # Выход из Pygame
    sys.exit()  # Завершение программы

if __name__ == "__main__":
    main()  # Запуск основной функции
