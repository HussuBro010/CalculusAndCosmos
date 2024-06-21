import numpy as np
from manim import *


class Thumbnail(Scene):
    def construct(self):
        title = Title("Continuity Of Functions", font_size=80)
        ax = Axes(
            x_range=(-1, 6),
            y_range=(-1, 6),
            x_length=5,
            y_length=5
        ).shift(LEFT * 3, DOWN)

        funcTex = MathTex(r"f(x)").next_to(ax, UP)

        def f(x):
            return np.sin(0.9 * x) + np.cos(0.5 * x) + 3

        graph = ax.plot(lambda a: f(a), x_range=(-1, 6))
        graph.set_color(BLUE)

        type1 = Tex("Removable discontinuity").shift(LEFT * 3.5, UP)
        type2 = Tex("Jump discontinuity").shift(LEFT * 3.5)
        type3 = Tex("Asymptote discontinuity").shift(LEFT * 3.5, DOWN)

        sumAx1 = Axes(
            x_range=(-1, 4),
            y_range=(-1, 3),
            x_length=5,
            y_length=2
        ).next_to(type1, RIGHT, buff=1)

        sumSegment1 = sumAx1.plot(lambda x: 1, x_range=(-1, 1.9))
        sumSegment1.color = RED
        sumSegment2 = sumAx1.plot(lambda x: 1, x_range=(2.1, 4))
        sumSegment2.color = RED

        sumHollowDotT1 = Circle(0.08).move_to(sumAx1.c2p(2, 1))
        sumHollowDotT1.color = RED
        sumDotT1 = Dot(sumAx1.c2p(2, 1.5))
        sumDotT1.color = RED

        sumAx2 = Axes(
            x_range=(-1, 4),
            y_range=(-1, 3),
            x_length=5,
            y_length=2
        ).next_to(type2, RIGHT, buff=1).shift(DOWN)

        def sf1(x):
            return np.sin(x) + np.cos(2 * x) + 1

        def sf2(x):
            return np.cos(x) + np.sin(3 * x) + 1

        sumSegment1T2 = sumAx2.plot(sf1, x_range=(-1, 2))
        sumSegment1T2.color = GREEN
        sumSegment2T2 = sumAx2.plot(sf2, x_range=(2, 4))
        sumSegment2T2.color = GREEN

        sumHollowDotT2 = Circle(0.08).move_to(sumAx2.c2p(2, sf1(2)))
        sumHollowDotT2.color = GREEN
        sumDotT2 = Dot(sumAx2.c2p(2, sf2(2)))
        sumDotT2.color = GREEN

        sumAx3 = Axes(
            x_range=(-1, 4),
            y_range=(-1, 3),
            x_length=5,
            y_length=2
        ).next_to(type3, RIGHT, buff=1).shift(DOWN * 2)

        def sf(x):
            return np.e ** x

        sumSegment1T3 = sumAx3.plot(sf, x_range=(-1, 4))
        sumSegment1T3.color = YELLOW

        self.add(title, ax, funcTex, graph, sumAx1, sumSegment1, sumSegment2, sumHollowDotT1, sumDotT1, sumAx2,
                 sumSegment1T2, sumSegment2T2, sumHollowDotT2, sumDotT2, sumAx3, sumSegment1T3)


class Intro(Scene):
    def construct(self):
        title = Tex("Hello Everyone!", font_size=80)

        cap1 = Tex("In this video, we are going to learn about:- ", font_size=60)
        topic1 = Tex("Continuous Function", font_size=40).next_to(cap1, DOWN)
        topic2 = Tex("Discontinuous Function", font_size=40).next_to(topic1, DOWN * 0.5)

        self.wait(1.5)
        self.play(Write(title))
        self.wait(1)
        self.play(ReplacementTransform(title, cap1))
        self.wait(1.5)
        self.play(Indicate(topic1))
        self.wait(1)
        self.play(Indicate(topic2))
        self.wait(2)
        self.play(FadeOut(cap1, topic1, topic2))
        self.wait(1)
        ContinuityOfFunction.construct(self)


