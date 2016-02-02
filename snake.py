from pygameHelper import *
from pygame import *
from pygame.locals import *
#from vec2d import *
import random
from math import e, pi, cos, sin, sqrt

color_white = (255,255,255)
color_black = (0,0,0)
color_red = (255,0,0)
color_green = (0,255,0)
color_blue = (0,0,255)

class Snake(PygameHelper):
	def __init__(self):
		self.w, self.h = 800,600
		PygameHelper.__init__(self, size=(self.w,self.h), background_color=color_white)
		self.snakePoints = [(self.w//2, self.h//2),(self.w//2+10, self.h//2)]
		self.lastKey = pygame.K_RIGHT
		self.score = 0
		self.createFood()

	def isFoodEaten(self):
		return self.snakePoints[0] == self.food
	def createFood(self):
		self.food = (random.randint(0, self.w//10-10)*10, random.randint(0, self.h//10-10)*10)

	def keyUp(self, key):
		if key == pygame.K_UP or key == pygame.K_DOWN or key == pygame.K_RIGHT or key == pygame.K_LEFT:
			self.lastKey = key

	def crash(self):
		scoreText = pygame.font.SysFont("comicsansms", 50)
		textSurf = scoreText.render("Your Score:" + str(self), True, color_red)
		textSurf.get_rect().center = (self.w//2, self.h//2)
		self.screen.blit(textSurf, textSurf.get_rect())


	def collision(self):
		for s in self.snakePoints[1:]:
			if s== self.snakePoints[0]:
				return True
		return False

	def update(self):
		if self.lastKey == pygame.K_LEFT:
			self.snakePoints.insert(0, (self.snakePoints[0][0]-10, self.snakePoints[0][1]))
		if self.lastKey == pygame.K_RIGHT:
			self.snakePoints.insert(0, (self.snakePoints[0][0]+10, self.snakePoints[0][1]))
		if self.lastKey == pygame.K_UP:
			self.snakePoints.insert(0, (self.snakePoints[0][0], self.snakePoints[0][1]-10))
		if self.lastKey == pygame.K_DOWN:
			self.snakePoints.insert(0, (self.snakePoints[0][0], self.snakePoints[0][1]+10))

		if self.collision():
			self.crash()
		print self.snakePoints
		print "food: " + str(self.food)

	def draw(self):
		self.screen.fill((255,255,255))
		self.drawSnake()
		if self.isFoodEaten():
			self.createFood()
			self.score += 1
		else:
			self.snakePoints.pop()
		pygame.draw.rect(self.screen, color_green, (self.food[0],self.food[1],9,9))

	def mouseUp(self, button, pos):
		pass

	def mouseMotion(self, button, pos, rel):
		pass

	def drawSnake(self):
		pygame.draw.rect(self.screen, color_black, (self.snakePoints[0][0], self.snakePoints[0][1], 9, 9))
		for p in self.snakePoints[1:]:
			pygame.draw.rect(self.screen, color_red, (p[0],p[1],9,9))

	def addRect(self, p):
		pass

	def isSnakeLeft(self):
		return self.snakePoints[0][0] - self.snakePoints[1][0] == -10

	def isSnakeRight(self):
		return self.snakePoints[0][0] - self.snakePoints[1][0] == 10

	def isSnakeUp(self):
		return self.snakePoints[0][1] - self.snakePoints[1][1] == -10

	def idSnakeDown(self):
		return self.snakePoints[0][1] - self.snakePoints[1][1] == 10

s= Snake()
s.mainLoop(10)
