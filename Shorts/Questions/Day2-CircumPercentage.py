from manim import *


class CircumPercentage(Scene):
    def construct(self):
        title = Tex("Question of the day", font_size=45).to_edge(UP)
        waterMark = Tex("MathViz Animations", font_size=50).to_edge(DOWN)

        question = Tex(
            r"If the smaller circle rolls on the larger one,\\than what percentage of the circumference\\of the larger circle will the\\ smaller one cover in one revolution", font_size=25).shift(UP*2.3)

        circle1 = Circle(1.5).shift(LEFT * 0.5, DOWN)
        radius1 = Line(circle1.get_center(), (circle1.get_center()[0], circle1.get_center()[1] - circle1.radius, 0))
        rLabel = MathTex("r", font_size=20).next_to(radius1, RIGHT, buff=0.1)

        circle2 = Circle(0.5).next_to(circle1, RIGHT, buff=0)
        radius2 = Line(circle2.get_center(), (circle2.get_center()[0] - circle2.radius, circle2.get_center()[1], 0))
        r2Label = MathTex(r"\frac{1}{6}r", font_size=20).next_to(radius2, RIGHT, buff=0.1)

        self.wait(1)
        self.play(Write(waterMark))
        self.play(Write(title))
        self.wait(1)
        self.play(Create(radius1))
        self.play(radius1.animate.rotate(360 * DEGREES, about_point=circle1.get_center()), Create(circle1), run_time=0.7, rate_func=smooth)
        self.play(Write(rLabel))
        self.play(Create(radius2))
        self.play(radius2.animate.rotate(360 * DEGREES, about_point=circle2.get_center()), Create(circle2), run_time=0.7, rate_func=smooth)
        self.play(Write(r2Label))
        self.play(Write(question))
        self.wait(15)


with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = CircumPercentage()
    scene.render()
