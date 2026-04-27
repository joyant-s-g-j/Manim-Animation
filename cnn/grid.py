from manim import *
from PIL import Image
from pathlib import Path
import numpy as np

def create_grid(data, cell_size=0.35, show_text=True):
    grid = VGroup()
    rows, cols = data.shape

    for i in range(rows):
        for j in range(cols):
            val = data[i][j]

            cell = Square(
                side_length=cell_size,
                fill_color=WHITE,
                fill_opacity=val,
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
        
