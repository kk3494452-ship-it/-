from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text='Welcome to my School App', 
                      background_color=(0, 0.5, 1, 1),
                      font_size='25sp')

if __name__ == '__main__':
    MyApp().run()
    
