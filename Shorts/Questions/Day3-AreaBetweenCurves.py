from manim import *


class AreaBetweenCurve(Scene):
    def construct(self):
        title = Tex("Question of the day", font_size=45).to_edge(UP)
        waterMark = Tex("MathViz Animations", font_size=50).to_edge(DOWN)

        ax = Axes(
            x_range=(-1, 7),
            y_range=(-1, 6),
            x_length=6,
            y_length=5
        )

        graph1 = ax.plot(lambda x: 0.9 * x, x_range=(-1, 6))
        graph1.color = GREEN

        graph2 = ax.plot(lambda x: 0.6 * (x - 3) ** 2, x_range=(-1, 6))
        graph2.color = BLUE

        area = ax.get_area(
            graph1,
            x_range=(1.5, 6),
            color=BLUE,
            bounded_graph=graph2
        )

        funcTex1 = MathTex("f(x) = 0.9x", font_size=40).next_to(title, DOWN, buff=0.3)
        funcTex1.color = GREEN
        funcTex2 = MathTex("f(x) = 0.6(x-3)^2", font_size=40).next_to(funcTex1, DOWN, buff=0.3)
        funcTex2.color = BLUE

        dashedLine = DashedLine(ax.c2p(1.5, 1.35), ax.c2p(1.5, 0))
        label1 = Tex("1.5", font_size=30).next_to(dashedLine, DOWN, buff=0.1)

        dashedLine2 = DashedLine(ax.c2p(6, 5.4), ax.c2p(6, 0))
        label2 = Tex("6", font_size=30).next_to(dashedLine2, DOWN, buff=0.1)

        question = Tex("?").move_to(area.get_center()).shift(DOWN * 1, LEFT * 0.5)

        self.wait(1)
        self.play(Write(waterMark))
        self.play(Write(title))
        self.play(Create(ax))
        self.play(Create(funcTex1), Create(funcTex2))
        self.play(Create(graph1), Create(graph2))
        self.play(Create(dashedLine), Create(dashedLine2))
        self.play(Create(label1), Create(label2))
        self.play(Create(area))
        self.play(Write(question))
        self.wait(18)


with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = AreaBetweenCurve()
    scene.render()
