import pandas as pd
from sklearn.model_selection import train_test_split
from typing import Tuple


# First node : cleaning the data
def clean_data(bank: pd.DataFrame) -> pd.DataFrame:
    print("Columns I actually got:", bank.columns.tolist())
    bank = bank.dropna()
    bank["day"] = bank["day"].astype("object")

    return bank


# Splitting train/test set
def split_raw_data(
    data_raw_all: pd.DataFrame, test_size: float, random_state: int
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    data_train, data_test = train_test_split(
        data_raw_all, test_size=test_size, random_state=random_state
    )
    return data_train, data_test
