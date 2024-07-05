import reflex as rx
from portafolio.components.progress import progress
from portafolio.components.heading import heading
from portafolio.data import Skills
from portafolio.styles.styles import Size

def skills(title: str, data: list[Skills]) -> rx.Component:
    return rx.vstack(
        heading(title),
        rx.vstack(
            *[
                progress(item)
                for item in data
            ],
            spacing=Size.DEFAULT.value,
            width="100%"
        ),
        spacing=Size.DEFAULT.value,
        width="100%"
    )
