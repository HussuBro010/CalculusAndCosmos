from manim import *


class SimplifyToLowestTerms(Scene):
    def construct(self):
        self.camera.background_color = "#111317"
        title = Tex("Question of the day", font_size=45).to_edge(UP)
        waterMark = Tex("MathViz Animations", font_size=50).to_edge(DOWN)

        expr = MathTex(r"\frac{x^6 + a^2 x^3y}{x^6-a^4y^2}", font_size=80).shift(UP * 0.5)
        question = Tex("Simplify to lowest terms", font_size=35).next_to(expr, DOWN, buff=1)

        self.wait(1)
        self.play(Write(waterMark))
        self.play(Write(title))
        self.play(Write(expr))
        self.play(Write(question))
        self.wait(15)


with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = SimplifyToLowestTerms()
    scene.render()
