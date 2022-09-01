import cyrtranslit


def translate_to_latin(text):
    if text is not None:
        return cyrtranslit.to_latin(text, 'bg')


def translate_to_cyrillic(text):
    if text is not None:
        return cyrtranslit.to_cyrillic(text, 'bg')

