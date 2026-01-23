import random
import csv
import numpy as np
import argparse
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.widgets import Button
from patron import Patron
from objects.building import Building
from rides.ride import Ride
from rides.pirate import Pirate
from rides.gyro import Gyro
from rides.ferris import Ferris
from rides.carousel import Carousel
from terrain import Terrain

# interactive mode
def interactive_mode():
	user_input= []

	print("=== Adventure World (Interactive Mode) ===")
	print("=== 1. Time steps ===")
	time_steps = input('Enter number of time steps(100~250)')
	# default
	if time_steps == "":
		print("********That's not valid. Time_steps will be setting to 200*******")
		time_steps = 200
	elif int(time_steps) < 100 or int(time_steps) > 250:
		print("*********That's not a valid range. Time_steps will be setting to 200*******")
		time_steps = 200
	elif 100 <= int(time_steps) <= 250 :
		time_steps = int(time_steps)

	user_input.append(int(time_steps))	

	print("=== 2. Number of Patrons ===")
	num_patrons = input('Enter number of Patrons (10~30)')
	# default
	if num_patrons == "":
		print("********That's not valid. num_patrons will be setting to 15*******")
		num_patrons = 15
	elif int(num_patrons) < 10 or int(num_patrons) > 30:
		print("***********That's not a valid range. num_patrons will be setting to 15***********")
		num_patrons = 15
	elif 10 <= int(num_patrons) <= 30 :
		num_patrons = int(num_patrons)
	
	user_input.append(int(num_patrons))	

	print("=== 3. Color of bounding box of the rides ===")
	color_bounding_box = input("Enter colour for bounding box of the rides(R=red, B=blue, Y=yellow)...")
	if color_bounding_box == "":
		print("**************That's not valid. The color will be setting to PINK************")
		color_bounding_box = "pink"
	elif color_bounding_box.lower() in ('r', 'red'):
		color_bounding_box = "red"
	elif color_bounding_box.lower() in ('b', 'blue'):
		color_bounding_box = "blue"
	elif color_bounding_box.lower() in ('y', 'yellow'):
		color_bounding_box = "yellow"
	else:
		print("***********That's not Red, Blue and Yellow either. The color will be setting to PINK************")
		color_bounding_box = "pink"

	user_input.append(color_bounding_box)	

	print("=== 4. Color of ship of the pirate ship ===")
	color_pirate_boat = input("Enter colour for ship(B=brown,R=red, K=black)...")
	if color_pirate_boat == "":
		print("************That's not valid. The color will be setting to PINK**************")
		color_pirate_boat = "pink"
	elif color_pirate_boat.lower() in ('b','brown'):
		color_pirate_boat = "brown"
	elif color_pirate_boat.lower() in ('r','red'):
		color_pirate_boat = "red"
	elif color_pirate_boat.lower() in ('k','black'):
		color_pirate_boat = "black"
	else:
		print("************That's not Brown, Red and Black either. The color will be setting to PINK***********")
		color_pirate_boat = "pink"
	
	user_input.append(color_pirate_boat)	
	
	print("=========[User Inputs]===============")
	print(f"Time Steps: {user_input[0]}")
	print(f"Number of Patrons: {user_input[1]}")
	print(f"Color of bouding box: {user_input[2]}")
	print(f"Color of the ship of the pirate ship: {user_input[3]}")

	return user_input


#batch_mode(args.file, args.param)
#terrain = batch_mode_terrain(args.file) 
#user_input = batch_mode_param(args.param)

def batch_mode_terrain(map_file_path):
	print("=== Adventure World (Batch Mode) ===")
	# check map_file_path
	try:
		with open(map_file_path, "r") as f:
			pass
	except FileNotFoundError:
		print(f"{map_file_path} cannot be found.")
		print(f"********default terrain file will be used********")
		return False
	return True

