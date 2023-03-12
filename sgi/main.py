import pyglet
from widgets.text import TextWidget
from widgets.button import Button
from widgets.text_button import TextButton


WINDOW_HEIGHT = 640
WINDOW_WIDTH = 1200

GUI_WIDTH = 400
GUI_HEIGHT = 40
GUI_PADDING = 32
GUI_BUTTON_HEIGHT = 16


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(WINDOW_WIDTH,
                                     WINDOW_HEIGHT, caption='SGI', *args, **kwargs)

        self.batch = pyglet.graphics.Batch()
        self.__zoom = 10
        self.button_zoom_in = self.__create_button_zoom_in()
        self.button_zoom_out = self.__create_button_zoom_out()
        self.zoom_label = pyglet.text.Label('Zoom = {0}'.format(self.__zoom), color=(
            0, 0, 0, 255), x=GUI_PADDING, y=WINDOW_HEIGHT - GUI_PADDING, batch=self.batch)
        self.widgets = [
            self.button_zoom_in,
            self.button_zoom_out
        ]
        self.focus = None

    def __create_button_zoom_in(self):
        button = TextButton(self)
        button.text = 'Zoom+'
        button.width = 90
        button.y = WINDOW_HEIGHT - GUI_PADDING
        button.x = GUI_PADDING + 80
        button.height = GUI_BUTTON_HEIGHT
        button.on_press = self.__zoom_in
        return button

    def __create_button_zoom_out(self):
        button = TextButton(self)
        button.text = 'Zoom-'
        button.width = 90
        button.y = WINDOW_HEIGHT - GUI_PADDING
        button.x = GUI_PADDING + 80 + 90 + GUI_PADDING
        button.height = GUI_BUTTON_HEIGHT
        button.on_press = self.__zoom_out
        return button

    def zoom(self, value):
        self.__zoom += value
        self.zoom_label.text = 'Zoom = {0}'.format(self.__zoom)
        self.batch.draw()

    def __zoom_in(self):
        self.zoom(5)
    
    def __zoom_out(self):
        self.zoom(-5)

    def on_draw(self):
        pyglet.gl.glClearColor(1, 1, 1, 1)
        self.clear()
        for widget in self.widgets:
            widget.draw()
        self.batch.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        for widget in self.widgets:
            if widget.hit_test(x, y):
                widget.on_mouse_press(x, y, button, modifiers)
                break
        else:
            self.set_focus(None)

        if self.focus:
            self.focus.caret.on_mouse_press(x, y, button, modifiers)

    # def on_text(self, text):
    #     if self.focus:
    #         self.focus.caret.on_text(text)

    # def on_text_motion(self, motion):
    #     if self.focus:
    #         self.focus.caret.on_text_motion(motion)

    def set_focus(self, focus):
        if focus is self.focus:
            return

        if self.focus:
            self.focus.caret.visible = False
            self.focus.caret.mark = self.focus.caret.position = 0

        self.focus = focus
        if self.focus:
            self.focus.caret.visible = True


window = Window()
pyglet.app.run()
