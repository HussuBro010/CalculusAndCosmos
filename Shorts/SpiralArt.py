import numpy as np
from manim import *


class SpiralArt(Scene):
    def construct(self):
        spiralArt = Tex("Spiral Art").to_edge(UP)

        ratio1: dict = {
            "0":
                {
                    "len": 1,
                    "rate": 2
                },
            "1":
                {
                    "len": 0.7,
                    "rate": 4
                },
            "2":
                {
                    "len": 1,
                    "rate": -2
                },
            "3":
                {
                    "len": 0.7,
                    "rate": 6
                },
        }

        speedRatio1 = Tex("Speed - $2:4:-2:6$", font_size=30).next_to(spiralArt, DOWN, buff=0.2)
        lenRatio1 = Tex("Length - $1:0.7:1:0.7$", font_size=30).next_to(speedRatio1, DOWN, buff=0.2)

        ratio2: dict = {
            "0":
                {
                    "len": 3,
                    "rate": 1
                },
            "1":
                {
                    "len": 1,
                    "rate": -3
                }
        }

        speedRatio2 = Tex("Speed - $1:-3$", font_size=30).next_to(spiralArt, DOWN, buff=0.2)
        lenRatio2 = Tex("Length - $3:1$", font_size=30).next_to(speedRatio2, DOWN, buff=0.2)

        ratio3: dict = {
            "0":
                {
                    "len": 3,
                    "rate": 1
                },
            "1":
                {
                    "len": 1,
                    "rate": -3
                },
            "2":
                {
                    "len": 0.5,
                    "rate": 7
                }
        }

        speedRatio3 = Tex("Speed - $1:-3:7$", font_size=30).next_to(spiralArt, DOWN, buff=0.2)
        lenRatio3 = Tex("Length - $3:1:0.5$", font_size=30).next_to(speedRatio3, DOWN, buff=0.2)

        ratio4: dict = {
            "0":
                {
                    "len": 1,
                    "rate": 1
                },
            "1":
                {
                    "len": 0.8,
                    "rate": -2
                },
            "2":
                {
                    "len": 0.8,
                    "rate": 3
                },
            "3":
                {
                    "len": 0.5,
                    "rate": -7
                },
            "4":
                {
                    "len": 0.8,
                    "rate": 10
                }
        }

        speedRatio4 = Tex("Speed - $1:-2:3:-7:10$", font_size=30).next_to(spiralArt, DOWN, buff=0.2)
        lenRatio4 = Tex("Length - $1:0.8:0.8:0.5:0.8$", font_size=30).next_to(speedRatio4, DOWN, buff=0.2)

        ratio5: dict = {
            "0":
                {
                    "len": 1,
                    "rate": 5
                },
            "1":
                {
                    "len": 1.6,
                    "rate": -4
                },
            "2":
                {
                    "len": 0.8,
                    "rate": -7
                }
        }

        speedRatio5 = Tex("Speed - $5:-4:-7$", font_size=30).next_to(spiralArt, DOWN, buff=0.2)
        lenRatio5 = Tex("Length - $1:1.6:0.8$", font_size=30).next_to(speedRatio5, DOWN, buff=0.2)

        self.wait(1)
        self.play(Write(spiralArt))
        self.wait(2)
        self.play(Write(VGroup(speedRatio5, lenRatio5)))
        self.wait(1)

        self.pendulum(3, ratio5, 7)
        self.play(Unwrite(VGroup(speedRatio5, lenRatio5)))


        self.wait(2)
        self.play(Write(VGroup(speedRatio1, lenRatio1)))
        self.wait(1)

        self.pendulum(4, ratio1, 7, True, True)
        self.play(Unwrite(VGroup(speedRatio1, lenRatio1)))


        self.wait(2)
        self.play(Write(VGroup(speedRatio2, lenRatio2)))
        self.wait(1)

        self.pendulum(2, ratio2, 7, True, True, True)
        self.play(Unwrite(VGroup(speedRatio2, lenRatio2)))


        self.wait(2)
        self.play(Write(VGroup(speedRatio3, lenRatio3)))
        self.wait(1)

        self.pendulum(3, ratio3, 7, True, True, True)
        self.play(Unwrite(VGroup(speedRatio3, lenRatio3)))


        self.wait(2)
        self.play(Write(VGroup(speedRatio4, lenRatio4)))
        self.wait(1)

        self.pendulum(5, ratio4, 7, True, False)
        self.play(Unwrite(VGroup(speedRatio4, lenRatio4)))


        self.wait(2)

    def pendulum(self, n: int, config: dict, duration: float, tracr2: bool = False, tracr3: bool = False, center: bool = False):
        scale = 0.65
        n = n - 1
        vect = Vector(color=GREY_A).scale(config["0"]["len"] * scale)
        if center:
            vect.put_start_and_end_on(ORIGIN, vect.get_end())
        vect.tip_length = 0.5
        vect.add_updater(lambda v, dt: v.set_angle(v.get_angle() + config["0"]["rate"] * dt))
        vect.suspend_updating()

        # vect2=Vector().shift(vect.get_end()).scale(1/3)
        def rotator(pv, rte):
            def update(mob, dt):
                mob.set_angle(mob.get_angle() + rte * dt, about_point=pv.get_end())
                mob.shift(pv.get_end() - mob.get_start())

            return update

        last = vect
        vgroup = VGroup()
        for i in range(n):
            vect2 = Vector().scale(config[f"{i + 1}"]["len"] * scale)
            vect2.shift(last.get_end() - vect2.get_start())
            vect2.add_updater(rotator(last, config[f"{i + 1}"]["rate"]))
            vect2.suspend_updating()
            vgroup.add(vect2)
            last = vect2

        tracerDot = always_redraw(lambda: Dot(last.get_end()))
        tracerDot2 = always_redraw(lambda: Dot(last.get_start()))
        tracerDot.color = RED
        tracerDot2.color = RED

        tracer = TracedPath(tracerDot.get_center, stroke_width=3.5)
        tracer2 = TracedPath(tracerDot2.get_center)
        tracer3 = TracedPath(last.get_midpoint)

        tracer.color = YELLOW_A
        tracer2.color = YELLOW_B
        tracer3.color = YELLOW_C

        group = VGroup(vect, vgroup, tracerDot, tracer)

        if tracr2:
            group.add(tracerDot2, tracer2)
        if tracr3:
            group.add(tracer3)

        self.play(Create(group, run_time=2))
        self.wait(5)
        vgroup.resume_updating()
        vect.resume_updating()
        self.wait(duration)
        self.play(FadeOut(group, run_time=2))
        vgroup.clear_updaters()
        vect.clear_updaters()


with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = SpiralArt()
    scene.render()
