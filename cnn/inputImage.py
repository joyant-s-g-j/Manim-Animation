from manim import *
from pathlib import Path
from PIL import Image
import numpy as np
from grid import create_pixel_grid

class InputImage(Scene):
    def construct(self):
        title = Text("Step 1 — Input Image", font_size=32, weight=BOLD)
        title.to_edge(UP * 1)
        self.add(title)

        image_path = Path(__file__).with_name("cat.png")
        image = ImageMobject(str(image_path))
        image.scale(1)
        image.next_to(title, DOWN, buff=0.35)

        step_1 = Text("Convert this Image to pixels matrix", font_size=22)
        step_1.next_to(image, DOWN, buff=0.35)

        grid = create_pixel_grid(image_path=image_path)
        grid.move_to(image.get_center())

        self.play(Write(title))
        self.play(FadeIn(image))
        self.wait(1)
        self.play(FadeIn(step_1))
        self.wait(1)
        self.play(FadeOut(image, run_time=5), FadeIn(grid, run_time=2))
        self.play(FadeOut(step_1))