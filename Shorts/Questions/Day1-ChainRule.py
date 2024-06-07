from manim import *


class ChainRule(Scene):
    def construct(self):
        title = Tex("Question of the day", font_size=45).to_edge(UP)
        questionText = (
            Tex(r"Let $f(y) = e^y$ and $g(y) = 10y$\\Calculate $h^{\prime}(y)$, where $h(y) = f(g(y))$", font_size=30)
            .shift(UP))

        hint = (Tex(r"Hint:- Use the Chain Rule", font_size=20).shift(DOWN * 2.7))
        waterMark = Tex("MathViz Animations", font_size=50).to_edge(DOWN)

        self.wait(1)
        self.play(Write(waterMark))
        self.play(Write(title))
        self.play(Write(questionText))
        self.wait(5)
        self.play(Write(hint, run_time=0.5))
        self.wait(14.5)


with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = ChainRule()
    scene.render()
