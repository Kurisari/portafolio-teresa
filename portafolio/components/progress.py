import reflex as rx
from portafolio.data import Skills
from portafolio.styles.styles import Size

def progress(data: Skills) -> rx.Component:
    return rx.box(
        rx.text(data.title),
        rx.progress(value=data.percentage),
        width="100%",
        spacing=Size.SMALL.value
    )