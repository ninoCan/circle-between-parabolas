

import marimo

__generated_with = "0.13.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import sympy as sym
    return mo, sym


@app.cell
def _(mo):
    mo.md(
        r"""
        Let's say we have two parabolas with equations: 

        $$
        \mathcal{P}_1: \quad y = x^2,\qquad
        \mathcal{P}_2: \quad y = x^2 - \frac{1}{2},
        $$

        Now, consider the circle centered on the x-axis and tangent to both parabolas on the first and fourth quadrants. Then, its Cartesian equation will be:

        $$
        \mathcal{C}:\ (x - a)^2 + y^2=r^2,
        $$

        where $a$ is the center x-coordinate and $r$ the radius.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        Since the parabolas are tangent to the circle, they will meet at two points $P_1$ and $P_2$. Say $\theta_1$ and $\theta_2$ are the angles between the x-axis. These points have coordinates:

        $$
        P_1: (a+r\cos\theta_1,\ r\sin\theta_2),\qquad
        P_2: (a+r\cos\theta_2,\ r\sin\theta_2).
        $$

        The tangent lines at these points will have the same slope, given by the derivative of the parabolic equation: $m = 2x$.
        Granted that their perpendicular line will pass through the center of the circle, it will follow the following equation:

        $$
        y_C = - \frac{x_C}{m}+b_i\quad\Rightarrow\quad b_i= \frac{x_C}{m} = \frac{x_C}{2 x_{P_i}}.
        $$

        Therefore, the perpendicular lines will be described by the equations:

        $$
        \mathcal{L}_1: \quad y = \frac{a - x}{2(a+r\cos\theta_1)},\qquad
        \mathcal{L}_2: \quad y = \frac{a - x}{2(a+r\cos\theta_2)}.
        $$
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        Evaluating these equations at the intersection points, we obtain a system of **4 equations**$-\mathcal{P}_1(P_1)$, $\mathcal{L}_1(P_1)$, $\mathcal{P}_2(P_2)$, $\mathcal{L}_2(P_2)-$in **4 unknowns**$-a$, $r$, $\theta_1$, $\theta_2$.

        However, they are not independent. We must place a constraint between $\theta_1$ and $\theta_2$. Using that $\widehat{P_2CP_1}$ forms an isosceles triangle, and that the angle opposite to the base $\overline{P_1P_2}$ is given by $\pi + \theta_1 - \theta_2$:

        $$ \sqrt{(P_{1_x} - P_{2_x})^2+(P_{1_y} -P_{2_y})^2} = 2 r (\sin\theta_1\cos\theta_2 - \cos\theta_1\sin\theta_2)$$

        Finally, we get the system of equations:

        $$
        r\sin\theta_1 = a + r\cos\theta_1,\\
        r\sin\theta_1 = \frac{- r\cos\theta_1}{2(a+r\cos\theta_1)},\\
        r\sin\theta_2 = a + r\cos\theta_2 - \frac{1}{2},\\
        r\sin\theta_2 = \frac{- r\cos\theta_2}{2(a+r\cos\theta_2)},\\
        \sqrt{(\cos\theta_1 -\cos\theta_2)^2 + (\sin\theta_1 - \sin\theta_2)^2} = 2 (\sin\theta_1\cos\theta_2 - \cos\theta_1\sin\theta_2).
        $$

        """
    )
    return


#@app.cell
#def _(sym):
#    d = sym.Rational(1, 2)
#    a = sym.Symbol("a", positive=True)
#    r = sym.Symbol("r", positive=True)
#    t1 = sym.Symbol("t1", positive=True)
#    t1_range = sym.And(t1 > 0, t1 < sym.pi)
#    t2 = sym.Symbol("t2", positive=True)
#    t2_range = sym.And(t2 > 0, t2 < sym.pi)

#    c1 = sym.cos(t1)
#    s1 = sym.sin(t1)
#    c2 = sym.cos(t2)
#    s2 = sym.sin(t2)

#    #sym.nsolve(
#    sym.solve(
#        [
#            r * s1 - a - r * c1,
#            2 * r * s1 * (a + r *c1) + r * c1 ,
#            r * s2 - a - r * c2 + d,
#            2 * r * s2 * (a + r *c2) + r * c2,
#            sym.sqrt((c1 - c2) ** 2  + (s1 - s2) ** 2 ) - 2 * (s1 * c2 - c1 * s2),
#        ],
#        [a, r, t1, t2],
#        #[0.5, 0.2, 0.5, 0.5],
#        dict=True
#    )
#    return


if __name__ == "__main__":
    app.run()
