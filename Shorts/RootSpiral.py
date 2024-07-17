from manim import *


class RootSpiral(MovingCameraScene):
    def construct(self):
        self.frame = self.camera.frame

        colors = ["#3D285A", "#502751", "#632547", "#8C2232", "#9D212A", "#B21F1F", "#C54623", "#CE5824",
                  "#D86D26",
                  "#CE5824", "#C54623", "#9D212A", "#8C2232", "#632547", "#502751", "#3D285A"]
        colors = iter(colors)

        title = Tex("Root Spiral", font_size=50).to_edge(UP)

        root2 = VGroup(
            LabeledLine("1", font_size=15, start=RIGHT, end=UR),
            LabeledLine("1", font_size=15, start=ORIGIN, end=RIGHT),
            LabeledLine(r"\sqrt{2}", font_size=15, start=UR, end=ORIGIN)
        )
        root2.set_z_index(2)

        fill = Polygon(root2[0].get_end(), root2[1].get_end(), root2[2].get_end(), fill_opacity=1)

        fill.set_z_index(1)

        fill.set_fill(next(colors))
        fill.stroke_width = 0
        
        self.wait(1)
        self.play(Write(title))
        self.wait(1)
        self.play(Create(root2))
        self.play(FadeIn(fill, run_time=0.2))
        previousRoot = root2

        for i in range(0, 15):
            rootI = VGroup(
                rt31 := LabeledLine("1", font_size=15, start=previousRoot[-1].get_start(),
                                    end=previousRoot[-1].get_start() + (1, 0, 0))
                .set_angle(previousRoot[-1].get_angle() - 90 * DEGREES),
                LabeledLine(fr"\sqrt{i + 3}", font_size=15, start=rt31.get_end(), end=ORIGIN)
            )
            rootI.set_z_index(2)

            fillTriangle = Polygon(previousRoot[0].get_end(), rootI[0].get_end(), rootI[1].get_end(), fill_opacity=1)

            fillTriangle.set_z_index(1)

            fillTriangle.set_fill(next(colors))
            fillTriangle.stroke_width = 0

            previousRoot = rootI
            self.play(self.frame.animate.move_to(rootI.get_center()), run_time=0.1)
            self.play(Create(rootI))
            self.play(FadeIn(fillTriangle, run_time=0.2))

        self.play(self.frame.animate.move_to(ORIGIN))
        self.play(self.frame.animate.set_height(20))
        self.wait(2)


with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = RootSpiral()
    scene.render()
