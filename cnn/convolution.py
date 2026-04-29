from manim import *
import inputImage
from grid import create_grid
import numpy as np

class Convolution(Scene):
    def construct(self):
        # ------------------ TITLE ------------------
        title = Text("Step 2 — Convolution Operation & Feature Map", font_size=32, weight=BOLD)
        title.to_edge(UP * 1)
        self.add(title)
        self.play(Write(title))

        # ------------------ INPUT IMAGE ------------------
        grid_ref = inputImage.grid
        self.play(grid_ref.animate.shift(LEFT * 3.5))

        img_cap = Text("Input Image (10 x 10)", font_size=22)
        img_cap.next_to(grid_ref, DOWN, buff=0.35)
        self.play(FadeIn(img_cap))

        # ------------------ KERNEL ------------------
        kernel = np.array([
            [1, 0, -1],
            [1, 0, -1],
            [1, 0, -1]
        ])
        filter = create_grid(kernel)
        filter.move_to(RIGHT * 2)
        filter.scale(2)
        self.play(FadeIn(filter))

        filter_cap = Text("Filter (Kernel) (3 x 3)", font_size=22)
        filter_cap.next_to(filter, DOWN, buff=0.35)
        self.play(FadeIn(filter_cap))

        # ------------------ GRID PROCESS ------------------
        cells = list(grid_ref)
        grid_2d = [cells[i * 10:(i + 1) * 10] for i in range(10)]

        # ------------------ HIGHLIGHT BLOCK (COPY) ------------------
        block = VGroup()
        original_styles = []

        for i in range(3):
            for j in range(3):
                cell = grid_2d[i][j]
                block.add(cell)
                square = cell[0]

                original_styles.append(
                    (square, square.get_fill_color(), square.get_fill_opacity())
                )

                self.play(square.animate.set_fill(RED, opacity=1), run_time=0.1)

        highlight_block = block.copy()
        mul_cap = Text("Element-wise Multiplication and Sum", font_size=22)
        mul_cap.next_to(filter, UP, buff=0.35)
        mul_cap.shift(RIGHT * 0.3)

        self.play(
            filter.animate.scale(0.66),
            FadeOut(filter_cap),
            highlight_block.animate.scale(0.7),
            highlight_block.animate.move_to(RIGHT * 0.2),
            FadeIn(mul_cap)
        )

        selected_cells = [grid_2d[i][j] for i in range(3) for j in range(3)]
        pixel_vals = [float(cell[1].text) for cell in selected_cells]
        kernel_vals = kernel.flatten().tolist()

        terms = [f"({p:g}\\times{k:g})" for p, k in zip(pixel_vals, kernel_vals)]
        row1 = " + ".join(terms[0:3])
        row2 = " + ".join(terms[3:6])
        row3 = " + ".join(terms[6:9])

        mul_sum = MathTex(row1 + r"\\ " + row2 + r"\\ " + row3).scale(0.5)
        mul_sum.next_to(filter, DOWN, buff=0.35)
        mul_sum.shift(LEFT * 0.7)

        total = sum(p * k for p, k in zip(pixel_vals, kernel_vals))
        result = MathTex(rf"= { total:.2f}").scale(0.6)
        result.next_to(mul_sum, DOWN, buff=0.25)

        self.play(Write(mul_sum))
        self.play(Write(result))

        out_rows = 10 - 3 + 1
        out_cols = 10 - 3 + 1

        result_grid = create_grid(np.ones((out_rows, out_cols)) * 0.15, show_text=False, fill_opacity=0)
        result_grid.scale(1.1)
        result_grid.next_to(filter, RIGHT, buff=0.7)
        result_grid.shift(DOWN * 0.5)
        result_grid_cap = Text("Feature Map", font_size=22)
        result_grid_cap.next_to(result_grid, DOWN, buff=0.35)
        self.play(FadeIn(result_grid, result_grid_cap))

        # ------------------ FIRST OUTPUT CELL ------------------
        result_copy = MathTex(rf"{total:.2f}").scale(0.2)
        result_copy.move_to(result.get_center())
        self.play(result_copy.animate.move_to(result_grid[0].get_center()))

        cell_w = grid_2d[0][0][0].width
        cell_h = grid_2d[0][0][0].height

        overlay_block = VGroup()

        # Create the red 3x3 overlay block on top of the input image.
        for i in range(3):
            for j in range(3):
                sq = Square(side_length=cell_w)
                sq.set_stroke(RED, width=2)
                sq.set_fill(RED, opacity=0.5)
                sq.move_to(grid_2d[i][j][0].get_center())
                overlay_block.add(sq)

        self.play(
            *[
                square.animate.set_fill(color, opacity=opacity)
                for square, color, opacity in original_styles
            ],
            FadeIn(overlay_block)
        )

        # ------------------ SLIDING WINDOW LOOP ------------------
        idx = 1

        for row in range(out_rows):
            for col in range(out_cols):

                if row == 0 and col == 0:
                    continue

                if col > 0:
                    self.play(
                        overlay_block.animate.shift(RIGHT * cell_w),
                        run_time=0.07,
                        rate_func=linear
                    )

                elif col == 0 and row > 0:
                    self.play(
                        overlay_block.animate.shift(DOWN * cell_h),
                        run_time=0.07,
                        rate_func=linear
                    )
                    self.play(
                        overlay_block.animate.shift(
                            LEFT * cell_w * (out_cols - 1) 
                        ),
                        run_time=0.07,
                        rate_func=linear
                    )

                selected_cells = [
                    grid_2d[row + i][col + j]
                    for i in range(3)
                    for j in range(3)
                ]

                pixel_vals = [float(cell[1].text) for cell in selected_cells]

                terms = [f"({p:g}\\times{k:g})" for p, k in zip(pixel_vals, kernel_vals)]
                row1 = " + ".join(terms[0:3])
                row2 = " + ".join(terms[3:6])
                row3 = " + ".join(terms[6:9])

                total = sum(p * k for p, k in zip(pixel_vals, kernel_vals))
                mul_sum_loop = MathTex(row1 + r"\\ " + row2 + r"\\ " + row3).scale(0.5)
                mul_sum_loop.next_to(filter, DOWN, buff=0.35)
                mul_sum_loop.shift(LEFT * 0.7)

                result_loop = MathTex(rf"= { total:.2f}").scale(0.6)
                result_loop.next_to(mul_sum_loop, DOWN, buff=0.25)

                result_copy_loop = MathTex(rf"{ total:.2f}").scale(0.2)
                result_copy_loop.move_to(result_loop.get_center())

                self.play(
                    Transform(mul_sum, mul_sum_loop),
                    Transform(result, result_loop),
                    run_time=0.07
                )
                self.play(result_copy_loop.animate.move_to(result_grid[idx].get_center()))

                idx += 1
                 
