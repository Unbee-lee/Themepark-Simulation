import matplotlib.patches as patches

class Ride:
    def __init__(self, name, xpos, ypos, width=150, height=150, queue_cap=5, ride_cap=3, duration=5):
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
        self.queue = []
        self.queue_cap = queue_cap
        self.ride_cap = ride_cap
        self.on_ride = []
        self.status = "idle"
        self.duration = duration
        self.timer = 0
        self.q_positions = [
            (self.boundary["xmin"] + i * 8, self.boundary["ymin"] - 10) 
            for i in range(queue_cap)
        ]
        self.r_positions = [
            (self.boundary["xmax"] - 4 , self.boundary["ymax"] - i*7 -4)
            for i in range(ride_cap)
        ]
        self.exit_x = self.xpos + self.width + 8 # will be fixed into a specific position
        self.exit_y = self.ypos + 5
        self.visual_shape = None

    def is_queue_available(self):
        #print(f"queue length : {len(self.queue)}, queue capacity: {self.queue_cap}")
        return len(self.queue) < self.queue_cap

    def add_queue(self, patron):
        if not self.is_queue_available():
            return False
        idx = len(self.queue)
        self.queue.append(patron)
        #for i in range(idx):
        #    print(f"{self.name} queue: {self.queue[i].name}")
        patron.status = "queued"
        qx, qy = self.q_positions[idx]
        patron.xpos, patron.ypos = qx, qy
        return True

    def attach_visual(self, visual_shape):
        self.visual_shape = visual_shape

    def check_queue(self):
        # Idle → Loading
        #print(f"{self.name} status : {self.status} | {self.name} queue: {self.queue}")
        if self.status == "idle" and self.queue:
            self.status = "loading"
            self.timer = 2
            #print(f"{self.name} starts loading")

            for p in self.queue[:self.ride_cap]:
                p.status = "loading"

        # Loading -> riding
        elif self.status == "loading":
            self.timer -= 1
            if self.timer <= 0:
                for i, p in enumerate(self.queue[:self.ride_cap]):
                    self.on_ride.append(p)
                    p.status = "riding"
                    rx, ry = self.r_positions[i]
                    p.xpos, p.ypos = rx, ry # fix it like q_locations
                self.queue = self.queue[self.ride_cap:]
                self.status = "riding"
                self.timer = self.duration
                #print(f"{self.name} starts riding")

        # riding -> unloading
        elif self.status == "riding":
            self.timer -= 1
            #print(f"{self.name} riding... (timer={self.timer})")

            if self.timer <= 0 :
                self.status = "unloading"
                self.timer = 2
                #print(f"{self.name} starts unloading")

                for p in self.on_ride:
                    p.status = "unloading"

                #ride_shape
                if self.visual_shape:
                    self.visual_shape.is_rotating = False
                    self.visual_shape.angle = 0
            else:
            #ride_shape
                if self.visual_shape:
                    self.visual_shape.step_update()

        # unloading -> idle
        elif self.status == "unloading":
            self.timer -= 1
            if self.timer <= 0:
                for p in self.on_ride:
                    p.status = "walking"
                    p.target_ride = None
                    p.just_finished_ride = self
                    p.total_rides += 1
                    p.xpos, p.ypos = self.exit_x, self.exit_y
                self.on_ride.clear()
                self.status = "idle"
                #print(f"{self.name} is now idle again")
    def plot_boundary(self, ax, color_bounding_box):
        ax.add_patch(patches.Rectangle((self.xpos, self.ypos),self.width, self.height,fill=False, color=color_bounding_box, linewidth=2))
    
    def plot_exit(self, ax, color_bounding_box):
        ax.add_patch(patches.Rectangle((self.xpos+self.width, self.ypos),10, 10,fill=False, color=color_bounding_box, linewidth=2))




