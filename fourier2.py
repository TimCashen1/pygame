import pygame as pg 
import sys
import math

pg.init()
clock = pg.time.Clock()

# screen dimensions
screen_width = 1100
screen_height = 660
screen = pg.display.set_mode((screen_width, screen_height))

# colors
bg_color = pg.Color('#2F373F')
accent_color = (27, 35, 43)
white = (255,255,255)
black = (0,0,0)

pg.display.set_caption('Fourier')
basic_font = pg.font.Font('freesansbold.ttf', 32)

middle_strip = pg.Rect(screen_width / 2 - 2, 0, 4, screen_height)

class Circle:
    def __init__(self, pos, r1, thickness, angle):
        self.pos = pos
        self.r1 = r1
        self.thickness = thickness
        self.angle = angle

        self.r2 = r1 // 3
        self.r3 = self.r2 // 2
        self.r4 = self.r3 // 2

    def update_positions(self):
        self.x2 = self.pos[0] + self.r1*math.cos(self.angle)
        self.x3 = self.x2 + self.r2*math.cos(2*self.angle)
        self.x4 = self.x3 + self.r3*math.cos(self.angle)
        self.x5 = self.x4 + self.r4*math.cos(-3*self.angle)

        self.y2 = self.pos[1] + self.r1*math.sin(0.5*self.angle)
        self.y3 = self.y2 + self.r2*math.sin(6*self.angle)
        self.y4 = self.y3 + self.r3*math.sin(3.2*self.angle)
        self.y5 = self.y4 + self.r4*math.sin(0.5*self.angle)

        # incrementing angle causes the rotation
        self.angle += 0.01

    def draw_circles(self):
        # draws each circle
        pg.draw.circle(screen,white,self.pos,self.r1,self.thickness)
        pg.draw.circle(screen,white,((self.x2,self.y2)),self.r2,self.thickness)
        pg.draw.circle(screen,white,(self.x3,self.y3),self.r3,self.thickness)
        pg.draw.circle(screen,white,(self.x4,self.y4),self.r4,self.thickness)

        # draws a line from the center of each circle to the center of the next circle
        pg.draw.line(screen,black,self.pos,(self.x2,self.y2),2)
        pg.draw.line(screen,black,(self.x2,self.y2),(self.x3,self.y3),2)
        pg.draw.line(screen,black,(self.x3,self.y3),(self.x4,self.y4),2)
        pg.draw.line(screen,black,(self.x4,self.y4),(self.x5,self.y5),2)

    def trace_wave(self):
        # add y-value of last circle to start of wave list
        wave.insert(0,float(self.y5))
        # removes the last value from list if it gets too long
        if len(wave) > 300: wave.pop
        # a hardset x pos for the beginning of the wave, offset from the big circle x pos by 400
        wave_x0 = self.pos[0] + 400
        # loops over each value in wave
        for i in range(1,len(wave)):
            # creates start point at (x[i],y[i-1])
            start_point = (wave_x0 + i,wave[i - 1])
            # creates an end point at (x[i]+1,y[i]), so basically creates a point one pixel to the right with the older y value 
            end_point = (wave_x0 + i + 1,wave[i])
            # draws a line from the start point to the end point. 
            pg.draw.line(screen,white,start_point,end_point,2)

        # draws a line that shows how the rotation of the circles traces out the wave
        if len(wave) > 0:
            pg.draw.line(screen,white,(self.x5,self.y5),(wave_x0,wave[0]),2)
        
        
# create instance of Circle with pos, radius, thickness, and angle (speed of rotation)
circle1 = Circle((300,330),150,2,0)
wave = []

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE): # quits program if hit x or escape
            pg.quit()
            sys.exit()

    screen.fill(bg_color)

    # draws a thin rectangle to divide screen in half
    pg.draw.rect(screen, accent_color, middle_strip)

    # measure performance
    fps = clock.get_fps()
    fps_text = basic_font.render(f"FPS: {fps:.2f}", True, white)
    screen.blit(fps_text, (10,10))
    
    # update positions
    circle1.update_positions()

    # draw the circles
    circle1.draw_circles()

    # draws wave and line to wave start
    circle1.trace_wave()

    pg.display.flip()
    clock.tick(120)