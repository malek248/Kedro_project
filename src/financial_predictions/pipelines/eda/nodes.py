# Exploring the type of the different variables of the dataset
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def get_dtypes(df: pd.DataFrame) -> pd.Series:
    return df.dtypes


# Positive and negative class distribution


def plot_count(df: pd.DataFrame) -> None:
    sns.countplot(x="y", data=df, palette="husl")
    plt.title("Count Plot of 'y'")
    plt.show()


# Exploring the numeric column


def groupby_mean(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("y").mean(numeric_only=True)


# Plotting the distribution of the features and their cross co-relation


def plot_pairplot(df: pd.DataFrame, num_cols_with_y: list) -> None:
    g = sns.pairplot(
        df[num_cols_with_y],
        hue="y",
        diag_kind="hist",
        dropna=True,
        markers=[",", ","],
        palette=sns.color_palette(["red", "green"]),
        plot_kws={"s": 3},
    )
    g = g.map_lower(sns.kdeplot, cmap="Blues_d")
    plt.title("Pair Plot")
    plt.show()


# The corelation between inputs


def plot_heatmap(df: pd.DataFrame, num_cols: list) -> None:
    corr = df[num_cols].corr()
    sns.heatmap(
        corr,
        xticklabels=corr.columns.values,
        yticklabels=corr.columns.values,
        cmap=sns.light_palette("navy"),
    )
    plt.title("Correlation Heatmap")
    plt.show()
