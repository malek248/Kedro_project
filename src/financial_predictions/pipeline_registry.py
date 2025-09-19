"""Project pipelines."""

from kedro.pipeline import Pipeline
from .pipelines.data_processing import pipeline as dp
from .pipelines.eda import pipeline as eda
from .pipelines.feature_engineering import pipeline as fe
from .pipelines.model_training import pipeline as mt
from .pipelines.evaluation import pipeline as ev


def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    data_processing_pipeline = dp.create_pipeline()
    eda_pipeline = eda.create_pipeline()
    feature_engineering_pipeline = fe.create_pipeline()
    model_training_pipeline = mt.create_pipeline()
    evaluation_pipeline = ev.create_pipeline()

    return {
        "__default__": data_processing_pipeline
        + eda_pipeline
        + feature_engineering_pipeline
        + model_training_pipeline
        + evaluation_pipeline,
        "data_processing": data_processing_pipeline,
        "eda": eda_pipeline,
        "feature_engineering": feature_engineering_pipeline,
        "model_training": model_training_pipeline,
        "evaluation": evaluation_pipeline,
    }
