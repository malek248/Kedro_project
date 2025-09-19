from kedro.pipeline import Pipeline, node
from .nodes import clean_data, split_raw_data


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=clean_data,
                inputs="bank",
                outputs="preprocessed_bank",
                name="clean_data_node",
            ),
            node(
                func=split_raw_data,
                inputs=dict(
                    data_raw_all="preprocessed_bank",
                    test_size="params:split_data.test_size",
                    random_state="params:split_data.random_state",
                ),
                outputs=["data_train", "data_test"],
                name="split_raw_data_node",
            ),
        ]
    )
