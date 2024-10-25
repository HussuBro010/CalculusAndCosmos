from manim import *
from manim_util_lib.mobject import BetterRegularPolygon


class Polygon2(VMobject):
    def __init__(self, n: int, angle, **kwargs):
        super().__init__(**kwargs)
        self.n = n
        self.poly = RegularPolygon(self.n).scale(1.5).set_z_index(3)
        if self.n % 2 == 0:
            self.angle = Angle.from_three_points(self.poly.get_vertices()[2],
                                                 self.poly.get_vertices()[1],
                                                 self.poly.get_vertices()[0])
        elif self.n % 2 != 0:
            self.angle = Angle.from_three_points(self.poly.get_vertices()[1],
                                                 self.poly.get_vertices()[0],
                                                 self.poly.get_vertices()[-1])
        self.label = MathTex(f"{angle}^\circ", font_size=30).next_to(self.angle, DOWN, buff=0.2)
        self.angle.set_z_index(2)
        self.label.set_z_index(2)

        self.lines = [Line(i, ORIGIN, color=DARK_GRAY).set_z_index(1) for i in self.poly.get_vertices()]

        self.angle2 = Angle.from_three_points(self.lines[-2].get_start(), ORIGIN, self.lines[-1].get_start(),
                                              color=DARK_GRAY).set_z_index(1)
        self.label2 = MathTex(f"{180 - angle}^\circ", font_size=30, color=DARK_GRAY).next_to(self.angle2, DOWN,
                                                                                             buff=0.2)

        self.add(self.poly, self.angle, self.label, *self.lines, self.angle2, self.label2)


class Polygons(Scene):

    def construct(self):
        self.camera.background_color = "#141414"
        def angle(n: int) -> int:
            return int((180 * (n - 2)) / n)

        triangle = Polygon2(3, angle(3))
        square = Polygon2(4, angle(4))
        pentagon = Polygon2(5, angle(5))
        hexagon = Polygon2(6, angle(6))
        heptagon = Polygon2(7, angle(7))
        octagon = Polygon2(8, angle(8))
        enneagon = Polygon2(9, angle(9))
        decagon = Polygon2(10, angle(10))

        undecagon = Polygon2(11, angle(11))
        dodecagon = Polygon2(12, angle(12))
        tridecagon = Polygon2(13, angle(13))
        tetradecagon = Polygon2(14, angle(14))
        pentadecagon = Polygon2(15, angle(15))
        hexadecagon = Polygon2(16, angle(16))
        heptadecagon = Polygon2(17, angle(17))
        octadecagon = Polygon2(18, angle(18))
        enneadecagon = Polygon2(19, angle(19))
        icosagon = Polygon2(20, angle(20))

        triangleTex = Tex("Triangle", font_size=65).to_edge(DOWN)
        squareTex = Tex("Square", font_size=65).to_edge(DOWN)
        pentagonTex = Tex("Pentagon", font_size=65).to_edge(DOWN)
        hexagonTex = Tex("Hexagon", font_size=65).to_edge(DOWN)
        heptagonTex = Tex("Heptagon", font_size=65).to_edge(DOWN)
        octagonTex = Tex("Octagon", font_size=65).to_edge(DOWN)
        enneagonTex = Tex("Enneagon", font_size=65).to_edge(DOWN)
        decagonTex = Tex("Decagon", font_size=65).to_edge(DOWN)

        undecagonTex = Tex("Undecagon", font_size=65).to_edge(DOWN)
        dodecagonTex = Tex("Dodecagon", font_size=65).to_edge(DOWN)
        tridecagonTex = Tex("Tridecagon", font_size=65).to_edge(DOWN)
        tetradecagonTex = Tex("Tetradecagon", font_size=65).to_edge(DOWN)
        pentadecagonTex = Tex("Pentadecagon", font_size=65).to_edge(DOWN)
        hexadecagonTex = Tex("Hexadecagon", font_size=65).to_edge(DOWN)
        heptadecagonTex = Tex("Heptadecagon", font_size=65).to_edge(DOWN)
        octadecagonTex = Tex("Octadecagon", font_size=65).to_edge(DOWN)
        enneadecagonTex = Tex("Enneadecagon", font_size=65).to_edge(DOWN)
        icosagonTex = Tex("Icosagon", font_size=65).to_edge(DOWN)

        polygons = [triangle, square, pentagon,
                    hexagon, heptagon, octagon,
                    enneagon, decagon,
                    undecagon, dodecagon, tridecagon,
                    tetradecagon, pentadecagon, hexadecagon,
                    heptadecagon, octadecagon, enneadecagon,
                    icosagon]
        polygonTex = [triangleTex, squareTex, pentagonTex,
                    hexagonTex, heptagonTex, octagonTex,
                    enneagonTex, decagonTex,
                    undecagonTex, dodecagonTex, tridecagonTex,
                    tetradecagonTex, pentadecagonTex, hexadecagonTex,
                    heptadecagonTex, octadecagonTex, enneadecagonTex,
                    icosagonTex]

        nTex = [Tex(f"No. of Sides: {i.n}", font_size=55).to_edge(UP) for i in polygons]

        self.wait(2)
        self.play(Create(triangle), Write(triangleTex), Write(nTex[0]))
        self.wait(1)
        prev = triangle
        prevTex = triangleTex
        prevNTex = nTex[0]
        for i, j, k in zip(polygons, polygonTex, nTex):
            self.play(ReplacementTransform(prev, i), ReplacementTransform(prevTex, j), ReplacementTransform(prevNTex, k))
            self.wait(1)
            prev = i
            prevTex = j
            prevNTex = k
        self.wait(2)
        self.play(Uncreate(icosagon), Uncreate(icosagonTex), Uncreate(nTex[-1]))
        self.wait(1)


with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": False}):
    scene = Polygons()
    scene.render()
