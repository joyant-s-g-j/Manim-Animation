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

        selected_cells = [grid_2d[i][j] for i in range(3) for j in range(3)]
        pixel_vals = [float(cell[1].text) for cell in selected_cells]
        kernel_vals = kernel.flatten().tolist()

        terms = [f"({p:g}\\times{k:g})" for p, k in zip(pixel_vals, kernel_vals)]
        row1 = " + ".join(terms[0:3])
        row2 = " + ".join(terms[3:6])
        row3 = " + ".join(terms[6:9])

        mul_sum = MathTex(row1 + r"\\ " + row2 + r"\\ " + row3).scale(0.6)
        mul_sum.next_to(filter, DOWN, buff=0.35)
        mul_sum.shift(LEFT * 1.2)

        total = sum(p * k for p, k in zip(pixel_vals, kernel_vals))
        result = MathTex(rf"= { total:.2f}").scale(0.7)
        result.next_to(mul_sum, DOWN, buff=0.25)

        self.play(Write(mul_sum))
        self.play(Write(result))

        result_grid = create_grid(np.ones((3, 3)) * 0.15, show_text=False, fill_opacity=0)
        result_grid.scale_to_fit_width(filter.width)
        result_grid.scale_to_fit_height(filter.height)
        result_grid.next_to(filter, RIGHT, buff=0.9)
        self.play(FadeIn(result_grid))