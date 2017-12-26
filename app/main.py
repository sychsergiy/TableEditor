from kivy.app import App
from kivy.uix.label import Label

from table.scroll_view import TableScrollView
from helper import MatrixHelper


class TableEditorApp(App):
    def build(self):
        data = mock_data()
        data_helper = MatrixHelper(data)
        return TableScrollView(data_helper=data_helper)


def mock_data():
    data = [
        ['123some text' * 2, ] * 5 + ['1', '2'],
        ['text' * 3,] * 3,
        ['some text' * 2, ] * 4 + ['3', '4'],
        ['some text' * 2, ] * 6,
        ['some text' * 2, ] * 6,
    ]
    return data


if __name__ == '__main__':
    TableEditorApp().run()
