import pygame
pygame.init()

import time
import numpy as np
import math

screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()

cube = np.array(((0, 0, 0), (0, 10, 0), (10, 10, 0), (10, 0, 0), (0, 0, 10), (0, 10, 10), (10, 10, 10), (10, 0, 10)))

y_rotation_matrix = np.array([[math.cos(0.01), 0, math.sin(0.01)],
                                [0, 1, 0],
                                [-math.sin(0.01), 0, math.cos(0.01)]])

def rotate_y_axis(points_array):
    rotated_points_array = np.dot(points_array, y_rotation_matrix)
    return rotated_points_array

def projection(points_array):
    projected_points_array = points_array[:, :2] / 10
    return projected_points_array

def convert_to_pygame(points_list):
    x_pygame = 1000/2 + ((1/10) * points_list[:, 0]) * 1000/2
    y_pygame = 1000/2 - ((1/10) * points_list[:, 1]) * 1000/2
    pygame_points_xy = np.column_stack((x_pygame, y_pygame))
    return pygame_points_xy

while True:
    
    
    screen.fill((255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    cube = rotate_y_axis(cube)
    cube_projected = projection(cube)
    pygame_xy = convert_to_pygame(cube_projected)
    
    
    start_time = time.time()
    for point in pygame_xy:
        pygame.draw.circle(screen, (0, 0, 0), point, 2)
    end_time = time.time()
    
    pygame.display.flip()
    
    if end_time-start_time != 0:
        pygame.display.set_caption(str(1/ (end_time-start_time)))
