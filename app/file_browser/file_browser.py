import os

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from helper import DataHelper

from .dialogs import LoadDialog, SaveDialog


class FileBrowser(FloatLayout):
    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        try:
            with open(os.path.join(path, filename[0])) as stream:
                data_helper = DataHelper(stream.read())
                self.scroll_view.set_data_helper(data_helper)
            self.dismiss_popup()
        except:
            self.error_popup('Something went wrong.\nCan not load selected file')

    def save(self, path, filename):
        try:
            with open(os.path.join(path, filename), 'w') as stream:
                for row in self.scroll_view.data_helper.data:
                    for cell in row:
                        stream.write('{}\t'.format(cell))
                    stream.write('\n')
                stream.write('\n')
            self.dismiss_popup()
        except:
            self.error_popup('Something went wrong.\nCan not save file')

    @staticmethod
    def error_popup(message):
        error_label = Label(text=message)
        popup = Popup(title="Load file", content=error_label,
                      size_hint=(0.4, 0.4))
        popup.open()
