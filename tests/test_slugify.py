from slugkit import slugify


def test_basic():
    assert slugify("Hello World") == "hello-world"


def test_punctuation():
    assert slugify("Hello, World!") == "hello-world"


def test_accents():
    assert slugify("Crème Brûlée Recipe") == "creme-brulee-recipe"


def test_repeated_separators():
    assert slugify("Crème Brûlée -- Recipe") == "creme-brulee-recipe"


def test_underscores():
    assert slugify("snake_case_name") == "snake-case-name"
