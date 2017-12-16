from kivy.app import App
from kivy.base import Builder
from kivy.properties import ListProperty

from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

Builder.load_string("""
<EditableCell>:
    multiline: True

<TableRowView>:
    width: 1000
    orientation: 'horizontal'

<TableView>:
    width: 1000
    height: 1000
    orientation: 'vertical'
""")


class EditableCell(TextInput):
    pass


class TableRowView(BoxLayout):
    initial_row_value = ListProperty()  # list of strings
    cells = ListProperty()  # list of EditableCell instances

    def __init__(self, **kwargs):
        super(TableRowView, self).__init__(**kwargs)

        for value in self.initial_row_value:
            self.insert_cell(value=value)

    def insert_cell(self, value=''):
        cell = EditableCell(text=value)
        self.cells.append(cell)
        self.add_widget(cell)

    def get_row_data(self):
        return [cell.text for cell in self.cells]


class TableView(BoxLayout):
    initial_data = ListProperty()  # list of list of strings
    rows = ListProperty()  # list of TableRowView instances

    def __init__(self, **kwargs):
        super(TableView, self).__init__(**kwargs)
        self.initial_data = self.normalize_data(self.initial_data)
        for row_value in self.initial_data:
            self.insert_row(row_value=row_value)

    def insert_row(self, row_value):
        table_row = TableRowView(initial_row_value=row_value)
        self.add_widget(table_row)
        self.rows.append(table_row)

    def get_table_data(self):
        return [row.get_row_data() for row in self.rows]

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
        table_layout = TableView(size_hint_x=None, size_hint_y=None, initial_data=data)
        table_layout.bind(minimum_width=table_layout.setter('width'))
        table_layout.bind(minimum_width=table_layout.setter('height'))

        self.add_widget(table_layout)


class TableEditorApp(App):
    def build(self):
        return TableScrollView()


def mock_data():
    data = [
        ['some text' * 2, ] * 5,
        ['some text' * 3, ] * 3,
        ['some text' * 2, ] * 4,
        ['some text' * 2, ] * 6,
        ['some text' * 2, ] * 6,
    ]
    return data


if __name__ == '__main__':
    TableEditorApp().run()
