import pygame
import random

class SnakeGame:

    def __init__(self, w=640, h=480):
            self.w = w
            self.h = h
        # init display

        # init game state

    def play_step(self):
        pass



if __name__ == '__main__':
    game = SnakeGame()
    
    # game loop
    while True:
        game_over, score = game.play_step()
        
        if game_over == True:
            break
        
    print('Final Score', score)
        
        
    pygame.quit()