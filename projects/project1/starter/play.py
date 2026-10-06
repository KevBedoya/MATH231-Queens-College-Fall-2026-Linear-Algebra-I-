"""
play.py -- watch your algorithms work, live.

PROVIDED.  Run it once your functions work:

    python play.py            the animations for the part TRACK names
    python play.py kmeans     only the k-means animations     (Part 2)
    python play.py marbles    only the five marbles           (Part 3)
    python play.py rates      only the learning-rate race     (Part 3)

Part 1 has no animation: its pictures are the decision regions that
runproject1.py saves in figures/.

Each animation plays in its own window.  Close the window to move on to the
next one.  Nothing here is graded -- it is for you, and for screenshots for
your report.
"""

import sys

import matplotlib.pyplot as plt
import numpy as np

import data
import viz
import project1 as p1


def show_kmeans():
    X = data.city()
    viz.watch_kmeans(X, data.city_bad_start(), p1.assign, p1.update, p1.wcss,
                     title="bad start")
    plt.show()
    start = data.random_start(X, 4, np.random.default_rng(231))
    viz.watch_kmeans(X, start, p1.assign, p1.update, p1.wcss,
                     title="random start")
    plt.show()


def show_marbles():
    paths = [p1.gradient_descent(p1.grad_f, s, 0.3, max_iter=2000)[0]
             for s in data.marble_starts()]
    viz.watch_descent(p1.f, paths, title="Five marbles, lr = 0.3")
    plt.show()


def show_rates():
    start = np.array([-4.0, 4.6])
    paths = [p1.gradient_descent(p1.grad_f, start, lr)[0] for lr in (0.1, 1.5)]
    viz.watch_descent(p1.f, paths, names=["lr = 0.1", "lr = 1.5"],
                      title="One start, two learning rates", pause=0.06)
    plt.show()


if __name__ == "__main__":
    shows = {"kmeans": show_kmeans, "marbles": show_marbles,
             "rates": show_rates}
    by_track = {"knn": [], "kmeans": ["kmeans"],
                "descent": ["marbles", "rates"]}
    track = str(getattr(p1, "TRACK", "")).strip().lower()
    chosen = sys.argv[1:] or by_track.get(track, list(shows))
    if not chosen:
        print("Part 1 has no animation: open the decision-region pictures "
              "that runproject1.py saved in figures/.")
    for name in chosen:
        if name not in shows:
            sys.exit(f"Unknown animation {name!r}: use kmeans, marbles or "
                     f"rates.")
        try:
            shows[name]()
        except NotImplementedError:
            print(f"{name}: a function it needs is not written yet.")
