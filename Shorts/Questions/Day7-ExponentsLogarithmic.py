from manim import *


class ExponentsLogarithmic(Scene):
    def construct(self):
        self.camera.background_color = "#111317"
        title = Tex("Question of the day", font_size=45).to_edge(UP)
        waterMark = Tex("MathViz Animations", font_size=50).to_edge(DOWN)

        expr = Tex(r"$40^{x-1}=2^{2x+1}$", font_size=55).shift(UP * 0.5)
        question = Tex("Solve for $x$", font_size=50).next_to(expr, DOWN, buff=1)

        self.wait(1)
        self.play(Write(waterMark))
        self.play(Write(title))
        self.play(Write(expr))
        self.play(Write(question))
        self.wait(15)


with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = ExponentsLogarithmic()
    scene.render()
