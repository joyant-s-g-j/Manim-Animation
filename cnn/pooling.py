from manim import *
import re
import function
import numpy as np
from allFunction import create_grid, cell_value

class Pooling(MovingCameraScene):
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

        cells = VGroup()
        block_cells = []
        
        row_len = int(len(relu_map) ** 0.5)
        for i in range(2):
            for j in range(2):
                idx = i * row_len + j
                cell = relu_map[idx]
                cells.add(cell)
                block_cells.append(cell)

        overlay_block = SurroundingRectangle(
            cells,
            color=RED,
            buff=0,
            stroke_width=2
        )

        self.play(Create(overlay_block))

        max_cell = max(
            block_cells,
            key=cell_value
        )
        self.play(
            max_cell[0].animate.set_fill(RED, opacity=0.25)
        )

        pooled_size = row_len // 2
        pooled_data = np.zeros((pooled_size, pooled_size))
        pooled_map = create_grid(
            pooled_data,
            cell_size=0.35,
            show_text=False,
            fill_opacity=0
        ).scale(1.15)
        
        arrow = Arrow(
            relu_map.get_right(),
            pooled_map.get_left(),
            buff=0.35
        ).shift(UP * 0.1)
        self.play(GrowArrow(arrow))
        self.play(FadeIn(pooled_map))

        pooled_map_cap = Text("After Pooling", font_size=18)
        pooled_map_cap.next_to(pooled_map, DOWN, buff=0.35)
        self.play(Write(pooled_map_cap))

        max_val = cell_value(max_cell)
        value_text = DecimalNumber(
            max_val,
            num_decimal_places=2 if max_val > 0 else 0,
            font_size=16
        )
        value_text.move_to(max_cell.get_center())
        self.play(
            value_text.animate.move_to(pooled_map[0].get_center()),
            run_time=0.7
        )
        pooled_map[0].add(value_text)