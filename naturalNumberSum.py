from manimlib import *
import manim

class Thumbnail(manim.Scene):
    def construct(self):
        que = manim.Tex("Why?", color=YELLOW, font_size=100).shift(UP * 2)
        title = manim.MathTex(r"1 + 2 + 3 + 4 + 5 + \cdots = ", r"-\frac{1}{12}", font_size=80)
        title.submobjects[-1].color = manim.BLUE

        self.add(title, que)


class NaturalNumberSum(Scene):
    def construct(self):
        # Intro
        title1 = Tex(r"1 + 2 + 3 + 4 + 5 + \cdots = ?", font_size=80, t2c={r"?": BLUE})
        title = Tex(r"1 + 2 + 3 + 4 + 5 + \cdots = -\frac{1}{12}", font_size=80, t2c={r"-\frac{1}{12}": BLUE})

        self.wait(2)
        self.play(Write(title1), run_time=5)
        self.wait(2)
        self.play(TransformMatchingParts(title1, title))
        self.wait(2)

        self.play(title.animate.shift(DOWN * 3))

        name = TexText("Srinivasa Ramanujan", font_size=75).set_color(GREEN).shift(UP * 3)

        self.play(Write(name), run_time=2)

        img = ImageMobject("Images/Srinivasa_Ramanujan.jpg")

        self.play(FadeIn(img))

        self.wait(5)

        self.play(FadeOut(VGroup(title, name)), FadeOut(img))

        # Proof p1
        #
        # sum1 = Tex(r"S_1 = 1 - 1 + 1 - 1 + 1 - 1 + \cdots", font_size=75, t2c={"S_1": GREEN}).shift(UP*2)
        # sum1equalTo_even = Tex(" = ", "0", font_size=75).next_to(sum1, DOWN, buff=0.3)
        # sum1equalTo_odd = Tex(" = ", "1", font_size=75).next_to(sum1, DOWN, buff=0.3)
        #
        # sum1equalTo = Tex(" = ", r"\frac{1}{2}", font_size=75, t2c={r"\frac{1}{2}": RED}).next_to(sum1, DOWN, buff=0.3)
        #
        # S1 = Tex(r"S_1 = 1 - 1 + 1 - 1 + 1 - 1 + \cdots = \frac{1}{2}", font_size=75, t2c={"S_1": GREEN, r"\frac{1}{2}": RED}).shift(UP*2)
        #
        # self.wait(5)
        # self.play(Write(sum1), run_time=2)
        # self.wait(5)
        # self.play(Write(sum1equalTo_even))
        # self.wait(5)
        # self.play(TransformMatchingTex(sum1equalTo_even, sum1equalTo_odd))
        # self.wait(5)
        # self.play(TransformMatchingTex(sum1equalTo_odd, sum1equalTo))
        # self.wait(5)
        # self.play(TransformMatchingParts(VGroup(sum1, sum1equalTo), S1))
        # self.wait(5)
        #
        # # Proof p2
        #
        # sum2 = Tex(r"S_2 = 1 - 2 + 3 - 4 + 5 - \cdots", font_size=75, t2c={"S_2": GREEN_A}).shift(UP)
        # sum2Double = Tex(r"2 \cdot S_2 = 1 - 2 + 3 - 4 + 5 - \cdots", font_size=75, t2c={"S_2": GREEN_A}).shift(DOWN * 0.5)
        # sum2Double_a = Tex(r" + 1 - 2 + 3 - 4 + 5 - \cdots", font_size=75).next_to(sum2Double, DOWN, buff=0.5).shift(RIGHT)
        # sum2Double_b = Tex(r" + 0 + 1 - 2 + 3 - 4 + 5 - \cdots", font_size=75).next_to(sum2Double, DOWN, buff=0.5).shift(RIGHT*1.6)
        #
        # self.wait(5)
        # self.play(Write(sum2))
        # self.wait(5)
        # self.play(Write(sum2Double))
        # self.wait(5)
        # self.play(Write(sum2Double_a))
        # self.wait(5)
        # self.play(TransformMatchingTex(sum2Double_a, sum2Double_b))
        # self.wait(5)
        #
        # line = Underline(sum2Double_b, buff=0.3)
        #
        # self.play(ShowCreation(line))
        #
        # sum2DoubleFinal = Tex(r" + 1 - 1 + 1 - 1 + 1 - 1 + \cdots", font_size=75).next_to(sum2Double_b, DOWN, buff=0.6)
        #
        # self.wait(5)
        # self.play(Write(sum2DoubleFinal), run_time=5)
        #
        # DoubleS2a = Tex(r"2 \cdot S_2 = 1 - 1 + 1 - 1 + 1 - 1 + \cdots", font_size=75, t2c={"S_2": GREEN_A}).shift(DOWN * 0.5)
        # DoubleS2b = Tex(r"2 \cdot S_2 = S_1", font_size=75, t2c={"S_2": GREEN_A}).shift(DOWN * 0.5)
        # DoubleS2c = Tex(r"2 \cdot S_2 = \frac{1}{2}", font_size=75, t2c={"S_2": GREEN_A, r"\frac{1}{2}": RED}).shift(DOWN * 0.5)
        # DoubleS2d = Tex(r"S_2 = \frac{1}{4}", font_size=75, t2c={"S_2": GREEN_A, r"\frac{1}{4}": RED_A}).shift(DOWN * 0.5)
        #
        # S2 = Tex(r"S_2 = 1 - 2 + 3 - 4 + 5 - \cdots = \frac{1}{4}", font_size=75, t2c={"S_2": GREEN_A, r"\frac{1}{4}": RED_A}).shift(UP)
        #
        # self.wait(5)
        # self.play(TransformMatchingParts(VGroup(sum2Double_b, line, sum2DoubleFinal, sum2Double), DoubleS2a))
        # self.wait(5)
        # self.play(TransformMatchingTex(DoubleS2a, DoubleS2b))
        # self.wait(5)
        # self.play(TransformMatchingTex(DoubleS2b, DoubleS2c))
        # self.wait(5)
        # self.play(TransformMatchingTex(DoubleS2c, DoubleS2d))
        # self.wait(5)
        # self.play(TransformMatchingParts(VGroup(sum2, DoubleS2d), S2))
        # self.wait(5)
        #
        # self.play(S1.animate.shift(UP*0.4), S2.animate.shift(UP*0.2))
        #
        # # Proof 3
        #
        # sum0 = Tex(r"S = 1 + 2 + 3 + 4 + 5 + \cdots", font_size=75, t2c={"S": YELLOW})
        #
        # sum0_sum2 = Tex(r"S - S_2 = 1 + 2 + 3 + 4 + 5 + \cdots", font_size=75, t2c={"S": YELLOW, "S_2": GREEN_A}).next_to(sum0, DOWN, buff=0.2)
        # sum0_sum2a = Tex(r" - (1 - 2 + 3 - 4 + 5 - \cdots)", font_size=75).next_to(sum0_sum2, DOWN, buff=0.2).shift(RIGHT*1.4)
        #
        # self.wait(5)
        # self.play(Write(sum0))
        # self.wait(5)
        # self.play(Write(sum0_sum2))
        # self.wait(5)
        # self.play(Write(sum0_sum2a))
        # self.wait(5)
        #
        # line2 = Underline(sum0_sum2a, buff=0.3)
        #
        # self.play(ShowCreation(line2))
        #
        # sum0_sum2b = Tex(r" 0 + 4 + 0 + 8 + 0 + 12 + \cdots", font_size=75).next_to(sum0_sum2a, DOWN, buff=0.6)
        # sum0_sum2c = Tex(r"4 + 8 + 12 + \cdots", font_size=75).next_to(sum0_sum2a, DOWN, buff=0.6)
        # sum0_sum2d = Tex(r"4 \cdot (1 + 2 + 3 + \cdots)", font_size=75).next_to(sum0_sum2a, DOWN, buff=0.6)
        #
        # self.wait(5)
        # self.play(Write(sum0_sum2b), run_time=5)
        # self.wait(5)
        # self.play(TransformMatchingTex(sum0_sum2b, sum0_sum2c))
        # self.wait(5)
        # self.play(TransformMatchingTex(sum0_sum2c, sum0_sum2d))
        # self.wait(5)
        #
        # S_S2a = Tex(r"S - S_2 = 4 \cdot (1 + 2 + 3 + \cdots)", font_size=75, t2c={"S": YELLOW, "S_2": GREEN_A}).next_to(sum0, DOWN, buff=0.2)
        # S_S2b = Tex(r"S - S_2 = 4S", font_size=75, t2c={"S": YELLOW, "S_2": GREEN_A}).next_to(sum0, DOWN, buff=0.2)
        # S_S2c = Tex(r"- S_2 = 3S", font_size=75, t2c={"S": YELLOW, "S_2": GREEN_A}).next_to(sum0, DOWN, buff=0.2)
        # S_S2d = Tex(r"- \frac{1}{4} = 3S", font_size=75, t2c={"S": YELLOW, r"\frac{1}{4}": RED_A}).next_to(sum0, DOWN, buff=0.2)
        # S_S2e = Tex(r"-\frac{1}{12} = S", font_size=75, t2c={"S": YELLOW, r"-\frac{1}{12}": BLUE}).next_to(sum0, DOWN, buff=0.2)
        #
        # self.play(FadeOut(VGroup(sum0_sum2a, line2)), TransformMatchingParts(VGroup(sum0_sum2, sum0_sum2d), S_S2a))
        # self.wait(5)
        # self.play(TransformMatchingTex(S_S2a, S_S2b))
        # self.wait(5)
        # self.play(TransformMatchingTex(S_S2b, S_S2c))
        # self.wait(5)
        # self.play(TransformMatchingTex(S_S2c, S_S2d))
        # self.wait(5)
        # self.play(TransformMatchingTex(S_S2d, S_S2e))
        # self.wait(5)
        #
        # S = Tex(r"S = 1 + 2 + 3 + 4 + 5 + \cdots = -\frac{1}{12}", font_size=75, t2c={"S": YELLOW, r"-\frac{1}{12}": BLUE}).shift(DOWN)
        #
        # self.play(TransformMatchingParts(VGroup(S_S2e, sum0), S))
        # self.wait(5)
        #
        # self.play(FadeOut(VGroup(S1, S2)))
        # self.play(S.animate.move_to(ORIGIN))
        # self.play(AnimationOnSurroundingRectangle(S))
        # self.wait(5)
        # self.play(FadeOut(S))
        #
        # # Outro
        # thanks = TexText("Thanks For Watching!!", font_size=90).set_color(GREEN)
        #
        # self.wait(1)
        # self.play(Write(thanks), run_time=3)
        # self.wait(3)
        # self.play(FadeOut(thanks))



