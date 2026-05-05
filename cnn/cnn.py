from manim import *
from steps import Steps
from inputImage import InputImage
from convolution import Convolution
from function import Function
from pooling import Pooling
from flatten import Flatten
from dense import Dense
from prediction import Prediction

class CNN(MovingCameraScene):
    def construct(self):
        Steps.construct(self)
        InputImage.construct(self)
        Convolution.construct(self)
        Function.construct(self)
        Pooling.construct(self)
        Flatten.construct(self)
        Dense.construct(self)
        Prediction.construct(self)
        