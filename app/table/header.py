from kivy.base import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.properties import NumericProperty, ObjectProperty, BooleanProperty

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


class ToggleModeButton(ToggleButton):
    pass


class TopHeaderButton(Button):
    index = NumericProperty()
    selected = BooleanProperty(False)
    selected_twice = BooleanProperty(False)

    def on_press(self):
        table = self.parent.table

        if self.selected_twice:
            self.deselect()
        elif self.selected:
            self.second_select()
            table.sort_by_column(self.index)
        else:
            self.select()
            table.sort_by_column(self.index, reverse=True)

    def second_select(self):
        self.selected = False
        self.selected_twice = True

    def select(self):
        self.parent.set_selected_cell(self)
        self.selected = True
        self.background_color = [.25, .25, .6, 1.0]

    def deselect(self):
        self.selected_twice = False
        self.selected = False
        self.background_color = [1, 1, 1, 1]


class LeftHeaderButton(Button):
    index = NumericProperty()


class TopHeaderView(BoxLayout):
    length = NumericProperty()
    table = ObjectProperty(None)
    selected_cell = ObjectProperty(None, allownone=True)

    def __init__(self, **kwargs):
        super(TopHeaderView, self).__init__(**kwargs)

        for i in range(self.length):
            cell = TopHeaderButton(text=str(i + 1), index=i)
            self.add_widget(cell)

    def set_selected_cell(self, cell):
        if self.selected_cell and self.selected_cell is not cell:
            self.selected_cell.deselect()
        self.selected_cell = cell


class LeftHeaderView(BoxLayout):
    length = NumericProperty()

    def __init__(self, **kwargs):
        super(LeftHeaderView, self).__init__(**kwargs)

        for i in range(self.length):
            cell = LeftHeaderButton(text=str(i + 1), index=i)
            self.add_widget(cell)