class ContinuityOfFunction(Scene):
    def construct(self):
        ax = Axes(
            x_range=(-1, 6),
            y_range=(-1, 6),
            x_length=5,
            y_length=5
        ).shift(LEFT * 3)

        funcTex = MathTex(r"f(x) = \sin(0.9x) + \cos(0.5x) + 3").next_to(ax, UP)

        def f(x):
            return np.sin(0.9 * x) + np.cos(0.5 * x) + 3

        graph = ax.plot(lambda a: f(a), x_range=(-1, 6))
        graph.set_color(YELLOW)

        caption1 = Tex("A function $f(x)$ is said to be continuous at $x=a$, If", font_size=30).to_edge(DOWN)

        pointA = Dot(ax.c2p(4, f(4)))
        dashedLine = DashedLine(ax.c2p(4, 0), pointA.get_center())

        labelA = MathTex("a").next_to(pointA, UP, buff=0.1)

        criteria1 = Tex("$f(x)$ is defined at $x = a$", font_size=45).shift(RIGHT * 3.5, UP * 1)
        criteria2 = MathTex(r"\lim_{x \to a} f(x) \text{ exists}", font_size=45).shift(RIGHT * 3.5)
        criteria3 = MathTex(r"\lim_{x \to a} f(x) = f(a)", font_size=45).shift(RIGHT * 3.5, -UP)

        caption2 = Tex(r"A function which doesn't meet\\ any of the criteria is a discontinuous function",
                       font_size=30).to_edge(DOWN)

        self.wait(1.5)
        self.play(Create(ax))
        self.play(Create(graph))
        self.play(Create(funcTex))
        self.wait(0.5)
        self.play(Write(caption1), Create(dashedLine))
        self.play(Create(pointA), Create(labelA))
        self.play(Write(criteria1))
        self.wait(1)
        self.play(Write(criteria2))
        self.wait(1)
        self.play(Write(criteria3))
        self.wait(1)
        self.play(ReplacementTransform(caption1, caption2))
        self.wait(2)
        self.play(FadeOut(ax, funcTex, graph, pointA, dashedLine, labelA, caption2, criteria1, criteria2, criteria3))
        self.wait(2)
        TypesOfDiscontinuity.construct(self)


