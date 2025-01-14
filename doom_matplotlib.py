import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def on_key(event):
    global player_look_angle
    if event.key == 'left':
        player_look_angle += 10
    elif event.key == 'right':
        player_look_angle += -20

ray_movement_size = 0.1
world_size = (10, 10)
wall_max_height = 10

#мир игры              0  1  2  3  4  5  6  7  8  9
world_map = np.array([[1, 0, 0, 0, 1, 1, 0, 0, 0, 1], #0
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], #1
                      [1, 0, 0, 0, 1, 1, 0, 0, 0, 1], #2
                      [1, 0, 0, 1, 0, 0, 0, 1, 0, 1], #3
                      [1, 0, 0, 0, 0, 0, 0, 0, 1, 1], #4
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], #5
                      [1, 0, 1, 0, 0, 0, 0, 1, 0, 1], #6
                      [1, 0, 0, 0, 1, 0, 1, 0, 0, 1], #7
                      [1, 0, 0, 0, 0, 0, 0, 1, 0, 1], #8
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])#9

# world_map = np.zeros((world_size[0], world_size[1]))
# world_map[0, :] = 1        # Верхняя граница
# world_map[-1, :] = 1       # Нижняя граница
# world_map[:, 0] = 1        # Левая граница
# world_map[:, -1] = 1       # Правая граница


#ray_angle - угол под которым идет луч | ray_x = player_x | ray_y = player_y
def raycasting(ray_angle, ray_x, ray_y):
    ray_angle = np.radians(ray_angle)
    ray_dx = np.cos(ray_angle)
    ray_dy = np.sin(ray_angle)

    while True:
        global ray_movement_size
        ray_x += ray_dx * ray_movement_size
        ray_y += ray_dy * ray_movement_size

        if ray_x - int(ray_x) < 0.2:
            map_x = int(ray_x)
        elif ray_x - int(ray_x) > 0.8:
            map_x = int(ray_x) + 1

        if ray_y - int(ray_y) < 0.2:
            map_y = int(ray_y)
        elif ray_y - int(ray_y) > 0.8:
            map_y = int(ray_y) + 1

        global world_map

        if map_x < 0 or map_x >= len(world_map) or map_y < 0 or map_y >= len(world_map):
            if map_x < 0:
                map_x = int(map_x)
            else:
                map_x = int(map_x) - 1
            if map_y < 0:
                map_y = int(map_y)
            else:
                map_y = int(map_y) - 1
            return [map_x, map_y], (0, 0)
        else:
            if world_map[map_x][map_y] == 1:
                length = abs(map_x - ray_x), abs(map_y - ray_y)
                return [ray_x, ray_y], length





render_map = np.zeros((world_size[0], world_size[1]))
#fig, ax = plt.subplots()
#img = ax.imshow(render_map, cmap='viridis', interpolation='nearest')
plt.axis('off')  # Убираем оси

player_look_angle = 90
player_x, player_y = world_size[0]/2, world_size[1]/2

#ray_amount = int(( world_size[0] * world_size[1] ) / 2) #N
ray_amount = 100 #N
fov = 60

angle_step = fov/(ray_amount - 1)
left_angle = player_look_angle + (fov/2)

# for i in range(ray_amount - 1):
#     ray_angle = left_angle - (i * angle_step)
#     temp = raycasting(ray_angle, player_x, player_y) #temp для отладки
#     if temp and 0 <= temp[0] < render_map.shape[0] and 0 <= temp[1] < render_map.shape[1]:
#         render_map[temp[0]][temp[1]] = 200

img.set_data(render_map)
ray_map = []
x = []
heights = []

def update(frame):
    global player_look_angle, wall_max_height
    #render_map = np.zeros((world_size[0], world_size[1]))
    left_angle = player_look_angle + (fov / 2)
    ray_map = []

    for i in range(ray_amount - 1):
        ray_angle = left_angle - (i * angle_step)
        ray_coords, length = raycasting(ray_angle, player_x, player_y)

        #render_map[ray_coords[0], ray_coords[1]] = 200 #визуализация в 2D

        # реверсер
        #temp = ray_coords[0]  # убрать реверсер мб, если логика ломается
        #ray_coords[0] = ray_coords[1]
        #ray_coords[1] = temp

        if length != (0, 0):
            ray_length = np.sqrt((length[0] * length[0]) + (length[1] * length[1]))
            fixed_length = ray_length * np.cos(np.radians(abs(ray_angle - player_look_angle)))
            ray_map.append([ray_coords, wall_max_height / fixed_length])
        else:
            ray_map.append([ray_coords, 0])

    for i in ray_map:
        x.append(i[0][1])
        heights.append(i[1])

    log_normalized_data = np.log(heights)

    img.set_data(log_normalized_data)
    print(ray_map)
    return [img]


plt.bar(x, log_normalized_data, color='skyblue', edgecolor='black')
log_normalized_data = np.log(heights)

fig.canvas.mpl_connect('key_press_event', on_key)

ani = FuncAnimation(fig, update, frames=20, interval=200, blit=True)


fig.colorbar(img)
plt.show()
