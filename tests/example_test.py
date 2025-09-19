import pandas as pd


def test_dummy_pandas():
    # Create a simple DataFrame
    data = {"col1": [1, 2, 3], "col2": [4, 5, 6]}
    df = pd.DataFrame(data)

    # Perform a dummy check
    assert df.shape == (3, 2), "DataFrame shape mismatch"
    assert list(df.columns) == ["col1", "col2"], "DataFrame columns mismatch"
