from manim import *
from numpy import *


class Fourier(Scene):
    def construct(self):
        self.camera.background_color = "#141414"

        colorGrad = color_gradient([LOGO_BLUE, LOGO_GREEN], 10)

        fourierMathTex = MathTex(r"1.5 \cdot \sum_{n=0}^{a}\frac{1}{2n+1}A\sin\left(\frac{\left(2n+1\right)\pi x}{l}\right)", color=LOGO_GREEN).shift(UP * 3)
        nTex = MathTex("n = 9").next_to(fourierMathTex, DOWN, buff=0.3)

        a = ValueTracker(0)
        SCALE = 1.5
        OFFSET = (LEFT * 4) + DOWN

        def f(x, n):
            cosine = cos((2 * n + 1) * PI * x)
            return SCALE * (1 / (2 * n + 1)) * cosine

        def g(x, n):
            sine = sin((2 * n + 1) * PI * x)
            return SCALE * (1 / (2 * n + 1)) * sine


        line1 = always_redraw(lambda: Line(OFFSET, OFFSET + (f(a.get_value(), 0), g(a.get_value(), 0), 0)))
        circle1 = Circle(line1.get_length()).shift(OFFSET).set_color(colorGrad[0])

        line2 = always_redraw(lambda: Line(line1.get_end(), (f(a.get_value(), 1), g(a.get_value(), 1), 0) + line1.get_end()))
        circle2 = always_redraw(lambda: Circle(line2.get_length(), color=colorGrad[1]).move_to(line2.get_start()))

        line3 = always_redraw(lambda: Line(line2.get_end(), (f(a.get_value(), 2), g(a.get_value(), 2), 0) + line2.get_end()))
        circle3 = always_redraw(lambda: Circle(line3.get_length(), color=colorGrad[2]).move_to(line3.get_start()))

        line4 = always_redraw(lambda: Line(line3.get_end(), (f(a.get_value(), 3), g(a.get_value(), 3), 0) + line3.get_end()))
        circle4 = always_redraw(lambda: Circle(line4.get_length(), color=colorGrad[3]).move_to(line4.get_start()))

        line5 = always_redraw(lambda: Line(line4.get_end(), (f(a.get_value(), 4), g(a.get_value(), 4), 0) + line4.get_end()))
        circle5 = always_redraw(lambda: Circle(line5.get_length(), color=colorGrad[4]).move_to(line5.get_start()))

        line6 = always_redraw(lambda: Line(line5.get_end(), (f(a.get_value(), 5), g(a.get_value(), 5), 0) + line5.get_end()))
        circle6 = always_redraw(lambda: Circle(line6.get_length(), color=colorGrad[5]).move_to(line6.get_start()))

        line7 = always_redraw(lambda: Line(line6.get_end(), (f(a.get_value(), 6), g(a.get_value(), 6), 0) + line6.get_end()))
        circle7 = always_redraw(lambda: Circle(line7.get_length(), color=colorGrad[6]).move_to(line7.get_start()))

        line8 = always_redraw(lambda: Line(line7.get_end(), (f(a.get_value(), 7), g(a.get_value(), 7), 0) + line7.get_end()))
        circle8 = always_redraw(lambda: Circle(line8.get_length(), color=colorGrad[7]).move_to(line8.get_start()))

        line9 = always_redraw(lambda: Line(line8.get_end(), (f(a.get_value(), 8), g(a.get_value(), 8), 0) + line8.get_end()))
        circle9 = always_redraw(lambda: Circle(line9.get_length(), color=colorGrad[8]).move_to(line9.get_start()))

        line10 = always_redraw(lambda: Line(line9.get_end(), (f(a.get_value(), 9), g(a.get_value(), 93), 0) + line9.get_end()))
        circle10 = always_redraw(lambda: Circle(line10.get_length(), color=colorGrad[9]).move_to(line10.get_start()))

        lines = VGroup(line1, line2, line3, line4, line5, line6, line7, line8, line9, line10)
        circles = VGroup(circle1, circle2, circle3, circle4, circle5, circle6, circle7, circle8, circle9, circle10)

        tracerDot = always_redraw(lambda: Dot((0, line10.get_end()[1], 0)))
        tracer = TracedPath(tracerDot.get_center, stroke_color=GOLD)
        tracer.add_updater(lambda v, dt: v.shift(RIGHT * (PI/4) * dt))

        self.play(Write(fourierMathTex))
        self.play(Write(nTex))
        self.wait(1)
        self.play(Create(lines), Create(circles))
        self.wait(1)
        self.play(Create(tracerDot))
        self.play(Create(tracer))
        self.wait(1)
        self.play(a.animate.set_value(4), run_time=12, rate_func=linear)
        self.wait(2)
        tracer.clear_updaters()
        self.play(FadeOut(lines, circles, tracerDot, tracer))
        self.wait(2)


with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = Fourier()
    scene.render()
