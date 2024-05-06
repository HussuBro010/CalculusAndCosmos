from manim import *


class Intro(Scene):
    def construct(self):
        title = Title("Types of Graph", font_size=80)

        caption = Text("Today, we will look at different types of graphs", font_size=50).center()

        self.play(Write(title))
        self.wait(1)
        self.play(AddTextLetterByLetter(caption))
        self.wait(2)
        self.play(Unwrite(caption))
        self.wait(0.5)
        self.play(Unwrite(title))
        self.wait(1.5)
        ConstantGraph.construct(self)


class ConstantGraph(Scene):
    def construct(self):
        title = Title("Constant Graph", font_size=80)

        ax = Axes(
            x_range=[-8, 8, 1],
            y_range=[-8, 8, 1],
            x_length=6,
            y_length=6,
            axis_config={"include_numbers": True, "font_size": 15},
            tips=True
        ).shift(RIGHT * 3.7).shift(DOWN * 0.7).add_coordinates()

        constant = ValueTracker(0)

        funcTexY = MathTex("y", " = c", font_size=80).shift(LEFT * 3.7)

        constantText = always_redraw(
            lambda: Text(f"Constant(c): {constant.get_value():.2f}", font_size=40).shift(LEFT * 3.7).next_to(funcTexY,
                                                                                                             DOWN,
                                                                                                             buff=1.5))

        graphY = always_redraw(lambda: ax.plot(lambda x: constant.get_value(), x_range=[-8, 8, 1], color=BLUE_C))

        self.play(Write(title))
        self.wait(1)
        self.play(Create(ax))
        self.wait(1)
        self.play(Write(funcTexY))
        self.wait(1)
        self.play(Write(constantText))
        self.wait(1)
        self.play(Create(graphY))
        self.wait(2)
        self.play(constant.animate.set_value(5))
        self.wait(2)
        self.play(constant.animate.set_value(3))
        self.wait(2)
        self.play(constant.animate.set_value(-6))
        self.wait(2)
        self.play(constant.animate.set_value(-4))
        self.wait(2)
        self.play(constant.animate.set_value(0))
        self.wait(3)
        self.play(FadeOut(title, ax, funcTexY, constantText, graphY))
        self.wait(2)
        LinearGraph.construct(self)


class LinearGraph(Scene):
    def construct(self):
        title = Title("Linear Graph", font_size=80)

        ax = Axes(
            x_range=[-8, 8, 1],
            y_range=[-8, 8, 1],
            x_length=6,
            y_length=6,
            axis_config={"include_numbers": True, "font_size": 15},
            tips=True
        ).shift(RIGHT * 3.7).shift(DOWN * 0.7).add_coordinates()

        slope = ValueTracker(1)
        intercept = ValueTracker(0)

        funcTex = MathTex("y = m", "x", " + c", font_size=80).shift(LEFT * 3.7)

        slopeText = always_redraw(
            lambda: Text(f"Slope(m): {slope.get_value():.2f}", font_size=40).shift(LEFT * 3.7).next_to(funcTex, DOWN,
                                                                                                       buff=0.8))
        interceptText = always_redraw(
            lambda: Text(f"Intercept(c): {intercept.get_value():.2f}", font_size=40).shift(LEFT * 3.7).next_to(funcTex,
                                                                                                               DOWN,
                                                                                                               buff=1.5))

        graph = always_redraw(
            lambda: ax.plot(lambda x: slope.get_value() * x + intercept.get_value(), x_range=[-8, 8, 1], color=BLUE_C))

        self.play(Write(title))
        self.wait(1)
        self.play(Create(ax))
        self.wait(1)
        self.play(Write(funcTex))
        self.wait(1)
        self.play(Write(slopeText), Write(interceptText))
        self.wait(1)
        self.play(Create(graph))
        self.wait(2)
        self.play(intercept.animate.set_value(5))
        self.wait(1)
        self.play(intercept.animate.set_value(-5))
        self.wait(2)
        self.play(intercept.animate.set_value(2))
        self.wait(0.5)
        self.play(slope.animate.set_value(3))
        self.wait(1)
        self.play(slope.animate.set_value(-3))
        self.wait(2.5)
        self.play(slope.animate.set_value(1))
        self.play(intercept.animate.set_value(0))
        self.wait(3)
        self.play(FadeOut(title, ax, funcTex, slopeText, interceptText, graph))
        self.wait(2)
        QuadraticGraph.construct(self)


class QuadraticGraph(Scene):
    def construct(self):
        title = Title("Quadratic Graph", font_size=80)

        ax = Axes(
            x_range=[-8, 8, 1],
            y_range=[-8, 8, 1],
            x_length=6,
            y_length=6,
            axis_config={"include_numbers": True, "font_size": 15},
            tips=True
        ).shift(RIGHT * 3.7).shift(DOWN * 0.7).add_coordinates()

        interceptX = ValueTracker(0)
        interceptY = ValueTracker(0)
        opening = ValueTracker(1)

        funcTex = MathTex("y = ax^2 + px + q", font_size=80).shift(LEFT * 3.7)

        interceptXtext = always_redraw(
            lambda: Text(f"X-Intercept(p): {interceptX.get_value():.2f}", font_size=40).shift(LEFT * 3.7).next_to(
                funcTex, DOWN, buff=0.8))
        interceptYtext = always_redraw(
            lambda: Text(f"Y-Intercept(q): {interceptY.get_value():.2f}", font_size=40).shift(LEFT * 3.7).next_to(
                funcTex, DOWN, buff=1.5))

        openingTex = always_redraw(
            lambda: Text(f"a: {opening.get_value():.2f}", font_size=40).shift(LEFT * 3.7).next_to(
                funcTex, DOWN, buff=2.2))

        graph = always_redraw(
            lambda: ax.plot(lambda x: (opening.get_value()*x ** 2) + interceptX.get_value() * x + interceptY.get_value(), x_range=[-8, 8, 1],
                            color=BLUE_C))

        self.play(Write(title))
        self.wait(1)
        self.play(Create(ax))
        self.wait(1)
        self.play(Write(funcTex))
        self.wait(1)
        self.play(Write(interceptXtext), Write(interceptYtext), Write(openingTex))
        self.wait(1)
        self.play(Create(graph))
        self.wait(2)
        self.play(interceptY.animate.set_value(5))
        self.wait(1)
        self.play(interceptY.animate.set_value(-5))
        self.wait(2)
        self.play(interceptY.animate.set_value(2))
        self.wait(0.5)
        self.play(interceptX.animate.set_value(3))
        self.wait(1)
        self.play(interceptX.animate.set_value(-3))
        self.wait(2.5)
        self.play(interceptX.animate.set_value(0))
        self.play(interceptY.animate.set_value(0))
        self.wait(2)
        self.play(opening.animate.set_value(7))
        self.wait(1.5)
        self.play(opening.animate.set_value(5))
        self.wait(2)
        self.play(opening.animate.set_value(-1.5))
        self.wait(1.5)
        self.play(opening.animate.set_value(-4))
        self.wait(2)
        self.play(opening.animate.set_value(1))
        self.wait(3)
        self.play(FadeOut(title, ax, funcTex, interceptXtext, interceptYtext, graph, openingTex))
        self.wait(2)


with tempconfig({"preview": True, "quality": "low_quality", "disable_caching": True}):
    scene = QuadraticGraph()
    scene.render()
