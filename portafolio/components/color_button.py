import reflex as rx
from reflex.style import toggle_color_mode

def color_button():
    return rx.button(
        rx.color_mode_cond(rx.icon("moon", size=32), rx.icon("sun", size=32)),
        on_click=toggle_color_mode,
        variant="soft",
        size="3",
        padding="0.5em",
    )