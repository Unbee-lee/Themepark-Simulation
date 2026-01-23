import numpy as np
import matplotlib.patches as patches
import math

class Carousel:
    def __init__(self, xpos, ypos, width=150, height=150, n_horses=8, color="pink"):
        self.xpos = xpos      
        self.ypos = ypos      
        self.width = width    
        self.height = height  
        self.n_horses = n_horses
        self.color = color

        # Ride logic - visual shape
        self.ride = None
        self.osc_amplitude = height * 0.4  # amplitude
        self.timer = 0

    #Ride logic - visual shape
    def attach_ride(self, ride):
        self.ride = ride

    # step change
    def step_update(self):
        if not self.ride:
            return

        if self.ride.status == "riding":
            self.timer += 1
        # if it's unloading and idle : Stop!

    def plot_carousel(self, ax):
        # central bar
        ax.add_patch(patches.Rectangle((self.xpos + self.width / 2 - 2, self.ypos),4, self.height-10,facecolor='darkred'))

        # --- horse bodies ---
        horse_w = 16
        horse_h = 10
        base_y = self.ypos + 20     
        bar_base_y = self.ypos + 30 
        bar_h = self.height * 0.6   
        amp = 6                     

        # 4 horses
        x_ratios = [1/8, 3/8, 5/8, 7/8]
        offsets = [0, math.pi, 0, math.pi]  # 1,3 / 2,4 

        # riding
        if self.ride and self.ride.status == "riding":
            duration = self.ride.duration
            ride_timer = self.ride.timer
            progress = 1 - (ride_timer / duration) if duration > 0 else 1
        else:
            progress = None

        for i, x_ratio in enumerate(x_ratios):
            # center x of the bar
            bx = self.xpos + self.width * x_ratio - 2
            hx = bx - horse_w / 2

            # riding -> up and down movement
            if progress is not None:
                osc = math.sin((progress * 2 * math.pi) + offsets[i]) * amp
                bar_y = bar_base_y + osc
                horse_y = base_y + osc
            else:
                bar_y = bar_base_y
                horse_y = base_y

            # --- horse bar (pole)  ---
            ax.add_patch(patches.Rectangle(
                (bx, bar_y),
                4, bar_h,
                facecolor='white',
                edgecolor='black'
            ))

            # --- horse body ---
            ax.add_patch(patches.Rectangle(
                (hx, horse_y),
                horse_w, horse_h,
                facecolor='pink',
                edgecolor='black'
            ))

        # roof
        canopy = patches.Polygon([
            (self.xpos, self.ypos + self.height - 30),
            (self.xpos + self.width / 2, self.ypos + self.height-10),
            (self.xpos + self.width, self.ypos + self.height - 30)
        ], closed=True, facecolor='lightcoral', edgecolor='red', linewidth=2)
        ax.add_patch(canopy)

        
