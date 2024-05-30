from manim import *


class Thumbnail(Scene):
    def construct(self):
        title = Title("Definition of Derivative", font_size=80)
        expr = MathTex(r"\lim_{h\to 0} \frac{f(x+h) - f(x)}{h}", font_size=85)
        self.add(title, expr)


class DerivativeProof(Scene):
    def construct(self):
        caption1 = Tex("Let's Plot $f(x)$ on a graph", font_size=40).shift(UP * 3).shift(RIGHT * 3)

        ax = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=6,
            y_length=6,
            tips=True,
            axis_config={'tip_shape': StealthTip}
        ).shift(LEFT * 2.5)
        graph = ax.plot(lambda x: (1 / 5) * x ** 2, x_range=(-5, 5), color=YELLOW)

        caption2 = Tex("We'll plot any 2 points on the graph", font_size=40).shift(UP * 3).shift(RIGHT * 3)

        point2tracker = ValueTracker(4)

        coord1 = ax.c2p(2, 0.8)
        coord2 = ax.c2p(point2tracker.get_value(), (1 / 5) * point2tracker.get_value() ** 2)
        point1 = Dot(coord1, color=PURPLE)
        point2 = Dot(coord2, color=PURPLE).add_updater(lambda m: m.become(
            Dot(ax.c2p(point2tracker.get_value(), (1 / 5) * point2tracker.get_value() ** 2), color=PURPLE)))

        point1DashedLines = [
            DashedLine(point1.get_center(), ax.c2p(0, 0.8), color=RED),
            DashedLine(point1.get_center(), ax.c2p(2, 0), color=BLUE)
        ]
        point2DashedLines = [
            DashedLine(point2.get_center(), ax.c2p(0, 3.2), color=RED),
            DashedLine(point2.get_center(), ax.c2p(4, 0), color=BLUE)
        ]

        dx = ValueTracker(2)

        caption3 = Tex(r"Now We'll draw a line\\ passing through these points", font_size=40).shift(UP * 3).shift(
            RIGHT * 3)

        secantLine = always_redraw(
            lambda: ax.get_secant_slope_group(
                x=2,
                graph=graph,
                dx=point2tracker.get_value() - 2,
                secant_line_length=5,
                dx_line_color=BLUE,
                dy_line_color=RED
            )
        )

        caption4 = Tex("We need to find the slope of this line", font_size=40).shift(UP * 3).shift(RIGHT * 3)

        caption5 = Tex("We know that: ").shift(UP * 3).shift(RIGHT * 2.5)
        slopeFunc = MathTex(r"\text{slope} = \frac{y_2 - y_1}{x_2 - x_1}").next_to(caption5, DOWN, 0.7)

        x1 = Tex("$x_1$", font_size=30).next_to(point1DashedLines[1], DOWN, buff=0.15)
        x2 = Tex("$x_2$", font_size=30).next_to(point2DashedLines[1], DOWN, buff=0.15)

        y1 = Tex("$y_1$", font_size=30).next_to(point1DashedLines[0], LEFT, buff=0.15)
        y2 = Tex("$y_2$", font_size=30).next_to(point2DashedLines[0], LEFT, buff=0.15)

        caption6 = Tex("Here we can replace $x_1$ with just $x$", font_size=40).shift(UP * 3).shift(RIGHT * 3)

        xLabel = Tex("$x$", font_size=30).next_to(point1DashedLines[1], DOWN, buff=0.15)

        caption6a = Tex("So, $y_1$ can be replaced with $f(x)$", font_size=40).shift(UP * 3).shift(RIGHT * 3)

        fxLabel = Tex("$f(x)$", font_size=30).next_to(point1DashedLines[0], LEFT, buff=0.15)

        caption7 = Tex(r"Let's say that the distance between\\ x values of the 2 points is $h$", font_size=40).shift(
            UP * 3).shift(RIGHT * 3)

        hBrace = always_redraw(
            lambda: BraceBetweenPoints((point1.get_x(), -0.3, 0), (point2.get_x(), -0.3, 0), color=BLUE_C))
        braceLabel = always_redraw(lambda: Tex("$h$", font_size=30).next_to(hBrace, DOWN, buff=0.1))

        caption8 = Tex(r"Then we can replace\\ $x_2$ with $x+h$", font_size=40).shift(UP * 3).shift(RIGHT * 3)

        xhLabel = Tex("$x+h$", font_size=30).next_to(point2DashedLines[1], DOWN, buff=0.15)

        caption8a = Tex(r"And replace\\ $y_2$ with $f(x+h)$", font_size=40).shift(UP * 3).shift(RIGHT * 3)

        fxhLabel = Tex("$f(x+h)$", font_size=30).next_to(point2DashedLines[0], LEFT, buff=0.15)

        caption9 = Tex(r"Now we substitute the values\\ in the slope function", font_size=40).shift(UP * 3).shift(
            RIGHT * 3)

        slopeFunc2 = MathTex(r"\text{slope} = \frac{f(x+h) - f(x)}{x + h - x}").next_to(caption5, DOWN, 0.7).shift(
            RIGHT * 1)
        slopeFunc3 = MathTex(r"\text{slope} = \frac{f(x+h) - f(x)}{h}").next_to(caption5, DOWN, 0.7).shift(RIGHT * 1)

        caption10 = Tex(r"Now if we let $h$ approach 0, \\the two points will be pretty much \\be at the same point",
                        font_size=30).shift(UP * 3).shift(RIGHT * 3)
        caption10a = Tex(r"The function becomes a limit\\ and the derivative is the slope of this line",
                         font_size=35).shift(UP * 3).shift(RIGHT * 3)

        slopeFunc4 = MathTex(r"\text{slope} =\lim_{h\space\to\space 0} \frac{f(x+h) - f(x)}{h}").next_to(caption10a,
                                                                                                         DOWN,
                                                                                                         0.7).shift(
            RIGHT * 0.5)

        finalCaption = Tex("Hence, the Definition of Derivative is:- ", font_size=75).shift(UP * 3)
        finalFunc = MathTex(r"\lim_{h\space\to\space 0} \frac{f(x+h) - f(x)}{h}", font_size=90).next_to(finalCaption,
                                                                                                        DOWN, buff=1)

        thankyouCaption = Tex("Thanks for Watching", font_size=80)

        self.wait(1)
        self.play(Write(caption1))
        self.wait(1.5)
        self.play(Create(ax))
        self.play(Create(graph))
        self.wait(2)
        self.play(ReplacementTransform(caption1, caption2))
        self.wait(1)
        self.play(Create(VGroup(point1, point2)))
        self.play(Create(VGroup(*point1DashedLines, *point2DashedLines)))
        self.wait(2)
        self.play(ReplacementTransform(caption2, caption3))
        self.wait(1)
        self.play(Create(secantLine))
        self.wait(2)
        self.play(ReplacementTransform(caption3, caption4))
        self.wait(2)
        self.play(ReplacementTransform(caption4, caption5))
        self.wait(1)
        self.play(Write(slopeFunc))
        self.wait(2)
        self.play(Create(VGroup(x1, x2, y1, y2)))
        self.wait(2)
        self.play(ReplacementTransform(caption5, caption6))
        self.wait(1)
        self.play(FadeOut(x1, run_time=0.1), FocusOn(xLabel, run_time=1.5), Indicate(xLabel))
        self.wait(1)
        self.play(ReplacementTransform(caption6, caption6a))
        self.wait(1)
        self.play(FadeOut(y1, run_time=0.1), FocusOn(fxLabel, run_time=1.5), Indicate(fxLabel))
        self.wait(2.5)
        self.play(ReplacementTransform(caption6a, caption7))
        self.play(Create(hBrace))
        self.wait(1)
        self.play(Write(braceLabel))
        self.wait(3)
        self.play(ReplacementTransform(caption7, caption8))
        self.wait(1)
        self.play(FadeOut(x2, run_time=0.1), FocusOn(xhLabel, run_time=1.5), Indicate(xhLabel))
        self.wait(1)
        self.play(ReplacementTransform(caption8, caption8a))
        self.wait(1)
        self.play(FadeOut(y2, run_time=0.1), FocusOn(fxhLabel, run_time=1.5), Indicate(fxhLabel))
        self.wait(2)
        self.play(ReplacementTransform(caption8a, caption9))
        self.wait(1)
        self.play(ReplacementTransform(slopeFunc, slopeFunc2))
        self.wait(1.5)
        self.play(ReplacementTransform(slopeFunc2, slopeFunc3))
        self.wait(2)
        self.play(FadeOut(*point1DashedLines, *point2DashedLines, xLabel, xhLabel, fxLabel, fxhLabel))
        self.play(ReplacementTransform(caption9, caption10))
        self.play(point2tracker.animate.set_value(1.9999), run_time=2)
        secantLine.clear_updaters()
        self.wait(2)
        self.play(ReplacementTransform(caption10, caption10a))
        self.wait(1)
        self.play(Indicate(secantLine))
        self.play(ReplacementTransform(slopeFunc3, slopeFunc4))
        self.wait(3)
        self.play(FadeOut(ax, graph, secantLine, point1, point2, hBrace, braceLabel))
        self.play(ReplacementTransform(caption10a, finalCaption))
        self.play(ReplacementTransform(slopeFunc4, finalFunc))
        self.wait(4)
        self.play(FadeOut(finalFunc, finalCaption))
        self.wait(1)
        self.play(Write(thankyouCaption))
        self.wait(2)
        self.play(Unwrite(thankyouCaption))
        self.wait(1)


with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = Thumbnail()
    scene.render()
