from kivy.app import App
from kivy.uix.gridlayout import GridLayout
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
# from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
# from kivy.graphics import Rectangle, Color

class AppGrid(GridLayout):
	goal = ObjectProperty(None)
	quantity = ObjectProperty(None)
	progress = ObjectProperty(None)
	def pressed(self):
		self.goal.value+= int(self.quantity.value)
		self.quantity.value = 0
		self.progress.text = str(self.goal.value*100//7000)+'%'
		print(self.progress.text)
		print(self.goal.value)
        
        
class Drink(App):
    def build(self):
        return AppGrid()


if __name__ == '__main__':
    Drink().run()