import pickle
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
# from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
# from kivy.graphics import Rectangle, Color
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.popup import Popup

Alarm_time = 0

class Manager(ScreenManager):
	pass

class MainScreen(Screen):
	goal = ObjectProperty(None)
	quantity = ObjectProperty(None)
	progress = ObjectProperty(None)
	
	def pressed(self):
		self.goal.value+= int(self.quantity.value)
		self.quantity.value = 0
		self.progress.text = str(self.goal.value*100//7000)+'%'
		print(self.progress.text)
		print(self.goal.value)

class SetScreen(Screen):
	#alarm_time = ObjectProperty(None)
	def alarm_btn(self):
		return set_alarm_popup()


class Alarm_Popup(FloatLayout):
	alarm_in = ObjectProperty(None)

	def save_alarm(self):
		Alarm_time = self.alarm_in.text
		print(f"Saved! Alarm go off in {Alarm_time} intervals!")

def set_alarm_popup():
	show = Alarm_Popup()
	popupWindow = Popup(title = "Set Alarm interval", content = show, size_hint = (None, None), size = (600, 400))
	popupWindow.open()


class Drink(App):
    def build(self):
        return


if __name__ == '__main__':
    Drink().run()
