from manim import *

class Thumbnail(Scene):
    def construct(self):
        title = Title("Fourth Side of a Triangle")
        triangle = Polygon((-2, -2, 0), (-1, 3, 0), (4, -2, 0), color=color_gradient(("#62d4a0", "#b76139"), 5)).shift(DOWN * 0.5).shift(LEFT * 1)
        fourthLine = Line([3, 3, 0], [0.55, -3.55, 0]).shift(DOWN * 0.5).shift(LEFT * 1)

        self.add(triangle, fourthLine, title)


class Explanation(Scene):
    def construct(self):
        caption1 = Text("Let's draw a triangle", font_size=35).shift(DOWN * 3)
        triangle = Polygon((-2, -2, 0), (-1, 3, 0), (4, -2, 0), color=color_gradient(("#62d4a0", "#b76139"), 5))
        triangleLines = [always_redraw(lambda: Line(triangle.get_vertices()[0], triangle.get_vertices()[1])),
                         always_redraw(lambda: Line(triangle.get_vertices()[1], triangle.get_vertices()[2])),
                         always_redraw(lambda: Line(triangle.get_vertices()[2], triangle.get_vertices()[0]))
                         ]
        # ===X===X===

        caption2 = Text("We'll mark the midpoints of the sides...", font_size=35).shift(DOWN * 3)

        midpoints = [
            Dot(triangleLines[0].get_center(), color="#2abdd2"),
            Dot(triangleLines[1].get_center(), color="#2abdd2"),
            Dot(triangleLines[2].get_center(), color="#2abdd2")
        ]

        caption3 = Text("The foot of each of it's altitude...", font_size=35).shift(DOWN * 3)

        footLines = [
            DashedLine(triangleLines[0].start, (1.09, 0.9, 0), dash_length=0.1, dashed_ratio=0.7),
            DashedLine(triangleLines[1].start, (triangleLines[1].start[0], -2, 0), dash_length=0.1, dashed_ratio=0.7),
            DashedLine(triangleLines[2].start, (-1.751, -0.841, 0), dash_length=0.1, dashed_ratio=0.7)
        ]

        foots = [
            Dot(footLines[0].end, color="#ebe78f"),
            Dot(footLines[1].end, color="#ebe78f"),
            Dot(footLines[2].end, color="#ebe78f")
        ]

        caption4 = Text("And the midpoints between the \ntriangle's ortho-centre and it's vertices",
                        font_size=35).center().shift(DOWN * 3)

        orthoCentre = Dot((-1, -1, 0), color="#6f0e9b")

        orthoMidpoints = [
            Dot(Line(triangleLines[0].start, orthoCentre.get_center()).get_center(), color="#ff8f42"),
            Dot(Line(triangleLines[1].start, orthoCentre.get_center()).get_center(), color="#ff8f42"),
            Dot(Line(triangleLines[2].start, orthoCentre.get_center()).get_center(), color="#ff8f42")
        ]

        vertices = [
            Dot(triangleLines[0].start, color="#6be870"),
            Dot(triangleLines[1].start, color="#6be870"),
            Dot(triangleLines[2].start, color="#6be870")
        ]

        point9Circle = Circle(1.8, color=LOGO_BLUE).shift(triangle.get_center() + (-1, -1, 0))
        inCircle = Circle(1.63, color=LOGO_RED).shift(triangle.get_center() + (-1, -0.85, 0))
        circumCircle = Circle.from_three_points(triangle.get_vertices()[0], triangle.get_vertices()[1], triangle.get_vertices()[2], color=LOGO_GREEN)

        caption5 = Text(
            "Draw the 9-point circle of this triangle,\n which intersects all the points lying on\neach of the "
            "triangle's sides",
            font_size=30).center().shift(DOWN * 3)

        caption6 = Text("We'll draw two more circles:- the in circle and the circum circle",
                        font_size=35).center().shift(DOWN * 3)

        captionInCircle = (Text("'In Circle' is the largest circle\n we could fit inside a triangle", font_size=35)
                           .center().shift(DOWN * 3))

        captionCircumCircle = (Text("'Circum Circle' is the circle\n on which the triangle's vertices lie", font_size=35)
                               .center().shift(DOWN * 3))

        criteriaCaption = Text("Each of the triangle's sides\n has 3 properties:-", font_size=25).next_to(triangle, LEFT, buff=1).shift(UP * 2)

        property1 = Text("They have end points\n on the Circum Circle", font_size=20, should_center=True).center().next_to(criteriaCaption, DOWN, buff=0.7)
        property2 = Text("They have midpoints\n on the 9-point circle", font_size=20, should_center=True).center().next_to(property1, DOWN, buff=0.7)
        property3 = Text("They are tangent\n to the In Circle ", font_size=20, should_center=True).center().next_to(property2, DOWN, buff=0.7)

        caption7 = Text("Let's draw a line like this",
                        font_size=35).center().shift(DOWN * 3)

        fourthLineCaption = Text("What's special about this line is that\n it follows all the properties of a triangle's side", font_size=35).center().shift(DOWN * 3)

        fourthLine = Line([3, 3, 0], [0.55, -3.55, 0])
        fourthLineMidPoint = Dot(fourthLine.get_center(), color="#982405")
        fourthLineEndpoints = VGroup(Dot(fourthLine.get_start()),
                                     Dot(fourthLine.get_end()))

        endCaption1 = Text("This line is the fourth side of a triangle", font_size=40)
        endCaption2 = Text("It is also known as the Sherman Line \nnamed after its discoverer B.F Sherman in 1993",
                           font_size=38).shift(DOWN * 3)

        diagramPicture = ImageMobject("Images/4SideTriangleDiagram.png")

        self.wait(1.5)
        self.play(Write(caption1))
        self.wait(1)
        self.play(Create(triangle))
        self.wait(1.5)
        self.play(ReplacementTransform(caption1, caption2))
        self.wait(1)
        self.play(Create(VGroup(*midpoints)))
        self.wait(2)
        self.play(ReplacementTransform(caption2, caption3))
        self.wait(1)
        self.play(Create(VGroup(*footLines)))
        self.play(Create(VGroup(*foots)))
        self.wait(2)
        self.play(ReplacementTransform(caption3, caption4))
        self.wait(1)
        self.play(Create(orthoCentre))
        self.play(Create(VGroup(*vertices)))
        self.play(Create(VGroup(*orthoMidpoints)))
        self.wait(2)
        self.play(ReplacementTransform(caption4, caption5))
        self.wait(1)
        self.play(Create(point9Circle))
        self.wait(2)
        self.play(ReplacementTransform(caption5, caption6))
        self.wait(1)
        self.play(Create(VGroup(inCircle, circumCircle)))
        self.wait(2)
        self.play(ReplacementTransform(caption6, captionInCircle))
        self.play(Indicate(inCircle))
        self.wait(2)
        self.play(ReplacementTransform(captionInCircle, captionCircumCircle))
        self.play(Indicate(circumCircle))
        self.wait(2)
        self.play(ReplacementTransform(captionCircumCircle, criteriaCaption))
        self.wait(2)
        self.play(Write(property1))
        self.wait(1)
        self.play(Flash(vertices[0]))
        self.play(Flash(vertices[1]))
        self.play(Flash(vertices[2]))
        self.wait(2)
        self.play(Write(property2))
        self.wait(1)
        self.play(Flash(midpoints[0]))
        self.play(Flash(midpoints[1]))
        self.play(Flash(midpoints[2]))
        self.wait(2)
        self.play(Write(property3))
        self.wait(1)
        self.play(Indicate(VGroup(triangleLines[0], inCircle)))
        self.play(Indicate(VGroup(triangleLines[1], inCircle)))
        self.play(Indicate(VGroup(triangleLines[2], inCircle)))
        self.wait(3)
        self.play(FadeOut(VGroup(*vertices, *midpoints, *triangleLines, *foots, *footLines, *orthoMidpoints, orthoCentre)))
        self.wait(1)
        self.play(Write(caption7))
        self.wait(1)
        self.play(Create(fourthLine))
        self.wait(2)
        self.play(ReplacementTransform(caption7, fourthLineCaption))
        self.play(ApplyWave(property1, run_time=0.8))
        self.play(ApplyWave(property2, run_time=0.8))
        self.play(ApplyWave(property3, run_time=0.8))
        self.wait(2)
        self.play(FadeOut(fourthLineCaption))
        self.play(Indicate(property1))
        self.play(Indicate(fourthLineEndpoints))
        self.wait(2)
        self.play(Indicate(property2))
        self.play(Indicate(fourthLineMidPoint))
        self.wait(2)
        self.play(Indicate(property3))
        self.play(Indicate(VGroup(inCircle, fourthLine)))
        self.wait(3)
        self.play(FadeOut(VGroup(fourthLineEndpoints, fourthLineMidPoint)))
        diagram = VGroup(triangle, inCircle, circumCircle, point9Circle, fourthLine)
        self.play(diagram.animate.scale(0.4).to_edge(UR))
        self.play(FadeOut(criteriaCaption, property1, property2, property3))
        self.wait(1)
        self.play(Write(endCaption1), Indicate(fourthLine))
        self.wait(2)
        self.play(ReplacementTransform(endCaption1, endCaption2))
        self.play(FadeIn(diagramPicture))
        self.wait(4)
        self.play(FadeOut(diagram, diagramPicture, endCaption2))
        self.wait(2)
        self.play(Write(end := Text("Thanks For Watching!!", font_size=70)))
        self.wait(2)
        self.play(FadeOut(end))
        self.wait(1)



with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = Explanation()
    scene.render()
