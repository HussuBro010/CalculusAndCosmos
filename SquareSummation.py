from manim import *

class SquareSummation(Scene):
	def construct(self):
		wholeSquare = Square(5).shift([0, 1, 0])

		# region Expressions

		half = MathTex(r"\frac{1}{2}").shift([0, -3, 0])
		fourth = MathTex(r"\frac{1}{2}", "+", r"\frac{1}{4}").shift([0, -3, 0])
		eighth = MathTex(r"\frac{1}{2}", "+", r"\frac{1}{4}", "+", r"\frac{1}{8}").shift([0, -3, 0])
		sixteenth = MathTex(r"\frac{1}{2}", "+", r"\frac{1}{4}", "+", r"\frac{1}{8}", "+",
		                    r"\frac{1}{16}").shift([0, -3, 0])
		semiFinal = MathTex(r"\frac{1}{2}", "+", r"\frac{1}{4}", "+", r"\frac{1}{8}",
		                       "+", r"\frac{1}{16}", "+", r"\dotsm", "=", "1").shift([0, -3, 0])

		final = MathTex("\sum_{n=1}^{\infty}", r"\frac{1}{2^n}", "=", "1").shift([0, -3, 0])


		# endregion

		# region Lines
		halfLine = Line(wholeSquare.get_top(), wholeSquare.get_bottom())
		fourthLine = Line(halfLine.get_center(), wholeSquare.get_right())
		eighthLine = Line(fourthLine.get_center(), fourthLine.get_center() + [0, 2.5, 0])
		sixteenthLine = Line(eighthLine.get_center(), eighthLine.get_center() + [1.25, 0, 0])
		thirtysecondLine = Line(sixteenthLine.get_center(), sixteenthLine.get_center() + [0, 1.25, 0])
		sixtyfourthLine = Line(thirtysecondLine.get_center(), thirtysecondLine.get_center() + [0.625, 0, 0])
		oneTwentyEighthLine = Line(sixtyfourthLine.get_center(), sixtyfourthLine.get_center() + [0, 0.625, 0])
		twoFiftySixthLine = Line(oneTwentyEighthLine.get_center(), oneTwentyEighthLine.get_center() + [0.3125, 0, 0])
		fiveTwelvthLine = Line(twoFiftySixthLine.get_center(), twoFiftySixthLine.get_center() + [0, 0.3125, 0])
		oneThousandTwentyFourthLine = Line(fiveTwelvthLine.get_center(), fiveTwelvthLine.get_center() + [0.15625, 0, 0])
		# endregion

		# region Labels
		halfLabel = MathTex(r"\frac{1}{2}").next_to(halfLine, LEFT, [1.2, 0, 0])
		fourthLabel = MathTex(r"\frac{1}{4}", font_size=40).next_to(fourthLine, DOWN * 2)
		eighthLabel = MathTex(r"\frac{1}{8}", font_size=35).next_to(eighthLine, LEFT * 2)
		sixteenthLabel = MathTex(r"\frac{1}{16}", font_size=30).next_to(sixteenthLine, DOWN * 1)
		thirtysecondLabel = MathTex(r"\frac{1}{32}", font_size=25).next_to(thirtysecondLine, LEFT * 1)
		sixtyfourthLabel = MathTex(r"\frac{1}{64}", font_size=20).next_to(sixtyfourthLine, DOWN * 0.5)
		oneTwentyEighthLabel = MathTex(r"\frac{1}{128}", font_size=15).next_to(oneTwentyEighthLine, LEFT * 0.2)
		twoFiftySixthLabel = MathTex(r"\frac{1}{256}", font_size=10).next_to(twoFiftySixthLine, DOWN * 0.25)
		fiveTwelvthLabel = MathTex(r"\frac{1}{512}", font_size=5).next_to(fiveTwelvthLine, LEFT * 0.15)
		oneThousandTwentyFourthLabel = MathTex(r"\frac{1}{1024}", font_size=4).next_to(oneThousandTwentyFourthLine,
		                                                                               DOWN * 0.125)
		# endregion

		all = VGroup(wholeSquare, halfLine, fourthLine, eighthLine, sixteenthLine, thirtysecondLine,
		             sixtyfourthLine, oneTwentyEighthLine, twoFiftySixthLine, fiveTwelvthLine,
		             oneThousandTwentyFourthLine,

		             halfLabel, fourthLabel, eighthLabel, sixteenthLabel, thirtysecondLabel,
		             sixtyfourthLabel, oneTwentyEighthLabel, twoFiftySixthLabel, fiveTwelvthLabel,
		             oneThousandTwentyFourthLabel,

		             semiFinal)

		self.play(Create(wholeSquare))
		self.wait(1)
		self.play(Create(halfLine), Create(halfLabel))
		self.play(Write(half))

		self.play(Create(fourthLine), Create(fourthLabel))
		self.play(TransformMatchingTex(half, fourth))

		self.play(Create(eighthLine), Create(eighthLabel))
		self.play(TransformMatchingTex(fourth, eighth))

		self.play(Create(sixteenthLine), Create(sixteenthLabel))
		self.play(TransformMatchingTex(eighth, sixteenth))

		self.play(Create(thirtysecondLine), Create(thirtysecondLabel))
		self.play(TransformMatchingTex(sixteenth, semiFinal))

		self.play(Create(sixtyfourthLine), Create(sixtyfourthLabel))

		self.play(Create(oneTwentyEighthLine), Create(oneTwentyEighthLabel))

		self.play(Create(twoFiftySixthLine), Create(twoFiftySixthLabel))

		self.play(Create(fiveTwelvthLine), Create(fiveTwelvthLabel))

		self.play(Create(oneThousandTwentyFourthLine), Create(oneThousandTwentyFourthLabel))
		self.wait(2)
		self.play(all.animate.scale(6, about_point=wholeSquare.get_corner(UR)))
		self.wait(1)
		self.play(all.animate.scale(1/6, about_point=wholeSquare.get_corner(UR)))
		self.wait(1.5)
		self.play(Transform(semiFinal, final))
		self.wait(2)

with tempconfig({"preview": True, "quality": "low_quality", "disable_caching": True}):
	scene = SquareSummation()
	scene.render()
