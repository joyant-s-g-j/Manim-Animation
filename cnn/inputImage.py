from manim import *
from pathlib import Path
from allFunction import create_grid
from PIL import Image
import numpy as np

class InputImage(Scene):
    def construct(self):
        title = Text("Step 1 — Input Image", font_size=32, weight=BOLD)
        title.to_edge(UP * 1)
        self.add(title)

        image_path = Path(__file__).with_name("cat.png")
        image = ImageMobject(str(image_path))
        image.scale(1)
        image.next_to(title, DOWN, buff=0.35)

        info = Text("Convert this Image to pixels matrix", font_size=22)
        info.next_to(image, DOWN, buff=0.35)

        pil_img = Image.open(image_path).convert("L").resize((10, 10))
        pixels = np.array(pil_img) / 255.0

        import inputImage
        cell_size = image.width / pixels.shape[1]
        grid = create_grid(pixels, cell_size=cell_size)
        inputImage.grid = grid
        grid.move_to(image.get_center())

        self.play(Write(title))
        self.play(FadeIn(image))
        self.wait(1)
        self.play(FadeIn(info))
        self.wait(1)
        self.play(FadeOut(image, run_time=5), FadeIn(grid, run_time=2))
        self.play(
            Unwrite(title),
            Unwrite(info)
        )