from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout

Window.size= (511,638)

#Builder.load_file('my_kv.kv')

class MyLayout(MDFloatLayout):
    pass

#class MainApp(MDApp):
#	title = 'My App'
#	def build(self):
#		return MyLayout()
#
#if __name__ == '__main__':
#	MainApp().run()