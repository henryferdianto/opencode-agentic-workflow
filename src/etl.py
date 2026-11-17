"""Example data pipeline agents can extend and refactor."""
from pathlib import Path
import pandas as pd


def extract(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates().dropna(how="all")
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    return df


def load(df: pd.DataFrame, out: Path) -> Path:
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(out, index=False)
    return out


def run(src: Path, dst: Path) -> Path:
    return load(transform(extract(src)), dst)
