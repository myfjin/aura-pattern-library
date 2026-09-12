"""
Simple Decision Tree Classifier

A complete implementation of a decision tree classifier with information gain,
prediction, and pruning capabilities.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Tuple, Any, Optional, Dict, Union
from collections import Counter
import math


class Split:
    """Represents a split in the decision tree."""
    
    def __init__(self, feature_index: int, threshold: float):
        """
        Initialize a split.
        
        Args:
            feature_index: Index of the feature to split on
            threshold: Threshold value for the split
        """
        self.feature_index = feature_index
        self.threshold = threshold
    
    def __repr__(self) -> str:
        return f"Split(feature={self.feature_index}, threshold={self.threshold})"


class Node:
    """Represents a node in the decision tree."""
    
    def __init__(self, 
                 samples: Optional[List[List[float]]] = None,
                 labels: Optional[List[Any]] = None,
                 split: Optional[Split] = None,
                 left: Optional['Node'] = None,
                 right: Optional['Node'] = None,
                 prediction: Optional[Any] = None):
        """
        Initialize a node.
        
        Args:
            samples: Training samples at this node
            labels: Labels for the samples
            split: Split information for internal nodes
            left: Left child node
            right: Right child node
            prediction: Prediction for leaf nodes
        """
        self.samples = samples or []
        self.labels = labels or []
        self.split = split
        self.left = left
        self.right = right
        self.prediction = prediction
    
    def is_leaf(self) -> bool:
        """Check if this node is a leaf."""
        return self.split is None
    
    def __repr__(self) -> str:
        if self.is_leaf():
            return f"Leaf(prediction={self.prediction}, samples={len(self.samples)})"
        return f"Node(split={self.split}, samples={len(self.samples)})"


class DecisionTree:
    """A simple decision tree classifier."""
    
    def __init__(self, max_depth: int = 10, min_samples_split: int = 2):
        """
        Initialize the decision tree.
        
        Args:
            max_depth: Maximum depth of the tree
            min_samples_split: Minimum number of samples required to split
        """
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.root: Optional[Node] = None
    
    def _entropy(self, labels: List[Any]) -> float:
        """
        Calculate entropy of a list of labels.
        
        Args:
            labels: List of labels
            
        Returns:
            Entropy value
        """
        if not labels:
            return 0.0
        
        label_counts = Counter(labels)
        total = len(labels)
        entropy = 0.0
        
        for count in label_counts.values():
            probability = count / total
            entropy -= probability * math.log2(probability)
        
        return entropy
    
    def _information_gain(self, 
                         samples: List[List[float]], 
                         labels: List[Any], 
                         split: Split) -> float:
        """
        Calculate information gain for a split.
        
        Args:
            samples: Training samples
            labels: Corresponding labels
            split: Split to evaluate
            
        Returns:
            Information gain
        """
        # Calculate entropy before split
        parent_entropy = self._entropy(labels)
        
        # Split samples
        left_samples, left_labels, right_samples, right_labels = [], [], [], []
        
        for sample, label in zip(samples, labels):
            if sample[split.feature_index] <= split.threshold:
                left_samples.append(sample)
                left_labels.append(label)
            else:
                right_samples.append(sample)
                right_labels.append(label)
        
        # Calculate weighted entropy after split
        total_samples = len(samples)
        if total_samples == 0:
            return 0.0
            
        left_weight = len(left_samples) / total_samples
        right_weight = len(right_samples) / total_samples
        
        left_entropy = self._entropy(left_labels)
        right_entropy = self._entropy(right_labels)
        
        weighted_entropy = left_weight * left_entropy + right_weight * right_entropy
        
        # Information gain
        return parent_entropy - weighted_entropy
    
    def _find_best_split(self, 
                        samples: List[List[float]], 
                        labels: List[Any]) -> Optional[Split]:
        """
        Find the best split for the given samples.
        
        Args:
            samples: Training samples
            labels: Corresponding labels
            
        Returns:
            Best split or None if no split is possible
        """
        if len(set(labels)) <= 1:
            return None
            
        best_gain = -1.0
        best_split = None
        n_features = len(samples[0]) if samples else 0
        
        # Try all features
        for feature_index in range(n_features):
            # Get unique values for this feature
            values = sorted(set(sample[feature_index] for sample in samples))
            
            # Try splits between consecutive values
            for i in range(len(values) - 1):
                threshold = (values[i] + values[i + 1]) / 2
                split = Split(feature_index, threshold)
                gain = self._information_gain(samples, labels, split)
                
                if gain > best_gain:
                    best_gain = gain
                    best_split = split
        
        return best_split
    
    def _build_tree(self, 
                   samples: List[List[float]], 
                   labels: List[Any], 
                   depth: int = 0) -> Node:
        """
        Recursively build the decision tree.
        
        Args:
            samples: Training samples
            labels: Corresponding labels
            depth: Current depth in the tree
            
        Returns:
            Root node of the built subtree
        """
        # Create node with current samples
        node = Node(samples=samples, labels=labels)
        
        # Check stopping conditions
        if (depth >= self.max_depth or 
            len(samples) < self.min_samples_split or 
            len(set(labels)) <= 1):
            # Make leaf node
            if labels:
                node.prediction = Counter(labels).most_common(1)[0][0]
            return node
        
        # Find best split
        best_split = self._find_best_split(samples, labels)
        
        # If no good split found, make leaf
        if best_split is None:
            if labels:
                node.prediction = Counter(labels).most_common(1)[0][0]
            return node
        
        # Split samples
        left_samples, left_labels, right_samples, right_labels = [], [], [], []
        
        for sample, label in zip(samples, labels):
            if sample[best_split.feature_index] <= best_split.threshold:
                left_samples.append(sample)
                left_labels.append(label)
            else:
                right_samples.append(sample)
                right_labels.append(label)
        
        # Create split node
        node.split = best_split
        node.left = self._build_tree(left_samples, left_labels, depth + 1)
        node.right = self._build_tree(right_samples, right_labels, depth + 1)
        
        return node
    
    def fit(self, samples: List[List[float]], labels: List[Any]) -> None:
        """
        Train the decision tree.
        
        Args:
            samples: Training samples
            labels: Corresponding labels
        """
        if not samples or not labels or len(samples) != len(labels):
            raise ValueError("Invalid training data")
        
        self.root = self._build_tree(samples, labels)
    
    def _predict_sample(self, sample: List[float], node: Node) -> Any:
        """
        Predict class for a single sample.
        
        Args:
            sample: Sample to predict
            node: Current node in the tree
            
        Returns:
            Predicted class
        """
        if node.is_leaf():
            if node.prediction is None:
                raise ValueError("Leaf node has no prediction")
            return node.prediction
        
        if node.split is None:
            raise ValueError("Internal node has no split")
        
        # Navigate to appropriate child
        if sample[node.split.feature_index] <= node.split.threshold:
            return self._predict_sample(sample, node.left)
        else:
            return self._predict_sample(sample, node.right)
    
    def predict(self, samples: List[List[float]]) -> List[Any]:
        """
        Predict classes for samples.
        
        Args:
            samples: Samples to predict
            
        Returns:
            Predicted classes
        """
        if self.root is None:
            raise ValueError("Model not trained yet")
        
        return [self._predict_sample(sample, self.root) for sample in samples]
    
    def _prune_node(self, node: Node, 
                   validation_samples: List[List[float]], 
                   validation_labels: List[Any]) -> Node:
        """
        Prune a subtree using validation data.
        
        Args:
            node: Node to prune
            validation_samples: Validation samples
            validation_labels: Validation labels
            
        Returns:
            Pruned node
        """
        if node.is_leaf():
            return node
        
        # If no validation data, keep as is
        if not validation_samples:
            return node
        
        # Split validation data according to node's split
        left_samples, left_labels, right_samples, right_labels = [], [], [], []
        
        for sample, label in zip(validation_samples, validation_labels):
            if sample[node.split.feature_index] <= node.split.threshold:
                left_samples.append(sample)
                left_labels.append(label)
            else:
                right_samples.append(sample)
                right_labels.append(label)
        
        # Prune children
        node.left = self._prune_node(node.left, left_samples, left_labels)
        node.right = self._prune_node(node.right, right_samples, right_labels)
        
        # If children are now leaves, consider pruning
        if node.left.is_leaf() and node.right.is_leaf():
            # Calculate accuracy without pruning
            predictions = self.predict(validation_samples)
            accuracy_without_pruning = sum(
                1 for p, l in zip(predictions, validation_labels) if p == l
            ) / len(validation_labels) if validation_labels else 0
            
            # Calculate accuracy with pruning (make this node a leaf)
            original_split = node.split
            original_left = node.left
            original_right = node.right
            
            # Make this node a leaf
            node.split = None
            node.left = None
            node.right = None
            if node.labels:
                node.prediction = Counter(node.labels).most_common(1)[0][0]
            
            # Calculate accuracy as leaf
            predictions = [node.prediction] * len(validation_samples)
            accuracy_with_pruning = sum(
                1 for p, l in zip(predictions, validation_labels) if p == l
            ) / len(validation_labels) if validation_labels else 0
            
            # If pruning doesn't improve accuracy, revert
            if accuracy_without_pruning > accuracy_with_pruning:
                node.split = original_split
                node.left = original_left
                node.right = original_right
                node.prediction = None
        
        return node
    
    def prune(self, validation_samples: List[List[float]], 
              validation_labels: List[Any]) -> None:
        """
        Prune the decision tree using validation data.
        
        Args:
            validation_samples: Validation samples
            validation_labels: Validation labels
        """
        if self.root is None:
            raise ValueError("Model not trained yet")
        
        self.root = self._prune_node(self.root, validation_samples, validation_labels)
    
    def __repr__(self) -> str:
        """String representation of the tree."""
        def _repr_node(node: Optional[Node], indent: int = 0) -> str:
            if node is None:
                return "None"
            
            if node.is_leaf():
                return "  " * indent + f"Leaf: {node.prediction} ({len(node.samples)} samples)"
            
            result = "  " * indent + f"Split: feature[{node.split.feature_index}] <= {node.split.threshold} ({len(node.samples)} samples)\n"
            result += _repr_node(node.left, indent + 1) + "\n"
            result += _repr_node(node.right, indent + 1)
            return result
        
        if self.root is None:
            return "DecisionTree(untrained)"
        
        return f"DecisionTree\n{_repr_node(self.root)}"


def main():
    """Self-test: a separable planted rule is learned exactly (100% train
    accuracy + correct generalization), pruning keeps validation accuracy,
    untrained refusal."""
    # PLANTED RULE: label = 0 if weight < 57, 1 if 57 <= weight < 73, else 2.
    samples = [
        [170, 65], [175, 70], [160, 55], [180, 80], [155, 50],
        [165, 60], [172, 75], [158, 52], [178, 78], [162, 58],
        [185, 90], [150, 45], [168, 68], [176, 76], [159, 54],
    ]
    labels = [1, 1, 0, 2, 0, 1, 2, 0, 2, 1, 2, 0, 1, 2, 0]

    tree = DecisionTree(max_depth=5, min_samples_split=2)
    tree.fit(samples, labels)

    # A separable rule must be learned to 100% on the training set.
    train_preds = tree.predict(samples)
    train_acc = sum(p == t for p, t in zip(train_preds, labels)) / len(labels)
    assert train_acc == 1.0, f"separable data must fit exactly, accuracy {train_acc}"

    # Generalization to fresh points obeying the planted rule.
    test_samples = [[165, 62], [180, 85], [155, 48], [163, 59], [179, 74]]
    truth = [1, 2, 0, 1, 2]
    preds = tree.predict(test_samples)
    assert preds == truth, f"planted rule not generalized: {preds} != {truth}"
    assert sum(preds) == 6, "prediction classes 1+2+0+1+2 must sum to 6"

    # Pruning on rule-consistent validation data must not hurt validation
    # accuracy (that is pruning's contract).
    validation_samples = [[167, 63], [177, 77], [157, 51], [182, 82]]
    validation_labels = [1, 2, 0, 2]
    before = tree.predict(validation_samples)
    acc_before = sum(p == t for p, t in zip(before, validation_labels)) / 4
    tree.prune(validation_samples, validation_labels)
    after = tree.predict(validation_samples)
    acc_after = sum(p == t for p, t in zip(after, validation_labels)) / 4
    assert acc_after >= acc_before, \
        f"pruning reduced validation accuracy {acc_before} -> {acc_after}"
    assert acc_after == 1.0, f"rule-consistent validation must stay perfect, got {acc_after}"

    # Single-class data collapses to a leaf that always answers that class.
    flat = DecisionTree(max_depth=3)
    flat.fit([[1, 1], [2, 2], [3, 3]], [7, 7, 7])
    assert flat.predict([[9, 9], [0, 0]]) == [7, 7], "constant labels not learned"

    # Untrained refusal.
    try:
        DecisionTree().predict([[1, 2]])
        assert False, "untrained tree predicted"
    except ValueError:
        pass
    try:
        DecisionTree().prune([[1, 2]], [0])
        assert False, "untrained tree pruned"
    except ValueError:
        pass

    print("decision_tree: separable rule fit 15/15, generalized 5/5 (sum 6), "
          "pruning kept validation at 1.0, constant leaf, refusals — PASS")


if __name__ == "__main__":
    main()