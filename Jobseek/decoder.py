import html
import re
import unicodedata

def decoder(a):
    while True:
        decoded = html.unescape(a)
        if decoded == a:
            break
        a = decoded
    cleaned_text = unicodedata.normalize("NFKC",re.sub(r'<.*?>', '\b', a))
    return cleaned_text

