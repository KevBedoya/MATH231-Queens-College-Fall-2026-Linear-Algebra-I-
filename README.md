# MATH 231 — Linear Algebra I (Queens College, Fall 2026)

## Homework out now

- [**Homework 1 — Vectors and Complex Numbers**](homework/MATH231_homework_1.pdf)
  — due **Sunday, September 20, 2026, 11:59 PM**

> **Homework 1 is not final yet.** It will be updated again later this week with
> the final set of questions. Pull the latest version before you start working,
> and check once more before you submit.

## Covered in class so far

Section ranges are **inclusive** at both ends. A section appearing on two
consecutive dates was started in the first meeting and finished in the second.

| Date | Lecture | Sections | What that was |
|---|---|---|---|
| Tue, Sep 1 | [Vector Unit, Part 1](lectures/vector-unit/MATH231_vectors_1_definition_and_arithmetic.pdf) | §1–§7 | magnitude and direction; the Euclidean norm; the derivative as a vector quantity; vector vs. scalar quantities; one-dimensional vectors; notation, $\mathbb{R}^2$, and signatures; addition and subtraction |
| Thu, Sep 3 | [Vector Unit, Part 1](lectures/vector-unit/MATH231_vectors_1_definition_and_arithmetic.pdf) | §7–§9 | addition and subtraction, the parallelogram rule and the triangle inequality; scalar multiplication, mirroring, and the eight algebraic laws; equality of vectors |
| Thu, Sep 3 | [Complex Numbers](lectures/vector-unit/MATH231_complex_numbers.pdf) | §1–§3 | where the real numbers run out; the imaginary unit and $a+bi$; the complex plane |

## Looking ahead

| Date | Lecture | Sections | What that will be |
|---|---|---|---|
| Tue, Sep 8 | [Complex Numbers](lectures/vector-unit/MATH231_complex_numbers.pdf) | §4–§7 | arithmetic — addition, multiplication, the conjugate, and division; the modulus, distance, and discs; the unit circle, trigonometric form, and Euler's formula; multiplication by $i$ as a rotation |
| Tue, Sep 8 | [Vector Unit, Part 2](lectures/vector-unit/MATH231_vectors_2_dot_product_and_projection.pdf) | from §10 | begins the part — relative orientation: parallel, orthogonal, and the angle between. The dot product and projection follow in §11–§12. |

> **Planned, not promised.** Pacing shifts, and this table is a forecast. The
> recap above it is the record of what actually happened.

## About this course

A first-semester linear algebra course covering a broad range of foundational
topics with a strong emphasis on **computational applications and methods**. The
course pairs the theory of vector spaces, matrices, and eigenstructure with the
numerical analysis and machine-learning applications that make it useful in
practice. **Python** is the only programming language used in this course.

> This is a **tentative, wide-breadth draft** — deliberately more than one
> semester of material — from which topics are selected by interest and
> importance. Items are priority-tagged `[Core]` / `[Recommended]` /
> `[Enrichment]` so a one-semester path can be carved cleanly.

## Course information

| | |
|---|---|
| **Institution** | Queens College (CUNY) |
| **Instructor** | Kevin Bedoya |
| **Term / session** | Fall 2026 — Regular Academic Session |
| **Meeting dates** | August 28, 2026 – December 21, 2026 |
| **Days / time** | Tuesday & Thursday, 12:10 – 2:00 PM |
| **Location** | Kiely Hall, Room 326 |
| **Credits / units** | 4 credits |
| **Instruction mode** | In-person |
| **Office hours** | Thursday, 3:00 – 4:00 PM |
| **Office location** | Kiely Hall, Room 508 — the Math lounge, in Kiely Tower |
| **Requirement designation** | Required Core — Mathematical & Quantitative Reasoning |
| **Enrollment requirement** | PRE: MATH 141 or 151, minimum grade C− |

The Math lounge is a good place to work — plenty of chalkboards and other people
doing mathematics. **Please email ahead** if you plan to come to office hours, so
I know to expect you.

## Grading

| Component | Weight | Detail |
|---|---|---|
| Homework — 5 assignments | 20% | 4% each; written and distributed by the instructor |
| Projects — 3 | 15% | 5% each; written and distributed by the instructor |
| Midterm 1 | 20% | |
| Midterm 2 | 20% | |
| Final exam | 25% | |
| **Total** | **100%** | |

Extra credit will be discussed as the semester progresses.

## Grades

Course grades are posted on **Gradesly** — <https://gradesly.com/users/sign_in> —
the platform students use to view their MATH 231 grades. Sign-in / enrollment
instructions will be announced by the instructor at the appropriate time.

## Repository layout

Every document is kept as LaTeX source alongside its compiled PDF; the PDF is
the artifact handed to students, and the `.tex` is what gets edited. Build
artifacts (`.aux`, `.log`, `.out`, …) are gitignored.

### Official course documents

- **`syllabus/`** — the Section 10 syllabus, `231_sec10_bedoya.tex` / `.pdf`.
  The filename follows the department's required `number_section_lastname`
  format; do not rename the exported PDF. This is the authoritative document.
- **`welcome-letter/`** — the letter sent to students before the term starts:
  logistics, platforms, and the textbook and programming stance.
- **`schedule/`** — the Fall 2026 meeting-by-meeting schedule (Tue/Thu), with
  college-closure and no-class days highlighted.

### Course design

- **`course_plan/`** — two companion progression documents: *A Natural
  Progression Through the Course Material* (`MATH231_progression_2026-07-01`),
  the unit-by-unit build order, and *A Historical Progression*
  (`MATH231_history_2026-08-04`), the same material in the order it was actually
  discovered.
- **`tentative_textbooks/`** — the referenced texts with bibliographic details
  and links.
- **`plan/`** — **working material, not finalized.** The candidate project and
  demo menu and the not-guaranteed topics list. Nothing here is assigned or
  promised; see `plan/README.md`. Where this directory and an official document
  disagree, the official document wins.

### Teaching material

- **`lectures/`** — lecture notes, grouped by unit:
  - `primer/` — the pre-course foundations review
  - `vector-unit/` — vectors, dot product and projection, norms and metrics,
    basis and span, orthogonality and subspaces, complex numbers
  - `matrix-unit/` — linear systems and matrix notation
  - `computational-unit/` — operation counting, $k$-nearest neighbours,
    $k$-means clustering, Gram–Schmidt, matrix multiplication
- **`setup/`** — student setup guides: 1 · Git and GitHub, 2 · Python, pip, and
  an IDE.

### Assessments

- **`homework/`** — the 5 homework assignments
- **`projects/`** — the 3 projects
- **`exams/`** — the two midterms and the final
- **`demos/`** — in-lecture computational demos

Projects, exams and demos are placeholders so far — those directories exist but
the material is written and distributed as the semester progresses. Assignments
that have been distributed are linked at the top of this README.

## Reference texts

- Boyd & Vandenberghe, *Introduction to Applied Linear Algebra* — applied spine
- Trefethen & Bau, *Numerical Linear Algebra* — numerical methods
- Strang, *Linear Algebra and Its Applications* — subspaces & intuition
- Axler, *Linear Algebra Done Right* — theoretical foundation
