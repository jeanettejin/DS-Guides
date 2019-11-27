#### Functions that have been helpful to me

import numpy as np
import pandas as pd

from sklearn.metrics import log_loss
from sklearn.metrics import roc_auc_score

import os

class ClassificationMetrics:
    def __init__(self, y_true, y_proba):
        """
        Class that calculated various metrics for classication (all are compatable for multiclass)
        :param y_true: np.array True values of y
        :param y_proba: np.array Predicted probabilities for each class. Normally found by sklearn predictors
                        .predict_proba method
        """
        self.y_true = y_true
        self.y_proba = y_proba
        self.dummy_y_true = pd.get_dummies(y_true).values

    def _brier_multi(self):
        return np.mean(np.sum((self.y_proba - self.dummy_y_true) ** 2, axis=1))

    def _target_probability(self):
        return np.multiply(self.dummy_y_true, self.y_proba).mean()

    def _square_log_likelihood(self, eps=1e-10):
        pred_values_matrix = self.y_proba * self.dummy_y_true
        pred_values = pred_values_matrix[pred_values_matrix > 0]

        np.putmask(pred_values, pred_values < eps, eps)
        sqlikelihoods = (-np.log(pred_values)) ** 2
        return sqlikelihoods.mean()

    def _log_loss(self):
        return log_loss(self.y_true, self.y_proba)

    def _auc(self):
        return roc_auc_score(self.dummy_y_true, self.y_proba)

    def get_all_metrics(self):

        auc = self._auc()
        bl = self.brier_multi()
        ll = self._log_loss()
        tp = self.target_probability()
        sloglik = self._square_log_likelihood()

        eval_metrics = {'auc': auc,
                        'log loss': ll,
                        'brier score': bl,
                        'square loglik': sloglik,
                        'target prob': tp}

        return eval_metrics


def s3_terminal(abs_local_path, s3_remote_path, file_name, local_to_s3 = True, s3_file_name = None, command='aws s3 cp'):
    """
    Python wrapper to use AWSCLI

    :param abs_local_path: (str) Absolute local path to file or desired location
    :param s3_remote_path: (str) S3 address to file or desired location
    :param file_name: (str) Actual/desired local file name
    :param local_to_s3: (Bool) if true then local_address then s3_address
                        if false then s3_address then local address
    :param s3_file_name: (str) Optional Actual/desired local filename
    :param command: (str) prefix command
    :return: None
    """
    if not s3_file_name:
        file_name = s3_file_name

    local_address = os.path.join(abs_local_path, file_name)
    s3_address = os.path.join(s3_remote_path, s3_file_name)

    if local_to_s3:
        run_line = " ".join([command, local_address, s3_address])
    else:
        run_line = " ".join([command, s3_address, local_address])

    os.system(run_line)

