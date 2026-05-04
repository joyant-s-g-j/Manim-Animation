from manim import *
import flatten
from allFunction import make_layer, fully_connect

class Dense(Scene):
    def construct(self):
        title = Text("Step 6 — Fully Connected Layer", font_size=32, weight=BOLD)
        title.to_edge(UP * 1)

        flat_map = flatten.flat_map
        self.add(flat_map)
        self.play(
            Write(title),
            flat_map.animate.shift(LEFT * 6)
        )

        hidden1 = make_layer(10, GREEN, GREEN_E)
        hidden2 = make_layer(8, YELLOW, YELLOW_E)
        hidden3 = make_layer(6, RED, RED_E)
        output_layer = make_layer(3, BLUE, BLUE_E)
        
        hidden1.next_to(flat_map, RIGHT, buff=2)
        hidden2.next_to(hidden1, RIGHT, buff=2)
        hidden3.next_to(hidden2, RIGHT, buff=2)
        output_layer.next_to(hidden3, RIGHT, buff=2)

        conn1 = fully_connect(flat_map.submobjects, hidden1.submobjects)
        conn2 = fully_connect(hidden1.submobjects, hidden2.submobjects)
        conn3 = fully_connect(hidden2.submobjects, hidden3.submobjects)
        conn4 = fully_connect(hidden3.submobjects, output_layer.submobjects)

        self.play(FadeIn(hidden1), FadeIn(hidden2), FadeIn(hidden3), FadeIn(output_layer))
        self.play(Create(conn1), Create(conn2), Create(conn3), Create(conn4), run_time=5)