# Hyperparameter Tuning Analysis

## 1. Baseline Model

**Model:** DecisionTreeClassifier

**CV F1 Macro:** 0.9663

**CV F1 Macro Standard Deviation:** 0.0316

**Test Accuracy:** 0.9000

The baseline Decision Tree was trained using default hyperparameters
and evaluated using 5-fold cross-validation.

---

## 2. Grid Search

**Model:** RandomForestClassifier

**Total Combinations:** 72

**Cross-validation:** 5-fold

**Total Fits:** 360

**Best CV F1 Macro:** 0.9663

**Test Accuracy:** 0.9667

### Best Hyperparameters

- `max_depth`: 3
- `max_features`: sqrt
- `min_samples_split`: 2
- `n_estimators`: 50

Grid Search exhaustively evaluated all 72 combinations in the
specified hyperparameter grid.

---

## 3. Random Search

**Model:** RandomForestClassifier

**Number of Iterations:** 30

**Cross-validation:** 5-fold

**Total Fits:** 150

**Best CV F1 Macro:** 0.9663

**Test Accuracy:** 0.9667

### Best Hyperparameters

- `max_depth`: 3
- `max_features`: sqrt
- `min_samples_split`: 6
- `n_estimators`: 100

Random Search evaluated 30 randomly selected configurations from
the specified hyperparameter distributions.

---

## 4. Comparison

| Method | CV F1 Macro | Test Accuracy | Total Fits |
|---|---:|---:|---:|
| Baseline Decision Tree | 0.9663 | 0.9000 | 5 |
| Grid Search Random Forest | 0.9663 | 0.9667 | 360 |
| Random Search Random Forest | 0.9663 | 0.9667 | 150 |

Both Grid Search and Random Search improved the test accuracy from
0.9000 for the baseline Decision Tree to 0.9667.

Both tuning methods achieved the same CV F1 Macro score of 0.9663
and the same test accuracy of 0.9667 in this experiment.

Grid Search required 360 model fits, while Random Search required
only 150 model fits.

Therefore, Random Search achieved the same observed performance
using 210 fewer model fits than Grid Search.

For this experiment, Random Search was more computationally
efficient while achieving the same observed performance as Grid
Search.

---

## 5. Conclusion

The hyperparameter tuning experiment demonstrated that the tuned
Random Forest models improved test accuracy compared with the
baseline Decision Tree.

Grid Search exhaustively evaluated the complete hyperparameter grid,
while Random Search evaluated a smaller number of randomly selected
configurations.

Random Search achieved the same CV F1 Macro and test accuracy as
Grid Search while requiring substantially fewer model fits.

Therefore, Random Search provided the better efficiency-performance
trade-off in this experiment.