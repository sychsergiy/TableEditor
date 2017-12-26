from kivy.base import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import NumericProperty

Builder.load_string("""
<ToggleModeButton>:
    size_hint_x: None
    size_hint_y: None
    width: 40
    height: 40

<TopHeader>:
    size_hint_y: None
    height: 40

<LeftHeader>:
    size_hint_x: None
    width: 40
""")


class ToggleModeButton(ToggleButton):
    pass


class TopHeader(BoxLayout):
    index = NumericProperty()


class LeftHeader(BoxLayout):
    index = NumericProperty()
