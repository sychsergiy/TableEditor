from kivy.properties import ObjectProperty

from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

from settings import CELL_SIZE, HEADER_SIZE

from .content_view import TableContentView
from .header import ToggleModeButton, TopHeaderView, LeftHeaderView


class TableScrollView(ScrollView):
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
    data_helper = ObjectProperty()

    def __init__(self, **kwargs):
        super(TableView, self).__init__(**kwargs)
        cols_n = self.data_helper.get_cols_n()
        rows_n = self.data_helper.get_rows_n()
        options = {
            'data_helper': self.data_helper,
            'cols': cols_n,
            'rows': rows_n,
        }
        content_view = TableContentView(**options)

        self.add_widget(ToggleModeButton(size=(HEADER_SIZE, HEADER_SIZE), table=content_view))

        self.add_widget(TopHeaderView(length=cols_n, height=HEADER_SIZE, table=content_view))

        self.add_widget(LeftHeaderView(length=rows_n, width=HEADER_SIZE))

        self.add_widget(content_view)
