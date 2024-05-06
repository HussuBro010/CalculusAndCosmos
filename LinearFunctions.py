from manim import *
import numpy as np


class Thumbnail(Scene):
    def construct(self):
        title = Title("Linear Functions", font_size=70)
        ax = Axes(
            x_range=[-8, 8, 1],
            y_range=[-8, 8, 1],
            x_length=6,
            y_length=6,
            axis_config={"include_numbers": True, "font_size": 15},
            tips=True
        ).shift(DOWN * 0.5)

        plotCoords = ax.plot_line_graph([-1, 0, 1], [1, 3, 5], vertex_dot_style={"color": GREEN_E})
        linearFuncGraph = ax.plot(lambda x: 2 * x + 3, x_range=[-8, 8, 1], color=YELLOW_D)

        self.add(ax, plotCoords, linearFuncGraph, title)


class Intro(Scene):
    def construct(self):
        title = Title("Linear Functions", font_size=80)
        caption = Text("Today we will learn about Linear Functions and\nhow to plot them on a graph",
                       font_size=40,
                       should_center=True,
                       disable_ligatures=False
                       )

        self.play(Write(title))
        self.play(AddTextLetterByLetter(caption, run_time=1))
        self.wait(2)
        self.play(FadeOut(caption, title, run_time=1.5))
        Definition.construct(self)


class Definition(Scene):
    def construct(self):
        title = Title("Definition", font_size=80)
        caption1 = Text("Let's see what is a linear function", font_size=40, should_center=True)
        definition = Text(
            "A linear function is defined as a function\nthat has either one or two variables without exponents.",
            font_size=40,
            should_center=True)
        exampleCaption = Text("Here is an example of a linear function", font_size=40, should_center=False).move_to(
            UP * 2)
        eq1Tex = MathTex(r"f(x)", " = 2", "x", " + 3", font_size=65)
        subCaption = Text("Which can also be written as:- ", font_size=30).move_to(DOWN * 1.57)
        eq1aTex = MathTex("y", " = ", "2", "x", " + ", "3", font_size=65)

        xCaption = Text("Here x is an independent variable \n i.e it can be any number",
                        font_size=40,
                        should_center=True
                        ).move_to(DOWN * 2)
        yCaption = Text(f"But y is a dependent variable \n as its value can only be determined by x",
                        font_size=40,
                        should_center=True
                        ).move_to(DOWN * 2)

        slopeText = Text("Slope", font_size=25, should_center=True).next_to(eq1aTex.submobjects[2], UP * 2.5)
        slopeArrow = Arrow(start=slopeText.get_bottom(), end=eq1aTex.submobjects[2].get_top(), buff=-0.4)

        interceptText = Text("Intercept", font_size=25, should_center=True).next_to(eq1aTex.submobjects[-1],
                                                                                    RIGHT * 2.5)
        interceptArrow = Arrow(start=interceptText.get_left(), end=eq1aTex.submobjects[-1].get_right(), buff=-0.4)

        slopeCaption = Text(
            "Slope means that change in x\n will result in a change in y by the amount of 2",
            font_size=35,
            should_center=True
        ).move_to(DOWN * 2)

        interceptCaption = Text("3 is the y-intercept i.e \nWhen x=0, the graph will intersect y-axis at y = 3",
                                font_size=40).move_to(DOWN * 2)

        self.play(Write(title))
        self.play(AddTextLetterByLetter(caption1, run_time=1))
        self.wait(1)
        self.play(Unwrite(caption1))
        self.play(AddTextLetterByLetter(definition, run_time=1.5))
        self.wait(2.5)
        self.play(Unwrite(definition))
        self.play(Write(exampleCaption))
        self.wait(0.7)
        self.play(Write(eq1Tex, run_time=2))
        self.wait(2)
        self.play(Write(subCaption))
        self.wait(0.5)
        self.play(TransformMatchingTex(eq1Tex, eq1aTex))
        self.wait(1)
        self.play(Unwrite(subCaption))
        self.wait(1)
        self.play(Write(xCaption, run_time=1), Indicate(eq1aTex.submobjects[3], run_time=2))
        self.wait(2)
        self.play(Unwrite(xCaption, run_time=0.5))
        self.play(Write(yCaption, run_time=1), Indicate(eq1aTex.submobjects[0], run_time=2))
        self.wait(2)
        self.play(Unwrite(yCaption, run_time=0.5))
        self.wait(3)
        self.play(Write(slopeText, run_time=1), Create(slopeArrow))
        self.wait(0.7)
        self.play(Write(slopeCaption, run_time=0.675))
        self.wait(2)
        self.play(Unwrite(slopeCaption, run_time=0.5))
        self.play(Write(interceptText, run_time=1), Create(interceptArrow))
        self.wait(0.7)
        self.play(Write(interceptCaption, run_time=1))
        self.wait(3.5)
        self.play(Unwrite(interceptCaption, run_time=0.5))
        self.play(
            FadeOut(title, exampleCaption, eq1aTex, slopeText, slopeArrow, slopeCaption, interceptText, interceptArrow))
        self.wait(3)
        Plotting.construct(self)


