#план действий
#TODO: 1. создать функцию для осмотра карты по лучам
#TODO: 2. создать ещё одну функцию для рендера 3д
#TODO: 3. реализовать хождение

import matplotlib
import numpy as np

map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

fov = 60
look_center_angle = 90
angle_amount = 320
angles = []
start_angle = look_center_angle - (fov / 2)
for i in range(angle_amount):
    angles.append(start_angle + (i / angle_amount) * fov)

print(angles)

def raycasting_dda(ray_angle):
    dx = np.cos(ray_angle)
    dy = np.sin(ray_angle)
    
