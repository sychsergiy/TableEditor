from kivy.base import Builder

from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

from settings import CELL_SIZE

from .table_content import TableContentView

Builder.load_string("""
<TableView>:
    cols: 1
    rows: 1
    size_hint_x: None
    size_hint_y: None
    # todo: add headers and align button
""")


class TableScrollView(ScrollView):
    """
    view for scrolling table_view
    """
    data_helper = ObjectProperty()

    def __init__(self, **kwargs):
        super(TableScrollView, self).__init__(**kwargs)
        table = TableView(data_helper=self.data_helper, size=self.get_table_size())
        self.add_widget(table)

    def get_table_size(self):
        cols_n = self.data_helper.get_cols_n()
        rows_n = self.data_helper.get_rows_n()
        return cols_n * CELL_SIZE[0], rows_n*CELL_SIZE[1]


class TableView(GridLayout):
    """
    4*4 view which include:
        1) align button (redact, not_redact)
        2) top header
        3) left header
        4) table content
    """
    data_helper = ObjectProperty()

    def __init__(self, **kwargs):
        super(TableView, self).__init__(**kwargs)
        self.bind(minimum_width=self.setter('width'))
        self.bind(minimum_width=self.setter('height'))

        options = {
            'data_helper': self.data_helper,
            'cols': self.data_helper.get_cols_n(),
            'rows': self.data_helper.get_rows_n(),
        }
        # todo: add width and height computing
        table_content = TableContentView(**options)
        self.add_widget(table_content)


