from manim import *
from pathlib import Path
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

        step_1 = Text("Convert this Image to pixels matrix", font_size=22)
        step_1.next_to(image, DOWN, buff=0.35)

        pil_img = Image.open(image_path).convert("L")
        pil_img = pil_img.resize((13, 13))
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
                text = Text(f"{val:.1f}", font_size=12, color=text_color)
                text.move_to(squrare.get_center())
                cell = VGroup(squrare, text)
                grid.add(cell)
        
        grid.move_to(image.get_center())

        self.play(Write(title))
        self.play(FadeIn(image))
        self.wait(1)
        self.play(FadeIn(step_1))
        self.wait(1)
        self.play(FadeOut(image, run_time=5), FadeIn(grid, run_time=2))
