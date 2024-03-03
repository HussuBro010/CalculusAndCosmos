from manim import *


class Thumbnail(ThreeDScene):
	def construct(self):
		title = Title("3D Shapes Formulas", font_size=80)
		cuboid = Prism([4, 2, 2]).rotate(-90 * DEGREES, X_AXIS).rotate(45 * DEGREES, Y_AXIS).shift([-4, 0, 0])
		sphere = Sphere(center=[0, 0, 0], radius=1.3, resolution=(150, 150)).rotate(40 * DEGREES, X_AXIS)
		cylinder = Cylinder(1.3, 4, Y_AXIS).shift([4, 0, 0])

		self.add(title, cuboid, sphere, cylinder)


class Intro(ThreeDScene):
	def construct(self):
		title = Title("3D Shapes Formulas", font_size=80)

		text1 = Text("Today we will see the ", font_size=50)
		text2 = Text("volume of different 3d shapes", font_size=50).next_to(text1, DOWN)

		self.play(Create(title))
		self.wait(1)
		self.play(AddTextLetterByLetter(text1, run_time=0.5))
		self.play(AddTextLetterByLetter(text2, run_time=0.5))
		self.wait(2)
		self.play(FadeOut(VGroup(title, text1, text2)))
		self.wait(2)
		CuboidVolume.construct(self)


class CuboidVolume(ThreeDScene):
	def construct(self):
		title = Title("Cuboid")

		length = MathTex("l").to_edge(DOWN * -3)
		area = MathTex("l", r"\cdot", "b").to_edge(DOWN * -3)
		volume = MathTex("l", r"\cdot", "b", r"\cdot", "h").to_edge(DOWN * -3)

		label = [
				Text("length").next_to(length, DOWN * 0.5),
				Text("area").next_to(area, DOWN * 0.5),
				Text("volume").next_to(volume, DOWN * 0.5),
		]

		dot = Dot()
		line = Rectangle(width=4, height=0.0000001)
		rect = Rectangle(width=4, height=2)
		cuboid = Prism([4, 2, 2]).rotate(-90 * DEGREES, X_AXIS).rotate(45 * DEGREES, Y_AXIS).shift([0, -1, 0])

		self.play(Create(title))
		self.play(Create(dot))
		self.wait(1.5)
		self.play(ReplacementTransform(dot, line), Write(length), Write(label[0]))
		self.wait(1.5)
		self.play(ReplacementTransform(line, rect), TransformMatchingTex(length, area),
		          TransformMatchingShapes(label[0], label[1]))
		self.wait(1.5)
		self.play(rect.animate.shift([0, -2, 0]))
		self.play(Rotate(rect, -90 * DEGREES, X_AXIS))
		self.wait(0.000000001)
		self.play(Rotate(rect, 45 * DEGREES, Y_AXIS))
		self.play(Transform(rect, cuboid), TransformMatchingTex(area, volume),
		          TransformMatchingShapes(label[1], label[2]))
		self.wait(3)
		self.play(FadeOut(title, volume, label[2]))
		self.remove(cuboid, rect)
		self.wait(2)
		SphereVolume.construct(self)


class SphereVolume(ThreeDScene):
	def construct(self):
		title = Title("Sphere", font_size=90)

		radius = MathTex("r").to_edge(DOWN * -3.4)
		area = MathTex(r"\pi", r"\cdot", "r^{2}").to_edge(DOWN * -3.4)
		volume = MathTex(r"\frac{4}{3}", "\pi", "r^{3}").to_edge(DOWN * -3.4)

		label = [
				Text("radius", font_size=40).next_to(radius, DOWN * 0.5),
				Text("area", font_size=40).next_to(area, DOWN * 0.5),
				Text("volume", font_size=40).next_to(volume, DOWN * 0.5),
		]

		dot = Dot().shift([0, -1, 0])
		line = Line([0, -1, 0], [1.3, -1, 0])
		circle = Circle(radius=1.3, color=WHITE).shift([0, -1, 0])

		sphere = Sphere(center=[0, -1, 0], radius=1.3, resolution=(150, 150)).rotate(40 * DEGREES, X_AXIS)

		self.play(Create(title))
		self.wait(2)
		self.play(Create(dot))
		self.play(Create(line), Write(radius), Write(label[0]))
		self.wait(1)
		self.play(Create(circle, run_time=1),
		          Rotate(line, 360 * DEGREES, run_time=1, about_point=[0, -1, 0]),
		          TransformMatchingTex(radius, area),
		          TransformMatchingShapes(label[0], label[1]))
		self.wait(1.5)
		self.play(FadeOut(line, dot))
		self.play(circle.animate.rotate(40 * DEGREES, X_AXIS))
		self.wait(1)
		self.play(Rotate(circle, 360 * DEGREES, axis=[0, 1, 1], run_time=1, rate_func=linear),
		          Create(sphere, run_time=1))
		self.play(TransformMatchingTex(area, volume),
		          TransformMatchingShapes(label[1], label[2]))
		self.wait(2)
		self.play(FadeOut(VGroup(title, volume, label[2], sphere, circle)))
		self.wait(2)
		CylinderVolume.construct(self)

class CylinderVolume(ThreeDScene):
	def construct(self):
		title = Title("Cylinder", font_size=90)

		radius = MathTex("r").to_edge(DOWN * -3.4)
		area = MathTex(r"\pi", r"\cdot", "r^{2}").to_edge(DOWN * -3.4)
		volume = MathTex(r"\pi", r"\cdot", "r^{2}", "\cdot", "h").to_edge(DOWN * -3.4)

		label = [
				Text("radius", font_size=40).next_to(radius, DOWN * 0.5),
				Text("area", font_size=40).next_to(area, DOWN * 0.5),
				Text("volume", font_size=40).next_to(volume, DOWN * 0.5),
		]

		dot = Dot().shift([0, -1, 0])
		line = Line([0, -1, 0], [1.3, -1, 0])
		circle = Circle(radius=1.3, color=WHITE).shift([0, -1, 0])

		cylinder = Cylinder(1.3, 4, Y_AXIS).shift([0, -1, 0])

		self.play(Create(title))
		self.wait(2)
		self.play(Create(dot))
		self.play(Create(line), Write(radius), Write(label[0]))
		self.wait(1)
		self.play(Create(circle, run_time=1),
		          Rotate(line, 360 * DEGREES, run_time=1, about_point=[0, -1, 0]),
		          TransformMatchingTex(radius, area),
		          TransformMatchingShapes(label[0], label[1]))
		self.wait(1.5)
		self.play(FadeOut(line, dot))
		self.wait(1)
		self.play(circle.animate.shift([0, -2, 0]))
		self.play(Rotate(circle, -90 * DEGREES, X_AXIS))
		self.wait(0.000000001)
		self.play(Rotate(circle, 45 * DEGREES, Y_AXIS))
		self.wait(1.5)
		self.play(Transform(circle, cylinder),
		          TransformMatchingTex(area, volume),
		          TransformMatchingShapes(label[1], label[2]))
		self.wait(2)
		self.play(FadeOut(VGroup(title, volume, label[2], cylinder, circle)))
		self.wait(3)

		self.play(AddTextLetterByLetter(Text("Thanks For Watching!", font_size=100)))


with tempconfig({"preview": True, "quality": "low_quality", "disable_caching": True}):
    scene = Thumbnail()
    scene.render()