def batch_mode_param_value_check(file, row):
	print(f"The content of {file} : {row}")
	if row:
		for i in range(4):
			# time-step
			if i == 0:
				if row[0] == "":
					row[0] = 200
				elif int(row[0]) < 100 or int(row[0]) > 250:
					print("********Time step is not a valid range. Time_steps will be setting to 200*******")
					row[0] = 200
				elif 100 <= int(row[0]) <= 250 :
					row[0] = int(row[0])
			# num-patrons
			elif i == 1:
				if row[1] == "":
					row[1] = 15
				elif int(row[1]) < 10 or int(row[1]) > 30:
					print("********Number of Patrons is not a valid range. num_patrons will be setting to 15*******")
					row[1] = 15
				elif 10 <= int(row[1]) <= 30 :
					row[1] = int(row[1])
			# bouding box color
			elif i == 2:
				if row[2].lower() in ('r','red'):
					row[2] = "red"
				elif row[2].lower() in ('b','blue'):
					print(f"{row[2].lower}")
					crow[2] = "blue"
				elif row[2].lower() in ('y','yellow'):
					row[2] = "yellow"
				else:
					print("********************The color of bounding box is not Red, Blue and Yellow either. The color will be setting to PINK************")
					row[2] = "pink"
			else:
				if row[3].lower() in ('b','brown'):
					row[3] = "brown"
				elif row[3].lower() in ('r','red'):
					row[3] = "red"
				elif row[3].lower() in ('k','black'):
					row[3] = "black"
				else:
					print("***************The color of ship is not Brown, Red and Black either. The color will be setting to PINK************")
					row[3] = "pink"
	else:
		print(f"*******The Parameter file is empty!!!!!!********")
		print(f"********default parameters will be used********")
		row = [200, 15, "pink", "pink"]
	return row

def batch_mode_param(param_file_path):
	# check param_file_path
	user_input = []
	try:
		with open(param_file_path, "r", newline='') as f:
			reader = csv.reader(f)
			for row in reader:
				user_input = batch_mode_param_value_check(param_file_path, row)				
	except FileNotFoundError:
		print(f"{param_file_path} cannot be found.")
		print(f"********default parameters will be used********")
		user_input = [200, 15, "pink", "pink"]
	return user_input

def create_buildings():
	#name, xpos, ypos, width, height
	building1 = Building("building1", xpos=100, ypos=120,width=45, height=45)
	building2 = Building("building2", xpos=250, ypos=300,width=80, height=130)
	building3 = Building("building3", xpos=500, ypos=80,width=30, height=50)
	building4 = Building("building4", xpos=650, ypos=280,width=160, height=70)
	buildings = [building1, building2, building3, building4]
	return buildings

def create_rides():
	pirate_logic = Ride("pirate", xpos=60, ypos=280, queue_cap=5, ride_cap=2,duration=14)
	gyro_logic = Ride("gyrodrop", xpos=400, ypos=280, queue_cap=5, ride_cap=3,duration=7)
	ferris_logic = Ride("ferriswheel", xpos=600, ypos=80, queue_cap=5, ride_cap=6,duration=15)
	carousel_logic = Ride("carousel", xpos=220, ypos=80, queue_cap=5, ride_cap=4, duration=12)

	rides = [pirate_logic,gyro_logic,ferris_logic, carousel_logic]
	return rides

def visualize_rides(rides, color_pirate_boat):
	pirate_logic,gyro_logic,ferris_logic, carousel_logic = rides

	pirate_shape = Pirate(xpos=88, ypos=280, width=100, height=100, ship_color=color_pirate_boat)
	gyro_shape = Gyro(xpos=450, ypos=280, width=50, height=100)
	ferris_shape = Ferris(ferris_logic,cx=675,cy=155,radius =54)
	carousel_shape = Carousel(xpos=220, ypos=80)

	#connect logic - visual
	ferris_logic.attach_visual(ferris_shape)

	pirate_logic.attach_visual(pirate_shape)
	pirate_shape.attach_ride(pirate_logic)

	gyro_logic.attach_visual(gyro_shape)
	gyro_shape.attach_ride(gyro_logic)

	carousel_logic.attach_visual(carousel_shape)
	carousel_shape.attach_ride(carousel_logic)
	
	ride_shapes = [pirate_shape, gyro_shape, ferris_shape, carousel_shape]

	return ride_shapes

