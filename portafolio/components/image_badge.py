import reflex as rx

from portafolio.styles.styles import EmSize


def image_badge(icon: str) -> rx.Component:
    return rx.badge(
        rx.image(
            src=icon,
            height="32px",
            width="32px"
        ),
        aspect_ratio="1",
        variant="soft"
    )