from pathlib import Path

from src.etl import run
from src.sample_data import main as make_sample


def main():
    src = Path("data/raw/orders.csv")
    if not src.exists():
        make_sample()
    dst = run(src, Path("data/processed/orders_clean.csv"))
    print(f"pipeline output -> {dst}")


if __name__ == "__main__":
    main()
