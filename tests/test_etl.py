import pandas as pd

from src.etl import run, transform


def test_transform_normalises_and_adds_revenue(tmp_path):
    df = pd.DataFrame({"Order ID": [1, 1], "Quantity": [2, 2], "Unit Price": [3.0, 3.0]})
    out = transform(df)
    assert list(out.columns) == ["order_id", "quantity", "unit_price", "revenue"]
    assert len(out) == 1
    assert out["revenue"].iloc[0] == 6.0


def test_run_writes_output(tmp_path):
    src = tmp_path / "in.csv"
    pd.DataFrame({"Order ID": [1], "Quantity": [2], "Unit Price": [5.0]}).to_csv(src, index=False)
    out = run(src, tmp_path / "out.csv")
    assert out.exists()
    assert "revenue" in pd.read_csv(out).columns
