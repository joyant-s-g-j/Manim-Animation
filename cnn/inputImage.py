from manim import *
from pathlib import Path

class InputImage(Scene):
    def construct(self):
        title = Text("Step 1 — Input Image", font_size=32, weight=BOLD)
        title.to_edge(UP * 1)
        self.add(title)

        image_path = Path(__file__).with_name("cat.png")
        image = ImageMobject(str(image_path))
        image.scale(1)
        image.next_to(title, DOWN, buff=0.8)

        self.play(Write(title))
        self.play(FadeIn(image))