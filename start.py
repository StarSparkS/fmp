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
from Dates2Hours import D2Hfx, AM
from decimal import *
from kivy.uix.textinput import TextInput

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
# def AM():
#     print("Hello")
    
Builder.load_string(""" 
<FPH>: 
    id: fz
    # ScreenManager:
    #     id: rt
    BoxLayout:
        orientation: 'vertical'
        NavBar_ActionBar:
            id: ActionBar
        Button:
            text: 'Financial Program Home'
            on_release: fz.ast2()
        Button:
            text: 'Financial Program Home'
            on_release: app.ast()
        Button:
            text: 'Progress Bar Test'
            on_release: app.pbaru()
        Label:
            id:lls
            text: "Test"
        # Label:
        #     text: 'Progression: {}%'.format(int(pb.value))
        #     size_hint_y: None
    
        #     height: '48dp'
        ProgressBar:
            id: pb
            size_hint_x: 1
            size_hint_y: None
            height: '48dp'
            value: 0
            # value: (fz.bar() * 10) % 100
    # <root>:
    #     id: sm
          
<NavBar_ActionBar@ActionBar>:
    # manager: rt
    ActionView:
        id: ActionView
        use_separator: True
        HiddenIcon_ActionPrevious:
        ActionGroup:
            id: App_ActionGroup
            mode: 'spinner'
            text: 'NAV'
            ActionButton:
                text: 'Home'
                on_release: app.root.current = 'FinancialProgramHome'
            ActionButton:
                text: 'DatesToHours'
                on_release: app.root.current = 'D2HA'
            ActionButton:
                text: 'APP 2 TBD'
                on_release:  app.root.current = 'A2'
            ActionButton:
                text: 'APP 3 TBD'
                on_release:  app.root.current = 'A3'
            ActionButton:
                text: 'APP 4 TBD'
                on_release:  app.root.current = 'A4'
            ActionButton:
                text: 'APP 5 TBD'
                on_release:  app.root.current = 'A5'
            ActionButton:
                text: 'APP 6 TBD'
                on_release:  app.root.current = 'A6'
            ActionButton:
                text: 'APP 7 TBD'
                on_release:  app.root.current = 'A7'
            ActionButton:
                text: 'APP 8 TBD'
                on_release:  app.root.current = 'A8'
            ActionButton:
                text: 'CREDITS'
                on_release:  app.root.current = 'CRR'

        ActionGroup:
            id: App_ActionGroup
            mode: 'spinner'
            text: 'SETTINGS'
            ActionButton:
                text: 'App Settings'
                on_press: app.open_settings()
            ActionButton:
                text: 'TBD'
            # ActionButton:
            #     text: 'Quit'
            #     on_press: app.get_running_app().stop()
        # ActionGroup:
        #     id: File_ActionGroup
        #     mode: 'spinner'
        #     text: 'TBD FILE OPS'
        #     ActionButton:
        #         text: 'Open'
        #     ActionButton:
        #         text: 'Save'
        ActionButton:
            text: 'EXIT'
            on_press: app.get_running_app().stop()
       

<HiddenIcon_ActionPrevious@ActionPrevious>:
    title: ''   # app.title if app.title is not None else 'Action Previous'
    with_previous: False
    app_icon: ''
    app_icon_width: 0
    app_icon_height: 0
    size_hint_x: None
    width: len(self.title) * 10

<D2H>: 
    # id: 'D2HA'

    BoxLayout: 
        orientation: 'vertical'
        NavBar_ActionBar:
            id: ActionBar
        BoxLayout:
            orientation: 'vertical'
            # Button: 
            #     text:'a'
            #     size_hint: (.5,.35)
            #     pos_hint: {'x': .33, 'y': .2}
            TextInput:
                size_hint: (.3,.3)
                text: 'Enter Start Date (MM/DD/YYYY)'
                multiline: False
                id: startDateInput
                # bind:
                #     on_text_validate: app.process()
                # self.bind(on_text_validate:on_enter)
            # TextInput:
            #     size_hint: (.3,.3)
            #     text: 'Enter optional Date (MM/DD/YYYY)'
            #     multiline: False
            #     id: startDateInput
            #     # self.bind(on_text_validate:on_enter)
            TextInput:
                size_hint: (.3,.3)
                text: 'Enter End Date (MM/DD/YYYY)'
                multiline: False
                id: startDateInput
                # self.bind(on_text_validate:on_enter)
            # startDateInput = TextInput(text='Enter Start Date (MM/DD/YYYY)')//, multiline=False)
            # startDateInput.bind(on_text_validate=on_enter)
            # start
            Button:
                text: 'Calculate Work Days in Between'
                size_hint: (.3,.3)
            Button:
                text:'b' 
                size_hint: (.3,.3)  
        ProgressBar:
            id: pb
            size_hint_x: 1
            size_hint_y: None
            height: '48dp'
            value: 20
            # app.pbaru()
            # value: 0
            # value: (fz.bar() * 10) % 100
    # 
    #     Label:
    #         text: 'Home'
    #     Button: 
    #         text: 'a'
    #     Button:
    #         text: 'b'
        
<S3A2>: 
    BoxLayout: 
        orientation: 'vertical'
        NavBar_ActionBar:
            id: ActionBar
        Button:
            text: 'Screen3 (App 2) TBD'
        ProgressBar:
            id: pb
            size_hint_x: 1
            size_hint_y: None
            height: '48dp'
            value: 30
<Screen4>: 
    BoxLayout: 
        orientation: 'vertical'
        NavBar_ActionBar:
            id: ActionBar
        Button:
            text: 'Screen4 (App 3) TBD'
        ProgressBar:
            id: pb
            size_hint_x: 1
            size_hint_y: None
            height: '48dp'
            value: 40
<Screen5>: 
    BoxLayout: 
        orientation: 'vertical'
        NavBar_ActionBar:
            id: ActionBar
        Button:
            text: 'Screen5 (App 4) TBD'
        ProgressBar:
            id: pb
            size_hint_x: 1
            size_hint_y: None
            height: '48dp'
            value: 50
<Screen6>: 
    BoxLayout: 
        orientation: 'vertical'
        NavBar_ActionBar:
            id: ActionBar
        Button:
            text: 'Screen6 (App 5) TBD'
        ProgressBar:
            id: pb
            size_hint_x: 1
            size_hint_y: None
            height: '48dp'
            value: 60
<Screen7>: 
    BoxLayout: 
        orientation: 'vertical'
        NavBar_ActionBar:
            id: ActionBar
        Button:
            text: 'Screen7 (App 6) TBD'
        ProgressBar:
            id: pb
            size_hint_x: 1
            size_hint_y: None
            height: '48dp'
            value: 70
<Screen8>: 
    BoxLayout: 
        orientation: 'vertical'
        NavBar_ActionBar:
            id: ActionBar
        Button:
            text: 'Screen8 (App 7) TBD'
        ProgressBar:
            id: pb
            size_hint_x: 1
            size_hint_y: None
            height: '48dp'
            value: 80
<Screen9>: 
    BoxLayout: 
        orientation: 'vertical'
        NavBar_ActionBar:
            id: ActionBar
        Button:
            text: 'Screen9 (App 8) TBD'
        ProgressBar:
            id: pb
            size_hint_x: 1
            size_hint_y: None
            height: '48dp'
            value: 90
<CRS>
    BoxLayout: 
        orientation: 'vertical'
        NavBar_ActionBar:
            id: ActionBar
        Button:
            text: 'CREDITS TBD'
        ProgressBar:
            id: pb
            size_hint_x: 1
            size_hint_y: None
            height: '48dp'
            value: 100
""")

