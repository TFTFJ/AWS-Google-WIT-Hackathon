from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image

#KV configuration for app
KV = '''
BoxLayout:
    orientation:'vertical'

    #Title Bar
    MDTopAppBar:
        title: 'Hydrate'
        md_bg_color: .78, .87, .92, 1
        specific_text_color: 0, 0, 0, 1

    #Navigation Bar
    MDBottomNavigation:
        panel_color: .78, .87, .92, 1

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Water Usage'
            icon: '1.png'

            #First Tab
            BoxLayout:
                orientation: "vertical"
                MDLabel:
                    text: 'Current Usage'
                    halign: 'center'
                Image:
                    id: imageView
                    source: 'chart1.png'
                    allow_stretch: True
                MDLabel:
                    text: 'Past Usage'
                    halign: 'center'
                Image:
                    id: imageView
                    source: 'chart2.png'
                    allow_stretch: True
            

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Recycling'
            icon: '2.png'

            #Second Tab
            BoxLayout:
                orientation: "vertical"
                MDLabel:
                    text: 'Waste Water Ratio'
                    halign: 'center'
                Image:
                    id: imageView
                    source: 'piechart.PNG'
                    allow_stretch: True
                MDLabel:
                    text: "Recyclable Water: 48.7L"
                    halign: 'center'
                    theme_text_color: "Custom"
                    text_color: 1, 0.7, 0, 1
            

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Water Goals'
            icon: '3.png'

            #Third Tab
            BoxLayout:
                orientation: "vertical"
                Image:
                    id: imageView
                    source: 'bar.PNG'
                    allow_stretch: False
'''

#Main App class
class App(MDApp):
    def build(self):
        screen = Builder.load_string(KV)
        # Names of standard color themes.
        return screen

#Running App
App().run()