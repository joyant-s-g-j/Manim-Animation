from manim import *
import flatten
from allFunction import make_layer, fully_connect
import numpy as np
import sys

class Dense(Scene):
    def construct(self):
        title = Text("Step 6 — Dense & Softmax", font_size=32, weight=BOLD)
        title.to_edge(UP * 1)

        down_shift = DOWN * 0.2

        flat_map = flatten.flat_map
        self.add(flat_map)
        self.play(
            Write(title),
            flat_map.animate.shift(LEFT * 6 + down_shift)
        )

        hidden1 = make_layer(10, GREEN, GREEN_E)
        hidden2 = make_layer(8, YELLOW, YELLOW_E)
        hidden3 = make_layer(6, RED, RED_E)
        output_layer = make_layer(3, BLUE, BLUE_E)
        
        hidden1.next_to(flat_map, RIGHT, buff=1.7).shift(down_shift)
        hidden2.next_to(hidden1, RIGHT, buff=1.7)
        hidden3.next_to(hidden2, RIGHT, buff=1.7)
        output_layer.next_to(hidden3, RIGHT, buff=1.7)

        conn1 = fully_connect(flat_map.submobjects, hidden1.submobjects)
        conn2 = fully_connect(hidden1.submobjects, hidden2.submobjects)
        conn3 = fully_connect(hidden2.submobjects, hidden3.submobjects)
        conn4 = fully_connect(hidden3.submobjects, output_layer.submobjects)

        self.play(FadeIn(hidden1), FadeIn(hidden2), FadeIn(hidden3), FadeIn(output_layer))
        self.play(Create(conn1), Create(conn2), Create(conn3), Create(conn4), run_time=5)

        output_vals = [2.3, 1.1, 0.4]

        output_texts = VGroup(*[
            DecimalNumber(v, num_decimal_places=2, font_size=22)
            for v in output_vals
        ])

        output_texts.arrange(DOWN, buff=0.5, aligned_edge=LEFT)

        left_bracket = MathTex(r"\left[")
        right_bracket = MathTex(r"\right]")
        left_bracket.match_height(output_texts)
        right_bracket.match_height(output_texts)

        output_group = VGroup(left_bracket, output_texts, right_bracket).arrange(RIGHT, buff=0.08)
        output_group.next_to(output_layer, RIGHT, buff=0.1)

        self.play(
            Write(left_bracket),
            Write(output_texts),
            Write(right_bracket)
        )

        arrow1 = Arrow(
            output_group.get_right(),
            output_group.get_right() + RIGHT * 0.5,
            buff=0.1,
            stroke_width=1.2
        )

        self.play(GrowArrow(arrow1))

        softmax_text = MathTex(r"\frac{e^{x_i}}{\sum_j e^{x_j}}", font_size=28)
        softmax_text.next_to(arrow1, RIGHT, buff=0.1)

        self.play(Write(softmax_text))

        arrow2 = Arrow(
            softmax_text.get_right(),
            softmax_text.get_right() + RIGHT * 0.5,
            buff=0.1,
            stroke_width=1.2
        )

        self.play(GrowArrow(arrow2))

        exp_vals = np.exp(output_vals)
        probs = exp_vals / np.sum(exp_vals)

        prob_texts = VGroup(*[
            DecimalNumber(v, num_decimal_places=2, font_size=22)
            for v in probs
        ])
        prob_texts.arrange(DOWN, buff=0.5, aligned_edge=LEFT)

        prob_left_bracket = MathTex(r"\left[")
        prob_right_bracket = MathTex(r"\right]")
        prob_left_bracket.match_height(prob_texts)
        prob_right_bracket.match_height(prob_texts)

        prob_group = VGroup(prob_left_bracket, prob_texts, prob_right_bracket).arrange(RIGHT, buff=0.08)
        prob_group.next_to(arrow2, RIGHT, buff=0.1)
        sys.modules[__name__].prob_group = prob_group

        self.play(
            Write(prob_left_bracket),
            Write(prob_texts),
            Write(prob_right_bracket)
        )

        all_out = VGroup(flat_map, conn1, hidden1, conn2, hidden2, conn3, hidden3, conn4, output_layer, output_group, arrow1, softmax_text, arrow2)
        self.play(
            Unwrite(title),
            FadeOut(all_out)
        )


