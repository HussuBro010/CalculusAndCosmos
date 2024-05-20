from manim import *


class CircleAreaDerivation(Scene):
    def construct(self):
        caption1 = Tex(r"Consider a circle\\ with radius $r$", font_size=40).shift(UP * 2)
        caption2 = Tex(
            r"We can approximate the area of the circle\\ by dividing it into thin concentric rings,\\ each with a width $\Delta r$",
            font_size=25).shift(UP * 2)

        radius = Line((0, -0.5, 0), (1.5, -0.5, 0))
        radiusTex = Tex("r", font_size=25).next_to(radius, UP, buff=0.1)

        circle = Circle(1.5, color=LOGO_WHITE).shift(DOWN * 0.5)

        rings = [Circle(1.3, color=LOGO_WHITE).shift(DOWN * 0.5),
                 Circle(1.1, color=LOGO_WHITE).shift(DOWN * 0.5),
                 Circle(0.9, color=LOGO_WHITE).shift(DOWN * 0.5),
                 Circle(0.7, color=LOGO_WHITE).shift(DOWN * 0.5),
                 Circle(0.5, color=LOGO_WHITE).shift(DOWN * 0.5),
                 Circle(0.3, color=LOGO_WHITE).shift(DOWN * 0.5),
                 Circle(0.1, color=LOGO_WHITE).shift(DOWN * 0.5),
                 Circle(0.05, color=LOGO_WHITE).shift(DOWN * 0.5),
                 Circle(0.005, color=LOGO_WHITE).shift(DOWN * 0.5),
                 Circle(0.0005, color=LOGO_WHITE).shift(DOWN * 0.5),
                 Circle(0.00005, color=LOGO_WHITE).shift(DOWN * 0.5),
                 Circle(0.000005, color=LOGO_WHITE).shift(DOWN * 0.5), ]

        caption3 = Tex(
            r"The area $\Delta A$ of each ring is\\ approximately equal to the\\ circumference of the ring multiplied\\ by its width:",
            font_size=30).shift(UP * 2)

        tex1 = MathTex(r"\Delta A", r"\approx", r"2\pi r", r"\Delta r", font_size=40).next_to(caption3, DOWN, buff=0.8)

        limTex = MathTex(r"A = \lim_{\Delta r \space\to\space0 } \sum2\pi r \Delta r", font_size=40).next_to(tex1, DOWN,
                                                                                                             buff=0.5)

        caption4 = Tex(r"Now, to find the total area of the circle,\\ we sum up the areas of all these thin rings.",
                       font_size=30).shift(UP * 2)

        caption5 = Tex(
            r"As we let $\Delta r$ approach zero\\ (i.e., make the rings infinitesimally thin),\\ this sum becomes an integral:",
            font_size=30).shift(UP * 2)

        caption6 = Tex("Now, evaluate the integral:",
                       font_size=30).shift(UP * 2)

        integralTexA = MathTex(r"A =", r"\int_{0}^{r}", r"2", r"\pi r\space dr", font_size=40).next_to(limTex, DOWN,
                                                                                                       buff=0.3)
        integralTexB = MathTex(r"A =", r"2\pi", r"\int_{0}^{r} r\space", r"dr", font_size=40).next_to(limTex, DOWN,
                                                                                                      buff=0.3)

        evaluationA = MathTex(r"A =", r"2", r"\pi", r"\left[ \frac{r^2}{r} \right]_{0}^{r}", font_size=40).next_to(
            integralTexB, DOWN,
            buff=0.3)
        evaluationB = MathTex(r"A =", r"2", r"\pi", r"\left( \frac{r^2}{2}", r" - \frac{0^2}{2} \right)",
                              font_size=40).next_to(
            integralTexB, DOWN, buff=0.3)
        evaluationBa = MathTex(r"A =", r"2", r"\pi", r"\left( \frac{r^2}{2}", r" - ", r"0 \right)",
                               font_size=40).next_to(integralTexB, DOWN,
                                                     buff=0.3)
        evaluationBb = MathTex(r"A =", r"2", r"\pi", r"\frac{r^2}{2}", font_size=40).next_to(integralTexB, DOWN,
                                                                                             buff=0.3)

        evaluationC = MathTex(r"A =", r"\pi", r"r^2", font_size=40).next_to(integralTexB, DOWN, buff=0.3)

        finalCaption = Tex("Hence, we get the area of the circle", font_size=35).shift(UP * 2)
        finalTex = MathTex(r"A =", r"\pi", r"r^2", font_size=70)

        self.play(Write(caption1))
        self.wait(1)
        self.play(Create(radius))
        self.wait(0.5)
        self.play(Rotate(radius, 360 * DEGREES, about_point=radius.start), Create(circle))
        self.play(Write(radiusTex))
        self.wait(1)
        self.play(ReplacementTransform(caption1, caption2))
        self.wait(2)
        for i in rings:
            self.play(Create(i, run_time=0.3))
        self.wait(2)
        self.play(FadeOut(VGroup(circle, *rings, radius, radiusTex)))
        self.wait(1)
        self.play(ReplacementTransform(caption2, caption3))
        self.wait(2)
        self.play(Write(tex1))
        self.wait(2)
        self.play(ReplacementTransform(caption3, caption4))
        self.wait(1)
        self.play(Write(limTex))
        self.wait(1.5)
        self.play(ReplacementTransform(caption4, caption5))
        self.wait(1)
        self.play(Write(integralTexA))
        self.wait(2)
        self.play(ReplacementTransform(integralTexA, integralTexB))
        self.wait(2)
        self.play(ReplacementTransform(caption5, caption6))
        self.wait(1.5)
        self.play(Write(evaluationA))
        self.wait(1.5)
        self.play(ReplacementTransform(evaluationA, evaluationB))
        self.wait(1.5)
        self.play(ReplacementTransform(evaluationB, evaluationBa))
        self.wait(1.5)
        self.play(ReplacementTransform(evaluationBa, evaluationBb))
        self.wait(1.5)
        self.play(ReplacementTransform(evaluationBb, evaluationC))
        self.wait(2)
        self.play(FadeOut(tex1, limTex, integralTexB))
        self.wait(1)
        self.play(ReplacementTransform(caption6, finalCaption))
        self.play(ReplacementTransform(evaluationC, finalTex))
        self.wait(3)


with tempconfig({"preview": True, "quality": "low_quality", "disable_caching": True}):
    scene = CircleAreaDerivation()
    scene.render()
