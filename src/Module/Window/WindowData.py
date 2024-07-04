from Module.Window.layout import *
from Module.Vector2.Vector2 import Vector2


class WindowData:
    layout = MainLayout
    window: sg.Window
    size: Vector2 = Vector2(640, 720)
    _event: any
    _value: any

    def Initialize(self) -> None:
        self.window = sg.Window("title", WindowData.layout, size=self.size.get())
        pass

    def read(self) -> None:
        self._event, self._value = self.window.read()

    def close(self) -> None:
        self.window.close()

    def isEvent(self, key) -> bool:
        return self._event == key

    def getValue(self, key):
        return self._value[key]

    def setValue(self, key, value):
        self.window[key].update(value)
