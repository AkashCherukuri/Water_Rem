from kivy.clock import Clock
from utils import Load
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.core.audio import SoundLoader
from kivy.uix.popup import Popup

class Timer():
    def Alarm(self, dt):
        show = Alarm()
        popupWindow = Popup(title = "Time to drink water!!!", content = show, size_hint = (None, None), size = (600, 400))
        popupWindow.open()

    def Start_Alarm(self):
        time = Load("Alarm_Time")
        # Multiply int(time) with 60 to convert to minutes later
        self.timer = Clock.schedule_interval(self.Alarm, int(time))

    def Cancel_Alarm(self):
        self.timer.cancel()

class Alarm(GridLayout):
	goal = ObjectProperty(None)
	def __init__(self):
		super().__init__()
		self.sound = SoundLoader.load(Load("Tune"))
		self.sound.play()

	def stop(self):
		self.sound.stop()