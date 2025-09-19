from kedro.pipeline import node, Pipeline
from .nodes import evaluate_model


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                evaluate_model,
                inputs=["y_test", "y_pred_test", "y_proba_test"],
                outputs="model_metrics",
                name="evaluate_model_node",
            ),
        ]
    )
