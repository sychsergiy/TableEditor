from kivy.app import App
from kivy.base import Builder
from kivy.uix.boxlayout import BoxLayout

from table.scroll_view import TableScrollView
from helper import MatrixHelper

from file_browser.file_browser import FileBrowserPanel

Builder.load_file('file_browser/filebrowser.kv')
Builder.load_file('table/table.kv')


class TableEditorApp(App):
    def build(self):
        data = mock_data()
        data_helper = MatrixHelper(data)

        container = BoxLayout(orientation='vertical')

        container.add_widget(FileBrowserPanel())
        container.add_widget(TableScrollView(data_helper=data_helper))

        return container


def mock_data():
    data = [
        ['123some text' * 2, ] * 5 + ['1', '2'],
        ['text' * 3, ] * 3,
        ['some text' * 2, ] * 4 + ['3', '4'],
        ['some text' * 2, ] * 6,
        ['some text' * 2, ] * 6,
    ]
    return data


if __name__ == '__main__':
    TableEditorApp().run()
