from manim import *
import re
import function
import numpy as np
from allFunction import create_grid, cell_value
import sys

class Pooling(Scene):
    def construct(self):
        title = Text("Step 4 — Pooling Layer(Max Pooling)", font_size=32, weight=BOLD)
        title.to_edge(UP * 1)

        relu_map = function.relu_map
        self.play(
            Write(title),
            relu_map.animate.shift(LEFT * 6)
        )

        relu_map_cap = Text("Before Pooling", font_size=22)
        relu_map_cap.next_to(relu_map, DOWN, buff=0.35)
        self.play(FadeIn(relu_map_cap))

        # ------------------ GRID SIZE ------------------
        row_len = int(len(relu_map) ** 0.5)
        window_size = 2
        stride = 2
        pooled_size = row_len // stride

        # ------------------ POOLED MAP ------------------
        pooled_data = np.zeros((pooled_size, pooled_size))

        pooled_map = create_grid(
            pooled_data,
            cell_size=0.35,
            show_text=False,
            fill_opacity=0
        ).scale(1.15)
        pooled_map.next_to(relu_map, RIGHT, buff=1.5)
        self.play(FadeIn(pooled_map))

        pooled_map_cap = Text("After Pooling", font_size=18)
        pooled_map_cap.next_to(pooled_map, DOWN, buff=0.35)
        self.play(Write(pooled_map_cap))

        # ------------------ FIRST CELL (MANUAL) ------------------
        first_block = []
        first_cells = VGroup()
        
        for i in range(window_size):
            for j in range(window_size):
                idx = i * row_len + j
                cell = relu_map[idx]
                first_block.append(cell)
                first_cells.add(cell)

        overlay_block = SurroundingRectangle(
            first_cells,
            color=RED,
            buff=0,
            stroke_width=2
        )

        self.play(Create(overlay_block))

        max_cell = max(first_block, key=cell_value)
        max_val = cell_value(max_cell)

        first_value = DecimalNumber(
            max_val,
            num_decimal_places=2 if max_val > 0 else 0,
            font_size=16
        )
        first_value.move_to(max_cell.get_center())

        self.play(
            first_value.animate.move_to(pooled_map[0].get_center()),
            run_time=0.6
        )

        pooled_map[0].add(first_value)

        # ------------------ LOOP START FROM 2ND CELL ------------------
        idx = 1

        for i in range(0, row_len, stride):
            for j in range(0, row_len, stride):

                if i == 0 and j == 0:
                    continue

                block = []
                cells_group = VGroup()

                for x in range(window_size):
                    for y in range(window_size):
                        cell = relu_map[(i + x) * row_len + (j + y)]
                        block.append(cell)
                        cells_group.add(cell)

                self.play(
                    Transform(overlay_block, SurroundingRectangle(
                        cells_group,
                        color=RED,
                        buff=0,
                        stroke_width=2
                    )),
                    run_time=0.3
                )

                max_cell = max(block, key=cell_value)
                max_val = cell_value(max_cell)

                value_text = DecimalNumber(
                    max_val,
                    num_decimal_places=2 if max_val > 0 else 0,
                    font_size=16
                )
                value_text.move_to(max_cell.get_center())

                self.play(
                    value_text.animate.move_to(pooled_map[idx].get_center()),
                    run_time=0.5
                )

                pooled_map[idx].add(value_text)

                idx += 1
        
        sys.modules[__name__].pooled_map = pooled_map
        self.play(
            Unwrite(title),
            FadeOut(relu_map),
            FadeOut(overlay_block),
            FadeOut(relu_map_cap),
            FadeOut(pooled_map_cap)
        )
        