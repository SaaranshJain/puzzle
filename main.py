import pygame
import pygame.display
import pygame.event
import pygame.image
import pygame.transform
import pygame.mouse
from time import sleep

import random

pygame.init()


class Game:
    def __init__(self, caption, screen_size=(700, 700)):
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption(caption)
        self.screen.fill((255, 255, 255))

        self.on_which_puzzle = 1
        self.won = False

        self.imgs1 = [pygame.transform.scale(pygame.image.load(f"./puzzles/puzzle1/Piece{i}.png"), (175, 175))
                      for i in range(16)]
        self.imgs2 = [pygame.transform.scale(pygame.image.load(f"./puzzles/puzzle2/Piece{i}.png"), (175, 175))
                      for i in range(16)]
        self.imgs3 = [pygame.transform.scale(pygame.image.load(f"./puzzles/puzzle3/Piece{i}.png"), (175, 175))
                      for i in range(16)]
        self.imgs4 = [pygame.transform.scale(pygame.image.load(f"./puzzles/puzzle4/Piece{i}.png"), (175, 175))
                      for i in range(16)]
        self.imgs5 = [pygame.transform.scale(pygame.image.load(f"./puzzles/puzzle5/Piece{i}.png"), (175, 175))
                      for i in range(16)]

    def setup_ui(self, pos):
        for ind, img in enumerate(eval(f"self.imgs{self.on_which_puzzle}")):
            self.screen.blit(img, pos[ind])

        pygame.display.update()

    def win(self):
        self.screen.blit(pygame.transform.scale(
            pygame.image.load("./puzzles/win.jpg"), (700, 700)), (0, 0))
        pygame.display.update()

    def mainloop(self):
        run = True
        NEXT = False

        winning_pos = [(0, 0), (175, 0), (175 * 2, 0), (175 * 3, 0), (0, 175), (175, 175), (175 * 2, 175), (175 * 3, 175), (0, 175 * 2),
                       (175, 175 * 2), (175 * 2, 175 * 2), (175 * 3, 175 * 2), (0, 175 * 3), (175, 175 * 3), (175 * 2, 175 * 3), (175 * 3, 175 * 3)]

        pos = winning_pos[:]
        random.shuffle(pos)

        while run:
            if not self.won:
                self.setup_ui(pos)
            else:
                self.win()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

                if not self.won:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = pygame.mouse.get_pos()
                        start = (175 * (x // 175), 175 * (y // 175))

                    elif event.type == pygame.MOUSEBUTTONUP:
                        if NEXT:
                            self.on_which_puzzle += 1
                            random.shuffle(pos)
                            NEXT = False

                        else:
                            x, y = pygame.mouse.get_pos()
                            stop = (175 * (x // 175), 175 * (y // 175))
                            start_ind = pos.index(start)
                            stop_ind = pos.index(stop)

                            if start_ind < stop_ind:
                                pos = pos[:start_ind] + [pos[stop_ind]] + pos[start_ind +
                                                                              1: stop_ind] + [pos[start_ind]] + pos[stop_ind + 1:]
                            elif start_ind > stop_ind:
                                pos = pos[:stop_ind] + [pos[start_ind]] + pos[stop_ind +
                                                                              1: start_ind] + [pos[stop_ind]] + pos[start_ind + 1:]

                            if pos == winning_pos:
                                if self.on_which_puzzle == 5:
                                    self.won = True
                                else:
                                    NEXT = True

            pygame.display.update()


game = Game("Happy birthday Nirav!")
game.mainloop()

pygame.quit()
