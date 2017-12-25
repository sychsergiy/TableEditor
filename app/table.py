from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, NumericProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from settings import HEADER_COL_WIDTH, HEADER_ROW_HEIGHT


class RowHeaderCell(Button):
    pass


class ColHeaderCell(Button):
    pass


class EditableCell(TextInput):
    pass


class TableRowView(BoxLayout):
    row_data = ListProperty()
    index = NumericProperty()

    def __init__(self, **kwargs):
        super(TableRowView, self).__init__(**kwargs)
        header_cell = ColHeaderCell(text=str(self.index + 1), size_hint_x=None, width=HEADER_COL_WIDTH)
        self.add_widget(header_cell)
        for value in self.row_data:
            self.insert_cell(value)

    def insert_cell(self, value):
        cell = EditableCell(text=value)
        self.add_widget(cell)

    def get_row_data(self):
        return [cell.text for cell in self.children if isinstance(cell, EditableCell)]


class TableViewSingleton(BoxLayout):
    table_data = ListProperty()
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self, **kwargs):
        super(TableViewSingleton, self).__init__(**kwargs)
        self.bind(minimum_width=self.setter('width'))
        self.bind(minimum_width=self.setter('height'))

        self.table_data = self.normalize_data(self.table_data)

        self.redraw()

    def redraw(self):
        self.clear_widgets()
        self.add_header_row()

        for index, row_value in enumerate(self.table_data):
            self.insert_row(row_value, index)

    def add_header_row(self):
        header_row = BoxLayout(orientation='horizontal', height=HEADER_ROW_HEIGHT, size_hint_y=None, )

        cols_n = self.get_cols_n()
        header_cell = ColHeaderCell(size=(HEADER_COL_WIDTH, HEADER_ROW_HEIGHT), size_hint_y=None, size_hint_x=None)
        header_row.add_widget(header_cell)  # square 40*40 for align header row

        for i in range(1, cols_n + 1):
            header_row.add_widget(RowHeaderCell(text='{}'.format(i)))
        self.add_widget(header_row)

    def insert_row(self, row_data, index):
        table_row = TableRowView(row_data=row_data, index=index)
        self.add_widget(table_row)

    def get_table_data(self):
        return [row.get_row_data() for row in self.children if isinstance(row, TableRowView)]

    def insert_empty_row(self):
        cells_n = len(self.table_data[0])
        self.table_data.append([''] * cells_n if cells_n else [''])
        self.redraw()

    def insert_empty_col(self):
        for row in self.table_data:
            row.append('')
        self.redraw()

    def get_cols_n(self):
        return len(self.table_data[0])

    def get_rows_n(self):
        return len(self.table_data)

    @staticmethod
    def normalize_data(data):
        cols_n = max((len(row) for row in data))
        for row in data:
            while len(row) < cols_n:
                row.append('')
        return data


class TableScrollView(ScrollView):
    def __init__(self, **kwargs):
        super(TableScrollView, self).__init__(**kwargs)
        data = mock_data()
        table_layout = TableViewSingleton(table_data=data)
        self.add_widget(table_layout)


def mock_data():
    data = [
        ['some text' * 2, ] * 5,
        ['some text' * 3, ] * 3,
        ['some text' * 2, ] * 4,
        ['some text' * 2, ] * 6,
        ['some text' * 2, ] * 6,
    ]
    return data
