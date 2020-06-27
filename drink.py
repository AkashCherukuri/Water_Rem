from kivy.app import App
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from Water import alarm
import easygui

time,tune = 1,'Rick.wav'

def select_time():
	popupWindow = Popup(title ="Select Time", content = Popup1(), 
	                size_hint =(None, None), size =(400, 400))
	popupWindow.open()

class SetScreen(Screen):
	minutes = ObjectProperty(None)
	minutes_saved = ObjectProperty(None)

	def new_setting(self):
		# Clock.schedule_interval(partial(alarm), minutes)
		self.minutes_saved.text = 'You will be reminded every '+str(self.minutes.text)+' mins.'
	def select_song(self):
		tune = easygui.fileopenbox()
		file = tune.split('/')[-1].split('.')[1]
		if file in ['mp3','mp4','wav']:
			self.tune_saved.text = tune.split('/')[-1]+ ' will be used to remind you.'
		else:
			self.tune_saved.text = "Select a valid audio file!"			
		# print()

	def start(self):
		alarm(int(self.minutes.text), tune)


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
