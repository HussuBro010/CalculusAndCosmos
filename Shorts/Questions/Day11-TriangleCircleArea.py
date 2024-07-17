import numpy as np
from manim import *
from manim_util_lib import *


class TriangleCircleArea(Scene):
    def construct(self):
        self.camera.background_color = "#111317"
        title = Tex("Question of the day", font_size=45).to_edge(UP)
        waterMark = Tex("MathViz Animations", font_size=50).to_edge(DOWN)

        rightTriangle = BetterPolygon((-1.5, -0.7, 0), (-1.5, 0.8, 0), (1.5, -0.7, 0))

        angle1Line1 = Line((-1.5, -0.7, 0), (1.5, -0.7, 0))
        angle1Line2 = Line((-1.5, 0.8, 0), (1.5, -0.7, 0))

        angle1 = Angle(angle1Line1, angle1Line2, radius=0.7, color=YELLOW, quadrant=(-1, -1), other_angle=True)
        angle1a = Angle(angle1Line1, angle1Line2, radius=0.9, color=YELLOW, quadrant=(-1, -1), other_angle=True)

        angle1Label = MathTex(r"30^{\circ}", font_size=20).move_to(angle1a.get_center())

        angle2Line1 = Line((-1.5, -0.7, 0), (-1.5, 0.8, 0))
        angle2Line2 = Line((1.5, -0.7, 0), (-1.5, 0.8, 0))

        angle2 = Angle(angle2Line1, angle2Line2, radius=0.5, color=YELLOW, quadrant=(-1, -1))
        angle2a = Angle(angle2Line1, angle2Line2, radius=0.8, color=YELLOW, quadrant=(-1, -1))

        angle2Label = MathTex(r"60^{\circ}", font_size=20).move_to(angle2a.get_center())

        angle3Line1 = Line((1.5, -0.7, 0), (-1.5, -0.7, 0))
        angle3Line2 = Line((-1.5, 0.8, 0), (-1.5, -0.7, 0))

        angle3 = RightAngle(angle3Line1, angle3Line2, length=0.2, color=YELLOW, quadrant=(-1, -1))
        angle3a = RightAngle(angle3Line1, angle3Line2, length=0.8, color=YELLOW, quadrant=(-1, -1))

        angle3Label = MathTex(r"90^{\circ}", font_size=20).move_to(angle3a.get_center())

        def distance(a, b):
            return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

        x = 3
        hypotenuse = distance(rightTriangle.get_vertices()[1], rightTriangle.get_vertices()[2] + 0.1)
        perpendicular = distance(rightTriangle.get_center_of_edges()[0], (-1.5, 1.05, 0))

        rect = (Rectangle(width=hypotenuse,
                         height=2).move_to(rightTriangle.get_vertices()[1] + (hypotenuse/2, perpendicular, 0)))
        rect.color = GREEN

        hypotenuseLine = Line(rightTriangle.get_vertices()[1], rightTriangle.get_vertices()[2] + 0.1)

        question = Tex(" $=$ ?", font_size=50).next_to(rightTriangle, DOWN, buff=1).shift(RIGHT * 0.5)

        self.wait(1)
        self.play(Write(waterMark))
        self.play(Write(title))
        self.play(Write(rightTriangle))

        self.play(Create(angle1), Create(angle2), Create(angle3))
        self.play(Write(angle1Label), Write(angle2Label), Write(angle3Label))

        self.play(TransformFromCopy(hypotenuseLine, rect))
        self.wait(1)
        self.play(Rotate(rect, -27 * DEGREES, about_point=rect.get_vertices()[2], rate_func=rate_functions.ease_out_back))

        circle = Circle(1).move_to(rect.get_center()).rotate(60*DEGREES)
        circle.color = GREEN

        radius = Line(circle.get_center(), circle.get_center() + (circle.radius, 0, 0)).rotate(60*DEGREES, about_point=circle.get_center())
        radiusLabel = MathTex("2", font_size=25).next_to(radius, LEFT, buff=0.01).shift(UP * 0.15, RIGHT * 0.15)

        self.play(Create(radius))
        self.play(Rotate(radius, 360 * DEGREES, about_point=circle.get_center(), run_time=1), Create(circle, run_time=1))

        self.play(Write(radiusLabel))
        self.play(rect.animate.set_fill(BLUE))

        findArea = Cutout(rect, circle, color=GREEN, fill_color=BLUE, fill_opacity=0.5)
        miniArea = findArea.copy().scale(0.3).next_to(question, LEFT, buff=0.3)

        self.play(Write(findArea))
        self.wait(1)
        self.play(TransformFromCopy(findArea, miniArea))
        self.play(Write(question))

        self.wait(15)


with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = TriangleCircleArea()
    scene.render()
