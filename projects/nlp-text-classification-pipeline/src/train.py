"""
Model training module for NLP text classification.
Supports Logistic Regression, BERT fine-tuning, and LLM zero-shot classification.
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from typing import Dict, List, Optional, Tuple
import pickle


class TextClassifier:
    """Text classification model wrapper."""
    
    def __init__(self, model_type: str = 'logistic_regression'):
        self.model_type = model_type
        self.model = None
        self.label_map = None
        self.fitted = False
        
    def fit(self, X: np.ndarray, y: np.ndarray, 
            label_map: Optional[Dict] = None,
            class_weights: Optional[Dict] = None):
        """Train classification model."""
        self.label_map = label_map
        
        if self.model_type == 'logistic_regression':
            self.model = LogisticRegression(
                max_iter=1000,
                random_state=42,
                C=1.0,
                class_weight=class_weights or 'balanced'
            )
            self.model.fit(X, y)
            self.fitted = True
        else:
            raise ValueError(f"Unsupported model type: {self.model_type}")
        
        return self
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """Predict class labels."""
        if not self.fitted:
            raise ValueError("Model not fitted. Call fit() first.")
        return self.model.predict(X)
    
    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        """Predict class probabilities."""
        if not self.fitted:
            raise ValueError("Model not fitted.")
        return self.model.predict_proba(X)
    
    def evaluate(self, X: np.ndarray, y_true: np.ndarray) -> Dict:
        """Evaluate model performance."""
        y_pred = self.predict(X)
        
        return {
            'accuracy': accuracy_score(y_true, y_pred),
            'classification_report': classification_report(y_true, y_pred),
            'confusion_matrix': confusion_matrix(y_true, y_pred)
        }
    
    def get_top_features(self, feature_names: List[str], n: int = 10) -> Dict:
        """Get top features per class."""
        if self.model_type != 'logistic_regression':
            return {}
        
        top_features = {}
        for i, class_name in enumerate(self.model.classes_):
            if self.label_map:
                class_name = [k for k, v in self.label_map.items() if v == class_name][0]
            
            coef = self.model.coef_[i]
            top_idx = np.argsort(coef)[-n:][::-1]
            top_features[class_name] = [(feature_names[idx], coef[idx]) for idx in top_idx]
        
        return top_features
    
    def save(self, path: str):
        """Save model to disk."""
        with open(path, 'wb') as f:
            pickle.dump({
                'model': self.model,
                'label_map': self.label_map,
                'model_type': self.model_type
            }, f)
        print(f"Saved model to: {path}")
    
    def load(self, path: str):
        """Load model from disk."""
        with open(path, 'rb') as f:
            data = pickle.load(f)
        self.model = data['model']
        self.label_map = data['label_map']
        self.model_type = data['model_type']
        self.fitted = True
        print(f"Loaded model from: {path}")


if __name__ == '__main__':
    # Test classifier
    from sklearn.feature_extraction.text import TfidfVectorizer

    texts = ["budget allocation", "policy implementation", "service request", "foia disclosure"]
    labels = [0, 1, 2, 3]

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    clf = TextClassifier('logistic_regression')
    clf.fit(X, labels)

    pred = clf.predict(X)
    print(f"Predictions: {pred}")
    print("Training module ready.")
