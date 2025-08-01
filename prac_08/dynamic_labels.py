from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

NEW_COLOUR = (1, 0, 0, 1)
ANOTHER_COLOUR = (1, 0, 1, 1)

class DynamicLabelsApp(App):
    """Dynamic labels app"""

    def __init__(self, **kwargs):
        """Construct main app"""
        super().__init__(**kwargs)
        # data - names
        self.names = ['Josh', 'Bobby', 'Ronald', 'Molly', 'Benson']

    def build(self):
        """GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in self.names:
            self.root.ids.main.add_widget(Label(text=name))
        return self.root

DynamicLabelsApp().run()