import matplotlib.pyplot as plt
import numpy as np
import math

def draw_trajectory(v0, theta):
    g = 9.8
    t_flight = 2 * v0 * math.sin(theta) / g

    t_list = np.arange(0, t_flight, 0.001)
    x_list = []
    y_list = []

    for t in t_list:
        x = v0 * math.cos(theta) * t
        y = v0 * math.sin(theta) * t - 0.5 * g * t * t
        x_list.append(x)
        y_list.append(y)
    draw_graph(x_list, y_list)

    t_dot = t_flight / 2
    x_dot = v0 * math.cos(theta) * t_dot
    y_dot = v0 * math.sin(theta) * t_dot- 0.5 * g * t_dot * t_dot
    draw_dot(x_dot, y_dot)
    print("The maximum height =", y_dot)

def draw_graph(x_list, y_list):
    plt.plot(x_list, y_list)
    plt.xlabel("x-coordinate")
    plt.ylabel("y-coordinate")
    plt.title("Trajectory of a ball")

def draw_dot(x_dot, y_dot):
    plt.plot(x_dot, y_dot, "o")


try:
    v0 = float(input("Enter the initial speed (m/s): "))
    theta = float(input("Enter the initial angle (degrees): "))
except ValueError:
    print("You entered an ivalid input")
else:
    theta = math.radians(theta)
    draw_trajectory(v0, theta)
    plt.show()
