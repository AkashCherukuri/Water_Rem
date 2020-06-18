from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

class Alarm_Popup(FloatLayout):
	alarm_in = ObjectProperty(None)
	Alarm_time = 0
	def save_alarm(self):
		Alarm_time = self.alarm_in.text
		print(f"Saved! Alarm go off in {Alarm_time} intervals!")

def set_alarm_popup():
	show = Alarm_Popup()
	popupWindow = Popup(title = "Set Alarm interval", content = show, size_hint = (None, None), size = (600, 400))
	popupWindow.open()

