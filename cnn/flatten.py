from manim import *
import pooling
import sys

class Flatten(Scene):
    def construct(self):
        title = Text("Step 5 — Flattening", font_size=32, weight=BOLD)
        title.to_edge(UP * 1)

        pooled_map = pooling.pooled_map
        self.play(
            Write(title),
            pooled_map.animate.shift(LEFT * 5 + UP * 0.5).scale(1.5)
        )

        pooled_map_cap = Text("Before Flatten", font_size=22)
        pooled_map_cap.next_to(pooled_map, DOWN, buff=0.35)
        self.play(FadeIn(pooled_map_cap))

        cells = list(pooled_map)
        flat_cells = [cell.copy() for cell in cells]
        flat_map = VGroup(*flat_cells)
        flat_map.arrange(DOWN, buff=0.02)
        flat_map.scale(0.55)

        self.play(
            FadeOut(pooled_map_cap),
            *[ Transform(cells[i], flat_cells[i]) for i in range(len(cells))],
            run_time=1.5
        )
        sys.modules[__name__].flat_map = pooled_map

        self.play(Unwrite(title))