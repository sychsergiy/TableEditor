import kivy

from kivy.app import App
from kivy.base import Builder
from kivy.factory import Factory

from file_browser.file_browser import FileBrowser
from table.scroll_view import TableScrollView

kivy.require('1.10.0')

Builder.load_file('file_browser/file_browser.kv')
Builder.load_file('table/table.kv')

Factory.register('FileBrowser', cls=FileBrowser)
Factory.register('TableScrollView', cls=TableScrollView)


class TableEditorApp(App):
    pass


if __name__ == '__main__':
    TableEditorApp().run()
