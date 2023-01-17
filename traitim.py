import pandas as pd
import numpy as np

num_points = 10000
theta = np.linspace(0,2 * np.pi, num_points)

x_1 = 16 * (np.sin(theta) ** 3)
y_1 = 13 * np.cos(theta) - 5*np.cos(2*theta) \
    - 2 * np.cos(3*theta) - np.cos(4*theta)

x_2 = 0.9 * x_1
y_2 = 0.9 * y_1
x_3 = 0.8 * x_1
y_3 = 0.8 * y_1

x = np.concatenate([x_1, x_2, x_3])
y = np.concatenate([y_1, y_2, y_3])


size = np.random.random_integers(1, 2, 3*num_points)
color = np.random.random_integers(1, 2, 3*num_points)
ani_frame = np.random.random_integers(1, 40, 3*num_points)

df = pd.DataFrame({"x":x, "y":y,
                    "size":size,"color":color,
                    "animation_frame":ani_frame})

#save data

df.to_csv("data.csv")