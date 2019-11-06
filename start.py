from kivy.app import App
from kivy.uix.widget import Widget

class Wid(Widget):
    pass

class FPR(App):
    def build(self):
        self.title = 'Project Financial Program'
        # return 1
        return Wid()

if __name__ == '__main__':
    FPR().run()