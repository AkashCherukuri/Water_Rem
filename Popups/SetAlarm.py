import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from utils import Save, Load
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

class Alarm_Popup(FloatLayout):
	alarm_in = ObjectProperty(None)
	Alarm_time = 0
	def save_alarm(self):
		Alarm_time = self.alarm_in.text
		Save("Alarm_Time", Alarm_time)
		save = Load("Alarm_Time")
		print(f"Saved! Alarm go off in {save} intervals!")

def set_alarm_popup():
	show = Alarm_Popup()
	popupWindow = Popup(title = "Set Alarm interval", content = show, size_hint = (None, None), size = (600, 400))
	popupWindow.open()

