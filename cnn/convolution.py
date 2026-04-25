from manim import *
import inputImage
from grid import create_grid
import numpy as np

class Convolution(Scene):
    def construct(self):
        title = Text("Step 2 — Convolution Operation", font_size=32, weight=BOLD)
        title.to_edge(UP * 1)
        self.add(title)
        self.play(Write(title))

        grid_ref = inputImage.grid
        self.play(grid_ref.animate.shift(LEFT * 3.5))

        img_cap = Text("Input Image (13 x 13)", font_size=22)
        img_cap.next_to(grid_ref, DOWN, buff=0.35)
        self.play(FadeIn(img_cap))

        kernel = np.array([
            [1, 0, -1],
            [1, 0, -1],
            [1, 0, -1]
        ])
        filter = create_grid(kernel)
        filter.move_to(RIGHT * 3.5)
        filter.scale(2)
        self.play(FadeIn(filter))

        filter_cap = Text("Filter (Kernel) (3 x 3)", font_size=22)
        filter_cap.next_to(filter, DOWN, buff=0.35)
        self.play(FadeIn(filter_cap))

        
