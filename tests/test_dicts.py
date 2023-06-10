from utils import dicts

ARRAY = {"py": "charm", "sky": "pro", "pip": "install"}


def test_get_val():
    assert dicts.get_val(ARRAY, "py") == "charm"


def test_get_default_val():
    assert dicts.get_val(ARRAY, "pipe", "git") == "git"


def test_get_val_empty_arr():
    assert dicts.get_val({}, "sky", "error") == "error"
