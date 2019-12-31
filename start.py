from kivy.config import Config
Config.set('kivy','window_icon', 'ico/fmp3.png')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import (ScreenManager, Screen, NoTransition, 
SlideTransition, CardTransition, SwapTransition, 
FadeTransition, WipeTransition, FallOutTransition, RiseInTransition)
from kivy.uix.progressbar import ProgressBar
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.lang import Builder
from Dates2Hours import D2Hfx, AM #, D2H
from decimal import *
from kivy.uix.textinput import TextInput
from datetime import date, timedelta, datetime
from kivy.properties import NumericProperty, StringProperty, BooleanProperty,ListProperty
import os
import csv
import xlrd, xlwt, xlutils # (possible upgrade)

Builder.load_file('fpr_kivy.kv')
Builder.load_file('D2H_SCREEN.kv')
Builder.load_file('HOME.kv')
Builder.load_file('navbar.kv')
Builder.load_string(""" 
<MIC>: 
    id: micwid
    BoxLayout: 
        orientation: 'vertical'
        NavBar_ActionBar:
            id:abar
        Accordion:
            id: acc
            orientation: 'horizontal'           
            AccordionItem:
                title: 'Select Existing Materiel List'
                BoxLayout:
                    orientation: 'vertical'
                    FileChooserIconView:
                        size_hint_x: 1
                        id: filechooser
                        # view_mode: 'icon'
                        path: app.pathfinder()
                        on_selection: micwid.show(filechooser.selection)
                    Label: 
                        id: ll
                        size_hint_y: .1
                        text: "status: no selection made"
                    BoxLayout:
                        size_hint_y: .1
                        Button:
                            text: "Press to reset file selector"
                            on_release: micwid.ids.filechooser.path = app.pathfinder(); micwid.ids.ll.color = 1,1,1,1; micwid.ids.fc.disabled = False#; micwid.ids.nl.disabled = False
                        Button:
                            id: fc
                            text: "Press to complete selection"
                            on_release: micwid.parse(filechooser.path, filechooser.selection); micwid.ids.ll.color = 0,.6,.6,1; self.disabled = True#; micwid.ids.nl.disabled = True
                    # Button: 
                    #     id: nl
                    #     size_hint_y: .1
                    #     text: "Make a new empty list with current date YYYY_MM_DD_matlist.xls)"
                    #     on_release: self.disabled = True; micwid.ids.fc.disabled = True
            AccordionItem:
                id: current_list
                title: 'Current List'
                ScrollView:
                    id: svm
                    do_scroll_y: True
                    size_hint_y: 1
                    bar_color: .2,.6, .6, 1
                    bar_inactive_color: 1,1,1,1
                    bar_width: 10
                    bar_text: "hello"
                    GridLayout:
                        id:clbl
                        cols: 8
                        # size_hint_x: 1
                        # size_hint_y: 1.0
                        orientation: 'vertical'
                        # Label: 
                        #     id:ltxt
                        #     text: "Tool Name -SW/FW-Static/Dynamic/Formal-Annual/Perpetual	Date of Last Purchase	Cost Per Unit	Qty	Total Cost	Vendor Agent Name	Vendor #	Vendor Email	Team POC"
            AccordionItem:
                title: 'Analysis'
                Label:
                    text: 'Total Cost:'
                    text_size: self.width, None
                Label:
                    id:cvalue
                    text: '$0.00'
                    text_size: self.width, None
        ProgressBar:
            id: pb
            height: '10dp'
            size_hint_x: 1
            size_hint_y: None
            value: 30                    
""")
#
#Class Declaration
#
class FPH(Screen): #Home Page
    # def ast2(obj):
    #     obj.ids.lls.text = "gotcha"
    pass
