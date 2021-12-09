from ..tokenizer_exceptions import BASE_EXCEPTIONS
from ...symbols import ORTH, NORM
from ...util import update_exc

_exc = {}

_abbrev_exc = [
    # Weekdays abbreviations
    {ORTH: "да", NORM: "даваа"},
    {ORTH: "мя", NORM: "мягмар"},
    {ORTH: "лх", NORM: "лхагва"},
    {ORTH: "пү", NORM: "пүрэв"},
    {ORTH: "ба", NORM: "баасан"},
    {ORTH: "бя", NORM: "бямба"},
    {ORTH: "ня", NORM: "ням"},
]

for abbr in _abbrev_exc:
    for orth in (abbr[ORTH], abbr[ORTH].capitalize(), abbr[ORTH].upper()):
        _exc[orth] = [{ORTH: orth, NORM: abbr[NORM]}]
        _exc[orth + "."] = [{ORTH: orth + ".", NORM: abbr[NORM]}]

for exc_data in [  # "etc." abbreviations
    {ORTH: "ө.х", NORM: "өөрөөр хэлбэл"},
    {ORTH: "г.м", NORM: "гэх мэт"},
    {ORTH: "ж.нь", NORM: "жишээ нь"},
    {ORTH: "УИХ", NORM: "Улсын Их Хурал"},
    {ORTH: "УБ", NORM: "Улаанбаатар"},
]:
    _exc[exc_data[ORTH]] = [exc_data]

TOKENIZER_EXCEPTIONS = update_exc(BASE_EXCEPTIONS, _exc)
