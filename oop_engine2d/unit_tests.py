from oop_engine2d.engine import Engine2D
from oop_engine2d.figures import *


def test_init_buttons_method():
    engine = Engine2D()
    engine.init_buttons()
    assert len(engine.buttons) == 5, "Buttons weren't initiated"


def test_button_recolor_method():
    engine = Engine2D()
    engine.button_recolor(engine.colors[0])
    prev_color = engine.current_color
    engine.button_recolor(engine.colors[1])
    new_color = engine.current_color
    assert new_color != prev_color, "Color hasn't been changed"


def test_add_triangle():
    engine = Engine2D()
    engine.button_add_triangle()
    assert type(engine.draw_queue.get()) is Triangle


def test_add_rectangle():
    engine = Engine2D()
    engine.button_add_rectangle()
    assert type(engine.draw_queue.get()) is Rectangle


def test_add_circle():
    engine = Engine2D()
    engine.button_add_circle()
    assert type(engine.draw_queue.get()) is Circle


def test_set_button_state_method():
    engine = Engine2D()
    engine.init_buttons()
    engine.set_buttons_state('active')
    for button in engine.buttons:
        assert button['state'] == 'active'
    engine.set_buttons_state('disabled')
    for button in engine.buttons:
        assert button['state'] == 'disabled'


def test_write_figure_name_method():
    engine = Engine2D()
    test_figure_name = 'test_figure_name_' + str(random.randrange(0, 100000))
    engine.write_figure_name(test_figure_name)
    item_found = False
    for item in engine.canvas.find_all():
        item_value = engine.canvas.itemcget(item, 'text')
        if item_value == test_figure_name:
            item_found = True
    assert item_found is True, "Figure name hasn't been added to canvas"
