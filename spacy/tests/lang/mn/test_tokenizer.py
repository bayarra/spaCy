import pytest


INFIX_HYPHEN_TESTS = [
    ("Говь-Алтай аймаг мөн үү?", "Говь-Алтай аймаг мөн үү ?".split()),
    ("Хутаг-Өндөр сум.", "Хутаг-Өндөр сум .".split()),
]

MIXED_ORDINAL_NUMS_TESTS = [("17-р жарны гал луу жил...", "17 - р жарны гал луу жил ...".split())]

ABBREV_TESTS = [
    ("Маселе б-ча эртең келет", "Маселе б-ча эртең келет".split()),
    ("Ахунбаев көч. турат.", "Ахунбаев көч. турат .".split()),
    ("«3-жылы (б.з.ч.) туулган", "« 3 - жылы ( б.з.ч. ) туулган".split()),
    ("Жүгөрү ж.б. дандар колдонулат", "Жүгөрү ж.б. дандар колдонулат".split()),
    ("3-4 кк. курулган.", "3 - 4 кк. курулган .".split()),
]

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
    + ABBREV_TESTS
    + NAME_ABBREV_TESTS
    + LONG_TEXTS_TESTS
)

NORM_TESTCASES = [
    (
        "ит, мышык ж.б.у.с. үй жаныбарлары.",
        ["ит", ",", "мышык", "жана башка ушул сыяктуу", "үй", "жаныбарлары", "."],
    )
]


@pytest.mark.parametrize("text,expected_tokens", TESTCASES)
def test_mn_tokenizer_handles_testcases(mn_tokenizer, text, expected_tokens):
    tokens = [token.text for token in mn_tokenizer(text) if not token.is_space]
    assert expected_tokens == tokens


@pytest.mark.parametrize("text,norms", NORM_TESTCASES)
def test_mn_tokenizer_handles_norm_exceptions(mn_tokenizer, text, norms):
    tokens = mn_tokenizer(text)
    assert [token.norm_ for token in tokens] == norms
