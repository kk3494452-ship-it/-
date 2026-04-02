from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        # هذا الزر سيظهر في وسط شاشة جوالك عند تشغيل التطبيق
        return Button(text='مرحباً بك في تطبيقي الأول!\nاضغط هنا', 
                      background_color=(0, 0.5, 1, 1),
                      font_size='20sp')

if __name__ == '__main__':
    MyApp().run()
