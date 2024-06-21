from manim import *
from manim_extras import *


class SemicircleArea(Scene):
    def construct(self):
        self.camera.background_color = "#111317"
        title = Tex("Question of the day", font_size=45).to_edge(UP)
        waterMark = Tex("MathViz Animations", font_size=50).to_edge(DOWN)
        vert1 = (-1.5, -0.5, 0)
        vert2 = (-1.5, 1.5, 0)
        vert3 = (1.5, -0.5, 0)

        triangle = BetterPolygon(vert1, vert2, vert3, color=GREEN)
        sideA = MathTex("3", font_size=30).next_to(triangle, LEFT, buff=0.15)
        sideB = MathTex("4", font_size=30).next_to(triangle, DOWN, buff=0.15)

        midPoint = Dot(triangle.get_center_of_edges(buff=0)[1])

        theta = ValueTracker(-33 * DEGREES)
        radiusLine = always_redraw(lambda:
                                   Line(midPoint.get_center(), triangle.get_vertices()[2]).set_color(YELLOW).set_angle(
                                       theta.get_value(), about_point=midPoint.get_center()))

        semicircle = ArcBetweenPoints(triangle.get_vertices()[2], triangle.get_vertices()[1], angle=PI)
        questionMark = Tex("Find the area of ", font_size=40).next_to(sideB, DOWN, buff=1).shift(LEFT * 0.5)
        miniSemicircle = ArcBetweenPoints(triangle.get_vertices()[2], triangle.get_vertices()[1], angle=PI, fill_opacity=0.5, fill_color=BLUE).scale(
            0.2).next_to(questionMark, RIGHT, buff=0.3)

        self.wait(1)
        self.play(Write(waterMark))
        self.play(Write(title))
        self.play(Create(VGroup(triangle, sideA, sideB)))
        self.play(Create(VGroup(midPoint, radiusLine)))
        self.wait(1)
        radiusLine.add_updater(lambda v: v.set_angle(theta.get_value(), about_point=midPoint.get_center()))
        self.play(theta.animate.set_value(147 * DEGREES), Create(semicircle, run_time=2), run_time=2)
        self.wait(0.5)
        self.play(theta.animate.set_value(57 * DEGREES))
        self.play(semicircle.animate.set_fill(BLUE, opacity=0.5))
        self.play(Write(questionMark))
        self.play(TransformFromCopy(semicircle, miniSemicircle))
        self.wait(15)


with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = SemicircleArea()
    scene.render()
