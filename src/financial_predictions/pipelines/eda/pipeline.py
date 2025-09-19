from kedro.pipeline import Pipeline, node
from .nodes import get_dtypes, plot_count, groupby_mean, plot_pairplot, plot_heatmap


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=get_dtypes,
                inputs="preprocessed_bank",
                outputs="dtypes",
                name="get_dtypes_node",
            ),
            node(
                func=plot_count,
                inputs="preprocessed_bank",
                outputs=None,
                name="plot_count_node",
            ),
            node(
                func=groupby_mean,
                inputs="preprocessed_bank",
                outputs="grouped_mean",
                name="groupby_mean_node",
            ),
            node(
                func=plot_pairplot,
                inputs=dict(
                    df="preprocessed_bank", num_cols_with_y="params:num_cols_with_y"
                ),
                outputs=None,
                name="plot_pairplot_node",
            ),
            node(
                func=plot_heatmap,
                inputs=dict(df="preprocessed_bank", num_cols="params:num_cols"),
                outputs=None,
                name="plot_heatmap_node",
            ),
        ]
    )
