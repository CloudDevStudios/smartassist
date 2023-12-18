import panel as pn

pn.extension(design="material")

def callback(contents: str, user: str, instance: pn.chat.ChatInterface):
    return f"Echoing {user}: {contents}"

chat_interface = pn.chat.ChatInterface(callback=callback)
chat_interface.send(
    "Enter a message in the TextInput below and receive an echo!",
    user="System",
    respond=False,
)
chat_interface.servable()