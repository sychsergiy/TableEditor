from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput


class EditableCell(TextInput):
    pass


class TableRowView(BoxLayout):
    row_data = ListProperty()

    def __init__(self, **kwargs):
        super(TableRowView, self).__init__(**kwargs)

        for value in self.row_data:
            self.insert_cell(value)

    def insert_cell(self, value):
        cell = EditableCell(text=value)
        self.add_widget(cell)

    def get_row_data(self):
        return [cell.text for cell in self.children]


class TableViewSingleton(BoxLayout):
    table_data = ListProperty()
    __instance = None

    def __new__(cls, *args, **kwargs):
        if TableViewSingleton.__instance is None:
            TableViewSingleton.__instance = super(TableViewSingleton, cls).__new__(cls, *args, **kwargs)
        return TableViewSingleton.__instance

    def __init__(self, **kwargs):
        super(TableViewSingleton, self).__init__(**kwargs)
        self.bind(minimum_width=self.setter('width'))
        self.bind(minimum_width=self.setter('height'))

        self.table_data = self.normalize_data(self.table_data)

        self.redraw()

    def redraw(self):
        self.clear_widgets()
        for row_value in self.table_data:
            self.insert_row(row_value)

    def insert_row(self, row_data):
        table_row = TableRowView(row_data=row_data)
        self.add_widget(table_row)

    def get_table_data(self):
        return [row.get_row_data() for row in self.children]

    def insert_empty_row(self):
        cells_n = len(self.table_data[0])
        self.table_data.append([''] * cells_n if cells_n else [''])
        self.redraw()

    def insert_empty_col(self):
        for row in self.table_data:
            row.append('')
        self.redraw()

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
