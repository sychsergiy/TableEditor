import kivy

from kivy.app import App
from kivy.base import Builder
from kivy.factory import Factory

from file_browser.manager import FileBrowserManager
from table.scroll_view import TableScrollView
from table.size_manager import TableSizeManager

kivy.require('1.10.0')

Builder.load_file('file_browser/dialogs.kv')
Builder.load_file('table/table.kv')

Factory.register('FileBrowserManager', cls=FileBrowserManager)
Factory.register('TableScrollView', cls=TableScrollView)
Factory.register('TableSizeManager', cls=TableSizeManager)


class TableEditorApp(App):
    pass
