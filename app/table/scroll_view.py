from kivy.base import Builder

from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

from settings import CELL_SIZE, HEADER_SIZE

from .content_view import TableContentView

from .header import ToggleModeButton, TopHeader, LeftHeader

Builder.load_string("""
<TableView>:
    cols: 2
    rows: 2
    size_hint_x: None
    size_hint_y: None
""")


class TableScrollView(ScrollView):
    """
    view for scrolling table_view
    """
    data_helper = ObjectProperty()

    def __init__(self, **kwargs):
        super(TableScrollView, self).__init__(**kwargs)
        table = TableView(data_helper=self.data_helper, size=self.get_table_content_size())
        self.add_widget(table)

    def get_table_content_size(self):
        cols_n = self.data_helper.get_cols_n()
        rows_n = self.data_helper.get_rows_n()
        return cols_n * CELL_SIZE[0] + HEADER_SIZE, rows_n * CELL_SIZE[1] + HEADER_SIZE


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
        options = {
            'data_helper': self.data_helper,
            'cols': self.data_helper.get_cols_n(),
            'rows': self.data_helper.get_rows_n(),
        }
        table_content = TableContentView(**options)
        self.add_widget(ToggleModeButton())

        self.add_widget(TopHeader())

        self.add_widget(LeftHeader())

        self.add_widget(table_content)
