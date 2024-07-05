import reflex as rx
from portafolio.components.icon_button import icon_button
from portafolio.data import Media
from portafolio.styles.styles import Size


def media(data: Media) -> rx.Component:
    return rx.flex(
        icon_button(
            "mail",
            f"mailto:{data.email}",
            data.email,
            True
        ),
        icon_button(
            "phone",
            f"tel:{data.tel}",
            data.tel,
            True
        ),
        rx.hstack(
            icon_button(
                "file-text",
                data.cv
            ),
            spacing=Size.SMALL.value
        ),
        spacing=Size.SMALL.value,
        flex_direction=["column", "column", "row"]
    )
