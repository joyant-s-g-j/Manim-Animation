from manim import *
import re
import function

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

class Pooling(MovingCameraScene):
    def construct(self):
        title = Text("Step 4 — Pooling Layer(Max Pooling)", font_size=32, weight=BOLD)
        title.to_edge(UP * 1)

        relu_map = function.relu_map
        self.play(
            Write(title),
            relu_map.animate.shift(LEFT * 5)
        )

        relu_map_cap = Text("Before Pooling", font_size=22)
        relu_map_cap.next_to(relu_map, DOWN, buff=0.35)
        self.play(FadeIn(relu_map_cap))

        cells = VGroup()
        block_cells = []
        
        row_len = int(len(relu_map) ** 0.5)
        for i in range(2):
            for j in range(2):
                idx = i * row_len + j
                cell = relu_map[idx]
                cells.add(cell)
                block_cells.append(cell)

        overlay_block = SurroundingRectangle(
            cells,
            color=RED,
            buff=0,
            stroke_width=2
        )

        self.play(Create(overlay_block))

        max_cell = max(
            block_cells,
            key=cell_value
        )
        self.play(
            max_cell[0].animate.set_fill(RED, opacity=0.25)
        )

                


