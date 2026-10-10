
from kivy.app import App
from kivy.lang import Builder
from kivy.utils import get_color_from_hex

KV = """
BoxLayout:
    orientation: "vertical"
    padding: "20dp"
    spacing: "14dp"

    canvas.before:
        Color:
            rgba: 0.03, 0.05, 0.10, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Label:
        text: "[b]J.A.R.V.I.S[/b]"
        markup: True
        font_size: "30sp"
        color: 0.2, 0.85, 1, 1
        size_hint_y: None
        height: "65dp"

    Label:
        text: "PERSONAL AI ASSISTANT"
        font_size: "12sp"
        color: 0.6, 0.7, 0.85, 1
        size_hint_y: None
        height: "30dp"

    Widget:

    Label:
        text: "◉"
        font_size: "100sp"
        color: 0.2, 0.85, 1, 1
        size_hint_y: None
        height: "150dp"

    Label:
        id: reply
        text: "JARVIS is ready for your command."
        color: 0.9, 0.95, 1, 1
        text_size: self.width, None
        halign: "left"
        valign: "middle"

    TextInput:
        id: question
        hint_text: "Ask JARVIS..."
        multiline: False
        size_hint_y: None
        height: "52dp"

    Button:
        text: "SEND"
        size_hint_y: None
        height: "50dp"
        on_release: app.send_message(question.text)

    Widget:
"""

class JarvisApp(App):
    def build(self):
        self.title = "JARVIS"
        return Builder.load_string(KV)

    def send_message(self, message):
        message = message.strip()
        if message:
            self.root.ids.reply.text = (
                "You: " + message +
                "\\n\\nJARVIS: Interface online. AI connection coming next."
            )
            self.root.ids.question.text = ""

JarvisApp().run()
