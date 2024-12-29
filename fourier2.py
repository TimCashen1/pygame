import pygame as pg
import sys
import math

pg.init()
clock = pg.time.Clock()

# Screen dimensions
screen_width = 1100
screen_height = 660
screen = pg.display.set_mode((screen_width, screen_height))

# Colors
bg_color = pg.Color('#2F373F')
accent_color = (27, 35, 43)
white = (255, 255, 255)
black = (0, 0, 0)

pg.display.set_caption('Fourier Square Wave')
basic_font = pg.font.Font('freesansbold.ttf', 32)

middle_strip = pg.Rect(screen_width / 2 - 2, 0, 4, screen_height)

class Circle:
    def __init__(self, pos, radius, thickness, angle):
        self.pos = pos
        self.radius = radius
        self.thickness = thickness
        self.angle = angle
        self.wave = []  # Stores the wave trace

    def update_positions(self):
        # Reset position variables
        x, y = self.pos
        sum_x, sum_y = x, y
        self.harmonics = []  # Store positions of circles and lines
        
        for i in range(1, 8, 2):  # Only odd harmonics
            
            # Fourier coefficients for a square wave
            radius = (4 / (i * math.pi)) * self.radius
            x_next = sum_x + radius * math.cos(i * self.angle)
            y_next = sum_y + radius * math.sin(i * self.angle)
            self.harmonics.append(((sum_x, sum_y), (x_next, y_next), radius))
            sum_x, sum_y = x_next, y_next

        # Add values to wave
        self.wave.insert(0, sum_y)
        if len(self.wave) > 400:  # Limit wave size
            self.wave.pop()

        # Increment angle for rotation
        self.angle += 0.02

    def draw_circles(self):
        for (start, end, radius) in self.harmonics:
            # Draw circles
            pg.draw.circle(screen, white, (int(start[0]), int(start[1])), int(radius), self.thickness)
            # Draw lines connecting centers
            pg.draw.line(screen, black, start, end, 2)

    def trace_wave(self):
        wave_x0 = self.pos[0] + 400
        # Draw the wave
        for i in range(1, len(self.wave)):
            start_point = (wave_x0 + i, self.wave[i - 1])
            end_point = (wave_x0 + i + 1, self.wave[i])
            pg.draw.line(screen, white, start_point, end_point, 2)

        # Draw line from last circle to wave start
        if self.wave:
            pg.draw.line(screen, white, self.harmonics[-1][1], (wave_x0, self.wave[0]), 2)

# Create a Circle instance
circle1 = Circle((300, 330), 150, 2, 0)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            pg.quit()
            sys.exit()

    screen.fill(bg_color)

    # Draw middle strip
    pg.draw.rect(screen, accent_color, middle_strip)

    # Measure performance
    fps = clock.get_fps()
    fps_text = basic_font.render(f"FPS: {fps:.2f}", True, white)
    screen.blit(fps_text, (10, 10))

    # Update and draw Fourier circles and wave
    circle1.update_positions()
    circle1.draw_circles()
    circle1.trace_wave()

    pg.display.flip()
    clock.tick(120)