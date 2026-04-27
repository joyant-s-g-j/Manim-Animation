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

        img_cap = Text("Input Image (10 x 10)", font_size=22)
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

        cells = list(grid_ref)
        grid_2d = [cells[i*10:(i+1)*10] for i in range(10)]
        
        block = VGroup()

        for i in range(3):
            for j in range(3):
                cell = grid_2d[i][j]
                block.add(cell)
                square = cell[0]

                self.play(square.animate.set_fill(RED, opacity=1), run_time=0.1)

        block_copy = block.copy()
        mul_cap = Text("Element-wise Multiplication and Sum", font_size=22)
        mul_cap.next_to(filter, UP, buff=0.35)
        mul_cap.shift(LEFT * 0.4)
        self.play(
            filter.animate.scale(0.66),
            FadeOut(filter_cap),
            block_copy.animate.scale(0.7),
            block_copy.animate.move_to(RIGHT * 1.1),
            FadeIn(mul_cap)
        )

