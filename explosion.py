import time, threading
import settings
class Explosion:
	def __init__(self, x, y, start = 0):
		self.X = x
		self.Y = y
		self.start = time.time()
		self.img = settings.bomb3Img
		self.explode = False
		self.thread = threading.Timer(0.0, self.check)
		self.thread.start()
	def check(self):
		if time.time() - self.start >= 1.0:
			self.explode = True
			self.thread._Thread__stop()
		self.thread = threading.Timer(0.0, self.check)
		self.thread.start()

