from kivy.config import Config
# Set screen size for desktop testing (simulating a phone)
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Load the KV file
Builder.load_file("calculator.kv")

class CalculatorLayout(BoxLayout):
    def calculate(self, expression):
        try:
            self.ids.result.text = str(eval(expression))
        except:
            self.ids.result.text = "Error"

class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()

if __name__ == "__main__":
    CalculatorApp().run()
