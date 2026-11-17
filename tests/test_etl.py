import pandas as pd
from src.etl import transform


def test_transform_drops_duplicates_and_normalises_columns():
    df = pd.DataFrame({"A B": [1, 1], "C": [2, 2]})
    out = transform(df)
    assert list(out.columns) == ["a_b", "c"]
    assert len(out) == 1
