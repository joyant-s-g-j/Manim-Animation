from manim import *
import pooling

class Flatten(Scene):
    def construct(self):
        title = Text("Step 4 — Flattening", font_size=32, weight=BOLD)
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
        one_d = VGroup(*[cell.copy() for cell in cells])
        one_d.arrange(DOWN, buff=0.02)
        one_d.scale(0.6)

        self.play(
            FadeOut(pooled_map_cap),
            *[ Transform(cells[i], one_d[i]) for i in range(len(cells))],
            run_time=1.5
        )