from kivy.app import App
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.screenmanager import Screen, ScreenManager
from functools import partial
from kivy.clock import Clock

# def alarm():
class Popup1(GridLayout): 
	def __init__(self):
		GridLayout.__init__(self)
		self.cols = 1

	def select_song(self):
		popupWindow = Popup(title ="Select Song", content = Popup2(), 
		                size_hint =(None, None), size =(400, 400))
		popupWindow.open()

class Popup2(GridLayout): 
	def __init__(self):
		GridLayout.__init__(self)
		self.cols = 1

	def select_file(self):
		popupWindow = Popup(title ="Select Song", content = Filechooser(), 
		                size_hint =(None, None), size =(600, 1000))
		popupWindow.open()

class Filechooser(GridLayout): 
    def selected(self, filename):
        try:
            self.ids.Yu.text = str(filename[0])
        except:
            pass

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

class Manager(ScreenManager):
	pass

class MainScreen(Screen):
	goal = ObjectProperty(None)
	quantity = ObjectProperty(None)
	progress = ObjectProperty(None)

	def pressed(self):
		select_time()
		self.goal.value+= int(self.quantity.value)
		self.quantity.value = 0
		self.progress.text = str(int(self.goal.value*100//7000))+'%'
                
class Drink(App):
	def build(self):
		return


if __name__ == '__main__':
    Drink().run()
