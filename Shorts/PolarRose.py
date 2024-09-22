import numpy as np
from manim import *


# This Code is not Fully Optimized

class PolarRose(Scene):
    def construct(self):
        # Displaying the Function Tex
        equation = MathTex(r"r = \cos(k \theta)", font_size=40).to_edge(UP)

        # A Changing Tracker for the k constant
        k = ValueTracker(1)
        # Displaying the value of k
        kTex = always_redraw(
            lambda: MathTex(fr"k = {k.get_value():.2f}", font_size=40).next_to(equation, DOWN, buff=0.4))

        # Displaying the theta Range 0 to PI
        thetaRange1 = MathTex(r"0", r"\le", r"\theta", r"\le", r"\pi", font_size=45).next_to(kTex, DOWN, buff=0.2)

        # Defining a stroke color gradient for all the functions
        strokeColor = color_gradient([TEAL, GREEN], 3)

        # A polar plane to plot the functions on
        polarPlane = PolarPlane(4, 4, 0.5)

        # Scale for the displayed function to be bigger and easier to see
        scale = 3

        # Defining function
        polarRose = lambda th: np.cos(k.get_value() * th)

        # First Function with theta range from 0 to PI
        function1 = always_redraw(
            lambda: polarPlane.plot_polar_graph(polarRose, theta_range=(0, PI),
                                                stroke_color=strokeColor).scale(scale))

        # Animating the 1st Function
        self.wait(2)
        self.play(Write(equation))
        self.play(Write(kTex))
        self.play(Write(thetaRange1))
        self.wait(2)
        self.play(Create(function1))
        self.wait(2)
        self.play(k.animate.set_value(0), run_time=2, rate_func=linear)
        self.wait(2)
        self.play(k.animate.set_value(1), run_time=2, rate_func=linear)
        self.wait(1)
        self.play(FadeOut(function1, run_time=0.2))
        self.wait(2)

        # Displaying the theta Range from 0 to 2PI
        thetaRange2 = MathTex(r"0", r"\le", r"\theta", r"\le", r"2\pi", font_size=45).next_to(kTex, DOWN, buff=0.2)

        # First Function with theta range from 0 to 2PI
        function2 = always_redraw(
            lambda: polarPlane.plot_polar_graph(polarRose, theta_range=(0, 2 * PI),
                                                stroke_color=strokeColor).scale(scale))

        # Animating the 2nd Function
        self.play(TransformMatchingTex(thetaRange1, thetaRange2))
        self.play(Create(function2))
        self.wait(2)
        self.play(k.animate.set_value(0), run_time=4, rate_func=linear)
        self.wait(2)
        self.play(k.animate.set_value(1), run_time=4, rate_func=linear)
        self.wait(1)
        self.play(FadeOut(function2, run_time=0.2))
        self.wait(2)

        # Displaying the theta Range from 0 to 5PI
        thetaRange5 = MathTex(r"0", r"\le", r"\theta", r"\le", r"5\pi", font_size=45).next_to(kTex, DOWN, buff=0.2)

        # First Function with theta range from 0 to 5PI
        function5 = always_redraw(
            lambda: polarPlane.plot_polar_graph(polarRose, theta_range=(0, 5 * PI),
                                                stroke_color=strokeColor).scale(scale))

        # Animating the 3rd Function
        self.play(TransformMatchingTex(thetaRange2, thetaRange5))
        self.play(Create(function5))
        self.wait(2)
        self.play(k.animate.set_value(0), run_time=5, rate_func=linear)
        self.wait(2)
        self.play(k.animate.set_value(1), run_time=5, rate_func=linear)
        self.wait(1)
        self.play(FadeOut(function5, run_time=0.2))
        self.wait(2)

        # Displaying the theta Range from 0 to 10PI
        thetaRange10 = MathTex(r"0", r"\le", r"\theta", r"\le", r"10\pi", font_size=45).next_to(kTex, DOWN, buff=0.2)

        # First Function with theta range from 0 to 10PI
        function10 = always_redraw(
            lambda: polarPlane.plot_polar_graph(lambda th: np.cos(k.get_value() * th), theta_range=(0, 10 * PI),
                                                stroke_color=strokeColor).scale(scale))

        # Animating the 4th Function
        self.play(TransformMatchingTex(thetaRange5, thetaRange10))
        self.play(Create(function10))
        self.wait(2)
        self.play(k.animate.set_value(0), run_time=10, rate_func=linear)
        self.wait(2)
        self.play(k.animate.set_value(1), run_time=10, rate_func=linear)
        self.wait(1)
        self.play(FadeOut(function10, run_time=0.2))
        self.wait(2)

        self.play(TransformMatchingTex(thetaRange10, thetaRange1))


with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = PolarRose()
    scene.render()