class TypesOfDiscontinuity(Scene):
    def construct(self):
        title = Tex("There are three types of discontinuity", font_size=70).shift(UP * 3.3)

        type1 = Tex("Removable discontinuity").shift(LEFT * 3.5, UP)
        type2 = Tex("Jump discontinuity").shift(LEFT * 3.5)
        type3 = Tex("Asymptote discontinuity").shift(LEFT * 3.5, DOWN)

        self.wait(1)
        self.play(Write(title))
        self.wait(2)
        self.play(Write(type1))
        self.wait(0.7)
        self.play(Write(type2))
        self.wait(0.7)
        self.play(Write(type3))

        # === Type 1 ===
        captionT1a = Tex("A function is said to be removable at $x=a$, if", font_size=30).to_edge(DOWN)

        type1Lim = MathTex(r"\lim_{x \to a} f(x) \neq f(a)").next_to(type1, RIGHT, buff=1.5)

        captionT1b = Tex("Here's an example of a removable discontinuous function", font_size=30).to_edge(DOWN)

        type1ax = Axes(
            x_range=(-1, 4),
            y_range=(-1, 3),
            x_length=5,
            y_length=2
        ).shift(RIGHT * 3, DOWN * 0.5)

        segment1 = type1ax.plot(lambda x: 1, x_range=(-1, 1.9))
        segment1.color = YELLOW
        segment2 = type1ax.plot(lambda x: 1, x_range=(2.1, 4))
        segment2.color = YELLOW

        hollowDotT1 = Circle(0.08).move_to(type1ax.c2p(2, 1))
        hollowDotT1.color = YELLOW
        dotT1 = Dot(type1ax.c2p(2, 1.5))
        dotT1.color = YELLOW

        self.wait(2.5)
        self.play(type1.animate.set_opacity(1), type2.animate.set_opacity(0.3), type3.animate.set_opacity(0.3))
        self.wait(2)
        self.play(Write(captionT1a))
        self.play(Write(type1Lim))
        self.wait(2.5)
        self.play(ReplacementTransform(captionT1a, captionT1b))
        self.wait(1)
        self.play(Create(type1ax))
        self.play(Create(VGroup(segment1, segment2)))
        self.play(Create(VGroup(hollowDotT1, dotT1)))
        self.wait(5)
        self.play(FadeOut(type1Lim, captionT1b, type1ax, segment1, segment2, hollowDotT1, dotT1))

        # === Type 2 ===
        captionT2a = Tex("A function is said to be jump discontinuous at $x=a$, if", font_size=30).to_edge(DOWN)

        type2Lim = MathTex(r"\lim_{x \to a", "^{-}}", r"f(x) \neq \lim_{x \to a", "^{+}}", "f(x)").next_to(type2, RIGHT,
                                                                                                           buff=1.5)

        captionT2b = Tex("Here the minus sign indicates that we are approaching the limit from the left side",
                         font_size=30).to_edge(DOWN)

        captionT2c = Tex("And the plus sign indicates that we are approaching the limit from the right side",
                         font_size=30).to_edge(DOWN)

        captionT2d = Tex("Here's an example of a jump discontinuous function", font_size=30).to_edge(DOWN)

        type2ax = Axes(
            x_range=(-1, 4),
            y_range=(-1, 3),
            x_length=5,
            y_length=2
        ).shift(RIGHT * 3, DOWN * 1.7)

        def f1(x):
            return np.sin(x) + np.cos(2 * x) + 1

        def f2(x):
            return np.cos(x) + np.sin(3 * x) + 1

        segment1T2 = type2ax.plot(f1, x_range=(-1, 2))
        segment1T2.color = YELLOW
        segment2T2 = type2ax.plot(f2, x_range=(2, 4))
        segment2T2.color = YELLOW

        hollowDotT2 = Circle(0.08).move_to(type2ax.c2p(2, f1(2)))
        hollowDotT2.color = YELLOW
        dotT2 = Dot(type2ax.c2p(2, f2(2)))
        dotT2.color = YELLOW

        rectT2a = SurroundingRectangle(type2Lim.submobjects[1])
        rectT2b = SurroundingRectangle(type2Lim.submobjects[3])

        self.wait(2.5)
        self.play(type1.animate.set_opacity(0.3), type2.animate.set_opacity(1), type3.animate.set_opacity(0.3))
        self.wait(2)
        self.play(Write(captionT2a))
        self.play(Write(type2Lim))
        self.wait(2.5)
        self.play(ReplacementTransform(captionT2a, captionT2b))
        self.play(Create(rectT2a))
        self.wait(2.5)
        self.play(ReplacementTransform(captionT2b, captionT2c))
        self.play(ReplacementTransform(rectT2a, rectT2b))
        self.wait(2.5)
        self.play(ReplacementTransform(captionT2c, captionT2d))
        self.wait(1)
        self.play(Create(type2ax))
        self.wait(2)
        self.play(Create(VGroup(segment1T2, segment2T2)))
        self.play(Create(VGroup(hollowDotT2, dotT2)))
        self.wait(3)
        self.play(FadeOut(type2Lim, captionT2d, type2ax, segment1T2, segment2T2, hollowDotT2, dotT2, rectT2b))
        self.wait(2.5)

        # === Type 3 ===
        captionT3a = Tex("A function is said to be asymptotic at $x=a$, if", font_size=30).to_edge(DOWN)

        type3Lim = MathTex(r"\lim_{x \to a} = \infty").next_to(type3, RIGHT, buff=1.5)

        captionT3b = Tex("This means that you see the graph approaching a point but never touching the point",
                         font_size=30).to_edge(DOWN)

        captionT3c = Tex("Or, it touches the point at infinity", font_size=30).to_edge(DOWN)

        captionT3d = Tex("Here's an example of an asymptote discontinuous function", font_size=30).to_edge(DOWN)

        type3ax = Axes(
            x_range=(-1, 4),
            y_range=(-1, 3),
            x_length=5,
            y_length=2
        ).shift(RIGHT * 3, UP * 1)

        def f1(x):
            return np.e ** x

        segment1T3 = type3ax.plot(f1, x_range=(-1, 4))
        segment1T3.color = YELLOW

        self.wait(2.5)
        self.play(type1.animate.set_opacity(0.3), type2.animate.set_opacity(0.3), type3.animate.set_opacity(1))
        self.wait(2)
        self.play(Write(captionT3a))
        self.play(Write(type3Lim))
        self.wait(2.5)
        self.play(ReplacementTransform(captionT3a, captionT3b))
        self.wait(2.5)
        self.play(ReplacementTransform(captionT3b, captionT3c))
        self.wait(2)
        self.play(ReplacementTransform(captionT3c, captionT3d))
        self.wait(1)
        self.play(Create(type3ax))
        self.wait(2)
        self.play(Create(VGroup(segment1T3)))
        self.wait(3)
        self.play(FadeOut(type3Lim, captionT3d, type3ax, segment1T3))
        self.wait(3)

        # === Summary ===
        sumAx1 = Axes(
            x_range=(-1, 4),
            y_range=(-1, 3),
            x_length=5,
            y_length=2
        ).next_to(type1, RIGHT, buff=1).shift(UP)

        sumSegment1 = sumAx1.plot(lambda x: 1, x_range=(-1, 1.9))
        sumSegment1.color = YELLOW
        sumSegment2 = sumAx1.plot(lambda x: 1, x_range=(2.1, 4))
        sumSegment2.color = YELLOW

        sumHollowDotT1 = Circle(0.08).move_to(sumAx1.c2p(2, 1))
        sumHollowDotT1.color = YELLOW
        sumDotT1 = Dot(sumAx1.c2p(2, 1.5))
        sumDotT1.color = YELLOW

        sumAx2 = Axes(
            x_range=(-1, 4),
            y_range=(-1, 3),
            x_length=5,
            y_length=2
        ).next_to(type2, RIGHT, buff=1)

        def sf1(x):
            return np.sin(x) + np.cos(2 * x) + 1

        def sf2(x):
            return np.cos(x) + np.sin(3 * x) + 1

        sumSegment1T2 = sumAx2.plot(sf1, x_range=(-1, 2))
        sumSegment1T2.color = YELLOW
        sumSegment2T2 = sumAx2.plot(sf2, x_range=(2, 4))
        sumSegment2T2.color = YELLOW

        sumHollowDotT2 = Circle(0.08).move_to(sumAx2.c2p(2, sf1(2)))
        sumHollowDotT2.color = YELLOW
        sumDotT2 = Dot(sumAx2.c2p(2, sf2(2)))
        sumDotT2.color = YELLOW

        sumAx3 = Axes(
            x_range=(-1, 4),
            y_range=(-1, 3),
            x_length=5,
            y_length=2
        ).next_to(type3, RIGHT, buff=1).shift(DOWN)

        def sf(x):
            return np.e ** x

        sumSegment1T3 = sumAx3.plot(sf, x_range=(-1, 4))
        sumSegment1T3.color = YELLOW

        self.play(type1.animate.set_opacity(1), type2.animate.set_opacity(1), type3.animate.set_opacity(1))
        self.wait(1)
        self.play(Create(VGroup(sumAx1, sumSegment1, sumSegment2, sumDotT1, sumHollowDotT1)))
        self.wait(1)
        self.play(Create(VGroup(sumAx2, sumSegment1T2, sumSegment2T2, sumDotT2, sumHollowDotT2)))
        self.wait(1)
        self.play(Create(VGroup(sumAx3, sumSegment1T3)))
        self.wait(3)
        self.play(
            FadeOut(sumAx1, sumSegment1, sumSegment2, sumDotT1, sumHollowDotT1, sumAx2, sumSegment1T2, sumSegment2T2,
                    sumDotT2, sumHollowDotT2, sumAx3, sumSegment1T3, type1, type2, type3, title))
        self.wait(1)
        Outro.construct(self)


class Outro(Scene):
    def construct(self):
        thanks = Text("Thanks for watching!", font_size=70)

        self.wait(1)
        self.play(Write(thanks))
        self.wait(2)
        self.play(Unwrite(thanks))
        self.wait(1)


with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = Thumbnail()
    scene.render()
