from manim import *

class Title(Scene):
    def construct(self):
        bg = Rectangle(width=16, height=9).set_fill(color="#010101", opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("How CNNs Detect Patterns", font_size=52, weight=BOLD)
        title.shift(UP * 1)
        sub = Text("Convolutional Neural Networks — A Visual Journey", font_size=22)
        sub.next_to(title, DOWN, buff=0.4)

        line = Line(LEFT * 5, RIGHT * 5, stroke_width=2)
        line.next_to(sub, DOWN, buff=0.35)

        steps = VGroup(
            Text("① Input", font_size=17),
            Text("② Convolution", font_size=17),
            Text("③ Map", font_size=17),
            Text("④ Filters", font_size=17),
            Text("⑤ ReLU", font_size=17),
            Text("⑥ Pool", font_size=17),
            Text("⑦ Flatten", font_size=17),
            Text("⑧ Dense", font_size=17),
            Text("⑨ Softmax", font_size=17),
            Text("⑩ Output", font_size=17)
        ).arrange_in_grid(rows=2, buff=0.4)
        steps.next_to(line, DOWN, buff=0.55)
        
        group = VGroup(title, sub, line, steps)
        group.move_to(ORIGIN)

        self.play(FadeIn(bg))
        self.play(Write(title, run_time=1.4))
        self.play(FadeIn(sub, shift=UP * 0.2))
        self.play(Create(line))
        self.play(LaggedStart(*[FadeIn(s, shift=UP * 0.15) for s in steps], lag_ratio=0.15))
        self.wait(3)