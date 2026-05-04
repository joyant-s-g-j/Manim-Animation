from manim import *
from title import Title
from inputImage import InputImage
from convolution import Convolution
from function import Function
from pooling import Pooling
from flatten import Flatten
from dense import Dense

class CNN(MovingCameraScene):
    def construct(self):
        Title.construct(self)
        InputImage.construct(self)
        Convolution.construct(self)
        Function.construct(self)
        Pooling.construct(self)
        Flatten.construct(self)
        Dense.construct(self)
        