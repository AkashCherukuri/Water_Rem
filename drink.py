from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager
import easygui
from Popups.SetAlarm import *

class SetScreen(Screen):

	def select_song(self):
		tune = easygui.fileopenbox()
		try:
			file = tune.split('/')[-1].split('.')[1]
			if file in ['mp3','mp4','wav']:
				Save("Tune", tune)
				self.tune_saved.text = f"{tune.split('/')[-1]} will be used to remind you."
			else:
				self.tune_saved.text = "Select a valid audio file!"			
		except:
			pass

	def alarm_btn(self):
		return set_alarm_popup()


class Manager(ScreenManager):
	pass

class MainScreen(Screen):
	goal = ObjectProperty(None)
	quantity = ObjectProperty(None)
	progress = ObjectProperty(None)

	def pressed(self):
		# select_time()
		self.goal.value+= int(self.quantity.value)
		self.quantity.value = 0
		self.progress.text = str(int(self.goal.value*100//7000))+'%'
                
class Drink(App):
	def build(self):
		return


if __name__ == '__main__':
    Drink().run()
