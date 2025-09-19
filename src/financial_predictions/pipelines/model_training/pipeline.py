from kedro.pipeline import Pipeline, node
from .nodes import (
    find_best_weight,
    train_initial_model,
    select_features_transformer,
    transform_train,
    transform_test,
    train_final_model,
    predict_model,
)


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                find_best_weight,
                inputs=[
                    "X_train",
                    "y_train",
                    "params:model_training.weights",
                    "params:model_training.cv",
                ],
                outputs="best_weight",
                name="find_best_weight_node",
            ),
            node(
                train_initial_model,
                inputs=[
                    "X_train",
                    "y_train",
                    "best_weight",
                    "params:model_training.xgb",
                ],
                outputs="initial_model",
                name="train_initial_model_node",
            ),
            node(
                select_features_transformer,
                inputs=["initial_model", "params:model_training.feature_threshold"],
                outputs="feature_selector",
                name="select_features_node",
            ),
            node(
                transform_train,
                inputs=["feature_selector", "X_train"],
                outputs="X_train_sel",
                name="transform_train_node",
            ),
            node(
                train_final_model,
                inputs=[
                    "X_train_sel",
                    "y_train",
                    "best_weight",
                    "params:model_training.xgb",
                ],
                outputs="xgb_model",
                name="train_final_model_node",
            ),
            node(
                transform_test,
                inputs=["feature_selector", "X_test"],
                outputs="X_test_sel",
                name="transform_test_node",
            ),
            node(
                predict_model,
                inputs=["xgb_model", "X_test_sel"],
                outputs=["y_pred_test", "y_proba_test"],
                name="predict_model_node",
            ),
        ]
    )
