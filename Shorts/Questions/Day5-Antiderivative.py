from manim import *


class Antiderivative(Scene):
    def construct(self):
        title = Tex("Question of the day", font_size=45).to_edge(UP)
        waterMark = Tex("MathViz Animations", font_size=50).to_edge(DOWN)

        questionTex = Tex("Find $f(x)$ if").shift(UP)
        funcTex = Tex(r"$f^{\prime}(x) =$\\$6x^{8} - 20x^{4} + x^{2} + 9$", font_size=35).next_to(questionTex, DOWN, 0.7)

        self.wait(1)
        self.play(Write(waterMark))
        self.play(Write(title))
        self.play(Write(questionTex))
        self.play(Write(funcTex))
        self.wait(15)


with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = Antiderivative()
    scene.render()