#
# every action creates a dynamic screen?
#     
class D2H(Screen): #Calculate dates/hours to be funded in a range
    # SDI_valid = 0
    # sd = ""
    # EDI_valid = 0
    # ed = ""  
    def __init__(self, **kwargs):
        self.SDI_valid = 0
        self.sd = ""
        self.EDI_valid = 0
        self.ed = ""
        self.r_days=0
        self.r_hours=0
        self.a_days =0
        self.a_hours = 0
        self.ftr = 1
        super().__init__(**kwargs)
    
    def D2H_reset(obj):
        # print (obj)
        # print (obj)
        obj.SDI_valid = 0
        obj.sd = ""
        obj.EDI_valid = 0
        obj.ed = ""
        obj.r_days =0
        obj.r_hours = 0
        obj.a_days =0
        obj.a_hours = 0
        obj.ftr = 1
        obj.ids.startDateInput.disabled = 0
        obj.ids.endDateInput.disabled = 0
        obj.ids.startDateInput.text = 'Enter Start Date (MM/DD/YYYY)'
        obj.ids.D2H_PROMPT1.text = 'Enter Start Date (MM/DD/YYYY)'
        obj.ids.endDateInput.text = 'Enter End Date (MM/DD/YYYY)'
        obj.ids.D2H_PROMPT2.text = 'Enter End Date (MM/DD/YYYY)'
        obj.ids.d2h_check_1.text = 'Start Date State: Incomplete'
        obj.ids.d2h_check_2.text = 'End Date State: Incomplete'
        obj.ids.d2h_check_1.color = 1,0,0,1
        obj.ids.d2h_check_2.color = 1,0,0,1
        obj.ids.s2.value = 1880
        obj.ids.s3.value = 1
        obj.ids.CalcFB.text = "Calculation Feedback: ?"
        obj.ids.CalcFB.color = 1, 1, 1, 1
        obj.ids.wdr.text = "-----"
        obj.ids.wdr.color = 1,0, 0, 1
        obj.ids.wda.text = "-----"
        obj.ids.wda.color = 1,0, 0, 1
        obj.ids.rwh.text = "-----"
        obj.ids.rwh.color = 1,0, 0, 1
        obj.ids.awh.text = "-----"
        obj.ids.awh.color = 1,0, 0, 1

    def SDI(self):   
        if (self.ids.startDateInput.focus):
            self.ids.startDateInput.text = ""
            self.ids.d2h_check_1.text = "Start Date Status: Focused/Data Entry"
            # (*args).ids.lcheck.text = "f2"
        else:
            if(len(self.ids.startDateInput.text) == 10):
                self.ids.d2h_check_1.text = "Start Date Status: Length Correct"
                try:
                    start_mm, start_dd, start_yyyy=  self.ids.startDateInput.text.strip().split("/")
                    self.sd = date(int(start_yyyy), int(start_mm), int(start_dd))
                    self.ids.d2h_check_1.text = "Start Date Status: Complete! " + str(self.sd)
                    self.ids.d2h_check_1.color = 0,1,0,1
                    self.ids.startDateInput.disabled = 1
                    self.SDI_valid = 1
                except: 
                    self.ids.d2h_check_1.text = "Start Date Status: Input Invalid"
            else:
                self.ids.d2h_check_1.text = "Start Date Status: Length Incorrect/Not Focused"

    def EDI(obj):   
        if (obj.ids.endDateInput.focus):
            obj.ids.endDateInput.text = ""
            obj.ids.d2h_check_2.text = "End Date Status: Focused/Data Entry"
            # (*args).ids.lcheck.text = "f2"
        else:
            if(len(obj.ids.endDateInput.text) == 10):
                obj.ids.d2h_check_2.text = "End Date Status: Length Correct"
                try:
                    end_mm, end_dd, end_yyyy=  obj.ids.endDateInput.text.strip().split("/")
                    obj.ed = date(int(end_yyyy), int(end_mm), int(end_dd))
                    if (obj.ed > obj.sd):
                        obj.ids.d2h_check_2.text = "End Date Status: Complete! "  + str(obj.ed)
                        obj.ids.d2h_check_2.color = 0,1,0,1
                        obj.ids.endDateInput.disabled = 1
                        obj.EDI_valid = 1
                    else:
                        obj.ids.d2h_check_2.text = "End Date Status: End Date needs to be past Start Date"
                except: 
                    obj.ids.d2h_check_2.text = "Start Date Status: Lenght Correct/Date Input Invalid"
            else:
                obj.ids.d2h_check_2.text = "Start Date Status: Length Incorrect/Not Focused"

    def calc(obj):   
        if(obj.EDI_valid and obj.SDI_valid):
            obj.ids.CalcFB.text = "input valid!"
            obj.ids.CalcFB.color = 0, 1, 0, 1
            loop_date = obj.sd #set variable to start date
            while(loop_date <= obj.ed):
                if(loop_date.weekday() < 5):
                    obj.r_days+=1
                loop_date += timedelta(days=1)
            obj.r_hours = obj.r_days*8
            obj.a_days = (Decimal(obj.ids.s2.value)/(Decimal(2088))) * (Decimal(obj.ftr)) * obj.r_days
            obj.a_hours = obj.a_days * 8
            obj.ids.wdr.text = str(obj.r_days)
            obj.ids.wdr.color = 0, 1, 0, 1
            obj.ids.wda.text = str(obj.a_days)
            obj.ids.wda.color = 0, 1, 0, 1
            obj.ids.rwh.text = str(obj.r_hours)
            obj.ids.rwh.color = 0, 1, 0, 1
            obj.ids.awh.text = str(obj.a_hours)
            obj.ids.awh.color = 0, 1, 0, 1
        else:
            obj.ids.CalcFB.text = "Calculation Feedback: Fix Input"
            obj.ids.CalcFB.color = 1, 0, 0, 1
        return 1
    def stp(obj):
        obj.ftr = obj.ids.s3.value
        obj.ftr = Decimal(obj.ftr)
        obj.ftr = round(obj.ftr,2)
        obj.ids.stp.text = str(round(obj.ftr*100)) + '%' #str(round(Decimal(s3), 1)) 

