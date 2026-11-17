"""Generate a sample orders CSV for the demo pipeline."""
from pathlib import Path

import numpy as np
import pandas as pd


def make(n: int = 50, seed: int = 7) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    return pd.DataFrame(
        {
            "Order ID": [f"ORD-{i:04d}" for i in range(n)],
            "Customer Name": rng.choice(["Ani", "Budi", "Citra", "Dewi"], n),
            "Quantity": rng.integers(1, 10, n),
            "Unit Price": np.round(rng.uniform(5_000, 250_000, n), 2),
            "Order Date": pd.date_range("2026-01-01", periods=n, freq="D").astype(str),
        }
    )


def main() -> Path:
    out = Path("data/raw/orders.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    make().to_csv(out, index=False)
    print(f"wrote sample orders -> {out}")
    return out


if __name__ == "__main__":
    main()
