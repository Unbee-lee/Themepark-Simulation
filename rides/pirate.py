import numpy as np
import matplotlib.patches as patches

class Pirate:
    #Class to represent a Pirate Ship ride with line-based drawing and rotation
    def __init__(self, xpos, ypos, width, height, ship_color="purple", frame_color="red"):
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.angle = 0
        self.swing_speed = 4
        self.max_angle = 25
        self.swing_direction = 1
        self.ride = None
        self.ship_color = ship_color
        self.frame_color = frame_color

    def attach_ride(self, ride):
        self.ride = ride

    def step_update(self):
        #riding-moving, unloading-slow
        if self.ride and self.ride.status == "riding":
            self.angle += self.swing_speed * self.swing_direction
            if abs(self.angle) >= self.max_angle:
                self.swing_direction *= -1
        elif self.ride and self.ride.status in ["unloading", "idle", "loading"]:
            if abs(self.angle) > 1:
                self.angle *= 0.8
            else:
                self.angle = 0

    def plot_me(self, ax):
        # a coordinate-based plotting method with rotation applied
        # --- setting the rotation center ---
        pivot_x = self.xpos + (self.width / 2)
        pivot_y = self.ypos + self.height

        # --- rotation vector---
        rad = np.radians(self.angle)
        rot = np.array([
            [np.cos(rad), -np.sin(rad)],
            [np.sin(rad),  np.cos(rad)]
        ])

        # ---rotation function---
        def rotate_points(x_arr, y_arr):
            # Rotate the coordinates of each line segment around a pivot and return them
            points = np.column_stack((x_arr, y_arr))
            translated = points - np.array([pivot_x, pivot_y])
            rotated = translated @ rot.T
            rotated += np.array([pivot_x, pivot_y])
            return rotated[:, 0], rotated[:, 1]

        # --- Frame ---
        frame_x_left = np.array([self.xpos, self.xpos + (self.width / 2)])
        frame_y_left = np.array([self.ypos, self.ypos + self.height])
        frame_x_right = np.array([self.xpos + (self.width / 2), self.xpos + self.width])
        frame_y_right = np.array([self.ypos + self.height, self.ypos])
        frame_x_line = np.array([self.xpos + (self.width / 5), self.xpos + (self.width / 5 * 4)])
        frame_y_line = np.array([self.ypos + (self.height / 5 * 2), self.ypos + (self.height / 5 * 2)])

        ax.plot(frame_x_left, frame_y_left, '-', color=self.frame_color, linewidth=4)
        ax.plot(frame_x_right, frame_y_right, '-', color=self.frame_color, linewidth=4)
        ax.plot(frame_x_line, frame_y_line, '-', color=self.frame_color, linewidth=4)

        # ---  Ship rotation ---
        ship_segments = [
            # (x,y) array
            (np.array([self.xpos, self.xpos + (self.width / 2)]),
             np.array([self.ypos + (self.height / 5 * 3), self.ypos + self.height])),

            (np.array([self.xpos, self.xpos + (self.width / 5 * 2)]),
             np.array([self.ypos + (self.height / 5 * 3), self.ypos + (self.height / 5 * 3) - (self.height * 0.1)])),

            (np.array([self.xpos, self.xpos + (self.width / 5 * 2)]),
             np.array([self.ypos + (self.height / 5 * 3), self.ypos + (self.height / 5)])),

            (np.array([self.xpos + (self.width / 5 * 2), self.xpos + (self.width / 5 * 3)]),
             np.array([self.ypos + (self.height / 5 * 3) - (self.height * 0.1),
                       self.ypos + (self.height / 5 * 3) - (self.height * 0.1)])),

            (np.array([self.xpos + (self.width / 5 * 2), self.xpos + (self.width / 5 * 3)]),
             np.array([self.ypos + (self.height / 5), self.ypos + (self.height / 5)])),

            (np.array([self.xpos + (self.width / 5 * 3), self.xpos + self.width]),
             np.array([self.ypos + (self.height / 5 * 3) - (self.height * 0.1),
                       self.ypos + (self.height / 5 * 3)])),

            (np.array([self.xpos + (self.width / 5 * 3), self.xpos + self.width]),
             np.array([self.ypos + (self.height / 5), self.ypos + (self.height / 5 * 3)])),

            (np.array([self.xpos + (self.width / 2), self.xpos + self.width]),
             np.array([self.ypos + self.height, self.ypos + (self.height / 5 * 3)]))
        ]

        # All the lines are rotated -> plot
        for x_arr, y_arr in ship_segments:
            x_rot, y_rot = rotate_points(x_arr, y_arr)
            ax.plot(x_rot, y_rot, '-', color=self.ship_color, linewidth=4)

        # --- plot pivot ---
        ax.plot(pivot_x, pivot_y, "o", color="gray", markersize=6)

