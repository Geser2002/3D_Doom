import pygame

def game():
    import pygame

    rect_size = (30, 30)
    screen_size = (1920, 1080)

    def collision(rect_list):
        for i in rect_list:  # подсчет всех соседей
            for j in rect_list:
                if j[1] == True:
                    if abs(i[0].x - j[0].x) <= 30 and abs(i[0].y - j[0].y) <= 30:  # сама коллизия
                        i[2] += 1
            if i[1] == True:
                i[2] -= 1

        for i in rect_list:  # раздача жизни и смерти
            if i[1] == True:
                if i[2] < 2 or i[2] > 3:
                    i[1] = False
            else:
                if i[2] == 3:
                    i[1] = True

        for i in rect_list:  # после одной ходки обнуляем соседей
            i[2] = 0

    pygame.init()
    screen = pygame.display.set_mode((screen_size))
    pygame.display.set_caption("Game of Life")

    clock = pygame.time.Clock()
    rect_list = []
    rect_color = (180, 180, 180)

    is_Vlad = False
    is_game = False

    running = True

    for i in range(screen_size[0] // rect_size[0]):  # инициализация поля
        for j in range(screen_size[1] // rect_size[1]):  # list = Rect, Is_Alive, Sosed_count
            rect_list.append([pygame.Rect(int(i) * 30, int(j) * 30, rect_size[0], rect_size[1]), False, 0])

    while running:
        screen.fill((0, 0, 120))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in rect_list:
                    if i[0].collidepoint(event.pos):
                        i[1] = not i[1]

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_game = not is_game
                if event.key == pygame.K_p:  # Для дебаггинга, удаляет все квадратики
                    is_Vlad = not is_Vlad

        if is_game:
            collision(rect_list)

        if is_Vlad == True:
            for i in rect_list:  # дебаг
                i[1] = False

        for i in rect_list:  # прорисовыватель квадратиков
            if i[1] == True:
                pygame.draw.rect(screen, rect_color, i[0])
            elif i[1] == False:
                pygame.draw.rect(screen, (0, 0, 120), i[0])

        pygame.display.flip()
        clock.tick(15)
    pygame.quit()
