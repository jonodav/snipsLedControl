# -*- coding: utf-8 -*-

###########################################################################################################
# SUBMIT YOUR OWN CUSTOM PATTERN AND SHARE WITH THE WORLD YOUR LED ANIMATIONS!
# Visit https://github.com/Psychokiller1888/snipsLedControl/issues/new?template=custom-pattern-proposal.md
# for more informations
#
# Check models/LedPattern.py for the available functions
# Do NEVER have a function call a super class function directly!!
# It could cause a deadlock! Instead, call self._controller.THE_METHOD_YOU_WANT
#
# @author:
# @weblink:
# @email:
#
###########################################################################################################

from models.LedPattern import LedPattern
import time

class CustomLedPattern(LedPattern):

	def __init__(self, controller):
		super(CustomLedPattern, self).__init__(controller)


	def wakeup(self, *args):
		start = self._controller.doa()
		self.off()
		self._animator.doubleSidedFilling(color=[255, 255, 255, 128], startAt=start, direction=-1, speed=25)

	def listen(self, *args):
		start = self._controller.doa()
		self._animator.breath(color=[255, 255, 255, 128], minBrightness=20, maxBrightness=128, speed=250)

	def think(self, *args):
		self._animator.rotate(color=[0, 255, 0, 128], speed=20, trail=int(self.numLeds / 3))

	def speak(self, *args):
		self._animator.doublePingPong(color=[255, 255, 255, 128], speed=10)

	def idle(self):
		self.off()

	def onError(self, *args):
		self._animator.blink(color=[255, 0, 0, 2], minBrightness=2, maxBrightness=20, speed=300, repeat=3)
		self.off()

	def onSuccess(self, *args):
		self._animator.blink(color=[0, 255, 0, 2], minBrightness=2, maxBrightness=25, speed=320, repeat=3)
		self.off()

	def onStart(self, *args):
		start = self._controller.doa()
		self._animator.doubleSidedFilling(color=[255, 0, 0, 15], startAt=start, direction=-1, speed=50)
		time.sleep(0.1)
		self._animator.doubleSidedFilling(color=[255, 255, 0, 15], startAt=start, direction=-1, speed=50)
		time.sleep(0.1)
		self._animator.doubleSidedFilling(color=[0, 255, 0, 15], startAt=start, direction=-1, speed=50)
		time.sleep(0.1)
		self._animator.doubleSidedFilling(color=[0, 255, 255, 15], startAt=start, direction=-1, speed=50)
		time.sleep(0.1)
		self._animator.doubleSidedFilling(color=[0, 0, 255, 15], startAt=start, direction=-1, speed=50)
		time.sleep(0.1)
		self._animator.doubleSidedFilling(color=[0,0,0,0], startAt=start, direction=-1, speed=50)