def create_patrons(num_patrons):
	names = [
		"Unbee", "Hyejin", "Siyuan", "Lin", "Eric", "Paul", "Mansi", "Helly", "Ashini", "Pawani",
		"Bhrugu", "Mia", "Zaha", "Valerie", "Mihai", "Laura", "Lea", "Sadia", "Lucy", "Aaron",
		"Ned", "Daisy", "Jin", "Molly", "John", "Min", "Eden", "Saki", "Daniel", "Saori",
		"NS", "chung", "Kim", "Qu", "Au", "Ui", "Binnie", "Aun", "Ty", "Am", "Ba", "Vi" 
		]

	random_names = random.sample(names, num_patrons)
	# to make instace of patrons
	patrons = []
	for i in range(num_patrons):
		name = random_names[i]
		# (50, 30) : entry
		patrons.append(Patron(50, 30, name))
	return patrons

def patrons_status(patron, rides, buildings, terrain_map):
	# Exit condition
	if patron.status == "walking" and patron.total_rides >=2:
		patron.status = "exiting"
		patron.target_ride = None
		patron.target_exit = (850, 30)
		#print(f"{patron.name} decided to leave the park.")
	
	# just after the ridiing
	if patron.status == "walking" and patron.just_finished_ride:
		patron.last_ride = patron.just_finished_ride
		patron.just_finished_ride = None
		#print(f"{patron.name} left {patron.last_ride.name} and is now walking again")

	# patrons' action based on the status
	if patron.status == "walking":
		if patron.target_ride is None and patron.status != "exiting":
			available_rides = [r for r in rides if r!=patron.last_ride]
			patron.decide_target(available_rides) 
		patron.walk(rides, buildings, terrain_map)

		# if they are near queue
		if patron.near_queue():
			# check if queue is available
			if patron.target_ride.is_queue_available():
				patron.target_ride.add_queue(patron)
					
	# if they are loading, queued, riding, unloading
	elif patron.status in ["loading","queued", "riding", "unloading"]:
		patron.stay() # don't update the position
	# they are exiting
	elif patron.status == "exiting":
		patron.walk(rides, buildings, terrain_map)

def rides_status(ride, ax):
	ride.check_queue()
	if ride.visual_shape is not None:
		ride.visual_shape.step_update()

		if ride.name == "ferriswheel":
			ride.visual_shape.plot_ferris(ax)
			ride.visual_shape.plot_frame(ax)

		elif ride.name == "pirate":
			ride.visual_shape.plot_me(ax)
		elif ride.name == "gyrodrop":
			ride.visual_shape.plot_gyro(ax)
		elif ride.name == "carousel":
			ride.visual_shape.plot_carousel(ax)
	#print(f"  [Ride: {r.name:12s}] Status={r.status:>7s} | Queue={len(r.queue)} | OnRide={len(r.on_ride)}")

