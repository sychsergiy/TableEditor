from kivy.base import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.properties import NumericProperty, ObjectProperty

Builder.load_string("""
<ToggleModeButton>:
    size_hint_x: None
    size_hint_y: None

<TopHeaderView>:
    size_hint_y: None

<LeftHeaderView>:
    orientation: 'vertical'
    size_hint_x: None
""")


# todo: on_press LeftHeaderButton sort with asc and desc

class ToggleModeButton(ToggleButton):
    pass


class TopHeaderButton(Button):
    index = NumericProperty()

    def on_press(self):
        table = self.get_content_view()
        table.sort_by_column(self.index)

    def get_content_view(self):
        return self.parent.table


class LeftHeaderButton(Button):
    index = NumericProperty()


class TopHeaderView(BoxLayout):
    length = NumericProperty()
    table = ObjectProperty()

    def __init__(self, **kwargs):
        super(TopHeaderView, self).__init__(**kwargs)

        for i in range(self.length):
            cell = TopHeaderButton(text=str(i + 1), index=i)
            self.add_widget(cell)


class LeftHeaderView(BoxLayout):
    length = NumericProperty()

    def __init__(self, **kwargs):
        super(LeftHeaderView, self).__init__(**kwargs)

        for i in range(self.length):
            cell = LeftHeaderButton(text=str(i + 1), index=i)
            self.add_widget(cell)
