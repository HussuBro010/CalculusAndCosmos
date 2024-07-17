from manim import *

class ApproxOne(Scene):
    def construct(self):
        self.camera.background_color = "#111317"
        caption = Tex(r"Today, We will see why\\ $0.99999 \cdots = 1$ ", font_size=35).shift(UP * 3)

        step1 = MathTex(r"x", r" = ", r"0", r".", r"\bar{9}", font_size=45).next_to(caption, DOWN, buff=0.8)
        step2 = MathTex(r"10x", " = ", r"0", r".", r"\bar{9}", r" \times", " 10", font_size=45).next_to(step1, DOWN, buff=0.7)
        step2expand = MathTex(r"10x", r" = ", r"0", r".", r"9", r"9", r"9", r"9", r"9", r" \cdots", r" \times", r" 10", font_size=45).next_to(step1, DOWN, buff=0.7)
        step3expand = MathTex(r"10x", r" =", r" 9", r".", r"9", r"9", r"9", r"9", r"9", r" \cdots", font_size=45).next_to(step1, DOWN, buff=0.7)
        step3 = MathTex(r"10x", r" = ", r"9", r".", r"\bar{9}", font_size=45).next_to(step1, DOWN, buff=0.7)
        step4 = MathTex(r"10x", r" - ", r"x", r" = ", r"9", r".", r"\bar{9}", r" - ", r"x", font_size=45).next_to(step2expand, DOWN, buff=0.7)
        step4expand = MathTex(r"10x", r" - ", r"x", r" = ", r"9", r".", r"9", r"9", r"9", r"9", r" \cdots", r"\\ - ", r"0", r".", r"9", r"9", r"9", r"9", r" \cdots", font_size=45).next_to(step2expand, DOWN, buff=0.7)
        step5 = MathTex(r"9", r"x", r" = ", r"9", font_size=45).next_to(step2expand, DOWN, buff=0.7)
        step6 = MathTex(r"x", r" = ", r"\frac{9}{9}", font_size=45).next_to(step2expand, DOWN, buff=0.7)
        step7 = MathTex(r"x", r" = ", r"1", font_size=45).next_to(step6, DOWN, buff=0.7)


        self.wait(1)
        self.play(Write(caption))
        self.wait(1)
        self.play(Write(step1))
        self.wait(3)
        self.play(Write(step2))
        self.wait(3)
        self.play(TransformMatchingTex(step2, step2expand))
        self.wait(3)
        self.play(TransformMatchingTex(step2expand, step3expand))
        self.wait(3)
        self.play(TransformMatchingTex(step3expand, step3))
        self.wait(3)
        self.play(Write(step4))
        self.wait(3)
        self.play(TransformMatchingTex(step4, step4expand))
        self.wait(3)
        self.play(TransformMatchingTex(step4expand, step5))
        self.wait(3)
        self.play(TransformMatchingTex(step5, step6))
        self.wait(3)
        self.play(Write(step7))
        self.wait(3)

with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = ApproxOne()
    scene.render()