def run_simulation(user_input, terrain=None):
	# parameters (interactive mode or batch mode)
	sim_length = user_input[0]
	num_patrons = user_input[1]
	color_bounding_box = user_input[2]
	color_pirate_boat = user_input[3]

	# terrain
	# initialization
	height, width = 600, 900
	terrain_day = np.loadtxt("terrain_day.csv", delimiter=',').reshape((height, width, 3)) / 255.0
	terrain_cloudy = np.loadtxt("terrain_cloudy.csv", delimiter=',').reshape((height, width, 3)) / 255.0
	terrain_night = np.loadtxt("terrain_night.csv", delimiter=',').reshape((height, width, 3)) / 255.0
	terrains = [terrain_day, terrain_cloudy, terrain_night]

	if terrain == "terrain_day.csv":
		current_map = terrains[0]
		mode = "day"
	elif terrain == "terrain_cloudy.csv":
		current_map = terrains[1]
		mode = "cloudy"
	elif terrain == "terrain_night.csv":
		current_map = terrains[2]
		mode = "night"
	else :
		current_map = terrains[0]
		mode = "day"

	# create objects
	buildings = create_buildings()
	rides = create_rides()
	# visualize objects
	ride_shapes = visualize_rides(rides,color_pirate_boat)
	pirate_shape, gyro_shape, ferris_shape, carousel_shape = ride_shapes
	# create patrons
	patrons = []
	patrons = create_patrons(num_patrons)


	# plotting 
	fig = plt.figure(figsize=(8,10))

	# subplot
	gs = gridspec.GridSpec(2,2,width_ratios=[3,1], height_ratios=[1,1])
	plt.subplots_adjust(wspace = 0.3, hspace = 0.4)
	# ax : simulator 
	ax = fig.add_subplot(gs[:,0])
	ax.set_xlim(0,900)
	ax.set_ylim(0,600)
	ax.axis('off')

	terrain_map = Terrain("terrain_map", xpos=0, ypos=0,width=900, height=500)
	terrain_map.plot_terrain(ax)

	#ax_real : live statistics
	ax_real = fig.add_subplot(gs[0,1])
	ax_real.set_xlabel("Time step")
	ax_real.set_ylabel("Current Usage")
	ax_real.set_title("Theme park simulation")
	ax_real.set_xlim(0, sim_length)
	ax_real.set_ylim(0,6)

	#ax_sum : summary statistics
	ax_sum = fig.add_subplot(gs[1,1])
	ax_sum.set_title("Summary Table")

	# data for the table
	total_user = [0,0,0,0]
	data = [[total_user[0],"AUD 3",0],[total_user[1],"AUD 3",0],[total_user[2],"AUD 3",0],[total_user[3],"AUD 3",0]]
	col_labels = ['Total Users', 'Fare per Ride', 'Total Revenue']
	row_labels = ["pirate", "gyrodrop", "ferriswheel", "carousel"]
	
	# Matplotlib table
	ax_sum.axis("off")
	table = ax_sum.table(cellText=data, colLabels =col_labels, rowLabels=row_labels, loc='center')
	table.auto_set_font_size(False)
	table.set_fontsize(9)
	table.scale(1.6,3.5)
	for (row, col), cell in table.get_celld().items():
		cell.set_text_props(ha='center', va='center')
	
	colors = ["orange", "green", "purple", "blue"]
	usage_lines = {}

	for i, name in enumerate(row_labels):
	 	line, = ax_real.plot([], [], lw = 2, color=colors[i], label=name)
	 	usage_lines[name] = {"line":line, "x":[], "y":[]}
	ax_real.legend(loc="upper right")

	def on_button_clicked(event):
		ax.set_title("!!!IT'S RAINING!!!")
		terrain_map.draw_shapes(ax, mode="cloudy")
		terrain_map.draw_shapes(ax, mode="rainy")
		fig.canvas.draw_idle()

	ax_btn = fig.add_axes([0.9, 0.03, 0.05, 0.05])
	btn = Button(ax_btn, 'Click Me', color='pink', hovercolor='skyblue')
	btn.on_clicked(on_button_clicked)	

	#for animation
	plt.ion()

	# --- simulation loop ---
	for t in range(sim_length):
		#plotting
		ax.clear()
		ax.set_title(f"Time step {t+1}")
		# show terrain 
		ax.imshow(current_map, origin='lower')
		terrain_map.draw_shapes(ax, mode=mode)

		print(f"\n=== Time step {t+1} ===")
		# to make extra patrons during the simulation
		ratio = t / sim_length
		extra_patron = []
		if 0.2 <= ratio <= 0.22:
			extra_patron = create_patrons(random.randint(1,5))
		elif 0.4 <= ratio == 0.42 :
			extra_patron = create_patrons(random.randint(1,5))
		elif 0.6 <= ratio <= 0.62 :
			extra_patron = create_patrons(random.randint(1,5))
		elif 0.8 <= ratio <= 0.82 :
			extra_patron = create_patrons(random.randint(1,5))
		elif 0.9 <= ratio <= 0.92 :
			extra_patron = create_patrons(random.randint(1,5))
		for i in range(len(extra_patron)):
			patrons.append(extra_patron[i])
		
	
		# patrons status
		for p in patrons:
			patrons_status(p, rides, buildings, terrain_map)
			
		# rides status
		for r in rides:
			rides_status(r, ax)
			# ride boundary
			r.plot_boundary(ax, color_bounding_box)
			# ride exit
			r.plot_exit(ax, color_bounding_box)
	
		# building boundary
		for b in buildings:
			b.plot_buildings(ax)
			
		# after the riding
		patrons = [p for p in patrons if p.status != "left"]

		# plotting the patrons
		for p in patrons:
			p.plot_patrons(ax)
		
		# plotting the rides
		pirate_shape.plot_me(ax)
		gyro_shape.plot_gyro(ax)
		ferris_shape.plot_frame(ax)
		ferris_shape.plot_ferris(ax)
		ferris_shape.step_update()
		carousel_shape.plot_carousel(ax)
		carousel_shape.step_update()
	
		plt.pause(0.1)
	
		# for summary - total_user
		for r in rides:
			current_usage = len(r.on_ride)
			usage_lines[r.name]["x"].append(t)
			usage_lines[r.name]["y"].append(current_usage)
			usage_lines[r.name]["line"].set_data(usage_lines[r.name]["x"], usage_lines[r.name]["y"])
			if r.name == "pirate":
				total_user[0] += len(r.on_ride)
			elif r.name == "gyrodrop":
				total_user[1] += len(r.on_ride)
			elif r.name == "ferriswheel":
				total_user[2] += len(r.on_ride)
			else:
				total_user[3] += len(r.on_ride)
	ax_sum.clear()
	ax_sum.axis('off')
	# data for the table (table should be made again)
	total_revenue = [3*total_user[0], 3*total_user[1], 3*total_user[2],3*total_user[3]]
	data = [[total_user[0],"AUD 3","AUD "+str(total_revenue[0])],[total_user[1],"AUD 3","AUD "+str(total_revenue[1])],[total_user[2],"AUD 3","AUD "+str(total_revenue[2])],[total_user[3],"AUD 3","AUD "+str(total_revenue[3])]]
	col_labels = ['Total Users', 'Fare per Ride', 'Total Revenue']
	row_labels = ["pirate", "gyrodrop", "ferriswheel", "carousel"]
	

	# Matplotlib table
	table = ax_sum.table(cellText=data, colLabels =col_labels, rowLabels=row_labels, loc='center')
	table.auto_set_font_size(False)
	table.set_fontsize(9)
	table.scale(1.6,3.5)
	for (row, col), cell in table.get_celld().items():
		cell.set_text_props(ha='center', va='center')
	plt.ioff()
	plt.show()



if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	#interactive mode
	parser.add_argument("-i", "--interactive", action="store_true", help="Run in interactive mode")
	
	#batch mode
	parser.add_argument("-f", "--file", type=str, help="Path to terrain CSV file")
	parser.add_argument("-p", "--param", type=str, help="Path to parameter CSV file")
	
	args = parser.parse_args()
	print(args)

	# interactive mode
	if args.interactive: 
		user_input = interactive_mode()
		run_simulation(user_input, terrain=None)
	# batch mode
	elif args.file and args.param:
		if batch_mode_terrain(args.file) :
			terrain = args.file
		else:
			terrain = "terrain_day.csv"
		user_input = batch_mode_param(args.param)
		run_simulation(user_input, terrain)
	else:
		print("Please provide either -i or both -f and -p options.")
