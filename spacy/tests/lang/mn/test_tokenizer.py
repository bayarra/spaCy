import pytest


INFIX_HYPHEN_TESTS = [
    ("Улаанбаатар хот мөн үү?", "Улаанбаатар хот мөн үү ?".split()),
    ("Халиун сум.", "Халиун сум .".split()),
]

MIXED_ORDINAL_NUMS_TESTS = [("17 дугаар жарны гал луу жил...", "17 дугаар жарны гал луу жил ...".split())]

NAME_ABBREV_TESTS = [
    ("ө.х", "өөрөөр хэлбэл".split()),
    ("г.м", "гэх мэт".split()),
    ("ж.нь", "жишээ нь".split()),
    ("УИХ", "Улсын Их Хурал".split()),
    ("УБ", "Улаанбаатар".split()),
]

LONG_TEXTS_TESTS = [
    (

        "Монгол хэл нь Монгол улсын албан ёсны хэл юм. "
        "Монгол үндэстний эрт эдүгээ цагийн хэл аялга, үсэг бичгийг хамтад нь "
        "Монгол хэл бичиг гэнэ. Түүнээс Монгол үндэстний эх хэлийг Монгол хэл "
        "(монгол бичгээр монггул хэлэ, тод монголоор монггол хэлэн) гэдэг. "
        "Монгол хэл XIII-XV, XVI зууны нэг, XVI-XVIII зуун, XIX зууны "
        "гэх мэтээр шатлан хөгжиж XX зуунд Орчин цагийн монгол хэлтэй "
        "золгосон ажээ.",
        "Монгол хэл нь Монгол улсын албан ёсны хэл юм . "
        "Монгол үндэстний эрт эдүгээ цагийн хэл аялга , үсэг бичгийг хамтад нь "
        "Монгол хэл бичиг гэнэ . Түүнээс Монгол үндэстний эх хэлийг Монгол хэл "
        "( монгол бичгээр монггул хэлэ , тод монголоор монггол хэлэн ) гэдэг . "
        "Монгол хэл XIII-XV , XVI зууны нэг, XVI-XVIII зуун , XIX зууны "
        "гэх мэтээр шатлан хөгжиж XX зуунд Орчин цагийн монгол хэлтэй "
        "золгосон ажээ .".split(),
    )
]

TESTCASES = (
    INFIX_HYPHEN_TESTS
    + MIXED_ORDINAL_NUMS_TESTS
    + NAME_ABBREV_TESTS
    + LONG_TEXTS_TESTS
)


@pytest.mark.parametrize("text,expected_tokens", TESTCASES)
def test_mn_tokenizer_handles_testcases(mn_tokenizer, text, expected_tokens):
    tokens = [token.text for token in mn_tokenizer(text) if not token.is_space]
    assert expected_tokens == tokens

