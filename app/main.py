import kivy

from kivy.app import App
from kivy.base import Builder
from kivy.factory import Factory

from file_browser.file_browser import FileBrowserManager
from table.scroll_view import TableScrollView
from change_size_popups import TableSizeManager

kivy.require('1.10.0')

Builder.load_file('file_browser/dialogs.kv')
Builder.load_file('table/table.kv')

Factory.register('FileBrowserManager', cls=FileBrowserManager)
Factory.register('TableSizeManager', cls=TableSizeManager)
Factory.register('TableScrollView', cls=TableScrollView)


class TableEditorApp(App):
    pass


if __name__ == '__main__':
    TableEditorApp().run()
