from manim import *

class TrigCotangent(Scene):
    def construct(self):
        self.camera.background_color = "#111317"
        title = Tex("Question of the day", font_size=45).to_edge(UP)
        waterMark = Tex("Calculus And Cosmos", font_size=40).to_edge(DOWN)

        question = Tex("Evaluate:- ").shift(UP * 2)
        expr = MathTex(r"\frac{(1+\sin\theta)(1-\sin\theta)}{(1+\cos\theta)(1-\cos\theta)}", font_size=50).next_to(question, DOWN, buff=0.5)
        cot = MathTex(r"\text{if}\space\cot\theta = \frac{7}{8}", font_size=40).next_to(expr, DOWN, buff=0.5)

        self.wait(1)
        self.play(Write(waterMark))
        self.play(Write(title))
        self.play(Write(question))
        self.play(Write(expr))
        self.play(Write(cot))
        self.wait(15)

        
with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = TrigCotangent()
    scene.render()