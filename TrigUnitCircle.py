import numpy as np
from manim import *


class TrigUnitCricle(Scene):
    def construct(self):
        grid = NumberPlane().set_opacity(0.3).scale(2)
        circle = Circle(radius=2)

        circleDrawer = Line([0, 0, 0], [2, 0, 0])

        theta = ValueTracker(45)
        radiusLine = always_redraw(
            lambda: Line([0, 0, 0], [2, 0, 0]).set_angle(theta.get_value() * DEGREES, about_point=ORIGIN))

        angleTheta = always_redraw(lambda: Angle(grid.x_axis, radiusLine, 0.4, quadrant=(1, 1), dot=True))
        thetaTex = always_redraw(lambda: MathTex(r"\theta", font_size=30).move_to(
            [angleTheta.get_center()[0] + 0.2, angleTheta.get_center()[1] + 0.1, 0]))

        thetaTexIndicator = always_redraw(
            lambda: MathTex(fr"\theta = {theta.get_value():.1f}", r"^{\circ}").shift(DOWN * 3))

        # sinTheta = np.sin(radiusLine.get_angle())
        # cosTheta = np.cos(radiusLine.get_angle())
        # tanTheta = np.tan(radiusLine.get_angle())
        # secThera = np.sec

        sinLabel = MathTex(r"\text{sin}\space", r"\theta", font_size=27)
        sinLabel.submobjects[0].color = BLUE_D

        sinLine = always_redraw(
            lambda: LabeledLine(sinLabel, font_size=27, color=BLUE_D, start=radiusLine.get_end(),
                                end=[radiusLine.get_end()[0],
                                     radiusLine.get_end()[1] - (2 * np.sin(radiusLine.get_angle())), 0]))

        cosLabel = MathTex(r"\text{cos}\space", r"\theta", font_size=27)
        cosLabel.submobjects[0].color = GREEN_C

        cosLine = always_redraw(
            lambda: LabeledLine(cosLabel, font_size=27, color=GREEN_C, start=radiusLine.get_end(),
                                end=[radiusLine.get_end()[0] - (2 * np.cos(radiusLine.get_angle())),
                                     radiusLine.get_end()[1], 0])
        )

        secLabel = MathTex(r"\text{sec}\space", r"\theta", font_size=27)
        secLabel.submobjects[0].color = TEAL_D

        secLine = always_redraw(
            lambda: LabeledLine(secLabel, font_size=27, color=TEAL_D, label_position=0.3, start=ORIGIN,
                                end=[2 * (1 / np.cos(radiusLine.get_angle())), 0, 0])

            )

        cscLabel = MathTex(r"\text{csc}\space", r"\theta", font_size=27)
        cscLabel.submobjects[0].color = GOLD

        cscLine = always_redraw(
            lambda: LabeledLine(cscLabel, font_size=27, color=GOLD, label_position=0.3, start=ORIGIN,
                                end=[0, 2 * (1 / np.sin(radiusLine.get_angle())), 0])

            )

        tanLabel = MathTex(r"\text{tan}\space", r"\theta", font_size=27)
        tanLabel.submobjects[0].color = YELLOW_D

        tanLine = always_redraw(lambda: LabeledLine(tanLabel, font_size=27, color=YELLOW_D, start=radiusLine.get_end(),
                                                    end=[2 * (1 / np.cos(radiusLine.get_angle())), secLine.get_end()[1],
                                                         0])

                                )

        cotLabel = MathTex(r"\text{cot}\space", r"\theta", font_size=27)
        cotLabel.submobjects[0].color = MAROON_E
        cotLine = always_redraw(lambda: LabeledLine(cotLabel, font_size=27, color=MAROON_E, start=radiusLine.get_end(),
                                                    end=[-cscLine.get_end()[0],
                                                         2 * (1 / np.sin(radiusLine.get_angle())), 0])

                                )

        self.play(Create(grid))
        self.wait(0.3)
        self.play(Create(circleDrawer, run_time=1))
        self.wait(0.5)
        self.play(Rotate(circleDrawer, 360 * DEGREES, run_time=0.85, about_point=ORIGIN, rate_func=smooth),
                  Create(circle, run_time=0.85))
        self.wait(1)
        self.play(Rotate(circleDrawer, 45 * DEGREES, about_point=ORIGIN, rate_func=smooth))
        self.wait(0.2)
        self.play(FadeTransform(circleDrawer, radiusLine), Create(angleTheta), Create(thetaTex),
                  Create(thetaTexIndicator))
        self.wait(2)
        self.play(Create(sinLine))
        self.wait(1.5)
        self.play(Create(cosLine))
        self.wait(1.5)
        self.play(Create(tanLine))
        self.wait(1.5)
        self.play(Create(secLine))
        self.wait(1.5)
        self.play(Create(cotLine))
        self.wait(1.5)
        self.play(Create(cscLine))
        self.wait(3)
        self.play(theta.animate.set_value(60))
        self.wait(1.5)
        self.play(theta.animate.set_value(30))
        self.wait(2)
        self.play(theta.animate.set_value(45))
        self.wait(2)
        self.play(AnimationGroup(theta.animate.set_value(360), run_time=5, rate_func=linear))
        self.play(AnimationGroup(theta.animate.set_value(45), run_time=5, rate_func=linear))
        self.wait(3)


with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = TrigUnitCricle()
    scene.render()
