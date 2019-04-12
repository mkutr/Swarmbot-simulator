import pygame
# import cairocffi as cairo
import os
from pathlib import Path
import cairo
from math import pi
from PIL import Image
import math
from swarm_bot_simulator.model import board
from swarm_bot_simulator.model.bot_components import Bot, BotInfo

class Visualizer:
    pygame.init()
    # width = 20
    # height = 20
    black = (0, 0, 0)
    white = (255, 255, 255)
    size = [800, 600]

    def __init__(self):
        # self.board = board
        self.game_display = pygame.display.set_mode(Visualizer.size)

    def display_bot(self, bot_image, x, y, angle):
        bot_image = pygame.transform.rotate(bot_image, angle)
        bot_image = pygame.transform.scale(bot_image, (20, 20))
        self.game_display.blit(bot_image, (x, y))

    def visualize(self, board):
        # bot_image = pygame.image.load(os.path.join('resources', 'car.png'))

        x = (800 * 0.45)
        y = (600 * 0.8)
        game_display = pygame.display.set_mode(Visualizer.size)
        pygame.draw.rect(game_display, Visualizer.black, (x, y, 100, 100))
        pygame.display.set_caption('Swarmbot visualization')

        game_display.fill(Visualizer.white)
        clock = pygame.time.Clock()
        crashed = False

        while not crashed:
            clock.tick(10)
            game_display.fill(Visualizer.white)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
            # display_bot(bot_image, 200, 200, 100)
            # bot1.draw()
            for bot in board.all_bots:
                image = BotImage(bot.bot_info, game_display)
                image.draw()
            # bot1 = BotImage(100, 100, 0, 40, 40, game_display)
            # bot1.change_poz(0, 0, -11)
            x += 2
            pygame.display.update()

        pygame.quit()
        quit()


class BotImage:
    blue = (0, 0, 204)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    def __init__(self, bot_info, game_display):
        # self.image_orginal = image
        # self.image = self.image_orginal
        self.poz_x = bot_info.poz_x
        self.poz_y = bot_info.poz_y
        self.dir = bot_info.dir
        self.size_x = BotInfo.size_x
        self.size_y = BotInfo.size_y
        self.game_display = game_display

    def change_poz(self, x, y, dir):
        self.poz_x = self.poz_x + x
        self.poz_y = self.poz_y + y
        self.dir = (self.dir + dir) % (2*pi)

    def draw(self):
        self.game_display.blit(self.convert2pygame(self.vectorize(self.dir)), (self.poz_x, self.poz_y))

    def convert2pygame(self, surface):
        def bgra_surf_to_rgba_string(cairo_surface):
            # We use PIL to do this
            img = Image.frombuffer(
                'RGBA', (cairo_surface.get_width(),
                         cairo_surface.get_height()),
                cairo_surface.get_data().tobytes(), 'raw', 'BGRA', 0, 1)

            return img.tobytes('raw', 'RGBA', 0, 1)
        return pygame.image.frombuffer(
    bgra_surf_to_rgba_string(surface), (surface.get_width(), surface.get_height()), 'RGBA')


    def vectorize(self, dir):
        WIDTH, HEIGHT = BotInfo.size_x, BotInfo.size_y

        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
        cr = cairo.Context(surface)
        cr.set_source_rgb(0, 0, 1)
        cr.translate(WIDTH / 2, HEIGHT / 2)
        cr.scale(WIDTH, HEIGHT)
        cr.rotate(dir)
        cr.rectangle(-0.2, -0.3, 0.4, 0.6)
        cr.fill()
        cr.set_source_rgb(1, 0, 0)
        cr.rectangle(0.2, 0.05, 0.1, 0.2)
        cr.fill()
        cr.rectangle(-0.2, 0.05, -0.1, 0.2)
        cr.fill()
        return surface
