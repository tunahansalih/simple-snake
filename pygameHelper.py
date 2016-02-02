import pygame
from pygame.locals import *

class PygameHelper:
	def __init__(self, size=(800,600), background_color=(255,255,255)):
		pygame.init()
		self.screen = pygame.display.set_mode(size)
		self.screen.fill(background_color)
		pygame.display.update()
		self.running = False
		self.clock = pygame.time.Clock()
		self.size = size
		self.fps = 0

	#Handles events
	def handleEvents(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				quit()
			elif event.type == KEYDOWN:
				self.keyDown(event.key)
			elif event.type == KEYUP:
				if event.key == K_ESCAPE:
					self.running = False
				self.keyUp(event.key)
			elif event.type == MOUSEBUTTONUP:
				self.mouseUp(event.button, event.pos)
			elif event.type == MOUSEMOTION:
				self.mouseMotion(event.buttons, event.pos, event.rel)
	#Waits for a key(any key)
	def waitForKey(self):
		press=False
		while not press:
			for event in pygame.event.get():
				if event.type == KEYUP:
					press = True
	#Main loop for games including update(), draw() and handleEvents()
	def mainLoop(self, fps=0):
		self.running = True
		self.fps = fps

		while self.running:
			pygame.display.set_caption("FPS :%i" % self.clock.get_fps())
			self.handleEvents()
			self.update()
			self.draw()
			pygame.display.update()
			self.clock.tick(self.fps)

	#updates every frame
	def update(self):
		pass

	#like update function, but for the use of drawing functions
	def draw(self):
		pass

	#waits for key
	def keyDown(self, key):
		pass

	#waits for key release
	def keyUp(self, key):
		pass

	#Handles mouse clicks
	def mouseUp(self, button, pos):
		pass

	#Handles mouse motion
	def mouseMotion(self, button, pos, rel):
		pass
