from manim import *

class Title(Scene):
    def construct(self):
        bg = Rectangle(width=16, height=9).set_fill(color="#000000", opacity=1).set_stroke(width=0)
        self.add.bg()