class MIC(Screen): #Calculate material and infrastructure costs
    
    def __init__(self, **kwargs):
        self.rcount = 0
        self.xwmax = 1
        self.colvals = []
        self.colfilter = ["PN", "LT(A|P)", "PD", "CPU", "QTY", "LC"]
        self.totalcost = 0
        self.cl= 0
        super().__init__(**kwargs)

    def show( self, filename):
        self.ids.ll.text = str(filename)

    def parse(self,path, filename):
        matxl = xlrd.open_workbook(os.path.join(path, filename[0]))
        mat_sheet = matxl.sheet_by_index(0)
        self.ids.clbl.rows = mat_sheet.nrows
        self.ids.clbl.cols = 8
        # if mat_sheet.ncols > 10:
        #     self.ids.clbl.size_hint_x = (mat_sheet.ncols/10)
        for row in range(0, mat_sheet.nrows):
            if(len(str(mat_sheet.cell(row,0).value)) > 0):
                self.rcount +=1
                if(self.rcount > 10):
                    self.ids.clbl.size_hint_y = (self.rcount/10)
                self.ids.clbl.add_widget(Label(text = (str(row))))
                for col in range (0, mat_sheet.ncols):
                    cell = mat_sheet.cell(row,col)
                    if row == 0:
                        if str(cell.value) in self.colfilter:
                            self.colvals.append(col)
                            if(str(cell.value)=="LC"):
                                self.cl = col
                    if col in self.colvals:
                        if cell.ctype ==3:
                            py_date = xlrd.xldate.xldate_as_datetime(cell.value, matxl.datemode)
                            py_date = date(py_date.year, py_date.month, py_date.day)
                            self.ids.clbl.add_widget(Label(text = (str(py_date))))
                        else:
                            # print (str(cell.ctype))
                            self.ids.clbl.add_widget(Label(text = (str(cell.value))))
                    if col == self.cl and row>0:
                        print(cell)
                        self.totalcost = Decimal(self.totalcost) + Decimal(str(cell.value))
                if row == 0:
                    self.ids.clbl.add_widget(Label(text = (str("+/-"))))
                else:
                    self.ids.clbl.add_widget(CheckBox(id = str(row), active = 1 ))  
        self.ids.cvalue.text = str("$" + str(self.totalcost))
            # print ("Cols: ")
            # print (str(mat_sheet.ncols))

        # pf = open(os.path.join(path, filename[0]))
        # rpf = pf.read().split('\n')
        # cpf = csv.reader(rpf)
        # for n in cpf:
        #     if len(str(n)) > 2:
        #         self.rcount +=1
        #         print (n[0])
        #         # self.ids.ltxt.text = str(n)
        #         self.ids.clbl.add_widget(Label(text = str(n)))

        #         if len(str(n))/100 > self.xwmax:
        #             self.ids.clbl.size_hint_x = len(str(n)) /100 
        #             self.xwmax = len(str(n))/100 

        #         if (self.rcount > 10):
        #             self.ids.clbl.size_hint_y = (self.rcount/10)
        # pf.close()

        
        # with open()) as stream:
        # self.text_input.text = stream.read()

    

    # def open(self, path, filename):
    #     with open(os.path.join(path, filename[0])) as f:
    #             print f.read()
    # def selected(self, filename)
    pass
class LPI(Screen): #Keys Input Labor Columns
    def __init__(self, **kwargs):
        self.rcount = 0
        self.xwmax = 1
        super().__init__(**kwargs)

    def show( self, filename):
        self.ids.ll.text = str(filename)

    pass
class LPI_VAL(Screen): #Values Inputs Labor Data
    pass
class TVL(Screen): # Travel Costs
    pass
class CALC(Screen): #Cost Output
    pass
class OT(Screen): #Output
    pass
# class ES(Screen): #Budget Estimator
#     pass
class CRS(Screen): #CREDITS
    pass

#main App
class FPR(App):
    current_title = StringProperty()
    from Dates2Hours import D2Hfx, AM   

    def pathfinder(self):
        cwd = os.getcwd()
        return cwd
    
    def __init__ (self):
        super().__init__()
        self.rt = ScreenManager( transition=FadeTransition(duration=.25))
        self.rt.add_widget(FPH(name='PFP_HOME'))
        self.rt.add_widget(D2H(name='D2HA'))
        self.rt.add_widget(MIC(name='MICinst'))
        self.rt.add_widget(LPI(name='LABORin'))
        self.rt.add_widget(LPI_VAL(name='LPIR'))
        self.rt.add_widget(TVL(name='TVLinst'))
        self.rt.add_widget(CALC(name='CALCinst'))
        self.rt.add_widget(OT(name='OTinst'))
        # self.rt.add_widget(ES(name='ESin'))
        self.rt.add_widget(CRS(name='CRR'))
        self.current_title = "FINANCE HOME"
        super().run()

    def build(self):
        self.title = 'FMP - A Management Assistant'
        self.icon = 'ico/fmp3.png'
        return self.rt

if __name__ == '__main__':
    # FPR().run()
    inst = FPR()