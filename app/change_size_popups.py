import re

from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput


class IntInput(TextInput):
    pat = re.compile('[0-9]')

    def insert_text(self, substring, from_undo=False):
        if re.match(self.pat, substring):
            return super(IntInput, self).insert_text(substring, from_undo=from_undo)


class ChangeTableSizeDialog(GridLayout):
    accept = ObjectProperty(None)
    cancel = ObjectProperty(None)


class TableSizeManager(FloatLayout):
    scroll_view = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_add_rows_dialog(self):
        content = ChangeTableSizeDialog(accept=self.insert_rows, cancel=self.dismiss_popup)
        self._popup = Popup(title='Add rows', content=content, size_hint=(.5, .5))
        self._popup.open()

    def show_add_cols_dialog(self):
        content = ChangeTableSizeDialog(accept=self.insert_cols, cancel=self.dismiss_popup)
        self._popup = Popup(title='Add cols', content=content, size_hint=(.5, .5))
        self._popup.open()

    def insert_rows(self, str_n, str_begin_index):
        n, begin_index = self.validate_input(str_n, str_begin_index)
        self.scroll_view.insert_empty_rows(int(n), int(begin_index))
        self._popup.dismiss()

    def insert_cols(self, str_n, str_begin_index):
        n, begin_index = self.validate_input(str_n, str_begin_index)
        self.scroll_view.insert_empty_cols(n, begin_index)
        self._popup.dismiss()

    @staticmethod
    def validate_input(str_n, str_begin_index):
        if str_n == '':
            str_n = 0
        if str_begin_index == '':
            str_begin_index = 0

        return int(str_n), int(str_begin_index)

