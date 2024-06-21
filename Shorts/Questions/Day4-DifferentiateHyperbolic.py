from manim import *


class DifferentiateHyperbolic(Scene):
    def construct(self):
        title = Tex("Question of the day", font_size=45).to_edge(UP)
        waterMark = Tex("MathViz Animations", font_size=50).to_edge(DOWN * 1.5)
        questionTex = Tex("Differentiate:-").shift(UP)
        funcTex = Tex(r"$f(x) = \sinh(x)$\\$+2\cosh(x) - \text{sech}(x)$", font_size=35, should_center=True).next_to(questionTex, DOWN).center()

        self.wait(1)
        self.play(Write(waterMark))
        self.play(Write(title))
        self.play(Write(questionTex))
        self.play(Write(funcTex))
        self.wait(15)


with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = DifferentiateHyperbolic()
    scene.render()
