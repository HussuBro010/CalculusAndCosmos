import numpy as np
from manim import *
import scipy as sp
import scipy.constants as spc


def summation(n: float, numberOfIter: float, expr):
    total = 0
    for i in range(n, int(numberOfIter + 1)):
        total += expr(i)
    return total


TEX_COLOR = TEAL_B


class Thumbnail(Scene):
    def construct(self):
        plane = NumberPlane()
        plane.set_opacity(0.3)
        plane.set_z_index(1)

        title = Title("Cool Graphs", font_size=80)
        title.set_z_index(4)

        rect = Rectangle(width=title.width, height=title.height+0.5, fill_opacity=1).move_to(title.get_center())
        rect.set_z_index(3)
        rect.fill_color = BLACK
        rect.stroke_width = 2
        rect.stroke_color = WHITE

        def func(x, y):
            if y == 0:  # Avoid division by zero
                return np.inf
            return x ** 2 + y ** 2 - 100 * (np.sin(x) / y) * np.cos(x * y)

        graph = always_redraw(
            lambda: ImplicitFunction(func, color=YELLOW_A))
        graph.set_z_index(2)

        self.add(plane, graph, rect, title)

class Intro(Scene):
    def construct(self):
        greet = Tex("Hello Everyone!!")
        aim = Tex(r"Today we will look at\\some Cool and weird Graphs")
        aim2 = Tex(r"We'll also look at how these graph change\\by changing specific values")

        self.wait(1)
        self.play(Write(greet))
        self.wait(2)
        self.play(ReplacementTransform(greet, aim))
        self.wait(2)
        self.play(TransformMatchingShapes(aim, aim2))
        self.wait(2)
        self.play(FadeOut(aim2))


