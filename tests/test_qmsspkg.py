import pandas as pd
import qmsspkg


def test_version_is_defined():
    assert isinstance(qmsspkg.__version__, str)


def test_catbind():
    a = pd.Categorical(["character", "hits", "your", "eyeballs"])
    b = pd.Categorical(["but", "integer", "where it", "counts"])
    assert (qmsspkg.catbind(a, b).codes == [1, 4, 7, 3, 0, 5, 6, 2]).all()
    assert (qmsspkg.catbind(a, b).categories == ["but", "character",
            "counts", "eyeballs", "hits", "integer", "where it", "your"]).all()
