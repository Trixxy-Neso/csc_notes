from tkinter import *
from random import choice, randint

# CONSTANTS
WIDTH = 400
HEIGHT = 400
POINT_COLORS = ("black", "red", "green", "blue")
POINT_RADIUS = 0
NUM_POINTS = 2500




class ChaosGame (Canvas):
    def __init__(self, master):
        Canvas.__init__(self, master, bg="white")
        self.pack(fill=BOTH, expand=1)

    def plot_all_points (self, num_points):
        # plot equilateral 
        v1 = [0, HEIGHT - 1]
        v2 = [WIDTH -1 / 2, 0 ]
        v3 = [WIDTH - 1, HEIGHT - 1]
        verts = [v1, v2, v3]

        # choose two random

        # plot mid

        # repeat