class CoolGraphs(Scene):
    def construct(self):
        self.wait(1)
        self.sinGraph1()
        self.sinGraph2()
        self.cosxRound()
        self.sincosMod()
        self.sincurve()
        self.bubblyGraph()
        self.shiningStar()
        self.checkerCircle()
        self.wait(2)
        Outro.construct(self)

    def sinGraph1(self):
        plane = NumberPlane()
        plane.set_opacity(0.3)
        a = ValueTracker(1)
        b = ValueTracker(1)
        func = lambda x: np.sin(b.get_value() * x) + np.sin(a.get_value() * x)
        graph = always_redraw(
            lambda: FunctionGraph(func, color=YELLOW_A))

        graphTex1 = MathTex("f(x) = \sin(bx) + sin(ax)", color=TEX_COLOR)
        graphTex = always_redraw(
            lambda: MathTex(fr"f(x) = \sin({b.get_value():.1f}x) + sin({a.get_value():.1f}x)", color=TEX_COLOR).to_edge(
                UP))

        graph.z_index = 1
        graphTex.z_index = 2
        graphTex1.z_index = 2

        self.play(Create(graphTex1))
        self.wait(2)
        self.play(ReplacementTransform(graphTex1, graphTex))
        self.play(Create(plane))
        self.wait(2)
        self.play(Create(graph))
        self.wait(2)
        self.play(a.animate.set_value(5))
        self.play(b.animate.set_value(-1))
        self.wait(1)
        self.play(b.animate.set_value(6))
        self.play(a.animate.set_value(5.5))
        self.wait(2)
        self.play(FadeOut(graph, graphTex, plane))

    def sinGraph2(self):
        plane = NumberPlane()
        plane.set_opacity(0.3)
        a = ValueTracker(0)
        b = ValueTracker(0)
        func = lambda x: a.get_value() * (np.sin(b.get_value() * x)) + np.sin(x ** 2)
        graph = always_redraw(
            lambda: FunctionGraph(func, color=YELLOW_A))

        graphTex1 = MathTex(r"f(x) = a\sin bx\ + \sin\left(x^{2}\right)", color=TEX_COLOR)
        graphTex = always_redraw(
            lambda: MathTex(fr"f(x) = {a.get_value():.1f}\sin {b.get_value():.1f}x\ + \sin\left(x^{2}\right)",
                            color=TEX_COLOR).to_edge(
                UP))

        graph.z_index = 1
        graphTex.z_index = 2
        graphTex1.z_index = 2

        self.play(Create(graphTex1))
        self.wait(2)
        self.play(ReplacementTransform(graphTex1, graphTex))
        self.play(Create(plane))
        self.wait(2)
        self.play(Create(graph))
        self.wait(2)
        self.play(b.animate.set_value(0.5))
        self.play(a.animate.set_value(1.5))
        self.wait(1)
        self.play(a.animate.set_value(2))
        self.wait(1)
        self.play(b.animate.set_value(0))
        self.wait(2)
        self.play(FadeOut(graph, graphTex, plane))

    def cosxRound(self):
        plane = NumberPlane()
        plane.set_opacity(0.3)

        a = ValueTracker(0)

        func = lambda x: np.sin(x) + (a.get_value() * round(np.cos(x)))
        graph = always_redraw(
            lambda: FunctionGraph(func, color=YELLOW_A))

        graphTex1 = MathTex(fr"f(x) = \sin x\ +\ a \cdot", " round", r"\left(\cos x\right)\ + 2", color=TEX_COLOR)
        graphTex = always_redraw(
            lambda: MathTex(fr"f(x) = \sin x\ +\ {a.get_value():.1f} \cdot", r"\text{round}3",
                            r"\left(\cos x\right)\ + 2", color=TEX_COLOR).to_edge(UP))

        graph.z_index = 1
        graphTex.z_index = 2
        graphTex1.z_index = 2

        self.play(Create(graphTex1))
        self.wait(2)
        self.play(ReplacementTransform(graphTex1, graphTex))
        self.play(Create(plane))
        self.wait(2)
        self.play(Create(graph))
        self.wait(2)
        self.play(a.animate.set_value(2), run_time=2)
        self.wait(1)
        self.play(a.animate.set_value(-2), run_time=3)
        self.wait(1)
        self.play(a.animate.set_value(0), run_time=2)
        self.wait(3)
        self.play(FadeOut(graph, graphTex, plane))

    def sincosMod(self):
        plane = NumberPlane()
        plane.set_opacity(0.3)

        a = ValueTracker(0)
        b = ValueTracker(0)

        func = lambda x: (a.get_value() * np.sin(b.get_value() * x) % np.cos(x))

        graph = always_redraw(
            lambda: FunctionGraph(func, color=YELLOW_A, discontinuities=(2, 2)))

        graphTex1 = MathTex(r"f(x) = \text{mod}\left(a\sin bx,\ \cos x\right)", color=TEX_COLOR)
        graphTex = always_redraw(
            lambda: MathTex(fr"f(x) =", r"\operatorname{mod}",
                            fr"\left({a.get_value():.1f} \cdot \sin {b.get_value():.1f}x,\ \cos x\right)",
                            color=TEX_COLOR).to_edge(UP))

        graph.z_index = 1
        graphTex.z_index = 2
        graphTex1.z_index = 2

        self.play(Create(graphTex1))
        self.wait(2)
        self.play(ReplacementTransform(graphTex1, graphTex))
        self.play(Create(plane))
        self.wait(2)
        self.play(Create(graph))
        self.wait(2)
        self.play(b.animate.set_value(1), run_time=1.5)
        self.wait(1)
        self.play(a.animate.set_value(4), run_time=5)
        self.wait(1)
        self.play(b.animate.set_value(2), run_time=2)
        self.wait(1)
        self.play(a.animate.set_value(1), run_time=2)
        self.wait(3)
        self.play(FadeOut(graph, graphTex, plane))

    def sincurve(self):
        plane = NumberPlane()
        plane.set_opacity(0.3)

        a = ValueTracker(0)

        func = lambda x: np.sin(x) + summation(1, 5 * a.get_value(), lambda n: np.cos(n * x))

        graph = always_redraw(
            lambda: FunctionGraph(func, color=YELLOW_A, discontinuities=(2, 2)))

        graphTex1 = MathTex(r"f(x) = \sin x\ +\ \sum_{n=1}^{5a}\left(\cos nx\right)", color=TEX_COLOR)
        graphTex = always_redraw(
            lambda: MathTex(r"f(x) = \sin x\ +\ \sum_{n=1}^{5 \cdot", f"{a.get_value():.1f}", r"}\left(\cos nx\right)",
                            color=TEX_COLOR).to_edge(
                UP))

        graph.z_index = 1
        graphTex.z_index = 2
        graphTex1.z_index = 2

        self.play(Create(graphTex1))
        self.wait(2)
        self.play(ReplacementTransform(graphTex1, graphTex))
        self.play(Create(plane))
        self.wait(2)
        self.play(Create(graph))
        self.wait(2)
        self.play(a.animate.set_value(10), run_time=7)
        self.wait(3)
        self.play(FadeOut(graph, graphTex, plane))

    def bubblyGraph(self):
        plane = NumberPlane()
        plane.set_opacity(0.3)

        a = ValueTracker(0)

        def func(x, y):
            if y == 0:  # Avoid division by zero
                return np.inf
            return x ** 2 + y ** 2 - a.get_value() * (np.sin(x) / y) * np.cos(x * y)

        graph = always_redraw(
            lambda: ImplicitFunction(func, color=YELLOW_A))

        graphTex1 = MathTex(r"x^{2}+y^{2}=a\frac{\sin x}{y}\cdot\cos xy", color=TEX_COLOR)
        graphTex = always_redraw(
            lambda: MathTex(fr"x^{2}+y^{2}={a.get_value():.1f}", r"\cdot \frac{\sin x}{y}\cdot\cos xy",
                            color=TEX_COLOR).to_edge(
                UP))

        graph.z_index = 1
        graphTex.z_index = 2
        graphTex1.z_index = 2

        self.play(Create(graphTex1))
        self.wait(2)
        self.play(ReplacementTransform(graphTex1, graphTex))
        self.play(Create(plane))
        self.wait(2)
        self.play(Create(graph))
        self.wait(2)
        self.play(a.animate.set_value(100), run_time=10)
        self.wait(3)
        self.play(FadeOut(graph, graphTex, plane))

    def shiningStar(self):
        plane = NumberPlane()
        plane.set_opacity(0.3)

        a = ValueTracker(0)

        def func(x, y):
            if y == 0:  # Avoid division by zero
                return np.inf
            return x ** 2 * y ** 2 - a.get_value() * (np.sin(x ** 2) + np.sin(y ** 2)) - (
                    np.cos(x ** 2) + np.cos(y ** 2))

        graph = always_redraw(
            lambda: ImplicitFunction(func, color=YELLOW_A)
        )

        graphTex1 = MathTex(r"x^{2}y^{2} = a(\sin x^{2}+\sin y^{2})+(\cos x^{2}+\cos y^{2})", color=TEX_COLOR)
        graphTex = always_redraw(
            lambda: MathTex(fr"x^{2}y^{2} = {a.get_value():.1f} \cdot (\sin x^{2}+\sin y^{2})+(\cos x^{2}+\cos y^{2})",
                            color=TEX_COLOR).to_edge(
                UP))

        graph.z_index = 1
        graphTex.z_index = 2
        graphTex1.z_index = 2

        self.play(Create(graphTex1))
        self.wait(2)
        self.play(ReplacementTransform(graphTex1, graphTex))
        self.play(Create(plane))
        self.wait(2)
        self.play(Create(graph))
        self.wait(2)
        self.play(a.animate.set_value(300), run_time=10)
        self.wait(3)
        self.play(FadeOut(graph, graphTex, plane))

    def checkerCircle(self):
        plane = NumberPlane()
        plane.set_opacity(0.3)

        a = ValueTracker(0)
        b = ValueTracker(0)

        def func(x, y):
            if y == 0:  # Avoid division by zero
                return 0
            return (x ** 2) * y - (np.sin(y)) + (np.cos(x) / (a.get_value() * x + b.get_value()))

        graph = always_redraw(
            lambda: ImplicitFunction(func, color=YELLOW_A)
        )

        graphTex1 = MathTex(r"x^{2}y\ =\sin y-\frac{\cos x}{ax+b}", color=TEX_COLOR)
        graphTex = always_redraw(
            lambda: MathTex(
                fr"x^{{2}}y\ =\sin y-\frac{{\cos x}}{{ {a.get_value():.1f} \cdot x + {b.get_value():.1f} }}",
                color=TEX_COLOR).to_edge(
                UP))

        graph.z_index = 1
        graphTex.z_index = 2
        graphTex1.z_index = 2

        self.play(Create(graphTex1))
        self.wait(2)
        self.play(ReplacementTransform(graphTex1, graphTex))
        self.play(Create(plane))
        self.wait(2)
        self.play(Create(graph))
        self.wait(2)
        self.play(b.animate.set_value(-5), run_time=2)
        self.wait(1)
        self.play(b.animate.set_value(10), run_time=4)
        self.wait(1)
        self.play(a.animate.set_value(50), run_time=7)
        self.wait(3)
        self.play(FadeOut(graph, graphTex, plane))


class Outro(Scene):
    def construct(self):
        thanks = Text("Thanks for watching!", font_size=70)

        self.wait(1)
        self.play(Write(thanks))
        self.wait(2)
        self.play(Unwrite(thanks))
        self.wait(1)


with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": False}):
    scene = Thumbnail()
    scene.render()
