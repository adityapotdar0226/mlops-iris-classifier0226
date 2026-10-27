

import pandas as pd

from src.pipeline.collect import collect_data


def test_collect_data_creates_csv_and_returns_dataframe(tmp_path):
    output_path = tmp_path / "iris_raw.csv"

    df = collect_data(str(output_path))

    # Verify returned object
    assert isinstance(df, pd.DataFrame)

    # Verify dataset contains expected rows
    assert len(df) == 150

    # Verify expected columns
    assert "species" in df.columns
    assert "collected_at" in df.columns
    assert "target" not in df.columns

    # Verify species labels are converted to names
    assert set(df["species"].unique()) == {
        "setosa",
        "versicolor",
        "virginica",
    }

    # Verify timestamp column is populated
    assert df["collected_at"].notna().all()

    # Verify CSV file was created
    assert output_path.exists()

    # Verify saved CSV can be read
    saved_df = pd.read_csv(output_path)
    assert len(saved_df) == 150
    assert "species" in saved_df.columns
