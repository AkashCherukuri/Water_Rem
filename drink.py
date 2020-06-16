from kivy.app import App
# from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager

class SetScreen(Screen):
	minutes = ObjectProperty(None)
	minutes_saved = ObjectProperty(None)

	def new_setting(self):
		self.minutes_saved.text = 'You will be reminded every '+str(self.minutes.text)+' mins.'

class Manager(ScreenManager):
	pass

class MainScreen(Screen):
	goal = ObjectProperty(None)
	quantity = ObjectProperty(None)
	progress = ObjectProperty(None)

	
	def pressed(self):
		self.goal.value+= int(self.quantity.value)
		self.quantity.value = 0
		self.progress.text = str(int(self.goal.value*100//7000))+'%'
		# print(self.progress.text)
		# print(self.goal.value)
        
        
class Drink(App):
    def build(self):
        return


if __name__ == '__main__':
    Drink().run()
