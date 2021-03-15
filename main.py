import math
import pygame

pygame.init()
pygame.display.set_caption("illusioon")
screen = pygame.display.set_mode([800, 600])

purple = [221, 148, 220]
white = [255, 255, 255]

delay_step = 25
delay = 250


class Circle:
    x: float
    y: float

    color: list
    radius: float

    def __init__(self, x: float, y: float, color: list, radius: float):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius

    def set_color(self, color: list):
        self.color = color

    def draw(self):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.radius)


class Shapes:
    shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def pop(self):
        if not self.is_empty():
            self.shapes.pop()

    def is_empty(self):
        return len(self.shapes) == 0

    def draw(self):
        for shape in self.shapes:
            shape.draw()


class Circles(Shapes):
    __right_angle = math.sin(math.radians(90))
    __current_index = 0

    def __init__(self, count):
        for i in range(count):
            self.shapes.append(self.__create_circle())
        self.__recalculate_shape_positions(count)

    @staticmethod
    def __create_circle():
        return Circle(0, 0, purple, 15)

    def __recalculate_shape_positions(self, count):
        degrees_between = 360 / count

        for i in range(len(self.shapes)):
            x = math.sin(math.radians(90 + (i * degrees_between))) * 150 / self.__right_angle
            y = math.sin(math.radians(0 + (i * degrees_between))) * 150 / self.__right_angle

            self.shapes[i].x = 400 + x
            self.shapes[i].y = 300 + y

    def add(self):
        super().add_shape(self.__create_circle())
        self.__recalculate_shape_positions(len(self.shapes))

    def pop(self):
        super().pop()
        self.__recalculate_shape_positions(len(self.shapes))

    def shift_colors(self):
        if self.is_empty():
            return

        count = len(self.shapes)

        current = self.__current_index % count
        last = (self.__current_index - 1) % count

        self.shapes[current].set_color(white)
        self.shapes[last].set_color(purple)

        self.shapes[current].draw()
        self.shapes[last].draw()

        self.__current_index += 1


def draw_background():
    screen.fill(white)
    pygame.draw.line(screen, [0, 0, 0], [385, 300], [415, 300])
    pygame.draw.line(screen, [0, 0, 0], [400, 285], [400, 315])


if __name__ == '__main__':
    draw_background()

    circles_object = Circles(12)
    circles_object.draw()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_LEFT:
                    draw_background()
                    circles_object.pop()
                    circles_object.draw()
                elif event.key == pygame.K_RIGHT:
                    draw_background()
                    circles_object.add()
                    circles_object.draw()
                elif event.key == pygame.K_UP:
                    if delay - delay_step > 0:
                        delay -= delay_step
                elif event.key == pygame.K_DOWN:
                    delay += delay_step
        else:
            circles_object.shift_colors()

        pygame.display.flip()
        pygame.time.delay(delay)

    pygame.quit()
