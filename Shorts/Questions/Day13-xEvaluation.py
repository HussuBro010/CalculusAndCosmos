from manim import *

class xEvaluation(Scene):
    def construct(self):
        self.camera.background_color = "#111317"
        title = Tex("Question of the day", font_size=45).to_edge(UP)
        waterMark = Tex("Calculus And Cosmos", font_size=40).to_edge(DOWN)

        question = MathTex(r"\text{if } x + \frac{1}{x} = 3").shift(UP * 0.5)
        find = MathTex(r"\text{find } x^2 + \frac{1}{x^2}").shift(DOWN * 0.5)

        self.wait(1)
        self.play(Write(waterMark))
        self.play(Write(title))
        self.play(Write(question))
        self.play(Write(find))
        self.wait(15)

with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = xEvaluation()
    scene.render()