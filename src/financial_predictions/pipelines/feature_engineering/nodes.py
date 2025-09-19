import pandas as pd
from .nodes_utils import (
    get_data_attrs_names,
    create_X_ml_pipeline,
    create_y_ml_pipeline,
)


def split_attributes(data_raw: pd.DataFrame) -> pd.DataFrame:
    """
    Return a one‐row DataFrame whose columns hold the lists of names.
    """
    return get_data_attrs_names(data_raw)


def transform_features(
    data_raw: pd.DataFrame, attrs_map: pd.DataFrame
) -> pd.DataFrame:  # Changed return type hint
    cat_attrs = attrs_map.loc[0, "X_cat"]
    num_attrs = attrs_map.loc[0, "X_num"]
    pipeline = create_X_ml_pipeline(cat_attrs=cat_attrs, num_attrs=num_attrs)
    transformed_data = pipeline.fit_transform(data_raw)
    # Convert NumPy array back to DataFrame to match ParquetDataset expectation
    # Note: Column names are lost in transformation, using default integer names.
    # For preserving names, the pipeline/node would need more complex handling.
    return pd.DataFrame(transformed_data)


def transform_target(
    data_raw: pd.DataFrame, attrs_map: pd.DataFrame
) -> pd.DataFrame:  # Changed return type hint
    target_col = attrs_map.loc[0, "y"]
    pipeline = create_y_ml_pipeline(target_attr=target_col)
    transformed_data = pipeline.fit_transform(data_raw)
    # Convert NumPy array back to DataFrame to match ParquetDataset expectation
    # Using the original target column name for the DataFrame
    return pd.DataFrame(transformed_data, columns=target_col)
