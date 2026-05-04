from manim import *
from PIL import Image
from pathlib import Path
import numpy as np
import re

def create_grid(data, cell_size=0.35, show_text=True, fill_opacity=None):
    grid = VGroup()
    rows, cols = data.shape

    for i in range(rows):
        for j in range(cols):
            val = data[i][j]

            cell = Square(
                side_length=cell_size,
                # fill_color=WHITE,
                fill_opacity=val if fill_opacity is None else fill_opacity,
                stroke_width=0.5,
                stroke_color=GRAY
            )

            cell.move_to(np.array([j, -i, 0]) * cell_size)

            if show_text:
                text_color = BLACK if val > 0.5 else GRAY_C
                text = Text(f"{val:.1f}", font_size=12, color=text_color).move_to(cell.get_center())
                grid.add(VGroup(cell, text))
            else:
                grid.add(cell)
    
    return grid
        
def relu_feature_map(grid):
    relu_grid = grid.copy()

    for cell in relu_grid:
        value_mob = cell[1]
        value = float(value_mob.get_tex_string())

        new_value = max(0, value)
        new_text = DecimalNumber(new_value, num_decimal_places=2 if new_value > 0 else 0, font_size=18)
        new_text.move_to(value_mob.get_center())

        cell.remove(value_mob)
        cell.add(new_text)

    return relu_grid

def cell_value(cell):
    mob = cell[1]

    if hasattr(mob, "get_value"):
        return float(mob.get_value())

    raw = getattr(mob, "text", None)
    if raw is None:
        raw = getattr(mob, "tex_string", None)
    if raw is None:
        raw = str(mob)
            
    raw = raw.replace("−", "-").strip()
    m = re.search(r"[-+]?\d*\.?\d+", raw)
    if not m:
        return float("-inf")
    return float(m.group())

def make_layer(n, color, fill_color):
    return VGroup(*[
        Circle(radius=0.18, color=color).set_fill(fill_color, opacity=0.25)
        for _ in range(n)
    ]).arrange(DOWN, buff=0.3)

def fully_connect(left_group, right_group):
            lines = VGroup()
            for left in left_group:
                for right in right_group:
                    lines.add(
                        Line(
                            left.get_right(),
                            right.get_left(),
                            stroke_width=1.2,
                            stroke_opacity=0.35,
                            buff=0.05
                        )
                    )
            return lines