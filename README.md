# MATH 231 — Linear Algebra I (Queens College, Fall 2026)

A first-semester linear algebra course covering a broad range of foundational
topics with a strong emphasis on **computational applications and methods**. The
course pairs the theory of vector spaces, matrices, and eigenstructure with the
numerical analysis and machine-learning applications that make it useful in
practice, implemented across C++ (low-level kernels), Python (high-level demos),
and MATLAB (verification).

> This is a **tentative, wide-breadth draft** — deliberately more than one
> semester of material — from which topics are selected by interest and
> importance. Items are priority-tagged `[Core]` / `[Recommended]` /
> `[Enrichment]` so a one-semester path can be carved cleanly.

## Structure at a glance

The material is sequenced for strict dependency-correctness into **12 units**
across **4 arcs**:

| Arc | Units | Theme |
|-----|-------|-------|
| **I. Foundations** | 1–3 | Vector spaces & inner-product geometry; norms & similarity; complex numbers & quaternions |
| **II. Matrices & Continuous Math** | 4–6 | Matrix algebra, determinant/trace/norms; multivariable calculus (gradients, Hessians, Taylor); numerical foundations (complexity, floating point, conditioning, stability) |
| **III. Core Matrix Theory** | 7–9 | Linear systems & elimination; linear transformations; the four fundamental subspaces |
| **IV. Advanced Methods & Applications** | 10–12 | Orthogonality, least squares & factorizations (QR, Cholesky); eigenvalues, spectral theorem & SVD (PCA, spectral graph theory); numerical optimization & an ML capstone |

Each unit specifies its **domain** (Pure LA / Numerical LA / Multivariable
Calculus / Optimization / Machine Learning / Spectral Graph Theory), primary
objects, topics, key theorems, computational tools, algorithms, applications,
and explicit **enter/exit** prerequisites for progression.

**Domains spanned:** Pure & Numerical Linear Algebra, Multivariable Calculus,
Optimization, Machine Learning, and Spectral Graph Theory.

**Representative theorems:** Cauchy–Schwarz, Euler/De Moivre, Taylor
(uni/multivariate), Rank–Nullity, the Fundamental Theorem of Linear Algebra,
the Spectral Theorem, Schur, SVD/Eckart–Young, Perron–Frobenius, and
Abel–Ruffini.

**Representative algorithms:** Gram–Schmidt (classical & modified), Householder
QR, Cholesky, LU/Gaussian elimination, OLS, KNN, K-means, PCA, the power method,
Gauss–Newton, Levenberg–Marquardt, and (mention) BFGS.

## Computational projects & demos

A menu of applied projects — a small subset **assigned** to students, the rest
delivered as in-lecture **demos**:

- **Assigned:** K-means image color segmentation · Eigencats (PCA) · a mini-ML
  study (OLS + SVM + KNN with validation) · signal trilateration
  (Gauss–Newton / Levenberg–Marquardt).
- **Demos:** SVD + DCT image compression (the JPEG connection) · Latent Semantic
  Analysis document search · collaborative-filtering recommender · PageRank (the
  power method) · semantic word-embedding geometry.

## Assessment (tentative)

3 exams (final includes a cheat sheet), 4 assigned projects, and 8–10 homework
assignments blending hand computation with MATLAB verification.

## Repository layout

- **`course_plan/`** — the full unit-by-unit progression (`.tex` + compiled PDF),
  including the projects/demos appendix and a one-semester carving suggestion.
- **`tentative_textbooks/`** — referenced texts with bibliographic details and
  links (`.tex` + compiled PDF).

## Reference texts

- Boyd & Vandenberghe, *Introduction to Applied Linear Algebra* — applied spine
- Trefethen & Bau, *Numerical Linear Algebra* — numerical methods
- Strang, *Linear Algebra and Its Applications* — subspaces & intuition
- Axler, *Linear Algebra Done Right* — theoretical foundation
