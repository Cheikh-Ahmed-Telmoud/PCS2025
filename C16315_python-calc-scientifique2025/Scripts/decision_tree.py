import numpy as np
from collections import Counter

class DecisionTreeRegressor:
    def __init__(self, max_depth=None, min_samples_split=2, n_features=None):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.n_features = n_features
        self.root = None

    def fit(self, X, y):
        self.n_features = X.shape[1] if self.n_features is None else min(self.n_features, X.shape[1])
        self.root = self._grow_tree(X, y, depth=0)

    def _grow_tree(self, X, y, depth):
        n_samples, n_feats = X.shape
        if (depth == self.max_depth or 
            n_samples < self.min_samples_split or 
            len(np.unique(y)) == 1):
            return self._create_leaf(y)
        
        best_split = self._find_best_split(X, y, n_feats)
        if not best_split:
            return self._create_leaf(y)
        
        feature_idx, threshold = best_split
        left_idxs = X[:, feature_idx] <= threshold
        left = self._grow_tree(X[left_idxs], y[left_idxs], depth+1)
        right = self._grow_tree(X[~left_idxs], y[~left_idxs], depth+1)
        return Node(feature_idx, threshold, left, right)

    def _find_best_split(self, X, y, n_feats):
        best_mse = float('inf')
        best_split = None
        features = np.random.choice(n_feats, self.n_features, replace=False)
        
        for feat_idx in features:
            thresholds = np.unique(X[:, feat_idx])
            for threshold in thresholds:
                left_idxs = X[:, feat_idx] <= threshold
                if np.sum(left_idxs) < 2 or np.sum(~left_idxs) < 2:
                    continue
                mse = self._calculate_mse(y[left_idxs], y[~left_idxs])
                if mse < best_mse:
                    best_mse = mse
                    best_split = (feat_idx, threshold)
        return best_split

    def _calculate_mse(self, left_y, right_y):
        n_left, n_right = len(left_y), len(right_y)
        mse_left = np.sum((left_y - np.mean(left_y)) ** 2) / n_left if n_left > 0 else 0
        mse_right = np.sum((right_y - np.mean(right_y)) ** 2) / n_right if n_right > 0 else 0
        return (n_left * mse_left + n_right * mse_right) / (n_left + n_right)

    def _create_leaf(self, y):
        return np.mean(y)

    def predict(self, X):
        return np.array([self._traverse_tree(x, self.root) for x in X])

    def _traverse_tree(self, x, node):
        if isinstance(node, float) or isinstance(node, int):  
            return node
        if x[node.feature_idx] <= node.threshold:
            return self._traverse_tree(x, node.left)
        return self._traverse_tree(x, node.right)

class Node:
    def __init__(self, feature_idx, threshold, left, right):
        self.feature_idx = feature_idx
        self.threshold = threshold
        self.left = left
        self.right = right