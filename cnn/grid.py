from manim import *
from PIL import Image
import numpy as np

def create_pixel_grid(image_path):
    pil_img = Image.open(image_path).convert("L").resize((13, 13))
    pixels = np.array(pil_img) / 255.0

    grid = VGroup()

    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            val = pixels[i][j]

            squrare = Square(
                side_length=0.35,
                fill_color=WHITE,
                fill_opacity=val,
                stroke_width=0.5,
                stroke_color=GRAY
            )

            squrare.move_to(np.array([j, -i, 0]) * 0.35)
            text_color = BLACK if val > 0.5 else GRAY_C
            text = Text(f"{val:.1f}", font_size=12, color=text_color).move_to(squrare.get_center())
            grid.add(VGroup(squrare, text))
    
    return grid
        
