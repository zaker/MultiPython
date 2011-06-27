'''
Created on Jun 27, 2011

@author: zaker
'''
from Snake.Snake import *

class World():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.snake = Snake()
        
    def move(self):
        self.snake.plot()
        
    def plot(self):
        self.snake.plot()
        
        