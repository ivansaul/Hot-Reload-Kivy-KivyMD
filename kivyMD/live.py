from kaki.app import App
from kivy.factory import Factory
from kivymd.app import MDApp

class MDLive(App, MDApp):
    KV_FILES = {
        'my_kv.kv'
    }
    CLASSES = {
        'MyLayout': 'my_py'
    }
    AUTORELOADER_PATHS = [
        ('.',{'recursive':True})
    ]
    def build_app(self,*args):
        print('Hot Reload KivyMD App')
        return Factory.MyLayout()

MDLive().run()