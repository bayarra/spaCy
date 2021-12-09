from .lex_attrs import LEX_ATTRS
from .punctuation import TOKENIZER_INFIXES
from .stop_words import STOP_WORDS
from .tokenizer_exceptions import TOKENIZER_EXCEPTIONS
from ...language import Language, BaseDefaults


class MongolianDefaults(BaseDefaults):
    tokenizer_exceptions = TOKENIZER_EXCEPTIONS
    infixes = TOKENIZER_INFIXES
    lex_attr_getters = LEX_ATTRS
    stop_words = STOP_WORDS


class Mongolian(Language):
    lang = "mn"
    Defaults = MongolianDefaults


__all__ = ["Mongolian"]
