from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.core.audio import SoundLoader
from utils import Load
from kivy.uix.popup import Popup

class Alarm(GridLayout):
	def __init__(self):
		super().__init__()
		self.sound = SoundLoader.load(Load("Tune"))
		self.sound.play()

	def stop(self):
		self.sound.stop()
		

def alarm_popup():
	show = Alarm()
	popupWindow = Popup(title = "Time to drink water!!!", content = show, size_hint = (None, None), size = (600, 400))
	popupWindow.open()