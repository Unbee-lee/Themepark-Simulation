import numpy as np
import matplotlib.patches as patches

class Gyro:
    # GYRO: during riding - up and down, unloading/idle - stop
    def __init__(self, xpos, ypos, width, height, color="orange"):
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.color = color

        # Ride logic - visual shape
        self.ride = None

        # position
        self.top_y = self.ypos + self.height - 25   # the very top
        self.bottom_y = self.ypos + 20              # the very bottom
        self.board_y = self.bottom_y                # current y position

        # duration
        self.timer = 0
        self.total_duration = 1
        self.phase = "idle"

    # ride logic - visual shape
    def attach_ride(self, ride):
        self.ride = ride
        self.total_duration = ride.duration

    # step change
    def step_update(self):
        # GYRO: during riding - up and down, unloading/idle - stop
        if not self.ride:
            return

        duration = self.total_duration
        progress = 1 - (self.ride.timer / duration) if duration > 0 else 1

        # riding : going up (80%) → going down(20%) -> one set
        if self.ride.status == "riding":
            if progress <= 0.8:
                # going up slowly
                ratio = progress / 0.8
                self.board_y = self.bottom_y + (self.top_y - self.bottom_y) * ratio
                self.phase = "up"

            elif progress < 1.0 :
                # going down real quick
                drop_ratio = (progress - 0.8) / 0.2
                self.board_y = self.top_y - (self.top_y - self.bottom_y) * (drop_ratio ** 2)
                self.phase = "drop"
            else:
                self.board_y = self.bottom_y
                self.phase = "stopped"

        # unloading / idle / loading : stop
        elif self.ride.status in ["unloading", "idle", "loading"]:
            self.phase = "stopped"
            self.board_y = self.bottom_y
    
    def plot_gyro(self, ax):
        # frame plotting
        rect = patches.Rectangle(
            (self.xpos, self.ypos),
            self.width, self.height,
            linewidth=2,
            edgecolor='red',
            facecolor='cornflowerblue'
        )

        # roof plotting
        tri = np.array([
            [self.xpos, self.ypos + self.height],
            [self.xpos + (self.width) * 0.5, self.ypos + self.height + 15],
            [self.xpos + self.width, self.ypos + self.height]
        ])
        triangle = patches.Polygon(tri, color='yellow')

        # board plotting (Gondola)
        board = patches.Rectangle(
            (self.xpos - 10, self.board_y),
            self.width + 20, 25,
            linewidth=2,
            edgecolor='red',
            facecolor='orange'
        )

        ax.add_patch(rect)
        ax.add_patch(triangle)
        ax.add_patch(board)

        # debugging
        #ax.text(self.xpos - 10, self.ypos - 10,
               #f"{self.phase} ({self.timer % self.total_duration}/{self.total_duration})",
               #fontsize=8, color="white")

