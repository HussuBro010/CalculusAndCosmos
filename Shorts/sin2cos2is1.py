from manim import *

config.pixel_width = 1080 * 2
config.pixel_height = 1920 * 2


class proof(Scene):
    def construct(self):
        # CONSTANTS
        EXPR_FONT_SIZE = 100
        BG = "#141414"

        self.camera.background_color = BG
        title = Tex(r"Why $\sin^{2}(\theta) + \cos^{2}(\theta) = 1$?", font_size=100)

        self.wait(1)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.shift(UP * 11))
        self.wait(2)


        pythagoreanTheorem = MathTex("a^2", " + ", "b^2", " = ", "c^2", font_size=EXPR_FONT_SIZE)
        expr2 = MathTex(r"\frac{a^2 + b^2}{c^2}", " = ", r"\frac{c^2}{c^2}", font_size=EXPR_FONT_SIZE)
        expr3 = MathTex(r"\frac{a^2}{c^2}", " + ", r"\frac{b^2}{c^2}", " = ", r"\frac{c^2}{c^2}", font_size=EXPR_FONT_SIZE)
        expr4 = MathTex(r"\left (\frac{a}{c} \right )^2 ", " + ", r"\left (\frac{b}{c} \right )^2 ", " = ", "1", font_size=EXPR_FONT_SIZE)
        expr5 = MathTex(r"(\sin(\theta))^2", " + ", r"(\cos(\theta))^2", " = ", "1", font_size=EXPR_FONT_SIZE)
        expr6 = MathTex(r"\sin^2(\theta)", " + ", r"\cos^2(\theta)", " = ", "1", font_size=EXPR_FONT_SIZE)

        expressions = VGroup(pythagoreanTheorem, expr2, expr3, expr4, expr5, expr6).arrange(DOWN, buff=1)
        boundingBox = SurroundingRectangle(expr6, buff=0.5)

        self.wait(2)
        for i in expressions:
            self.play(Write(i))
            self.wait(3)
        self.wait(2)
        self.play(Create(boundingBox), expr6.animate.set_fill(color=YELLOW))
        self.wait(1)


