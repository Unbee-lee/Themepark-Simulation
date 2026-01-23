import numpy as np
import matplotlib.patches as patches

class Ferris():
    def __init__(self,ride, cx=200, cy=100, radius = 54, seat_r=8, color = "pink"):
        self.ride = ride
        self.cx = cx
        self.cy = cy
        self.radius = radius
        self.seat_r = seat_r
        self.duration = self.ride.duration
        self.angle = 0
        self.num_seats = 8
        self.base_angles = np.arange(0,360,360 / self.num_seats)
        self.timer = 0
        self.is_rotating = False
        self.color = color

    def step_update(self):
        # riding
        if self.ride.status == "riding":
            if not self.is_rotating:
                self.is_rotating = True
                self.timer = 0
                self.angle = 0

            # It's rotating only the duration
            if self.timer < self.duration:
                delta = 360 / self.duration
                self.angle = (self.angle + delta) % 360
                self.timer += 1
            else:
                # Initialize - once the ride is done
                self.angle = 0
                self.is_rotating = False
                self.timer = 0

        # If it's not running - It should stop
        else:
            self.angle = 0
            self.is_rotating = False

    # plotting
    def plot_ferris(self,ax):
        ax.set_aspect("equal")
        # line (spoke)
        for angle in self.base_angles:
            rad = np.radians(angle+self.angle-90)
            x_end = self.cx + self.radius * np.cos(rad)
            y_end = self.cy + self.radius * np.sin(rad)
            ax.plot([self.cx, x_end], [self.cy, y_end], color='gray', linewidth=1)

        # cabins
        for angle in self.base_angles:
            rad = np.radians(angle+self.angle-90)
            sx = self.cx + self.radius * np.cos(rad)
            sy = self.cy + self.radius * np.sin(rad) 
            seat = patches.Circle((sx, sy), self.seat_r, facecolor='pink', edgecolor='black', linewidth=1.5)
            ax.add_patch(seat)

        
        ax.set_aspect("equal")
        
        # outer circles (Rim)
        inner_circle = patches.Circle((675,155),18, facecolor='none', edgecolor='orange', linewidth=3)
        middle_circle = patches.Circle((675,155),36, facecolor='none', edgecolor='pink', linewidth=3)
        outer_circle = patches.Circle((675,155),54, facecolor='none', edgecolor='white', linewidth=3)

        ax.add_patch(inner_circle)
        ax.add_patch(middle_circle)
        ax.add_patch(outer_circle)



        ax.add_patch(patches.Circle((self.cx, self.cy),4, color='black'))


    # plotting    
    def plot_frame(self,ax):
        frame_x_left = np.array([645,675])
        frame_y_left = np.array([80,155])
        frame_x_right = np.array([675,705])
        frame_y_right = np.array([155,80])

        #Frame plotting
        ax.plot(frame_x_left, frame_y_left,'-',color='red',linewidth=2)
        ax.plot(frame_x_right, frame_y_right,'-',color='red',linewidth=2)



