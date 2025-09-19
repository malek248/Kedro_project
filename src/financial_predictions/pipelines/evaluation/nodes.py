import numpy as np


def evaluate_model(
    y_test: np.ndarray,
    y_pred: np.ndarray,
    y_proba: np.ndarray,
) -> dict[str, float]:
    """Compute and return a small metrics dict."""
    from sklearn.metrics import recall_score, precision_score, roc_auc_score

    return {
        "recall_pos": recall_score(y_test, y_pred, pos_label=1),
        "precision_pos": precision_score(y_test, y_pred, pos_label=1),
        "roc_auc": roc_auc_score(y_test, y_proba),
    }
