from manim import *
from title import Title
from inputImage import InputImage
from convolution import Convolution
from function import Function

class CNN(Scene):
    def construct(self):
        # Title.construct(self)
        InputImage.construct(self)
        Convolution.construct(self)
        Function.construct(self)
        