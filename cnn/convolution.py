from manim import *
import inputImage

class Convolution(Scene):
    def construct(self):
        title = Text("Step 2 — Convolution Operation", font_size=32, weight=BOLD)
        title.to_edge(UP * 1)
        self.add(title)

        grid_ref = inputImage.grid

        img_cap = Text("Input Image (13 x 13)", font_size=22)
        img_cap.next_to(grid_ref, DOWN, buff=0.35)

        
        
        self.play(grid_ref.animate.shift(LEFT * 3.5))
        self.play(Write(title))
        self.play(FadeIn(img_cap))


