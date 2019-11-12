from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import (ScreenManager, Screen, NoTransition, 
SlideTransition, CardTransition, SwapTransition, 
FadeTransition, WipeTransition, FallOutTransition, RiseInTransition)
from kivy.uix.progressbar import ProgressBar
from kivy.lang import Builder

# class Wid(Widget):
# #   Button(text='Begin')
#     # Wid.add_widget(pb)
#     # pb = ProgressBar(max=1000)
#     pb.value = 750
#     pass

Builder.load_string(""" 
<StartScreen>: 
    # BoxLayout: 
    # Label(text="StartScreen")
        # Button: 
        #     text: "Go to Screen 2" 
        #     background_color : 0, 0, 1, 1 
        #     on_press: 
        #         # You can define the duration of the change 
        #         # and the direction of the slide 
        #         # root.manager.transition.direction = 'left' 
        #         root.manager.transition.duration = 1 
        #         root.manager.current = 'Screen2' 

""")
class StartScreen(Screen):
    # StartScreen.name("main")
    # StartScreen.name="StartScreen"
    # return Label(text="StartScreen")
    pass
class Screen2(Screen):
    pass

class FPR(App):
    def build(self):
        self.title = 'Project Financial Program'
        # return 1
        # # 
        # v = Wid()
        # v.add_widget(ProgressBar(max=1000))
        # self.screens = {}
        # self.available_screens = sorted([
        #     'Buttons', 'ToggleButton', 'Sliders', 'ProgressBar', 'Switches',
        #     'CheckBoxes', 'TextInputs', 'Accordions', 'FileChoosers',
        #     'Carousel', 'Bubbles', 'CodeInput', 'DropDown', 'Spinner',
        #     'Scatter', 'Splitter', 'TabbedPanel + Layouts', 'RstDocument',
        #     'Popups', 'ScreenManager'])
            
        root = ScreenManager(transition=CardTransition())
        root.add_widget(StartScreen(name='StartScreen'))
        root.add_widget(Screen2(name='Screen2'))
        return root
        # return Label(text='Hello World')



# class Screen2 (Screen)
#     pass
# class Screen3 (Screen)
#     pass
# class Screen4 (Screen)
#     pass
# class Screen5 (Screen)
#     pass
# class Screen6 (Screen)
#     pass



if __name__ == '__main__':
    FPR().run()