from manim import *


class IrrationalPi1(MovingCameraScene):
    def construct(self):
        self.frame = self.camera.frame
        self.frame.set_height(10)

        vect = Line(ORIGIN, DOWN * 2)
        vect2 = Line(DOWN * 2, DOWN * 4)

        value = ValueTracker(0)
        value2 = ValueTracker(0)

        rate = 0.3

        self.play(Create(vect))
        self.play(Create(vect2))

        trace = TracedPath(vect2.get_end).set_color(GREEN)

        value.add_updater(lambda v, dt: v.set_value(dt * rate))
        value2.add_updater(lambda v, dt: v.set_value(dt * rate * PI))

        self.add(value)
        self.add(value2)

        vect.add_updater(lambda v: v.set_angle(v.get_angle() + 0.5 * TAU * value.get_value()))
        vect2.add_updater(
            lambda v: v.set_angle(v.get_angle() + 0.5 * TAU * value2.get_value(), about_point=vect.get_end()).move_to(
                vect.get_end()))

        def update_curve(mob):
            mob.move_to(vect2.get_end())

        self.add(trace)
        self.wait(43)
        self.play(self.camera.frame.animate.scale(0.2).move_to(vect2.get_end()))
        self.frame.add_updater(update_curve)
        self.wait(5)
        self.frame.remove_updater(update_curve)
        self.wait(0.5)
        self.play(FadeOut(vect, vect2, trace), self.camera.frame.animate.scale(10).move_to(ORIGIN))
        self.wait(1)
        IrrationalPi2.construct(self)


class IrrationalPi2(MovingCameraScene):
    def construct(self):
        self.frame = self.camera.frame
        self.frame.set_height(10)

        vect = Line(ORIGIN, DOWN * 2)
        vect2 = Line(DOWN * 2, DOWN * 4)

        value = ValueTracker(0)
        value2 = ValueTracker(0)

        rate = 0.3

        self.play(Create(vect))
        self.play(Create(vect2))

        trace = TracedPath(vect2.get_start).set_color(YELLOW)

        value.add_updater(lambda v, dt: v.set_value(dt * rate))
        value2.add_updater(lambda v, dt: v.set_value(dt * rate * PI))

        self.add(value)
        self.add(value2)

        vect.add_updater(lambda v: v.set_angle(v.get_angle() + 0.5 * TAU * value.get_value()))
        vect2.add_updater(
            lambda v: v.set_angle(v.get_angle() + 0.5 * TAU * value2.get_value(), about_point=vect.get_end()).move_to(
                vect.get_end()))

        def update_curve(mob):
            mob.move_to(vect2.get_start())

        self.add(trace)
        self.wait(43)
        self.play(self.camera.frame.animate.scale(0.2).move_to(vect2.get_start()))
        self.frame.add_updater(update_curve)
        self.wait(5)
        self.frame.remove_updater(update_curve)
        self.wait(0.5)
        self.play(FadeOut(vect, vect2, trace), self.camera.frame.animate.scale(10).move_to(ORIGIN))
        self.wait(1)


with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = IrrationalPi1()
    scene.render()
