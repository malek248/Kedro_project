from kedro.pipeline import Pipeline, node
from .nodes import (
    split_attributes,
    transform_features,
    transform_target,
)


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=split_attributes,
                inputs="data_train",
                outputs="attrs_map",
                name="split_attributes_node",
            ),
            node(
                func=transform_features,
                inputs=["data_train", "attrs_map"],
                outputs="X_train",
                name="transform_features_train_node",
            ),
            node(
                func=transform_target,
                inputs=["data_train", "attrs_map"],
                outputs="y_train",
                name="transform_target_train_node",
            ),
            node(
                func=transform_features,
                inputs=["data_test", "attrs_map"],
                outputs="X_test",
                name="transform_features_test_node",
            ),
            node(
                func=transform_target,
                inputs=["data_test", "attrs_map"],
                outputs="y_test",
                name="transform_target_test_node",
            ),
        ]
    )
