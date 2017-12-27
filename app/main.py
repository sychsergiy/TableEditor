import kivy

from kivy.app import App
from kivy.base import Builder

kivy.require('1.10.0')

Builder.load_file('file_browser/file_browser.kv')
Builder.load_file('table/table.kv')


class TableEditorApp(App):
    pass


if __name__ == '__main__':
    TableEditorApp().run()
