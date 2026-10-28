import pandas as pd

def catbind(a, b):
    """
    Concatenates two pandas categoricals.

    Parameters
    ----------
    a : pandas.Categorical
      A pandas categorical.
    b : pandas.Categorical
      A pandas categorical that you wish to concatenate to a.

    Returns
    -------
    pandas.Categorical
      The new concatenated pandas categorical.

    Examples
    --------
    >>> import qmsspkg
    >>> a = pd.Categorical(["character", "hits", "your", "eyeballs"])
    >>> b = pd.Categorical(["but", "integer", "where it", "counts"])
    >>> qmsspkg.catbind(a, b)
    ['character', 'hits', 'your', 'eyeballs', 'but', 'integer', 'where it', 'counts']
    Categories (8, str): ['but', 'character', 'counts', 'eyeballs', 'hits', 'integer',
                          'where it', 'your']
    """
    concatenated = pd.concat([pd.Series(a.astype("str")),
                              pd.Series(b.astype("str"))])
    return pd.Categorical(concatenated)
