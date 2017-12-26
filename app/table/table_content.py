from kivy.base import Builder

from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.textinput import TextInput

from settings import CELL_SIZE

Builder.load_string("""
<EditableCell>:
    multiline: True
    size_hint_x: None
    size_hint_y: None
""")


class EditableCell(TextInput):
    row_index = NumericProperty()
    col_index = NumericProperty()


class TableContentView(GridLayout):
    data_helper = ObjectProperty()

    def __init__(self, **kwargs):
        super(TableContentView, self).__init__(**kwargs)

        self.redraw()

    def redraw(self):
        data = self.data_helper.data
        for row_index, row_value in enumerate(data):
            for col_index, cell_value in enumerate(row_value):
                cell = EditableCell(text=cell_value, index=row_index, col_index=col_index, size=CELL_SIZE)
                self.add_widget(cell)
