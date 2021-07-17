from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

Window.size= (511,638)

#Builder.load_file('my_kv.kv')

class MyLayout(FloatLayout):
    pass

#class MainApp(App):
#	title = 'My App'
#	def build(self):
#		return MyLayout()
#
#if __name__ == '__main__':
#	MainApp().run()