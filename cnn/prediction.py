from manim import *
import dense
import numpy as np

class Prediction(Scene):
    def construct(self):
        title = Text("Step 7 — Prediction", font_size=32, weight=BOLD)
        title.to_edge(UP * 1)

        prob_group = dense.prob_group

        self.play(
            Write(title),
            prob_group.animate.move_to(ORIGIN),
            run_time=1
        )

        probs = [float(m.get_value()) for m in prob_group[1]]

        axes = Axes(
            x_range=[0, 3, 1],
            y_range=[0, 1, 0.2],
            x_length=5,
            y_length=3,
            axis_config={"include_numbers": True},
            x_axis_config={"include_numbers": False},
            y_axis_config={"include_numbers": True},
            tips=False
        ).move_to(ORIGIN)

        bar_colors = [GREEN, BLUE, RED]

        bars = VGroup()
        prob_labels = VGroup()
        for i, p in enumerate(probs):
            bar = Rectangle(
                width=0.6,
                height=axes.y_length * p,
                fill_color=bar_colors[i],
                fill_opacity=0.8,
            )
            bar.move_to(axes.c2p(i + 0.5, p / 2))
            bars.add(bar)

            label = DecimalNumber(p, num_decimal_places=2, font_size=20)
            label.next_to(bar, UP, buff=0.2)
            prob_labels.add(label)

        self.play(
            Create(axes),
            FadeOut(prob_group[0]),
            FadeOut(prob_group[2])
        )

        self.play(
            *[
                Transform(prob_group[1][i], bars[i])
                for i in range(len(probs))
            ],
            run_time=1.5
        )

        self.play(Write(prob_labels))

        labels = ["Cat", "Dog", "Rabbit"]

        x_labels = VGroup(*[
            Text(lbl, font_size=18)
            for lbl in labels
        ])

        for i, lbl in enumerate(x_labels):
            lbl.next_to(axes.c2p(i + 0.5, 0), DOWN, buff=0.2)

        self.play(Write(x_labels))

        max_idx = int(np.argmax(probs))
        pred_text = Text(f"Prediction: {labels[max_idx]}", font_size=26, color=GREEN)
        pred_text.next_to(axes, DOWN, buff=0.6)

        self.play(Write(pred_text))
        self.wait(2)
        fade_out = VGroup(prob_group[1], prob_labels, x_labels, pred_text)
        self.play(
            Unwrite(title),
            Uncreate(axes),
            FadeOut(fade_out)
        )