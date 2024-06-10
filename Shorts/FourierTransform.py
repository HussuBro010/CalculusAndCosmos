import numpy as np
from manim import *


class FourierTransform(Scene):
    def construct(self):
        self.camera.background_color = "#111317"
        ax = Axes(
            x_range=[0, 2, 0.01],
            y_range=[0, 1.5, 0.01],
            x_length=3,
            y_length=3,
            x_axis_config={"include_ticks": False},
            y_axis_config={"include_ticks": False},)

        title = Tex("Fourier Series", font_size=50).next_to(ax, UP, buff=1.5)
        n = 0
        nTex = Tex(fr"n = {n}", font_size=40).next_to(title, DOWN, buff=1.2)

        def getSum(a, l, x):
            result = 0
            for n in range(0, a + 1):
                expr = (1/(2*n + 1)) * (np.sin((2*n + 1) * PI * x))
                result += expr
            return result

        fourierFunc = lambda x: (4/PI) * getSum(n, 2.5, x)
        
        graph = ax.plot(fourierFunc, color=BLUE)

        self.wait(1)
        self.play(Write(title))
        self.play(Create(ax))
        self.play(Write(nTex))
        self.play(Create(graph))
        for i in range(1, 26, 1):
            self.play(ReplacementTransform(nTex, nTex := Tex(fr"n = {i}", font_size=40).next_to(title, DOWN, buff=1.2)),
                      ReplacementTransform(graph, graph := ax.plot(lambda x: (4/PI) * getSum(i, 2, x), color=BLUE)))
            self.wait(0.1)
        self.wait(2)


with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = FourierTransform()
    scene.render()
