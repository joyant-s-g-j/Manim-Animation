from manim import *
import convolution

class Function(Scene):
    def construct(self):
        title = Text("Step 3 — Activation Function (ReLU)", font_size=32, weight=BOLD)
        title.to_edge(UP * 1)
        self.add(title)

        feature_map = convolution.result_grid
        feature_map_cap = convolution.result_grid_cap
        self.play(
            Write(title),
            feature_map.animate.shift(LEFT * 8 + UP * 0.5).scale(1.6),
            feature_map_cap.animate.shift(LEFT * 8 + DOWN * 0.5).scale(1)
        )

    
