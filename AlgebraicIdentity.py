from manim import *


class Thumbnail(Scene):
	def construct(self):
		title = Title("Algebraic Identity Proof", font_size=80)
		expression = MathTex("(a+b)^{2} = a^{2} + 2ab + b^{2}")
		expression.font_size = 80
		self.add(title, expression)


class Intro(Scene):
	def construct(self):
		title = Title("Algebraic Identity Proof", font_size=80)
		expression = MathTex("(a+b)^{2} = a^{2} + 2ab + b^{2}")
		expression.font_size = 80


		text2 = Text("\nmathematical and visual proof of the Algebraic identity").to_edge(DOWN)
		text = Text(f"Today we will see the").next_to(text2, UP)
		text.font_size = 35
		text2.font_size = 35

		self.play(AddTextLetterByLetter(title, run_time=1))
		self.play(AddTextLetterByLetter(expression, run_time=1))
		self.wait(1.4)
		self.play(AddTextLetterByLetter(text))
		self.wait(0.01)
		self.play(AddTextLetterByLetter(text2))
		self.wait(2)
		self.play(FadeOut(title, expression, text, text2, run_time=1.5))
		self.remove(title, expression, text, text2)
		AlgebraicIdentityMathematical.construct(self)


class AlgebraicIdentityMathematical(Scene):
	def construct(self):
		title = Title("Mathematical Proof", font_size=80)
		expression = MathTex("(", "a", "+", "b", ")", "^{2}")
		expression1 = MathTex("(", "a", "+", "b", ")", r"\cdot", "(", "a", "+", "b", ")")
		expression2 = MathTex("a", "(", "a", "+", "b", ")", "+", "b", "(", "a", "+", "b", ")")
		expression3 = MathTex("a", "^{2}", "+", "a", "b", "+", "a", "b", "+", "b", "^{2}")
		expression4 = MathTex("a", "^{2}", "+", "2", "a", "b", "+", "b", "^{2}")

		finalExpression = MathTex("(", "a", "+", "b", ")", "^{2}", "=", "a", "^{2}", "+", "2", "a", "b", "+", "b", "^{2}")

		fontSize = 70
		expression.font_size = fontSize
		expression1.font_size = fontSize
		expression2.font_size = fontSize
		expression3.font_size = fontSize
		expression4.font_size = fontSize
		finalExpression.font_size = fontSize

		self.play(AddTextWordByWord(title, run_time=1.5))
		self.play(AddTextWordByWord(expression, run_time=1))
		self.wait(1)
		self.play(TransformMatchingTex(expression, expression1))
		self.wait(1)
		self.play(TransformMatchingTex(expression1, expression2))
		self.wait(1)
		self.play(TransformMatchingTex(expression2, expression3))
		self.wait(1)
		self.play(TransformMatchingTex(expression3, expression4))
		self.wait(1)
		self.play(TransformMatchingTex(expression4, finalExpression))
		self.wait(2)
		self.play(RemoveTextLetterByLetter(title, run_time=0.5))
		self.play(RemoveTextLetterByLetter(finalExpression, run_time=0.3))
		self.wait(2)
		AlgebraicIdentityVisual.construct(self)

class AlgebraicIdentityVisual(Scene):
	def construct(self):
		title = Title("Visual Proof", font_size=80)
		expression1 = MathTex("a").shift(UP * 2).set_color_by_tex("a", BLUE)
		expression2 = MathTex("a", "+", "b").shift(UP * 2).set_color_by_tex("a", BLUE).set_color_by_tex("b", RED)
		expression3 = MathTex("(", "a", "+", "b", ")", "^{2}").shift(UP * 2).set_color_by_tex("a", BLUE).set_color_by_tex("b", RED)
		expression4 = MathTex("(", "a", "+", "b", ")", "^{2}", "=", "a^{2}", "+", "ab", "+", "ab", "+", "b^{2}").shift(UP * 2)

		finalExpression = MathTex("(", "a", "+", "b", ")", "^{2}", "=", "a^{2}", "+", "2", "ab", "+", "b^{2}")

		exprFontSize = 70
		expression1.font_size = exprFontSize
		expression2.font_size = exprFontSize
		expression3.font_size = exprFontSize
		expression4.font_size = exprFontSize
		finalExpression.font_size = exprFontSize

		sideA = Line([-1.5, -2, 0], [0.5, -2, 0], color=BLUE)
		sideB = Line(sideA.end, [1.5, -2, 0], color=RED)
		side1A = Line(sideB.end, [1.5, -1, 0], color=RED)
		side1B = Line(side1A.end, [1.5, 1, 0], color=BLUE)
		side2A = Line(side1B.end, [0.5, 1, 0], color=RED)
		side2B = Line(side2A.end, [-1.5, 1, 0], color=BLUE)
		side3A = Line(side2B.end, [-1.5, -1, 0], color=BLUE)
		side3B = Line(side3A.end, [-1.5, -2, 0], color=RED)


		aSquare = Square(side_length=2, color=BLUE).shift([-0.5, 0, 0])
		bSquare = Square(side_length=1, color=RED).shift([1, -1.5, 0])
		labelAsquare = MathTex("a^{2}").shift(aSquare.get_center())
		labelBsquare = MathTex("b^{2}").shift(bSquare.get_center())
		labelAB = Tex("ab").next_to(side1B, LEFT)
		labelBA = Tex("ab").next_to(sideA, UP)

		labelFontSize = 28
		labelAsquare.font_size = labelFontSize
		labelBsquare.font_size = labelFontSize
		labelAB.font_size = labelFontSize
		labelBA.font_size = labelFontSize

		end = Text("Thanks for watching!", font_size=80)

		self.play(AddTextWordByWord(title, run_time=1.5))
		self.wait(1)
		self.play(Create(sideA), Write(expression1))
		self.wait(1)
		self.play(Create(sideB), TransformMatchingTex(expression1, expression2))
		self.wait(1)
		self.play(Create(VGroup(side1A, side1B, side2A, side2B, side3A, side3B)), TransformMatchingTex(expression2, expression3))
		self.wait(1)
		self.play(Create(VGroup(aSquare, bSquare)))
		self.remove(side2B, side3A, sideB, side1A)
		self.wait(0.5)
		self.play(Write(VGroup(labelAsquare, labelBsquare, labelAB, labelBA)))
		self.wait(1)
		self.play(TransformMatchingTex(VGroup(labelAsquare, labelBsquare, labelAB, labelBA, expression3), expression4, key_map={"a^2": "a", "b^2": "b"}))
		self.wait(1.5)
		self.play(Uncreate(VGroup(sideA, side1A, side1B, side2A, side3B, aSquare, bSquare)))
		self.wait(0.8)
		self.play(TransformMatchingTex(expression4, finalExpression))
		self.wait(3.4)

		self.play(FadeOut(title, finalExpression, run_time=1.5))
		self.remove(title, finalExpression)
		self.play(FadeIn(end))
		self.wait(3)
