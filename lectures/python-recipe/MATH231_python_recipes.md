# MATH 231 — Python Recipe Book

**Linear Algebra I · Queens College, CUNY · Fall 2026**
Instructor: Kevin Bedoya

A catalogue of the library calls that perform the operations and algorithms
covered in lecture. Every recipe is a short block you can copy straight into a
file or a notebook.

This is a **reference**, not a tutorial — look things up as you need them rather
than reading front to back. Each entry names the lecture material it corresponds
to, so you can move between the notes and the code in either direction.

---

## Contents

1. [Setup](#1-setup)
2. [Vectors](#2-vectors)
3. [Complex numbers](#3-complex-numbers)
4. [Matrices](#4-matrices)
5. [Bases, rank, and orthogonality](#5-bases-rank-and-orthogonality)
6. [Linear systems](#6-linear-systems)
7. [Floating point](#7-floating-point)
8. [Algorithms from the computational unit](#8-algorithms-from-the-computational-unit)
9. [Quick reference](#9-quick-reference)
10. [Common pitfalls](#10-common-pitfalls)

---

## 1. Setup

Install once (see **Setup Guide 2** for the full walkthrough):

```
python -m pip install numpy scipy
```

Every block below assumes this import:

```python
import numpy as np
```

A few recipes additionally need SciPy; those are marked **(SciPy)** and carry
their own import line.

---

## 2. Vectors

*Vector unit, §1–§24.*

### Creating a vector

```python
u = np.array([1, 2, 3])
v = np.array([4, 5, 6])
```

Use floats when the results will not be whole numbers — this avoids surprises
when dividing:

```python
w = np.array([1.0, 2.0, 3.0])       # or np.array([1, 2, 3], dtype=float)
```

### Components and length of the list

```python
u[0]        # 1   — first component (indexing starts at 0)
u[-1]       # 3   — last component
len(u)      # 3   — number of components, the n in R^n
u.shape     # (3,)
```

### Addition, subtraction, scaling

*§7, §8.*

```python
u + v          # array([5, 7, 9])
u - v          # array([-3, -3, -3])
3 * u          # array([3, 6, 9])
-u             # array([-1, -2, -3])
```

Adding vectors of different lengths is an error, exactly as in lecture.

### Dot product

*§11.3.*

```python
np.dot(u, v)    # 32
u @ v           # 32  — the @ operator, preferred
```

### Norm

*§11.9.*

```python
np.linalg.norm(u)              # 3.7416...  the Euclidean norm ||u||
np.sqrt(u @ u)                 # same value, via v'v = ||v||^2
```

### Unit vector (normalisation)

*§11.9.*

```python
u_hat = u / np.linalg.norm(u)
np.linalg.norm(u_hat)          # 1.0
```

### Distance between two vectors

*§14.2.*

```python
np.linalg.norm(u - v)          # the Euclidean distance d(u, v)
```

### Angle and cosine similarity

*§10, §11.6.*

```python
cos_theta = (u @ v) / (np.linalg.norm(u) * np.linalg.norm(v))
theta = np.arccos(np.clip(cos_theta, -1.0, 1.0))    # radians, in [0, pi]
np.degrees(theta)                                    # in degrees
```

`np.clip` guards against rounding pushing the ratio a hair outside `[-1, 1]`,
which would make `arccos` fail.

### Projection and component

*§12.4.*

```python
# projection of v onto u  —  proj_u(v)
proj = (u @ v) / (u @ u) * u

# the scalar component  —  comp_u(v)
comp = (u @ v) / np.linalg.norm(u)

# the orthogonal piece  —  v - proj_u(v), orthogonal to u
orth = v - proj
orth @ u                        # ~0
```

### Other norms

*§14.3.*

```python
np.linalg.norm(u, ord=1)        # Manhattan (l1)
np.linalg.norm(u, ord=2)        # Euclidean (l2) — the default
np.linalg.norm(u, ord=np.inf)   # Chebyshev (l-infinity)
np.linalg.norm(u, ord=3)        # general p-norm, p = 3
```

### Testing orthogonality

*§11.7.*

```python
a = np.array([1, 0])
b = np.array([0, 1])
np.isclose(a @ b, 0.0)          # True
```

Compare against zero with `np.isclose`, never with `==` — see §7 and §10.

---

## 3. Complex numbers

*Complex numbers lecture.*

### Creating

Python writes the imaginary unit as `j`, and it must carry a coefficient — `1j`,
not `j`:

```python
z = 3 + 4j
w = complex(1, -2)              # 1 - 2j
```

### Arithmetic

```python
z + w
z * w
z / w
z ** 2
```

### Real part, imaginary part, conjugate

```python
z.real          # 3.0
z.imag          # 4.0
z.conjugate()   # (3-4j)
np.conj(z)      # same
```

### Modulus and argument

```python
abs(z)              # 5.0        — the modulus |z|
np.angle(z)         # 0.9272...  — the argument, in radians
np.angle(z, deg=True)
```

### Polar form and Euler's formula

```python
r, theta = abs(z), np.angle(z)
r * np.exp(1j * theta)          # back to 3+4j
np.exp(1j * np.pi)              # ~ -1 + 0j  (Euler's identity)
```

### Powers — de Moivre

```python
z ** 5                          # direct
r**5 * np.exp(5j * theta)       # via polar form; same answer
```

### Roots of unity

```python
n = 5
k = np.arange(n)
roots = np.exp(2j * np.pi * k / n)
```

### Roots of a polynomial

Coefficients run from the highest power down. For `x^2 + 1`:

```python
np.roots([1, 0, 1])             # array([0.+1.j, 0.-1.j])
```

### Arrays of complex numbers

```python
zs = np.array([1 + 2j, 3 - 1j])
np.abs(zs)                      # moduli, elementwise
zs.conj()                       # conjugates
```

---

## 4. Matrices

*Matrix unit, §3–§8.*

### Creating a matrix

A matrix is a two-dimensional array — a list of rows:

```python
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[2, 3],
              [4, 5],
              [6, 7]])          # 3 x 2
```

### Shape and entries

*§3.1.*

```python
A.shape         # (2, 2)   — (rows, columns)
B.shape         # (3, 2)
A.shape[0]      # 2  — number of rows, m
A.shape[1]      # 2  — number of columns, n
A.size          # 4  — total entries, m*n

A[0, 1]         # entry a_12 — row 0, column 1 (zero-based!)
B[2, 1]         # entry b_32 = 7
```

> Lecture indexes from 1 (`a_11` is the top-left entry); Python indexes from 0
> (`A[0, 0]` is the top-left entry). Subtract one from each lecture index.

### Rows and columns

*§3.5.*

```python
A[0, :]         # first row, as a 1-D array
A[:, 1]         # second column, as a 1-D array
B[1:3, :]       # rows 1 and 2
```

### Special matrices

*§4.*

```python
np.eye(3)                       # 3x3 identity
np.zeros((2, 3))                # 2x3 zero matrix
np.ones((2, 3))
np.diag([3, -1, 5])             # diagonal matrix diag(3, -1, 5)
np.diag(A)                      # extract the diagonal of A
np.triu(A)                      # upper triangular part
np.tril(A)                      # lower triangular part
np.diag([1, 1, 1], k=1)         # a superdiagonal — building banded matrices
```

Building a tridiagonal matrix:

```python
main = 2 * np.eye(4)
off  = -np.diag(np.ones(3), k=1) - np.diag(np.ones(3), k=-1)
T = main + off
```

### Addition and scaling

*§5.*

```python
A + A
A - A
2.5 * A
```

Shapes must match exactly, as in lecture.

### Transpose

*§6.*

```python
B.T             # 2 x 3
A.T
```

### Symmetry

*§6.5.*

```python
S = np.array([[1, 2, 3],
              [2, 5, 4],
              [3, 4, 6]])
np.allclose(S, S.T)             # True — S is symmetric
```

### Matrix multiplication

*§8.1. Also computational unit §21–§23.*

```python
C = A @ A                       # use @, not *
np.matmul(A, A)                 # identical
```

The inner dimensions must agree; NumPy raises an error if they do not.

### Matrix–vector product

*§8.5, and §2.3.*

```python
x = np.array([5, 6])
A @ x                           # array([17, 39])
```

### Inner and outer products

*§7.*

```python
u = np.array([1, 2, 3])
v = np.array([4, 5, 6])

u @ v                           # 32        — inner product, a scalar
np.outer(u, v)                  # 3x3       — outer product, a matrix

p = np.array([1, 2, 3])
q = np.array([4, 5])
np.outer(p, q)                  # 3x2 — lengths need not match
```

### Powers of a matrix

```python
np.linalg.matrix_power(A, 3)    # A @ A @ A
```

### Sparse matrices **(SciPy)**

*§4.6.*

```python
from scipy import sparse

M = np.array([[0, 0, 4],
              [0, 0, 0],
              [7, 0, 0]])
S = sparse.csr_matrix(M)        # stores only the nonzeros
S.nnz                           # 2 — number of stored entries
S.toarray()                     # back to a dense array
```

---

## 5. Bases, rank, and orthogonality

*Vector unit §16–§21; Gram–Schmidt in computational unit §16–§20.*

### Are these vectors linearly independent?

*§18.4.*

Stack them as **columns** and compare the rank to the number of vectors:

```python
V = np.column_stack([np.array([1, 0]), np.array([0, 1])])
rank = np.linalg.matrix_rank(V)
independent = (rank == V.shape[1])      # True
```

A dependent set:

```python
V2 = np.column_stack([np.array([1, 2]), np.array([2, 4])])
np.linalg.matrix_rank(V2)               # 1 — the second is twice the first
```

### Dimension of a span

The rank *is* the dimension of the span of the columns:

```python
np.linalg.matrix_rank(V2)               # 1 — a line, not a plane
```

### Orthonormal basis from a set of vectors

*Computational unit §18 — Gram–Schmidt.*

```python
V = np.column_stack([np.array([1., 1., 0.]),
                     np.array([1., 0., 1.]),
                     np.array([0., 1., 1.])])

Q, R = np.linalg.qr(V)
```

The columns of `Q` are an orthonormal basis for the span of the columns of `V`,
with the same nesting property established in lecture: the first `k` columns of
`Q` span the same space as the first `k` columns of `V`.

> Columns of `Q` may differ from hand-computed Gram–Schmidt by a factor of −1.
> Both answers are correct; a unit vector and its negative both work as a basis
> direction.

### Checking orthonormality

```python
np.allclose(Q.T @ Q, np.eye(Q.shape[1]))    # True
```

This is the Kronecker-delta condition `<q_i, q_j> = delta_ij` written all at
once: every column against every column gives the identity.

### Coordinates against an orthonormal basis

*Computational unit §16.3 — coordinates are dot products.*

```python
u = np.array([1., 2., 3.])
beta = Q.T @ u                  # all n coordinates at once

np.allclose(Q @ beta, u)        # True — reconstruction check
```

### Projection onto a subspace

Given an orthonormal basis `Q` for a subspace:

```python
u_proj = Q @ (Q.T @ u)          # the part of u lying in the subspace
u_perp = u - u_proj             # the part orthogonal to it
```

---

## 6. Linear systems

*Matrix unit §1–§2, §8.6.*

### Building the system

The coordinate problem puts the basis vectors in the **columns**:

```python
V = np.column_stack([np.array([1., 1.]), np.array([1., -1.])])
u = np.array([3., 1.])
```

### Solving

```python
x = np.linalg.solve(V, u)       # coordinates of u against the basis
np.allclose(V @ x, u)           # True — always verify
```

> The method behind `solve` is covered in the next part of the matrix unit. The
> call is listed here so you can check work you have done by hand.

### When there is no unique solution

`np.linalg.solve` requires a square, invertible matrix. If the columns are
dependent it raises `LinAlgError` — which corresponds exactly to the failure
case in lecture, where the basis hypothesis breaks down.

```python
try:
    np.linalg.solve(np.array([[1., 2.], [2., 4.]]), np.array([3., 1.]))
except np.linalg.LinAlgError as e:
    print("no unique solution:", e)
```

---

## 7. Floating point

*Computational unit §3–§4.*

### Machine epsilon and precision

```python
np.finfo(np.float64).eps        # 2.22e-16  — double precision
np.finfo(np.float32).eps        # 1.19e-07  — single precision
np.finfo(np.float64).max
```

### Choosing a precision

```python
a = np.array([1, 2, 3], dtype=np.float32)       # single
b = np.array([1, 2, 3], dtype=np.float64)       # double — NumPy's default
a.dtype
```

### The classic demonstration

```python
0.1 + 0.2 == 0.3                # False
0.1 + 0.2                       # 0.30000000000000004
np.isclose(0.1 + 0.2, 0.3)      # True — the right way to compare
```

### Comparing arrays

```python
a = np.array([1.0, 2.0, 3.0])
b = np.array([1.0, 2.0, 3.0000000001])

np.isclose(a, b)                        # array([True, True, True])
np.allclose(a, b)                       # True — every entry is close
np.allclose(a, b, atol=1e-14, rtol=0)   # False — with a tighter tolerance
```

### Watching cancellation

```python
big = 1e16
big + 1 - big                   # 0.0 — the 1 was lost entirely
```

---

## 8. Algorithms from the computational unit

### Matrix multiplication

*§21–§23.*

```python
A = np.random.rand(200, 300)
B = np.random.rand(300, 400)
C = A @ B
C.shape                         # (200, 400)
```

Timing it, to see the cubic cost for yourself:

```python
import time
n = 400
A = np.random.rand(n, n)
B = np.random.rand(n, n)
t0 = time.perf_counter()
C = A @ B
print(f"{n=}  {time.perf_counter() - t0:.3f} s")
```

Double `n` and the time should grow by roughly a factor of eight.

### Gram–Schmidt / orthonormalisation

*§16–§20.* See [§5](#5-bases-rank-and-orthogonality) above — `np.linalg.qr`.

### k-nearest neighbours **(SciPy)**

*§5–§10.*

```python
from scipy.spatial import KDTree

X = np.array([[0., 0.], [1., 0.], [0., 1.], [4., 4.], [5., 4.]])
query = np.array([0.2, 0.2])

tree = KDTree(X)
distances, indices = tree.query(query, k=3)     # the 3 nearest points
```

For distances alone, without the tree:

```python
from scipy.spatial.distance import cdist
D = cdist(np.atleast_2d(query), X)              # 1 x N matrix of distances
nearest = np.argsort(D[0])[:3]                  # indices of the 3 closest
```

### k-means clustering **(SciPy)**

*§11–§15.*

```python
from scipy.cluster.vq import kmeans2

data = np.random.rand(100, 2)
centroids, labels = kmeans2(data, k=3, seed=0)
```

`centroids` is a `k x n` array of cluster centres; `labels[i]` says which
cluster point `i` belongs to.

### LU factorisation **(SciPy)**

```python
from scipy.linalg import lu

P, L, U = lu(np.array([[2., 1.], [4., 3.]]))
```

---

## 9. Quick reference

| Task | Call |
|---|---|
| Vector | `np.array([1, 2, 3])` |
| Matrix | `np.array([[1, 2], [3, 4]])` |
| Shape | `A.shape` |
| Dot / inner product | `u @ v` |
| Outer product | `np.outer(u, v)` |
| Norm | `np.linalg.norm(v)` |
| p-norm | `np.linalg.norm(v, ord=p)` |
| Distance | `np.linalg.norm(u - v)` |
| Normalise | `v / np.linalg.norm(v)` |
| Projection onto `u` | `(u @ v) / (u @ u) * u` |
| Matrix product | `A @ B` |
| Matrix–vector product | `A @ x` |
| Transpose | `A.T` |
| Identity | `np.eye(n)` |
| Diagonal matrix | `np.diag([...])` |
| Upper / lower triangle | `np.triu(A)` / `np.tril(A)` |
| Matrix power | `np.linalg.matrix_power(A, k)` |
| Rank | `np.linalg.matrix_rank(A)` |
| Orthonormal basis | `Q, R = np.linalg.qr(V)` |
| Solve a system | `np.linalg.solve(A, b)` |
| Stack vectors as columns | `np.column_stack([u, v])` |
| Modulus of a complex number | `abs(z)` |
| Argument | `np.angle(z)` |
| Conjugate | `z.conjugate()` |
| Polynomial roots | `np.roots([...])` |
| Machine epsilon | `np.finfo(np.float64).eps` |
| Approximate equality | `np.isclose` / `np.allclose` |

---

## 10. Common pitfalls

**`*` is not matrix multiplication.** For arrays, `*` multiplies entry by entry.
Matrix multiplication is `@`.

```python
A = np.array([[1, 2], [3, 4]])
A * A       # array([[1, 4], [9, 16]])    — entrywise squares
A @ A       # array([[7, 10], [15, 22]])  — the matrix product
```

**A 1-D array has no orientation.** `u.T` does nothing to a 1-D array — it is
neither a row nor a column. NumPy figures out the right interpretation inside
`@`, so this rarely matters. When you genuinely need a column, reshape:

```python
u = np.array([1, 2, 3])
u.shape             # (3,)
u.T.shape           # (3,)  — unchanged!
u.reshape(-1, 1)    # a genuine 3 x 1 column
u.reshape(1, -1)    # a genuine 1 x 3 row
```

**Integer arrays divide strangely.** An array of ints stays an int array, and
some operations will truncate. Use floats when the answer is not a whole number:

```python
np.array([1, 2, 3]) / 2         # fine — NumPy promotes to float here
np.array([1., 2., 3.])          # but be explicit when it matters
```

**Never test floating-point values with `==`.** Use `np.isclose` or
`np.allclose`. This applies to checking orthogonality, checking that a vector is
a unit vector, and verifying any reconstruction.

**Do not use `np.matrix`.** It is a deprecated class that changes what `*`
means. Use ordinary arrays with `@` throughout.

**Indices start at zero.** Lecture's `a_11` is `A[0, 0]`.

**Shape errors are your friend.** If NumPy refuses to multiply, the dimensions
genuinely do not line up — check them against the rule that the columns of the
left matrix must equal the rows of the right.

---

## Getting help

Every function above has built-in documentation:

```python
help(np.linalg.qr)
```

Official references: [NumPy](https://numpy.org/doc/stable/) ·
[NumPy linear algebra](https://numpy.org/doc/stable/reference/routines.linalg.html) ·
[SciPy](https://docs.scipy.org/doc/scipy/)

Questions to <Kevin.Bedoya32@stu-mail.qc.cuny.edu> or the class Discord.