class Plotting(Scene):
    def construct(self):
        title = Title("Plotting Linear Functions", font_size=80)
        caption1 = Text("Now let's look at how can we plot a linear function", font_size=37, should_center=True)
        exampleCaption = Text("Let's take our previous example:- ", font_size=28).next_to(title, DOWN, buff=0.3).shift(
            LEFT * 2.5)
        func1 = MathTex(r"f(x)", " = 2", "x", " + 3", font_size=65).next_to(exampleCaption, DOWN, buff=0.5)

        tableCaption = Text("Let's plot it using a table", font_size=30, should_center=True).next_to(func1, DOWN * 0.5)
        table = Table(
            [["-1", "0", "1"],
             ["1", "3", "5"]],
            row_labels=[Text("x"), Text("y")],
            include_outer_lines=True
        ).next_to(func1, DOWN, buff=-0.4).scale(0.5)

        ax = Axes(
            x_range=[-8, 8, 1],
            y_range=[-8, 8, 1],
            x_length=6,
            y_length=6,
            axis_config={"include_numbers": True, "font_size": 15},
            tips=True
        ).shift(RIGHT * 3.7).shift(DOWN * 0.7).add_coordinates()

        independ = Text("Here we can take any number for x\n as it is an independent variable", font_size=30,
                        should_center=True).next_to(table, RIGHT * 1.5)
        depend = Text("However, for y values we need to solve\n the function by evaluating \nit with the x values",
                      font_size=25, should_center=True).next_to(table, RIGHT * 1.5)

        evaluationCaption = Text(
            "After putting each value in our function\n and solving it we get the \nfollowing y values", font_size=27,
            should_center=True).next_to(table, RIGHT * 1.5)

        coordCaption = Text("According to the table, we now have 3 points:- ", font_size=20,
                            should_center=True).next_to(table, DOWN, buff=-0.5)

        coord1 = MathTex("(-1, 1)").next_to(coordCaption, DOWN, buff=0.5).shift(LEFT * 1.5)
        coord2 = MathTex("(0, 3)").next_to(coord1, DOWN, buff=0.3)
        coord3 = MathTex("(1, 5)").next_to(coord2, DOWN, buff=0.3)

        plotCaption = Text("Now we can plot these points on a graph", font_size=20, should_center=True).next_to(table,
                                                                                                                DOWN,
                                                                                                                buff=-0.5)

        plotCoords = ax.plot_line_graph([-1, 0, 1], [1, 3, 5], vertex_dot_style={"color": GREEN_E})

        joinCaption = Text("Now we can draw a line passing through these points", font_size=20,
                           should_center=True).next_to(table, DOWN, buff=-0.5)

        finalCaption = Text("The following graph is the result", font_size=20, should_center=True).next_to(table, DOWN,
                                                                                                           buff=-0.5)

        func2 = MathTex(r"f(x)", " = p", "x", " + q", font_size=65).next_to(title, DOWN, buff=0.5).shift(LEFT * 3)
        valueChangeCaption = Text("Let's try changing p and q", font_size=20).next_to(func2, DOWN, buff=0.5)

        p = ValueTracker(2)
        pText = always_redraw(lambda: Text(f"p = {p.get_value():.2f}").next_to(valueChangeCaption, DOWN, buff=0.7))

        q = ValueTracker(3)
        qText = always_redraw(lambda: Text(f"q = {q.get_value():.2f}").next_to(pText, DOWN, buff=0.7))

        linearFuncGraph = always_redraw(
            lambda: ax.plot(lambda x: p.get_value() * x + q.get_value(), x_range=[-8, 8, 1], color=YELLOW_D))

        self.play(Write(title))
        self.play(AddTextLetterByLetter(caption1, run_time=0.5))
        self.wait(1)
        self.play(Unwrite(caption1))
        self.wait(1.5)
        self.play(Write(exampleCaption))
        self.wait(1.5)
        self.play(Write(func1))
        self.wait(1.7)
        self.play(Write(tableCaption))
        self.wait(1)
        self.play(Unwrite(tableCaption))
        self.play(Create(table))
        self.wait(1)
        self.play(Write(independ), Indicate(table.get_rows()[0], run_time=2))
        self.wait(1)
        self.play(ReplacementTransform(independ, depend))
        self.wait(2.5)
        self.play(ReplacementTransform(depend, evaluationCaption), Indicate(table.get_rows()[1], run_time=2))
        self.wait(3)
        self.play(Unwrite(evaluationCaption), Unwrite(exampleCaption))
        self.play(VGroup(func1, table).animate.next_to(title, DOWN, buff=0.5).shift(LEFT * 3))
        self.wait(1)
        self.play(Write(coordCaption))
        self.wait(1)
        self.play(Write(coord1))
        self.play(Write(coord2))
        self.play(Write(coord3))
        self.wait(2)
        self.play(ReplacementTransform(coordCaption, plotCaption))
        self.play(Create(ax))
        self.wait(3)
        self.play(Create(plotCoords["vertex_dots"]))
        self.wait(2)
        self.play(ReplacementTransform(plotCaption, joinCaption))
        self.wait(1)
        self.play(Create(linearFuncGraph, run_time=2))
        self.wait(1)
        self.play(ReplacementTransform(joinCaption, finalCaption))
        self.wait(3)
        self.play(FadeOut(plotCoords, coord1, coord2, coord3, table))
        self.play(ReplacementTransform(finalCaption, valueChangeCaption))
        self.play(Write(pText), Write(qText), TransformMatchingTex(func1, func2))
        self.add(p, q)
        self.wait(1.5)
        self.play(p.animate.set_value(5))
        self.play(q.animate.set_value(7))
        self.wait(1)
        self.play(p.animate.set_value(-5))
        self.play(q.animate.set_value(-7))
        self.wait(1.5)
        self.play(p.animate.set_value(2), q.animate.set_value(3))
        self.wait(2)
        self.play(FadeOut(func2, valueChangeCaption, pText, qText, p, q))
        self.play(VGroup(linearFuncGraph, ax).animate.move_to([0, 0.5, 0]))
        self.wait(3)
        self.play(FadeOut(VGroup(linearFuncGraph, ax, title)))
        self.wait(1)
        self.play(AddTextLetterByLetter(Text("Thanks for watching!", font_size=80), run_time=2))
        self.wait(4)


with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = Intro()
    scene.render()
