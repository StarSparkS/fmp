from kivy.config import Config
Config.set('kivy','window_icon', "")

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import (ScreenManager, Screen, NoTransition, 
SlideTransition, CardTransition, SwapTransition, 
FadeTransition, WipeTransition, FallOutTransition, RiseInTransition)
from kivy.uix.progressbar import ProgressBar
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from Dates2Hours import D2Hfx
from decimal import *

# # class Wid(Widget):
# # #   Button(text='Begin')
# #     # Wid.add_widget(pb)
# #     # pb = ProgressBar(max=1000)
# #     pb.value = 750
# #     pass

# StartScreen.name("main")
# StartScreen.name="StartScreen"
# self.name = "StartScreen"
# return Label(text="StartScreen")

# def main():
#     val = D2Hfx(0, 1, .5)
#     print(val)
#     return 0


Builder.load_string(""" 
<FPH>: 
    name: "Home" 
    BoxLayout: 
        orientation: 'vertical'
        NavBar_ActionBar:
            id: ActionBar
        Button:
            text: 'Home1'   
        Button:
            text: "h2"
<NavBar_ActionBar@ActionBar>:
    ActionView:
        id: ActionView
        
        HiddenIcon_ActionPrevious:

        ActionGroup:
            id: App_ActionGroup
            mode: 'spinner'
            text: 'Jump to Screen'

            ActionButton:
                text: 'Crime Prediction'
                on_release: app.root.ids.sm.current = 'second'
            ActionButton:
                text: 'Forum'
                on_release:  app.root.ids.sm.current = 'second'
            ActionButton:
                text: 'Probable Suspect'
                on_release:  app.root.ids.sm.current = 'second'

        ActionGroup:
            id: App_ActionGroup
            mode: 'spinner'
            text: 'App'

            ActionButton:
                text: 'Settings'
                on_press: app.open_settings()
            ActionButton:
                text: 'Quit'
                on_press: app.get_running_app().stop()

        ActionGroup:
            id: File_ActionGroup
            mode: 'spinner'
            text: 'File'

            ActionButton:
                text: 'Open'
            ActionButton:
                text: 'Save'
                
<HiddenIcon_ActionPrevious@ActionPrevious>:
    title: ''   # app.title if app.title is not None else 'Action Previous'
    with_previous: False
    app_icon: ''
    app_icon_width: 0
    app_icon_height: 0
    size_hint_x: None
    width: len(self.title) * 10

<d2h>: 
    Button:
        text: 'D2H'
    BoxLayout:
        Label:
            text: 'Home'
        Button: 
            text: 'a'
        Button:
            text: 'b'
        
<Screen3>: 
    Button:
        text: 'Screen3'
<Screen4>: 
    Button:
        text: 'Screen4'
<Screen5>: 
    Button:
        text: 'Screen5'
<Screen6>: 
    Button:
        text: 'Screen6'
<Screen7>: 
    Button:
        text: 'Screen7'
<Screen8>: 
    Button:
        text: 'Screen8'
""")

#
#Class Declaration
#
class FPH(Screen): #Home Page
    pass
class D2H(Screen): #Calculate dates/hours to be funded in a range
    pass
class Screen3(Screen): #Calculate materiels
    pass
class Screen4(Screen): #Keys Input
    pass
class Screen5(Screen): #Values Inputs
    pass
class Screen6(Screen): #Cost Output
    pass
class Screen7(Screen): #Cost with Fees
    pass
class Screen8(Screen): #Budget Estimator
    pass

#main App
class FPR(App):
    # icon = 'PFPICON.ico'
    def build(self):
        # self.icon = ""
        self.title = 'Project Financial Program'
        
        # self.screens = {}
        # self.available_screens = sorted([
        #     'Buttons', 'ToggleButton', 'Sliders', 'ProgressBar', 'Switches',
        #     'CheckBoxes', 'TextInputs', 'Accordions', 'FileChoosers',
        #     'Carousel', 'Bubbles', 'CodeInput', 'DropDown', 'Spinner',
        #     'Scatter', 'Splitter', 'TabbedPanel + Layouts', 'RstDocument',
        #     'Popups', 'ScreenManager'])
            
        root = ScreenManager(transition=CardTransition())
        root.add_widget(FPH(name='FinancialProgramHome'))
        root.add_widget(D2H(name='d2h')) # name is how to navigate
        root.add_widget(Screen3(name='Screen3'))
        root.add_widget(Screen4(name='Screen4'))
        root.add_widget(Screen5(name='Screen5'))
        root.add_widget(Screen6(name='Screen6'))
        root.add_widget(Screen7(name='Screen7'))
        root.add_widget(Screen8(name='Screen8'))
        self.get_application_icon()
        return root

if __name__ == '__main__':
    FPR().run()