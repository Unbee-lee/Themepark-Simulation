import matplotlib.patches as patches

class Terrain:
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

    def plot_terrain(self, ax):
        ax.add_patch(patches.Rectangle((self.xpos, self.ypos),self.width, self.height,fill=False, color='black', linewidth=2))

    # difference between the terrain (day, cloudy, night)
    def draw_shapes(self, ax, mode="day"):
        if mode == "day":
            triangles = [
                [[25,560], [35,560], [30,570]],
                [[25,540], [35,540], [30,530]],
                [[40,555], [40,545], [50,550]],
                [[10,550], [20,555], [20,545]]
            ]
            for coords in triangles:
                ax.add_patch(patches.Polygon(coords, color='yellow'))
            circle = patches.Circle((30,550), 10, color='orange')
            ax.add_patch(circle)
        elif mode == "night":
            # Yellow full moon
            full_moon = patches.Circle((30, 550), 10, color='yellow')
            ax.add_patch(full_moon)

            # cover moon
            cover_moon = patches.Circle((33, 555), 10, color='black')
            ax.add_patch(cover_moon)
        elif mode == "cloudy":
            # representation - cloud
            cloud_1 = patches.Circle((30, 570), 7, color='white')
            ax.add_patch(cloud_1)

            cloud_2 = patches.Circle((40, 570), 7, color='white')
            ax.add_patch(cloud_2)

            cloud_3 = patches.Circle((50, 570), 7, color='white')
            ax.add_patch(cloud_3)

            cloud_4 = patches.Circle((30, 550), 7, color='white')
            ax.add_patch(cloud_4)

            cloud_5 = patches.Circle((40, 550), 7, color='white')
            ax.add_patch(cloud_5)

            cloud_6 = patches.Circle((50, 550), 7, color='white')
            ax.add_patch(cloud_6)

            cloud_7 = patches.Circle((25, 560), 7, color='white')
            ax.add_patch(cloud_7)

            cloud_8 = patches.Circle((55, 560), 7, color='white')
            ax.add_patch(cloud_8)
            
            cloud_2_1 = patches.Circle((200, 570), 7, color='white')
            ax.add_patch(cloud_2_1)

            cloud_2_2 = patches.Circle((210, 570), 7, color='white')
            ax.add_patch(cloud_2_2)

            cloud_2_3 = patches.Circle((220, 570), 7, color='white')
            ax.add_patch(cloud_2_3)

            cloud_2_4 = patches.Circle((200, 550), 7, color='white')
            ax.add_patch(cloud_2_4)

            cloud_2_5 = patches.Circle((210, 550), 7, color='white')
            ax.add_patch(cloud_2_5)

            cloud_2_6 = patches.Circle((220, 550), 7, color='white')
            ax.add_patch(cloud_2_6)

            cloud_2_7 = patches.Circle((195, 560), 7, color='white')
            ax.add_patch(cloud_2_7)

            cloud_2_8 = patches.Circle((225, 560), 7, color='white')
            ax.add_patch(cloud_2_8)

            cloud_3_1 = patches.Circle((370, 570), 7, color='white')
            ax.add_patch(cloud_3_1)

            cloud_3_2 = patches.Circle((380, 570), 7, color='white')
            ax.add_patch(cloud_3_2)

            cloud_3_3 = patches.Circle((390, 570), 7, color='white')
            ax.add_patch(cloud_3_3)

            cloud_3_4 = patches.Circle((370, 550), 7, color='white')
            ax.add_patch(cloud_3_4)

            cloud_3_5 = patches.Circle((380, 550), 7, color='white')
            ax.add_patch(cloud_3_5)

            cloud_3_6 = patches.Circle((390, 550), 7, color='white')
            ax.add_patch(cloud_3_6)

            cloud_3_7 = patches.Circle((365, 560), 7, color='white')
            ax.add_patch(cloud_3_7)

            cloud_3_8 = patches.Circle((395, 560), 7, color='white')
            ax.add_patch(cloud_3_8)

            cloud_4_1 = patches.Circle((540, 570), 7, color='white')
            ax.add_patch(cloud_4_1)

            cloud_4_2 = patches.Circle((550, 570), 7, color='white')
            ax.add_patch(cloud_4_2)

            cloud_4_3 = patches.Circle((560, 570), 7, color='white')
            ax.add_patch(cloud_4_3)

            cloud_4_4 = patches.Circle((540, 550), 7, color='white')
            ax.add_patch(cloud_4_4)

            cloud_4_5 = patches.Circle((550, 550), 7, color='white')
            ax.add_patch(cloud_4_5)

            cloud_4_6 = patches.Circle((560, 550), 7, color='white')
            ax.add_patch(cloud_4_6)

            cloud_4_7 = patches.Circle((535, 560), 7, color='white')
            ax.add_patch(cloud_4_7)

            cloud_4_8 = patches.Circle((565, 560), 7, color='white')
            ax.add_patch(cloud_4_8)

            cloud_5_1 = patches.Circle((710, 570), 7, color='white')
            ax.add_patch(cloud_5_1)

            cloud_5_2 = patches.Circle((720, 570), 7, color='white')
            ax.add_patch(cloud_5_2)

            cloud_5_3 = patches.Circle((730, 570), 7, color='white')
            ax.add_patch(cloud_5_3)

            cloud_5_4 = patches.Circle((710, 550), 7, color='white')
            ax.add_patch(cloud_5_4)

            cloud_5_5 = patches.Circle((720, 550), 7, color='white')
            ax.add_patch(cloud_5_5)

            cloud_5_6 = patches.Circle((730, 550), 7, color='white')
            ax.add_patch(cloud_5_6)

            cloud_5_7 = patches.Circle((705, 560), 7, color='white')
            ax.add_patch(cloud_5_7)

            cloud_5_8 = patches.Circle((735, 560), 7, color='white')
            ax.add_patch(cloud_5_8)

            filler_1 = patches.Rectangle((710, 550),20, 20, color='white')
            filler_2 = patches.Rectangle((370, 550),20, 20, color='white')
            filler_3 = patches.Rectangle((540, 550),20, 20, color='white')
            filler_4 = patches.Rectangle((200, 550),20, 20, color='white')
            filler_5 = patches.Rectangle((30, 550),20, 20, color='white')
            
            ax.add_patch(filler_1)
            ax.add_patch(filler_2)
            ax.add_patch(filler_3)
            ax.add_patch(filler_4)
            ax.add_patch(filler_5)
            

        elif mode == "rainy":
            rain_1 = patches.Rectangle((190, 500),5, 20, color='gray')
            rain_2 = patches.Rectangle((200, 520),5, 20, color='gray')
            rain_3 = patches.Rectangle((210, 500),5, 20, color='gray')
            rain_4 = patches.Rectangle((220, 520),5, 20, color='gray')

            rain_5 = patches.Rectangle((360, 500),5, 20, color='gray')
            rain_6 = patches.Rectangle((370, 520),5, 20, color='gray')
            rain_7 = patches.Rectangle((380, 500),5, 20, color='gray')
            rain_8 = patches.Rectangle((390, 520),5, 20, color='gray')
            
            rain_9 = patches.Rectangle((530, 500),5, 20, color='gray')
            rain_10 = patches.Rectangle((540, 520),5, 20, color='gray')
            rain_11 = patches.Rectangle((550, 500),5, 20, color='gray')
            rain_12 = patches.Rectangle((560, 520),5, 20, color='gray')

            rain_13 = patches.Rectangle((700, 500),5, 20, color='gray')
            rain_14 = patches.Rectangle((710, 520),5, 20, color='gray')
            rain_15 = patches.Rectangle((720, 500),5, 20, color='gray')
            rain_16 = patches.Rectangle((730, 520),5, 20, color='gray')

            rain_17 = patches.Rectangle((20, 500),5, 20, color='gray')
            rain_18 = patches.Rectangle((30, 520),5, 20, color='gray')
            rain_19 = patches.Rectangle((40, 500),5, 20, color='gray')
            rain_20 = patches.Rectangle((50, 520),5, 20, color='gray')

            ax.add_patch(rain_1)
            ax.add_patch(rain_2)
            ax.add_patch(rain_3)
            ax.add_patch(rain_4)
            ax.add_patch(rain_5)
            ax.add_patch(rain_6)
            ax.add_patch(rain_7)
            ax.add_patch(rain_8)
            ax.add_patch(rain_9)
            ax.add_patch(rain_10)
            ax.add_patch(rain_11)
            ax.add_patch(rain_12)
            ax.add_patch(rain_13)
            ax.add_patch(rain_14)
            ax.add_patch(rain_15)
            ax.add_patch(rain_16)
            ax.add_patch(rain_17)
            ax.add_patch(rain_18)
            ax.add_patch(rain_19)
            ax.add_patch(rain_20)


        # entry and exit
        entry = patches.Rectangle((0, 0),48, 28, fill=True, facecolor='white', edgecolor='black', linewidth=2)
        exits = patches.Rectangle((852, 0),47, 28,fill=True, facecolor='white', edgecolor='black', linewidth=2)

        ax.add_patch(entry)
        ax.add_patch(exits)
        

