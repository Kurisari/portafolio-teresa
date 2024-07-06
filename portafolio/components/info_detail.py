import reflex as rx
from portafolio.components.icon_badge import icon_badge
from portafolio.components.icon_button import icon_button
from portafolio.components.image_badge import image_badge
from portafolio.data import Info
from portafolio.styles.styles import IMAGE_HEIGHT, EmSize, Size


def info_detail(info: Info) -> rx.Component:
    return rx.flex(
        rx.hstack(
            rx.cond(
                info.icon != "",
                icon_badge(info.icon),
            ),
            rx.cond(
                info.image_icon != "",
                image_badge(info.image_icon),
            ),
            rx.vstack(
                rx.text.strong(info.title),
                rx.text(info.subtitle),
                rx.vstack(
                    *[
                        rx.text(item, size=Size.SMALL.value, color_scheme="gray")
                        for item in info.list
                    ],
                    spacing=Size.SMALL.value,
                    width="100%"
                ),
                rx.text(
                    info.description,
                    size=Size.SMALL.value,
                    color_scheme="gray"
                ),
                rx.hstack(
                    rx.cond(
                        info.url != "",
                        icon_button(
                            "link",
                            info.url
                        )
                    ),
                    rx.cond(
                        info.github != "",
                        icon_button(
                            "github",
                            info.github
                        )
                    )
                ),
                spacing=Size.SMALL.value,
                width="100%"
            ),
            spacing=Size.DEFAULT.value,
            width="100%"
        ),
        rx.cond(
            info.image != "",
            rx.tablet_and_desktop(
                rx.image(
                    src=info.image,
                    height=IMAGE_HEIGHT,
                    width="100%",
                    border_radius=EmSize.DEFAULT.value,
                    object_fit="contain"
                )
            )
        ),
        rx.cond(
            info.image_mobile != "",
            rx.mobile_only(
                rx.image(
                    src=info.image_mobile,
                    height=IMAGE_HEIGHT,
                    width="100%",
                    border_radius=EmSize.DEFAULT.value,
                    object_fit="contain"
                )
            )
        ),
        rx.vstack(
            rx.cond(
                info.date != "",
                rx.badge(info.date)
            ),
            rx.cond(
                info.certificate != "",
                icon_button(
                    "shield-check",
                    info.certificate,
                    solid=True
                )
            ),
            spacing=Size.SMALL.value,
            align="end",
        ),
        flex_direction=["column", "row"],
        spacing=Size.DEFAULT.value,
        width="100%"
    )
