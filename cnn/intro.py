from manim import *

class Intro(Scene):
    def construct(self):
        title = Text("Welcome to Joy-Verse", font_size=52, weight=BOLD)
        sub = Text("Creativity Sparks Revolution", font_size=22)
        sub.next_to(title, DOWN, buff=0.4)

        self.play(Write(title))
        self.play(FadeIn(sub, shift=UP * 0.2))

        self.wait(1)

        self.play(
            Unwrite(title),
            FadeOut(sub)
        )