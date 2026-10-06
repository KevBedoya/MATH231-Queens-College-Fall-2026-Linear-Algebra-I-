"""
project1.py -- YOUR WORK for Project 1.

You do ONE of the three parts.  Set TRACK below to the part you chose, then
fill in every function marked TODO in that part; leave the other two parts
alone.  Each unfinished function raises NotImplementedError; runproject1.py
reports those tasks as "not implemented yet" and carries on with the rest, so
you can work through your part in order and run the driver as often as you
like.

Rules for this file:
  * NumPy only (plus Python itself).  No scikit-learn, no scipy.
  * Definitions only -- nothing should run or print when the file is imported.
    The TRACK line below is the one exception, and it only sets a name.
  * Do not change a function's name or the arguments it takes: runproject1.py
    calls them by name.

Name:
Generative AI used (tool and what for, or "none"):
"""

import numpy as np


# Which part are you doing?  Exactly one of:
#     "knn"       Part 1 -- k-nearest neighbours
#     "kmeans"    Part 2 -- k-means
#     "descent"   Part 3 -- gradient descent
# runproject1.py runs only this part, and only this part is graded.
TRACK = ""


# ==========================================================================
# Part 1 -- k-nearest neighbours            (TRACK = "knn")
# ==========================================================================

def distance(x, y, p=2):
    """The distance between points x and y under the p-norm.

    p = 1        Manhattan distance   sum of |x_i - y_i|
    p = 2        Euclidean distance   square root of sum of (x_i - y_i)^2
    p = np.inf   Chebyshev distance   largest |x_i - y_i|

    Use np.abs, np.sum, np.max, np.sqrt -- not np.linalg.norm.
    """
    # TODO (Task 1.1)
    raise NotImplementedError


def knn_predict(X_train, y_train, q, k, p=2):
    """Predict the label of the query point q by k-nearest neighbours.

    X_train  training points, one per row
    y_train  their labels (y_train[i] is the label of X_train[i])
    q        the query point
    k        how many neighbours vote
    p        which distance to use, as in distance()

    Steps (computational unit Sec. 6.1):
      1. Measure: the distance from q to every training point.
      2. Select:  the indices of the k smallest distances  (np.argsort helps).
      3. Vote:    the most common label among those k neighbours.
    Tie rule: if several labels share the most votes, return the one whose
    closest representative is nearest to q -- that is, walk through the
    neighbours from nearest to farthest and return the first label that has
    the top vote count.
    """
    # TODO (Task 1.2)
    raise NotImplementedError


def accuracy(X_train, y_train, X_test, y_test, k, p=2):
    """The fraction of test points that knn_predict labels correctly.

    Returns a number between 0 and 1.
    """
    # TODO (Task 1.3)
    raise NotImplementedError


def standardize(X_train, X_test):
    """Rescale every feature to mean 0 and standard deviation 1.

    Compute the mean and standard deviation of each feature (each column) from
    the TRAINING points only, then apply the same shift and scale to both sets:

        scaled = (X - mean) / sd

    X_train.mean(axis=0) averages down each column: it returns one mean per
    feature.  X_train.std(axis=0) does the same for the standard deviation.

    Returns X_train_scaled, X_test_scaled.
    """
    # TODO (Task 1.4)
    raise NotImplementedError


# ==========================================================================
# Part 2 -- k-means                         (TRACK = "kmeans")
# ==========================================================================

def assign(X, centres):
    """The assignment step: send every point to its nearest centre.

    X        data points, one per row
    centres  the k current centres, one per row
    Returns an integer array `labels` with labels[i] = j when centre j is the
    nearest centre to X[i].  Compare SQUARED distances -- same answer, and no
    square roots (computational unit Sec. 7.5).  If two centres are equally
    near, choose the one with the smaller index.
    """
    # TODO (Task 2.1)
    raise NotImplementedError


def update(X, labels, centres):
    """The update step: move every centre to the mean of its cluster.

    Returns a NEW array of centres (do not modify `centres` in place).  If a
    cluster has no points, leave its centre where it was.
    """
    # TODO (Task 2.2)
    raise NotImplementedError


def wcss(X, labels, centres):
    """The within-cluster sum of squares

        J = sum over all points i of  || X[i] - centres[labels[i]] ||^2
    """
    # TODO (Task 2.3)
    raise NotImplementedError


def kmeans(X, init_centres, max_iter=100):
    """Lloyd's algorithm (computational unit Sec. 12.3).

    Start from init_centres.  Repeat: assign, then update.  Stop when an
    assignment step changes no labels, or after max_iter passes.

    Returns (centres, labels, history), where history is the list of J
    values, one recorded after every update step.
    """
    # TODO (Task 2.4)
    raise NotImplementedError


# ==========================================================================
# Part 3 -- gradient descent                (TRACK = "descent")
# ==========================================================================

def f(p):
    """PROVIDED -- do not change.  The landscape for Part 3:

        f(x, y) = sin(x) cos(y) + 0.08 (x^2 + y^2)

    p is a point [x, y].
    """
    x, y = p
    return np.sin(x) * np.cos(y) + 0.08 * (x**2 + y**2)


def grad_f(p):
    """The gradient of f at p = [x, y], as a NumPy array [df/dx, df/dy].

    Work out the two partial derivatives by hand first (they go in your
    report), then code them here.
    """
    # TODO (Task 3.1)
    raise NotImplementedError


def gradient_descent(grad, x0, lr, tol=1e-6, max_iter=1000):
    """Gradient descent (computational unit Sec. 27.4), keeping the whole path.

    grad      a function returning the gradient at a point
    x0        the starting point
    lr        the learning rate (eta in lecture)
    tol       stop when the norm of the gradient is below tol
    max_iter  the iteration cap: take at most this many steps

    Each pass: compute g = grad(x); if the norm of g is below tol, stop and
    report success; otherwise step to x - lr * g and record the new point.

    Returns (path, converged):
      path       the list of points visited, starting with x0 itself
      converged  True if the gradient test passed, False if max_iter steps
                 were taken without it passing
    """
    # TODO (Task 3.2)
    raise NotImplementedError


def valley_census(endpoints, radius=0.01):
    """Group the end points of many descents into valleys.

    Go through the end points in order.  If an end point lies within `radius`
    (Euclidean distance) of a valley already found, it belongs to that valley;
    otherwise it starts a new valley, located at that end point.

    Returns (valleys, counts, which):
      valleys  list of valley locations, in the order they were found
      counts   counts[v] = how many end points landed in valley v
      which    which[i] = the index v of the valley end point i landed in
    """
    # TODO (Task 3.5)
    raise NotImplementedError
