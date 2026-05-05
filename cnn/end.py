from manim import *

class End(Scene):
    def construct(self):
        title = Text("Thanks for watching", font_size=52, weight=BOLD)
        sub = Text("Please leave a review", font_size=22)
        sub.next_to(title, DOWN, buff=0.4)

        self.play(Write(title, run_time=1.4))
        self.play(FadeIn(sub, shift=UP * 0.2))
        