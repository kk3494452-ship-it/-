from kivy.app import App
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        return Label(text='Al-Hajr School App\nStatus: Online')

if __name__ == '__main__':
    TestApp().run()
  
