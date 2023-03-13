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

        # TODO: implement viewport and window objects

        self.batch = pyglet.graphics.Batch()
        self.__zoom = 10
        self.button_zoom_in = TextButton(parent=self, label='Zoom+', width=90, y=WINDOW_HEIGHT -
                                         GUI_PADDING, x=GUI_PADDING + 80, height=GUI_BUTTON_HEIGHT, on_press=self.__zoom_in)
        self.button_zoom_out = TextButton(parent=self, label='Zoom-', width=90, y=WINDOW_HEIGHT - GUI_PADDING,
                                          x=GUI_PADDING + 80 + 90 + GUI_PADDING, height=GUI_BUTTON_HEIGHT, on_press=self.__zoom_out)
        self.zoom_label = pyglet.text.Label('Zoom = {0}'.format(self.__zoom), color=(
            0, 0, 0, 255), x=GUI_PADDING, y=WINDOW_HEIGHT - GUI_PADDING, batch=self.batch)
        self.move_up_button = TextButton(parent=self, label='Cima', width=64, y=WINDOW_HEIGHT -
                                         3*GUI_PADDING, x=3*GUI_PADDING, height=GUI_BUTTON_HEIGHT, on_press=self.move_up)
        self.move_left_button = TextButton(parent=self, label='Esquerda', width=64, y=WINDOW_HEIGHT -
                                           4.5*GUI_PADDING, x=GUI_PADDING, height=GUI_BUTTON_HEIGHT, on_press=self.move_left)
        self.move_right_button = TextButton(parent=self, label='Direita', width=64, y=WINDOW_HEIGHT -
                                            4.5*GUI_PADDING, x=5*GUI_PADDING, height=GUI_BUTTON_HEIGHT, on_press=self.move_right)
        self.move_down_button = TextButton(parent=self, label='Baixo', width=64, y=WINDOW_HEIGHT -
                                           6*GUI_PADDING, x=3*GUI_PADDING, height=GUI_BUTTON_HEIGHT, on_press=self.move_down)
        self.widgets = [
            self.button_zoom_in,
            self.button_zoom_out,
            self.move_down_button,
            self.move_up_button,
            self.move_left_button,
            self.move_right_button
        ]
        self.focus = None

    def move_up(self):
        # TODO: implement actual moving of window
        print('Moving up')

    def move_down(self):
        # TODO: implement actual moving of window
        print('Moving down')

    def move_right(self):
        # TODO: implement actual moving of window
        print('Moving right')

    def move_left(self):
        # TODO: implement actual moving of window
        print('Moving left')

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
