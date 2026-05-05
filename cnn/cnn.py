from manim import *
from allFunction import add_watermark
from intro import Intro
from steps import Steps
from inputImage import InputImage
from convolution import Convolution
from function import Function
from pooling import Pooling
from flatten import Flatten
from dense import Dense
from prediction import Prediction
from end import End

class CNN(MovingCameraScene):
    def construct(self):
        add_watermark(self)
        Intro.construct(self)
        Steps.construct(self)
        InputImage.construct(self)
        Convolution.construct(self)
        Function.construct(self)
        Pooling.construct(self)
        Flatten.construct(self)
        Dense.construct(self)
        Prediction.construct(self)
        End.construct(self)