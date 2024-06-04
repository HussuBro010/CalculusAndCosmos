from manim import *
from manim_chemistry import *


class AtomModels(Scene):
    def construct(self):
        atomData = {
            "Hydrogen": (1, 1, 0),
            "Helium": (2, 2, 2),
            "Lithium": (3, 3, 4),
            "Beryllium": (4, 4, 5),
            "Boron": (5, 5, 6),
            "Carbon": (6, 6, 6),
            "Nitrogen": (7, 7, 7),
            "Oxygen": (8, 8, 8),
            "Fluorine": (9, 9, 10),
            "Neon": (10, 10, 10),
            "Sodium": (11, 11, 12),
            "Magnesium": (12, 12, 12),
            "Aluminum": (13, 13, 14),
            "Silicon": (14, 14, 14),
            "Phosphorus": (15, 15, 16),
            "Sulfur": (16, 16, 16),
            "Chlorine": (17, 17, 18),
            "Argon": (18, 18, 22),
            "Potassium": (19, 19, 20),
            "Calcium": (20, 20, 20),
            "Scandium": (21, 21, 24),
            "Titanium": (22, 22, 26),
            "Vanadium": (23, 23, 28),
            "Chromium": (24, 24, 28),
            "Manganese": (25, 25, 30),
            "Iron": (26, 26, 30),
            "Cobalt": (27, 27, 32),
            "Nickel": (28, 28, 31),
            "Copper": (29, 29, 35),
            "Zinc": (30, 30, 35),
            "Gallium": (31, 31, 39),
            "Germanium": (32, 32, 41),
            "Arsenic": (33, 33, 42),
            "Selenium": (34, 34, 45),
            "Bromine": (35, 35, 45),
            "Krypton": (36, 36, 48),
            "Rubidium": (37, 37, 48),
            "Strontium": (38, 38, 50),
            "Yttrium": (39, 39, 50),
            "Zirconium": (40, 40, 51),
            "Niobium": (41, 41, 52),
            "Molybdenum": (42, 42, 54),
            "Technetium": (43, 43, 55),
            "Ruthenium": (44, 44, 57),
            "Rhodium": (45, 45, 58),
            "Palladium": (46, 46, 60),
            "Silver": (47, 47, 61),
            "Cadmium": (48, 48, 64),
            "Indium": (49, 49, 66),
            "Tin": (50, 50, 69),
            "Antimony": (51, 51, 71),
            "Tellurium": (52, 52, 76),
            "Iodine": (53, 53, 74),
            "Xenon": (54, 54, 77),
            "Cesium": (55, 55, 78),
            "Barium": (56, 56, 81),
            "Lanthanum": (57, 57, 82),
            "Cerium": (58, 58, 82),
            "Praseodymium": (59, 59, 82),
            "Neodymium": (60, 60, 84),
            "Promethium": (61, 61, 84),
            "Samarium": (62, 62, 88),
            "Europium": (63, 63, 89),
            "Gadolinium": (64, 64, 93),
            "Terbium": (65, 65, 94),
            "Dysprosium": (66, 66, 97),
            "Holmium": (67, 67, 98),
            "Erbium": (68, 68, 99),
            "Thulium": (69, 69, 100),
            "Ytterbium": (70, 70, 103),
            "Lutetium": (71, 71, 104),
            "Hafnium": (72, 72, 106),
            "Tantalum": (73, 73, 108),
            "Tungsten": (74, 74, 110),
            "Rhenium": (75, 75, 111),
            "Osmium": (76, 76, 114),
            "Iridium": (77, 77, 115),
            "Platinum": (78, 78, 117),
            "Gold": (79, 79, 118),
            "Mercury": (80, 80, 121),
            "Thallium": (81, 81, 123),
            "Lead": (82, 82, 125),
            "Bismuth": (83, 83, 126),
            "Polonium": (84, 84, 125),
            "Astatine": (85, 85, 125),
            "Radon": (86, 86, 136),
            "Francium": (87, 87, 136),
            "Radium": (88, 88, 138),
            "Actinium": (89, 89, 138),
            "Thorium": (90, 90, 142),
            "Protactinium": (91, 91, 140),
            "Uranium": (92, 92, 146),
            "Neptunium": (93, 93, 144),
            "Plutonium": (94, 94, 150),
            "Americium": (95, 95, 148),
            "Curium": (96, 96, 151),
            "Berkelium": (97, 97, 150),
            "Californium": (98, 98, 153),
            "Einsteinium": (99, 99, 153),
            "Fermium": (100, 100, 157),
            "Mendelevium": (101, 101, 157),
            "Nobelium": (102, 102, 157),
            "Lawrencium": (103, 103, 159),
            "Rutherfordium": (104, 104, 157),
            "Dubnium": (105, 105, 157),
            "Seaborgium": (106, 106, 160),
            "Bohrium": (107, 107, 160),
            "Hassium": (108, 108, 169),
            "Meitnerium": (109, 109, 159),
            "Darmstadtium": (110, 110, 161),
            "Roentgenium": (111, 111, 161),
            "Copernicium": (112, 112, 173),
            "Nihonium": (113, 113, 171),
            "Flerovium": (114, 114, 175),
            "Moscovium": (115, 115, 173),
            "Livermorium": (116, 116, 177),
            "Tennessine": (117, 117, 177),
            "Oganesson": (118, 118, 176)
        }
        elementList = [BohrAtom(*i).scale(0.45) for i in atomData.values()]
        elementLabelList = [
            MElementObject.from_csv_file_data(filename="../Assets/Atoms/Elements.csv", atomic_number=i + 1).shift(
                DOWN * 2).scale(0.5) for i in range(118)]

        # Initialize with the first shape
        currentShape = elementList[0]
        currentLabel = elementLabelList[0]
        self.play(FadeIn(currentShape), FadeIn(currentLabel))
        self.wait(0.2)

        # Iterate over the list and transform each shape to the next
        for nextShape, nextLabel in zip(elementList[1:], elementLabelList[1:]):
            self.play(Transform(currentShape, nextShape),
                      Transform(currentLabel, nextLabel))
            self.wait(0.2)

        # Fade out the final shape
        self.play(FadeOut(currentShape), FadeOut(currentLabel))
        self.wait(1)


with tempconfig({"preview": True, "quality": "fourk_quality", "disable_caching": True}):
    scene = AtomModels()
    scene.render()
