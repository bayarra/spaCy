from ...attrs import LIKE_NUM

_num_words = [
    "тэг", "нэг", "хоёр", "гурав", "дөрөв", "тав", "зургаа", "долоо", "найм", "ес", "арав",
    "нэгэн", "хоёрон", "гурван", "дөрвөн", "таван", "зургаан", "долоон", "найман", "есөн",
    "арван", "хорин", "гучин", "дөчин", "тавин", "жаран", "далан", "наян", "ерөн", 
    "зуу", "зуун",
    "мянга", "мянган",
    "сая", "тэрбум", "наяд", "ихнаяд",
]


def like_num(text):
    if text.startswith(("+", "-", "±", "~")):
        text = text[1:]
    text = text.replace(",", "").replace(".", "")
    if text.isdigit():
        return True
    if text.count("/") == 1:
        num, denom = text.split("/")
        if num.isdigit() and denom.isdigit():
            return True
    if text in _num_words:
        return True
    return False


LEX_ATTRS = {LIKE_NUM: like_num}
