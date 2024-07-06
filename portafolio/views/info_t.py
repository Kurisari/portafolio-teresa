import reflex as rx

from portafolio.components.heading import heading
from portafolio.components.info_training import info_detail
from portafolio.data import Info
from portafolio.styles.styles import Size


def info_t(title: str, info: list[Info]) -> rx.Component:
    return rx.vstack(
        heading(title),
        rx.vstack(
            *[
                info_detail(item)
                for item in info
            ],
            spacing=Size.DEFAULT.value,
            width="100%",
            border_width="3px",
            padding="1em",
            # background_color="#53B7F520"
        ),
        spacing=Size.DEFAULT.value,
        width="100%"
    )
