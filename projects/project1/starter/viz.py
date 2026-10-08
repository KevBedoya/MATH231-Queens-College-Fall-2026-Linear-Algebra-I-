"""
viz.py -- pictures and animations for Project 1.

PROVIDED.  You do not need to read or edit this file; runproject1.py and
play.py call it for you.  (You are welcome to read it -- it is ordinary
matplotlib.)
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

COLOURS = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple",
           "tab:brown", "tab:pink", "tab:olive", "tab:cyan", "tab:gray"]


def _interactive():
    """True when figures appear on screen (False when they are only saved)."""
    return matplotlib.get_backend().lower() not in ("agg", "pdf", "svg", "ps",
                                                    "cairo", "template")


def _pause(fig, seconds):
    if _interactive():
        plt.pause(seconds)
    else:
        fig.canvas.draw()


def _finish(fig, filename):
    if filename is not None:
        fig.savefig(filename, dpi=130, bbox_inches="tight")
    if not _interactive():
        plt.close(fig)


# --------------------------------------------------------------------------
# Choice 1 -- k-nearest neighbours
# --------------------------------------------------------------------------

def plot_decision_regions(predict, X_train, y_train, title="", filename=None,
                          resolution=90, xlabel="feature 1",
                          ylabel="feature 2"):
    """Colour every point of the plane by the label predict() gives it.

    predict(q) must take a point q = [x, y] and return a label.
    """
    labels = sorted(set(y_train.tolist()))
    code = {lab: i for i, lab in enumerate(labels)}
    pad_x = 0.08 * (X_train[:, 0].max() - X_train[:, 0].min())
    pad_y = 0.08 * (X_train[:, 1].max() - X_train[:, 1].min())
    xs = np.linspace(X_train[:, 0].min() - pad_x, X_train[:, 0].max() + pad_x,
                     resolution)
    ys = np.linspace(X_train[:, 1].min() - pad_y, X_train[:, 1].max() + pad_y,
                     resolution)
    Z = np.zeros((len(ys), len(xs)))
    for r, yv in enumerate(ys):
        for c, xv in enumerate(xs):
            Z[r, c] = code[predict(np.array([xv, yv]))]

    fig, ax = plt.subplots(figsize=(6.4, 5.0))
    cmap = matplotlib.colors.ListedColormap(COLOURS[:len(labels)])
    ax.pcolormesh(xs, ys, Z, cmap=cmap, alpha=0.25, shading="auto",
                  vmin=-0.5, vmax=len(labels) - 0.5)
    for lab in labels:
        pts = X_train[y_train == lab]
        ax.scatter(pts[:, 0], pts[:, 1], s=18, color=COLOURS[code[lab]],
                   edgecolor="k", linewidth=0.3, label=lab)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend(loc="best", fontsize=8)
    _finish(fig, filename)


# --------------------------------------------------------------------------
# Choice 2 -- k-means
# --------------------------------------------------------------------------

def _draw_clusters(ax, X, labels, centres, title):
    ax.clear()
    for j in range(len(centres)):
        pts = X[labels == j]
        ax.scatter(pts[:, 0], pts[:, 1], s=12, color=COLOURS[j % 10],
                   alpha=0.7)
    ax.scatter(centres[:, 0], centres[:, 1], s=260, marker="*",
               color=[COLOURS[j % 10] for j in range(len(centres))],
               edgecolor="k", linewidth=1.2, zorder=3)
    ax.set_aspect("equal")
    ax.set_title(title)


def plot_clusters(X, labels, centres, title="", filename=None):
    """Points coloured by cluster, centres drawn as stars."""
    fig, ax = plt.subplots(figsize=(5.6, 5.6))
    _draw_clusters(ax, X, labels, centres, title)
    _finish(fig, filename)


def watch_kmeans(X, init_centres, assign, update, wcss, max_iter=30,
                 pause=0.9, title="k-means", filename=None):
    """Run Lloyd's algorithm one step at a time, redrawing after every step.

    It uses YOUR assign, update and wcss functions.
    """
    fig, ax = plt.subplots(figsize=(6.0, 6.0))
    centres = np.array(init_centres, dtype=float)
    labels = assign(X, centres)
    _draw_clusters(ax, X, labels, centres,
                   f"{title}: start,  J = {wcss(X, labels, centres):.2f}")
    _pause(fig, pause)
    for it in range(1, max_iter + 1):
        centres = update(X, labels, centres)
        _draw_clusters(ax, X, labels, centres,
                       f"{title}: pass {it}, centres moved,  "
                       f"J = {wcss(X, labels, centres):.2f}")
        _pause(fig, pause)
        new_labels = assign(X, centres)
        changed = int(np.sum(new_labels != labels))
        labels = new_labels
        _draw_clusters(ax, X, labels, centres,
                       f"{title}: pass {it}, {changed} points switched,  "
                       f"J = {wcss(X, labels, centres):.2f}")
        _pause(fig, pause)
        if changed == 0:
            break
    _finish(fig, filename)


def plot_elbow(ks, Js, filename=None):
    fig, ax = plt.subplots(figsize=(5.6, 4.0))
    ax.plot(ks, Js, "o-")
    ax.set_xlabel("number of clusters k")
    ax.set_ylabel("best within-cluster sum of squares J")
    ax.set_title("The elbow plot")
    ax.grid(alpha=0.3)
    _finish(fig, filename)


# --------------------------------------------------------------------------
# Choice 3 -- gradient descent
# --------------------------------------------------------------------------

def _grid(f, window, n):
    xs = np.linspace(-window, window, n)
    X, Y = np.meshgrid(xs, xs)
    Z = np.zeros_like(X)
    for r in range(n):
        for c in range(n):
            Z[r, c] = f(np.array([X[r, c], Y[r, c]]))
    return X, Y, Z


def _landscape_axes(f, window, title):
    fig = plt.figure(figsize=(12.5, 5.6))
    ax3 = fig.add_subplot(1, 2, 1, projection="3d")
    ax2 = fig.add_subplot(1, 2, 2)
    X, Y, Z = _grid(f, window, 70)
    ax3.plot_surface(X, Y, Z, cmap="terrain", alpha=0.75, linewidth=0,
                     antialiased=True, rstride=1, cstride=1)
    ax3.set_xlabel("x")
    ax3.set_ylabel("y")
    ax3.set_zlabel("f(x, y)")
    ax3.view_init(elev=42, azim=-60)
    X2, Y2, Z2 = _grid(f, window, 160)
    ax2.contourf(X2, Y2, Z2, levels=30, cmap="terrain", alpha=0.85)
    ax2.contour(X2, Y2, Z2, levels=30, colors="k", linewidths=0.25)
    ax2.set_aspect("equal")
    ax2.set_xlim(-window, window)
    ax2.set_ylim(-window, window)
    ax2.set_xlabel("x")
    ax2.set_ylabel("y")
    fig.suptitle(title)
    return fig, ax3, ax2


def plot_landscape(f, window=6.0, title="The landscape", filename=None):
    """The surface z = f(x, y) in 3-D, next to its contour map."""
    fig, ax3, ax2 = _landscape_axes(f, window, title)
    _finish(fig, filename)


def watch_descent(f, paths, window=6.0, pause=0.03, max_frames=160,
                  title="Gradient descent", names=None, filename=None,
                  save_frames=None):
    """Animate one or more marbles rolling down z = f(x, y).

    paths is a list of paths; each path is a list of points [x, y], as returned
    by gradient_descent.  All marbles move together, one step per frame (long
    runs are sped up by skipping frames), and each leaves a trail.

    When figures are only being saved (as in runproject1.py), only the final
    frame is drawn.  save_frames, if given, is a file-name pattern such as
    "frame_{:03d}.png": every frame is then drawn and saved, which is one way
    to make an animated GIF for your report.
    """
    fig, ax3, ax2 = _landscape_axes(f, window, title)
    paths = [np.array(p, dtype=float) for p in paths]
    heights = [np.array([f(q) for q in p]) for p in paths]
    longest = max(len(p) for p in paths)
    frames = np.unique(np.linspace(0, longest - 1,
                                   min(max_frames, longest)).astype(int))
    lift = 0.07 * (max(h.max() for h in heights) - min(h.min() for h in heights))
    if names is None:
        names = [f"marble {i + 1}" for i in range(len(paths))]

    trails3, dots3, trails2, dots2 = [], [], [], []
    for i in range(len(paths)):
        col = COLOURS[i % 10]
        trails3.append(ax3.plot([], [], [], "-", color=col, lw=2)[0])
        dots3.append(ax3.plot([], [], [], "o", color=col, ms=8,
                              markeredgecolor="k")[0])
        trails2.append(ax2.plot([], [], "-", color=col, lw=2)[0])
        dots2.append(ax2.plot([], [], "o", color=col, ms=7,
                              markeredgecolor="k", label=names[i])[0])
    ax2.legend(loc="upper right", fontsize=7)

    if not _interactive() and save_frames is None:
        frames = frames[-1:]
    for n, k in enumerate(frames):
        for i, (p, h) in enumerate(zip(paths, heights)):
            m = min(k, len(p) - 1)
            trails3[i].set_data(p[:m + 1, 0], p[:m + 1, 1])
            trails3[i].set_3d_properties(h[:m + 1] + lift)
            dots3[i].set_data([p[m, 0]], [p[m, 1]])
            dots3[i].set_3d_properties([h[m] + lift])
            trails2[i].set_data(p[:m + 1, 0], p[:m + 1, 1])
            dots2[i].set_data([p[m, 0]], [p[m, 1]])
        ax2.set_title(f"step {k}")
        _pause(fig, pause)
        if save_frames is not None:
            fig.savefig(save_frames.format(n), dpi=80)
    _finish(fig, filename)
