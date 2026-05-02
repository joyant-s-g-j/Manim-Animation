from manim import *
import convolution

def relu_feature_map(grid):
    relu_grid = grid.copy()

    for cell in relu_grid:
        value_mob = cell[1]
        value = float(value_mob.get_tex_string())

        new_value = max(0, value)
        new_text = DecimalNumber(new_value, num_decimal_places=2 if new_value > 0 else 0, font_size=18)
        new_text.move_to(value_mob.get_center())

        cell.remove(value_mob)
        cell.add(new_text)

    return relu_grid

class Function(MovingCameraScene):
    def construct(self):
        title = Text("Step 3 — Activation Function (ReLU)", font_size=32, weight=BOLD)
        title.to_edge(UP * 1)

        feature_map = convolution.result_grid
        self.play(
            Write(title),
            feature_map.animate.shift(LEFT * 8.5 + UP * 0.5).scale(1.4),
        )

        feature_map_cap = Text("Before ReLU", font_size=22)
        feature_map_cap.next_to(feature_map, DOWN, buff=0.35)
        self.play(FadeIn(feature_map_cap))

        axes = Axes(
            x_range=[-5, 6],
            y_range=[-5, 6],
            x_length=9,
            axis_config={"include_numbers": True}
        ).scale(0.6)

        axes.to_edge(RIGHT, buff=0.7)
        axes.shift(UP * 0.2)

        relu_text = MathTex("ReLU(x) = max(0, x)", font_size=26)
        relu_text.next_to(axes, UP, buff=0.35)

        self.play(
            Create(axes),
            Write(relu_text)
        )

        p1 = axes.c2p(-4, -4)
        p2 = axes.c2p(4, 4)

        dot1 = Dot(p1, color=BLUE)
        dot2 = Dot(p2, color=BLUE)
        line = Line(p1, p2, color=RED)

        self.play(FadeIn(dot1), FadeIn(dot2))
        
        self.play(
            self.camera.frame.animate.move_to(dot1).scale(0.5),
            run_time=1
        )

        self.play(
            Create(line),
            self.camera.frame.animate.move_to(line).scale(1),
            run_time=1,
            rate_func=linear
        )

        self.play(
            self.camera.frame.animate.move_to(dot2).scale(1.5),
            run_time=1
        )

        self.play(
            self.camera.frame.animate.move_to(ORIGIN).scale(1.3),
            run_time=1
        )

        p1_relu = axes.c2p(-4, 0)

        dot1_relu = Dot(p1_relu, color=BLUE)
        line_relu = Line(p1_relu, axes.c2p(4, 4), color=RED)

        relu_info = Text("ReLU adds non-linearity by \n setting negative value to 0", font_size=18)
        relu_info.next_to(axes, DOWN, buff=0.35)

        self.play(
            Write(relu_info)
        )
        self.wait(1)
        self.play(
            Transform(dot1, dot1_relu),
            Transform(line, line_relu),
            run_time=1.5
        )

        all_out = VGroup(relu_text, axes, line, dot1, dot2, relu_info)
        relu_map = relu_feature_map(feature_map)
        relu_target = relu_map.copy()
        relu_target.shift(RIGHT * 6)

        self.play(FadeOut(all_out))

        import sys
        sys.modules[__name__].relu_map = relu_map

        arrow = Arrow(
            start=feature_map.get_right() + RIGHT * 0.2,
            end=relu_target.get_left() + LEFT * 0.2,
            buff=0.05
        )
        self.play(GrowArrow(arrow))
        self.play(relu_map.animate.move_to(relu_target))

        relu_map_cap = Text("After ReLU", font_size=22)
        relu_map_cap.next_to(relu_map, DOWN, buff=0.35)
        self.play(Write(relu_map_cap))

        self.wait(1)

        vanish = VGroup(feature_map, feature_map_cap, arrow, relu_map_cap)
        self.play(FadeOut(vanish), Unwrite(title))