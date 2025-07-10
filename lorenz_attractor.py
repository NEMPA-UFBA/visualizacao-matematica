from manim import (
    ThreeDScene, ThreeDAxes, VMobject, Dot, VGroup, color_gradient,
    Create, DEGREES, MathTex, UP, LEFT, ORIGIN, FadeIn, FadeOut,
    always_redraw, UpdateFromAlphaFunc
)
import numpy as np
from scipy.integrate import solve_ivp


def lorenz_system(t, state, sigma=10, rho=28, beta=8 / 3):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]


def ode_solution_points(function, state0, time, dt=0.01):
    solution = solve_ivp(
        function,
        t_span=(0, time),
        y0=state0,
        t_eval=np.arange(0, time, dt),
    )
    return solution.y.T


class LorenzAttractor(ThreeDScene):
    def construct(self):
        # Ajusta orientação inicial da câmera
        self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)

        # Eixos 3D
        axes = ThreeDAxes(
            x_range=(-30, 30, 10),
            y_range=(-30, 30, 10),
            z_range=(0, 60, 10),
        )
        self.add(axes)

        # Equações no canto
        equations = MathTex(
            r"\dot x = \sigma(y - x),\quad",
            r"\dot y = x(\rho - z) - y,\quad",
            r"\dot z = xy - \beta z",
            font_size=36
        )
        equations.to_corner(UP + LEFT)
        self.add_fixed_in_frame_mobjects(equations)
        self.play(FadeIn(equations))

        # Soluções para diferentes condições iniciais
        evolution_time = 25
        dt = 0.01
        n_curves = 8
        epsilon = 1e-5
        initial_states = [[10, 10, 10 + i * epsilon] for i in range(n_curves)]
        colors = color_gradient(["BLUE", "GREEN"], n_curves)

        curves = VGroup()
        dots = VGroup()
        tails = VGroup()

        for state, color in zip(initial_states, colors):
            points = ode_solution_points(lorenz_system, state, evolution_time, dt)
            curve_points = [axes.c2p(*p) for p in points]

            curve = VMobject(color=color).set_points_smoothly(curve_points)
            curves.add(curve)

            dot = Dot(curve_points[0], color=color)
            dots.add(dot)

            # Cria a cauda para cada ponto
            tail = always_redraw(lambda c=curve, d=dot: 
                VMobject(color=color, stroke_opacity=0.5).set_points_smoothly(
                    [d.get_center(), *[c.point_from_proportion(a) for a in np.linspace(0.95, 1.0, 5)]]
                )
            )
            tails.add(tail)

        # Anima o surgimento das curvas do campo
        self.play(*[Create(c) for c in curves], run_time=6)
        self.add(dots, tails)

        # Faz os pontos seguirem as curvas
        def get_updater(curve):
            def updater(dot, alpha):
                point = curve.point_from_proportion(alpha)
                dot.move_to(point)
            return updater

        animations = [
            UpdateFromAlphaFunc(dot, get_updater(curve))
            for dot, curve in zip(dots, curves)
        ]
        self.begin_ambient_camera_rotation(rate=0.1)
        self.play(*animations, run_time=12)
        self.wait()
        self.stop_ambient_camera_rotation()