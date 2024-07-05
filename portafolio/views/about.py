import reflex as rx
from portafolio.components.heading import heading

def about(description: str) -> rx.Component:
    formatted_description = description.replace('\n', '<br>')
    return rx.vstack(
        heading("Sobre mí"),
        rx.html(f"<div>{formatted_description}</div>")
    )
