from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, NumericProperty, ObjectProperty, BooleanProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from settings import HEADER_COL_WIDTH, HEADER_ROW_HEIGHT


class SelectableButton(Button):
    pressed = BooleanProperty(False)

    def select(self):
        self.background_color = [.25, .25, .6, 1.0]
        self.pressed = True

    def deselect(self):
        self.background_color = [1, 1, 1, 1]
        self.pressed = False


class TopHeaderCell(SelectableButton):
    def on_press(self):
        # todo: not deselect after second click but sort
        table = TableViewSingleton()
        if not self.pressed:
            # select this button if it is not pressed
            # and send it to table with set_selected method
            self.select()
            table.set_selected_col(self)
            table.sort_column_by_ascending(int(self.text) - 1)
        else:
            # deselect this button if it is already pressed
            # and send None to table with set_selected_col method
            self.deselect()
            table.set_selected_col(None)


class LeftHeaderCell(SelectableButton):
    def on_press(self):
        table = TableViewSingleton()
        if not self.pressed:
            self.select()
            table.set_selected_row(self)
        else:
            self.deselect()
            table.set_selected_row(None)


class EditableCell(TextInput):
    pass


class HeaderTableRowView(BoxLayout):
    cols_n = NumericProperty()

    def __init__(self, **kwargs):
        super(HeaderTableRowView, self).__init__(**kwargs)

        header_cell = LeftHeaderCell(size=(HEADER_COL_WIDTH, HEADER_ROW_HEIGHT), size_hint_y=None, size_hint_x=None)
        self.add_widget(header_cell)  # square 40*40 for align header row

        for i in range(1, self.cols_n + 1):
            self.add_widget(TopHeaderCell(text='{}'.format(i)))


class TableRowView(BoxLayout):
    row_data = ListProperty()
    row_index = NumericProperty()

    def __init__(self, **kwargs):
        super(TableRowView, self).__init__(**kwargs)
        header_cell = LeftHeaderCell(text=str(self.row_index + 1), size_hint_x=None, width=HEADER_COL_WIDTH)
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

    selected_col_index = NumericProperty()
    selected_row_index = NumericProperty()

    header_row = ObjectProperty()

    painted = BooleanProperty(False)

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

        # not redraw table when creating new singleton instance
        if not self.painted:
            # save selected row and col


            self.redraw()
            self.painted = True

    def redraw(self):
        self.clear_widgets()

        self.header_row = self.create_header_row()
        self.add_widget(self.header_row)

        for index, row_value in enumerate(self.table_data):
            self.insert_row(row_value, index)

    def create_header_row(self):
        return HeaderTableRowView(cols_n=self.get_cols_n(), height=HEADER_ROW_HEIGHT)

    def insert_row(self, row_data, index):
        table_row = TableRowView(row_data=row_data, row_index=index)
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

    # def set_selected_col_index(self, index):
    #     if self.selected_col:
    #         self.selected_col.deselect()  # set off selected col
    #     self.selected_col = header_cell

    # def set_selected_row_index(self, index):
    #     if self.selected_row:
    #         self.selected_row.deselect()  # set off selected row
    #     self.selected_row = header_cell

    def sort_column_by_ascending(self, index):
        sorted_column = sorted([row[index] for row in self.table_data])
        for row in self.table_data:
            row[index] = sorted_column[index]

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
        ['123some text' * 2, ] * 5,
        ['text' * 3, ] * 3,
        ['some text' * 2, ] * 4,
        ['some text' * 2, ] * 6,
        ['some text' * 2, ] * 6,
    ]
    return data
