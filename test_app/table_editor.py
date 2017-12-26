from kivy.app import App
from kivy.base import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from table_view import TableViewSingleton, TableScrollView


Builder.load_string("""
<EditableCell>:
    multiline: True

<ColHeader>:
    bold: True

<RowHeader>:
    background_down: self.background_normal

<TableRowView>:
    width: 1000
    orientation: 'horizontal'

<TableViewSingleton>:
    id: table
    width: 1000
    height: 1000
    orientation: 'vertical'
    size_hint_x: None
    size_hint_y: None
    


<TableEditor>:
    orientation: 'vertical'


<TableEditorTopPanel>:
    InsertRowButton:
        text: 'add row'
    
    InsertColButton:
        text: 'add col'

<HeaderTableRowView>:
    size_hint_y: None
    orientation: 'horizontal'

""")


class InsertButton(Button):
    pass


class InsertRowButton(InsertButton):
    def on_press(self):
        TableViewSingleton().insert_empty_row()


class InsertColButton(InsertButton):
    def on_press(self):
        TableViewSingleton().insert_empty_col()


class TableEditorTopPanel(BoxLayout):
    pass


class TableEditor(BoxLayout):
    def __init__(self, **kwargs):
        super(TableEditor, self).__init__(**kwargs)
        box_layout = TableEditorTopPanel(width=200, height=50, size_hint_x=None, size_hint_y=None)
        table_scroll_view = TableScrollView()

        self.add_widget(box_layout)
        self.add_widget(table_scroll_view)


class TableEditorApp(App):
    def build(self):
        return TableEditor()


if __name__ == '__main__':
    TableEditorApp().run()
