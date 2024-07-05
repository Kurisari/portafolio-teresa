import reflex as rx
from portafolio import data
from portafolio.styles.styles import BASE_STYLE, MAX_WIDTH, STYLESHEETS, EmSize, Size
from portafolio.views.about import about
from portafolio.views.extra import extra
from portafolio.views.footer import footer
from portafolio.views.header import header
from portafolio.views.info import info
from portafolio.views.skills import skills
from portafolio.components.color_button import color_button

DATA = data.data


def index() -> rx.Component:
    return rx.center(
        # rx.theme_panel(),
        rx.vstack(
            # color_button(),
            header(DATA),
            # about(DATA.about),
            rx.divider(),
            info("Formación Academica", DATA.training),
            info("Formación Complentaria", DATA.projects),
            info("Experiencia Laboral", DATA.experience),
            info("Información Adicional", DATA.extra),
            # skills("Programas Computacionales", DATA.skills_comp),
            # skills("Habilidades", DATA.skills_hab),
            # skills("Idiomas", DATA.languages),
            # extra(DATA.extras),
            rx.divider(),
            footer(DATA.media),
            spacing=Size.MEDIUM.value,
            padding_x=EmSize.MEDIUM.value,
            padding_y=EmSize.BIG.value,
            max_width=MAX_WIDTH,
            width="100%"
        )
    )


app = rx.App(
    stylesheets=STYLESHEETS,
    style=BASE_STYLE,
    theme=rx.theme(
        appearance="light",
        accent_color="jade",
        radius="small"
    )
)

title = DATA.title
description = DATA.description
image = DATA.image

app.add_page(
    index,
    title=title,
    description=description,
    image=image,
    meta=[
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": image}
    ]
)
