import argparse
import pathlib
import pandas as pd
import matplotlib.pyplot as plt


def read_stats_csv(path: pathlib.Path) -> pd.DataFrame:
    df = pd.read_csv(
        path,
        sep=";",
        comment="#",
        engine="python",
    )
    df.columns = [c.strip() for c in df.columns]
    for c in df.columns:
        if df[c].dtype == object:
            df[c] = df[c].astype(str).str.strip()
    for c in df.columns:
        df[c] = pd.to_numeric(df[c], errors="ignore")
    return df


def plot_histogram(
    df: pd.DataFrame,
    column: str,
    n_bins: int,
    out_dir: pathlib.Path,
    basename: str,
):
    series = pd.to_numeric(df[column], errors="coerce").dropna()
    if series.empty:
        print(f"Column {column} has no numeric data, skipping")
        return

    min_v, max_v = series.min(), series.max()

    plt.figure(figsize=(8, 5), dpi=120)
    plt.hist(
        series,
        bins=n_bins,
        range=(min_v, max_v),
        histtype="stepfilled",
        edgecolor="black",
    )
    plt.xlabel(column)
    plt.ylabel("entries")
    plt.title(f"{column} distribution\n[min={min_v:.4g}, max={max_v:.4g}]")
    plt.tight_layout()

    observable = column.replace(" ", "")
    out_name = f"{basename}-{observable}.png"
    out_path = out_dir / out_name

    plt.savefig(out_path)
    plt.close()
    print(f"Saved {out_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Plot histograms from hega-rs statistics CSV",
    )
    parser.add_argument(
        "csv_path",
        type=pathlib.Path,
        help="Path to statistics CSV file",
    )
    parser.add_argument(
        "-o",
        "--out-dir",
        type=pathlib.Path,
        default=pathlib.Path("."),
        help="Output directory for plots (default: current dir)",
    )
    parser.add_argument(
        "-n",
        "--bins",
        type=int,
        default=80,
        help="Number of histogram bins (default: 80)",
    )
    parser.add_argument(
        "--cols",
        nargs="+",
        default=[
            "FinEnergy",
            "ECharge",
            "BCharge",
            "LCharge",
            "FinCnt",
            "FinChargedCnt",
        ],
        help=(
            "Columns to plot "
            "(default: FinEnergy ECharge BCharge LCharge FinCnt FinChargedCnt)"
        ),
    )

    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)

    df = read_stats_csv(args.csv_path)

    basename = args.csv_path.stem

    for col in args.cols:
        if col in df.columns:
            plot_histogram(df, col, args.bins, args.out_dir, basename)
        else:
            print(f"Column {col} not found in file, skipping")


if __name__ == "__main__":
    main()