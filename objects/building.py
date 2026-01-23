import matplotlib.patches as patches

class Building:
    def __init__(self, name, xpos, ypos, width, height):
        self.name = name
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.boundary = {
            "xmin" : self.xpos,
            "xmax" : self.xpos + self.width,
            "ymin" : self.ypos,
            "ymax" : self.ypos + self.height
        }

    def plot_buildings(self, ax):
        ax.add_patch(patches.Rectangle((self.xpos, self.ypos),self.width, self.height,fill=True, color='palevioletred', linewidth=2))

