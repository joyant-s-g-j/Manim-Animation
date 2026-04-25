from manim import *
from title import Title
from inputImage import InputImage

class CNN(Scene):
    def construct(self):
        Title.construct(self)
        InputImage.construct(self)