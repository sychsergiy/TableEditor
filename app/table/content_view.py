from kivy.properties import ObjectProperty, NumericProperty, BooleanProperty

from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

from settings import CELL_SIZE


class EditableCell(TextInput):
    data_helper = ObjectProperty()
    row_index = NumericProperty()
    col_index = NumericProperty()

    def __init__(self, **kwargs):
        super(EditableCell, self).__init__(**kwargs)

        def on_text(instance, value):
            instance.data_helper.update_cell(value, instance.row_index, instance.col_index)

        self.bind(text=on_text)


class TableContentView(GridLayout):
    data_helper = ObjectProperty()
    read_only_mode = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(TableContentView, self).__init__(**kwargs)
        self.redraw()

    def redraw(self):
        self.clear_widgets()
        self.draw_cells()

    def draw_cells(self):
        for row_index, row_value in enumerate(self.data_helper.data):
            for col_index, cell_value in enumerate(row_value):
                cell = EditableCell(text=cell_value, row_index=row_index, col_index=col_index, size=CELL_SIZE,
                                    data_helper=self.data_helper, readonly=self.read_only_mode)
                self.add_widget(cell)

    def sort_by_column(self, index, reverse=False):
        self.data_helper.sort_by_column(index, reverse=reverse)
        self.redraw()

    def toggle_mode(self):
        self.read_only_mode = not self.read_only_mode
        self.redraw()
