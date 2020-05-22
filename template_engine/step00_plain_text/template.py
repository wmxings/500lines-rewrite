class Template:
    """Render template in flask-like syntax."""
    def __init__(self, text: str):
        self._text = text

    def render(self, ctx) -> str:
        return self._text

