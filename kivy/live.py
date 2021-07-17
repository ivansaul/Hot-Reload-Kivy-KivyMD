from kaki.app import App
from kivy.factory import Factory

class MDLive(App):
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
        print('Hot Reload Kivy App')
        return Factory.MyLayout()

MDLive().run()