import numpy as np
from manim import *


class Thumbnail(Scene):
    def construct(self):
        title = Title("Calculus - Limits", font_size=100)
        ax = Axes(
            x_range=(-1, 6),
            y_range=(-1, 6),
            x_length=5,
            y_length=5
        ).shift(DOWN * 1.3, LEFT * 2)

        funcTex = MathTex("f(x)").next_to(ax, UP)
        limTex = MathTex(r"\lim_{x \to x_0} f(x) = L", font_size=80).shift(RIGHT * 3.5)

        def f(x):
            return 0.15 * x ** 2

        graph = ax.plot(lambda a: f(a), x_range=(-1, 6))
        graph.set_color(YELLOW)

        self.add(title, limTex, ax, funcTex, graph)


class LimitsIntro(Scene):
    def construct(self):
        ax = Axes(
            x_range=(-1, 6),
            y_range=(-1, 6),
            x_length=5,
            y_length=5
        ).shift(LEFT * 3)

        funcTex = MathTex("f(x)").next_to(ax, UP)

        def f(x):
            return 0.15 * x ** 2

        graph = ax.plot(lambda a: f(a), x_range=(-1, 6))
        graph.set_color(YELLOW)

        caption1 = Tex(
            r"Let $f(x)$ be a function defined on an open interval about point $x_0$,\\except possibly $x_0$ itself",
            font_size=30).to_edge(
            DOWN)

        rangeBrace = BraceBetweenPoints(ax.c2p(3, 0), ax.c2p(5, 0))

        rangeLines = [
            DashedLine(ax.c2p(3, 0), ax.c2p(3, 6)),
            DashedLine(ax.c2p(5, 0), ax.c2p(5, 6))
        ]

        x0 = Dot(ax.c2p(4, f(4)))
        x0Label = MathTex("x_0", font_size=30).next_to(x0, UP, buff=0.15)

        dashedLineL = Line(x0.get_center(), ax.c2p(0, 2.4), color=RED)
        Ltex = MathTex("L", font_size=30).next_to(dashedLineL, LEFT, buff=0.15)

        value = ValueTracker(3)
        caption2 = Tex("If $f(x)$ gets arbitrarily close to L ...", font_size=30).to_edge(DOWN)

        x = always_redraw(lambda: Dot(ax.c2p(value.get_value(), f(value.get_x())), color=GREEN))
        xDashedLines = [
            always_redraw(lambda: DashedLine(x.get_center(), ax.c2p(0, f(value.get_value())), color=RED)),
            always_redraw(lambda: DashedLine(x.get_center(), ax.c2p(value.get_value(), 0), color=BLUE))
        ]

        labels = [
            always_redraw(lambda: Tex("x", font_size=30).next_to(xDashedLines[1], DOWN, buff=0.2)),
            always_redraw(lambda: Tex("F", font_size=30).next_to(xDashedLines[0], LEFT, buff=0.2))
        ]
        caption3 = Tex("We say $F$ approaches the limit $L$ as $x$ approaches to $x_0$ and we write",
                       font_size=30).to_edge(DOWN)

        limTex = MathTex(r"\lim_{x \to x_0} f(x) = L", font_size=60).shift(RIGHT * 3, UP * 2)

        finalCaption = Tex("Hence, this limit is defined", font_size=30).to_edge(DOWN)

        self.wait(2)
        self.play(Create(ax))
        self.play(Write(funcTex))
        self.play(Create(graph))
        self.wait(2)
        self.play(Write(caption1))
        self.play(Create(rangeBrace))
        self.play(Create(VGroup(*rangeLines)))
        self.wait(1)
        self.play(Create(VGroup(x0, x0Label)))
        self.play(Create(dashedLineL), Create(Ltex))
        self.wait(3)
        self.play(Create(x))
        self.play(Create(VGroup(*xDashedLines, *labels)))
        self.wait(1)
        self.play(ReplacementTransform(caption1, caption2))
        self.play(value.animate.set_value(3.99), run_time=7, rate_func=linear)
        self.wait(3)
        self.play(ReplacementTransform(caption2, caption3))
        self.play(Write(limTex))
        self.wait(7)
        self.play(ReplacementTransform(caption3, finalCaption))
        self.wait(3)
        self.play(FadeOut(ax, funcTex, graph, rangeBrace, *rangeLines, x0, x0Label, dashedLineL, Ltex, x, *xDashedLines,
                          *labels, limTex, finalCaption))
        self.wait(4)

        self.play(Write(Tex("Thanks for Watching!", font_size=100)))
        self.wait(3)


with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = Thumbnail()
    scene.render()