#
#Class Declaration
#
class FPH(Screen): #Home Page
    def ast2(self):
        self.ids.lls.text = "gotcha"
    # pass
class D2H(Screen): #Calculate dates/hours to be funded in a range
    pass
class S3A2(Screen): #Calculate material costs
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
class Screen9(Screen): #??
    pass
class CRS(Screen): #CREDITS
    pass

# cl
rt = ScreenManager( transition=FadeTransition(duration=.5))
rt.add_widget(FPH(name='FinancialProgramHome'))
rt.add_widget(D2H(name='D2HA')) # name is how to navigate
rt.add_widget(S3A2(name='A2'))
rt.add_widget(Screen4(name='A3'))
rt.add_widget(Screen5(name='A4'))
rt.add_widget(Screen6(name='A5'))
rt.add_widget(Screen7(name='A6'))
rt.add_widget(Screen8(name='A7'))
rt.add_widget(Screen9(name='A8'))
rt.add_widget(CRS(name='CRR'))
#main App
class FPR(App):
    from Dates2Hours import D2Hfx, AM
    # icon = 'PFPICON.ico'
    global pbar
    D2HSD = 0
    D2HED = 0
    # = 0
    pbar =0
    # def datevalidator(self):
    def pbaru(self):
        global pbar
        if(pbar < 100):
            pbar +=10
            self.root.get_screen('FinancialProgramHome').ids.pb.value = pbar
        else:
            
            pbar = 0
            self.root.get_screen('FinancialProgramHome').ids.pb.value = pbar
        return

    def pbar2(self):
        global pbar
        if(pbar < 100):
            pbar +=10
            # self.root.get_screen('FinancialProgramHome').ids.pb.value = pbar
        else:
            
            pbar = 0
            # self.root.get_screen('FinancialProgramHome').ids.pb.value = pbar
        return pbar
        
        # return pbar

    def ast(self):
        self.root.get_screen('FinancialProgramHome').ids.lls.text = "more"
        # rt.get_screen('A3')

        return
    def build(self):
        # self.icon = 'PFPICON.ico'
        self.title = 'Project Financial Program (PFP)'
        
        # self.screens = {}
        # self.available_screens = sorted([
        #     'Buttons', 'ToggleButton', 'Sliders', 'ProgressBar', 'Switches',
        #     'CheckBoxes', 'TextInputs', 'Accordions', 'FileChoosers',
        #     'Carousel', 'Bubbles', 'CodeInput', 'DropDown', 'Spinner',
        #     'Scatter', 'Splitter', 'TabbedPanel + Layouts', 'RstDocument',
        #     'Popups', 'ScreenManager'])
            
    
        # self.get_application_icon()

        return rt

if __name__ == '__main__':
    FPR().run()