import random
import math

class Patron:
	def __init__(self, xpos, ypos, name):
		self.name = name
		self.xpos = xpos + random.uniform(-5,5) # starting point 
		self.ypos = ypos + random.uniform(-5,5)
		self.status = "walking"
		self.target_ride = None
		self.last_ride = None
		self.just_finished_ride = None
		self.total_rides = 0
		self.target_exit = None
		self.step_size = random.uniform(2.5, 3.5) # speed
		self.target_offset = None # a bit of noise

	# deciding target_ride
	def decide_target(self, rides):
		if not rides:
			return
		self.target_ride = random.choice(rides)
		#print(f"{self.name} decided to ride {self.target_ride.name}")
		# a bit of noise to make them different
		base_qx, base_qy = self.target_ride.q_positions[0]
		self.target_offset = (
			base_qx + random.uniform(-10,10),
			base_qy + random.uniform(-10,10)
		)
	# walking while avoiding the boundary
	def walk(self, rides=None, buildings=None, terrain_map=None):
		#print(rides)
		# Walking to exit
		if self.status == "exiting" and self.target_exit:
			tx, ty = self.target_exit
		# walking to the target_ride
		elif self.target_ride:
			qx, qy = self.target_offset
			margin = 5
			tx = qx
			ty = qy - margin
		else:
			return

		#step size
		step=7 
		# distance betwwen the target area and current position
		dx, dy = tx - self.xpos, ty - self.ypos
		# distance calculation using math module
		dist = math.hypot(dx, dy)
		if dist == 0:
			return

		# next_xpos avoiding the boundary
		next_xpos = self.xpos + step * dx / dist
		next_ypos = self.ypos + step * dy / dist

		#boundary
		offset = 7 # margin from the boundary
		trigger = 12 # margin from the boundary
		bounce_strength = 0.8

		#boundary
		# terrain boundary
		t = terrain_map.boundary
		
		if (t["xmin"] - trigger <= next_xpos <= t["xmax"] + trigger) and (t["ymin"] - trigger <= next_ypos <= t["ymax"] + trigger):
			crossed_y = (self.ypos > t["ymax"] and next_ypos < t["ymax"]) or (self.ypos < t["ymin"] and next_ypos > t["ymin"])
			crossed_x = (self.xpos > t["xmax"] and next_xpos < t["xmax"]) or (self.xpos < t["xmin"] and next_xpos > t["xmin"])

			if crossed_y:
				next_ypos = t["ymax"] + offset if dy < 0 else t["ymin"] - offset
				dy = -dy * bounce_strength

			if crossed_x:
				next_xpos = t["xmax"] + offset if dx < 0 else t["xmin"] - offset
				dx = -dx * bounce_strength

		# exit area
		if ( 852  <= next_xpos <= 900 and 0 <= next_ypos <= 28) :
			crossed_y = (self.ypos > 28 and next_ypos < 28) or (self.ypos < 0 and next_ypos > 0)
			crossed_x = (self.xpos > 900 and next_xpos < 900) or (self.xpos < 852 and next_xpos > 852)

			# ride 내부로 들어가는 대신, 경계선에서 멈추게
			if crossed_y:
				next_ypos = 28 + offset if dy < 0 else 0 - offset
				dy = -dy * bounce_strength

			if crossed_x:
				next_xpos = 900 + offset if dx < 0 else 852 - offset
				dx = -dx * bounce_strength
		# entry area
		if ( 0  <= next_xpos <= 48 and 0 <= next_ypos <= 28) :
			# 현재 위치와 다음 위치가 ride의 y영역을 가로질렀는지 확인
			crossed_y = (self.ypos > 28 and next_ypos < 28) or (self.ypos < 0 and next_ypos > 0)
			crossed_x = (self.xpos > 48 and next_xpos < 48) or (self.xpos < 0 and next_xpos > 0)

			# ride 내부로 들어가는 대신, 경계선에서 멈추게
			if crossed_y:
				next_ypos = 28 + offset if dy < 0 else 0 - offset
				dy = -dy * bounce_strength

			if crossed_x:
				next_xpos = 48 + offset if dx < 0 else 0 - offset
				dx = -dx * bounce_strength
	
		# ride boundary
		for r in rides:
			b = r.boundary
			
			if (b["xmin"] - trigger <= next_xpos <= b["xmax"] + trigger) and (b["ymin"] - trigger <= next_ypos <= b["ymax"] + trigger):
				crossed_y = (self.ypos > b["ymax"] and next_ypos < b["ymax"]) or (self.ypos < b["ymin"] and next_ypos > b["ymin"])
				crossed_x = (self.xpos > b["xmax"] and next_xpos < b["xmax"]) or (self.xpos < b["xmin"] and next_xpos > b["xmin"])

				if crossed_y:
					next_ypos = b["ymax"] + offset if dy < 0 else b["ymin"] - offset
					dy = -dy * bounce_strength

				if crossed_x:
					next_xpos = b["xmax"] + offset if dx < 0 else b["xmin"] - offset
					dx = -dx * bounce_strength
			
		# building boundary
		for bu in buildings:
			b = bu.boundary
			
			if (b["xmin"] - trigger <= next_xpos <= b["xmax"] + trigger) and (b["ymin"] - trigger <= next_ypos <= b["ymax"] + trigger):
				crossed_y = (self.ypos > b["ymax"] and next_ypos < b["ymax"]) or (self.ypos < b["ymin"] and next_ypos > b["ymin"])
				crossed_x = (self.xpos > b["xmax"] and next_xpos < b["xmax"]) or (self.xpos < b["xmin"] and next_xpos > b["xmin"])

				if crossed_y:
					next_ypos = b["ymax"] + offset if dy < 0 else b["ymin"] - offset
					dy = -dy * bounce_strength

				if crossed_x:
					next_xpos = b["xmax"] + offset if dx < 0 else b["xmin"] - offset
					dx = -dx * bounce_strength
		
		self.xpos = next_xpos
		self.ypos = next_ypos


		if self.status == "exiting" and dist < 5:
			self.status = "left"
			#print(f"{self.name} has exited the park.")
	# check if the patron is near the queue of the ride
	def near_queue(self):
		if self.target_ride is None:
			return False
		qx, qy = self.target_ride.q_positions[0]
		#print(f"target q_xpos: {qx}, target q_ypos: {qy} / current xpos : {self.xpos}, current_ypos: {self.ypos}")
		#print(f"x distance : {qx-self.xpos}, y distance : {qy-self.ypos}")
		return (qx - 15 <= self.xpos <= qx + 15) and (qy - 15 <= self.ypos <= qy + 15)
	# When they don't have to move
	def stay(self):
		pass

	def plot_patrons(self, ax):
		color = (
		"blue" if self.status == "walking"
		else "orange" if self.status == "queued"
		else "purple" if self.status == "riding"
		else "gray" if self.status == "exiting"
		else "black" if self.status == "unloading"
		else "red" if self.status == "loading"
		else "pink"
		)
		ax.scatter(self.xpos, self.ypos, marker='.', color=color, s=60)
		ax.text(self.xpos+2, self.ypos+2, self.name, fontsize=6, color='white')

