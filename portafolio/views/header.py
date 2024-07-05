import reflex as rx
from portafolio.components.heading import heading
from portafolio.components.media import media
from portafolio.data import Data
from portafolio.styles.styles import Size


def header(data: Data) -> rx.Component:
    return rx.hstack(
        rx.vstack(
            heading(data.name, True),
            heading(data.skill),
            rx.text(
                rx.icon("map-pin"),
                data.location,
                display="inherit"
            ),
            media(data.media),
            spacing=Size.SMALL.value,
            border_width="3px",
            padding="1em",
        ),
        rx.avatar(
            src=data.avatar,
            size=Size.BIG.value,
            height="150px",
        ),
        spacing=Size.DEFAULT.value,
    )
