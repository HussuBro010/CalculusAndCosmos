from manim import *


class DoubleDerivative(Scene):
    def construct(self):
        self.camera.background_color = "#111317"
        title = Tex("Question of the day", font_size=45).to_edge(UP)
        waterMark = Tex("MathViz Animations", font_size=50).to_edge(DOWN)
        expr = MathTex("f(x)", font_size=50).shift(UP * 1.5)
        expr2 = MathTex(r"= \frac{\sin x^2 + \cos x^2}{5x^2 + 2x}", font_size=50).next_to(expr, DOWN, buff=0.4)

        question = Tex(r"Find $f^{\prime\prime}(x)$", font_size=50).next_to(expr2, DOWN, buff=1)

        self.wait(1)
        self.play(Write(waterMark))
        self.play(Write(title))
        self.play(Write(VGroup(expr, expr2)))
        self.play(Write(question))
        self.wait(15)


with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = DoubleDerivative()
    scene.render()
