from kivy.app import App
from kivy.base import Builder
from kivy.properties import ListProperty, ObjectProperty

from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

Builder.load_string("""
<EditableCell>:
    multiline: True

<TableRowView>:
    width: 1000
    orientation: 'horizontal'

<TableView>:
    id: table
    width: 1000
    height: 1000
    orientation: 'vertical'
    size_hint_x: None
    size_hint_y: None
    


<TableEditor>:
    orientation: 'vertical'


<TableEditorTopPanel>:
    InsertRowButton:
        text: 'add row'
    
    InsertColButton:
        text: 'add col'
    
""")


class EditableCell(TextInput):
    pass


class InsertButton(Button):
    pass


class InsertRowButton(InsertButton):
    def on_press(self):
        TableView().insert_empty_row()


class InsertColButton(InsertButton):
    def on_press(self):
        TableView().insert_empty_col()


class TableEditorTopPanel(BoxLayout):
    pass


class TableEditor(BoxLayout):
    def __init__(self, **kwargs):
        super(TableEditor, self).__init__(**kwargs)
        box_layout = TableEditorTopPanel(width=200, height=50, size_hint_x=None, size_hint_y=None)
        table_scroll_view = TableScrollView()

        self.add_widget(box_layout)
        self.add_widget(table_scroll_view)


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


class TableView(BoxLayout):
    table_data = ListProperty()
    __instance = None

    def __new__(cls, *args, **kwargs):
        if TableView.__instance is None:
            TableView.__instance = super(TableView, cls).__new__(cls, *args, **kwargs)
        return TableView.__instance

    def __init__(self, **kwargs):
        super(TableView, self).__init__(**kwargs)
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
        table_layout = TableView(table_data=data)
        self.add_widget(table_layout)


class TableEditorApp(App):
    def build(self):
        return TableEditor()


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
