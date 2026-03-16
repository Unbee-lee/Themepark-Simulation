## Overview
The program simulates a theme park with 4 rides, which are Pirate Ship, Ferris Wheel, Gyrodrop and
Carousel, with varying movement patterns and provides realtime and summary statistics of each of simulations.

Each ride has a queue to handle waiting passengers, and patrons wait in each queue. Rides have different statuses: “idle”, “loading”, “riding”, and “unloading”. They check the queues and load passengers according to the ride's capacity. Rides operate according to their respective durations, and when the ride concludes, patrons exit through the ride's exit.

Patrons enter and exit the theme park through the entrances. Each patron has a target ride and must avoid the entire boundary of the rides, buildings, and terrain, with patrons continuing to enter and exit along the way. 

Real-time ride utilization was implemented and after the simulation was over, created summary statistics showing the total number of users for each ride and the corresponding total revenue. The map that serves as the base for the ride has day, cloudy days, and night implemented, and a button has been implemented on the plot so that when you press the button, it suddenly starts raining.

## Structure
```text
Themepark-Simulation/                 # Project Container
├── adventureworld.py                 # Entry point to run the entire simulation
├── patron.py                         # Patron object
├── terrain.py                        # Terrain setup
├── rides/                            # Submodule for theme park rides
│   ├── carousel.py                   # Plot Carousel
│   ├── ferris.py                     # Plot Ferris wheel
|   |── gyro.py                       # Plot Gyrodrop
|   |── pirate.py                     # Plot Pirate ship
│   └── ride.py                       # Base class for all ride types
├── objects/                          # Submodule for obstacles
│   └── building.py                   # Static obstacles
├── param_blank.csv                   # Uses default values (empty file)
├── param_error.csv                   # Uses default values (fallback for invalid parameters)
├── param_normal.csv                  # Standard operational parameters
├── terrain_cloudy.csv                # Terrain parameter: Cloudy weather
├── terrain_day.csv                   # Terrain parameter: Day
└── terrain_night.csv                 # Terrain parameter: Night
```

## Project Setup and Usage

### 1. Environment Setup
Python 3.10.14

### 2. Dependencies
numpy

matplotlib

### 3. Running the program

#### - Interactive Mode
Interactive mode will ask for number/type of rides and any other variables you include

command example : python3 adventureworld.py -i

#### - Batch Mode  
In batch mode, you will use command line parameters to get the terrain and parameters

command example : python3 adventureworld.py -f terrain_day.csv -p param_normal.csv

## Version information
4/10/2025 - initial version of 9 programs

## Scenario 1 - Day version initialized with 10 patrons
Batch mode - python3 adventureworld.py -f terrain_day.csv -p param_normal.csv

!https://github.com/Unbee-lee/Themepark-Simulation/blob/main/Scenario1.png

## Scenario 2 - Cloudy version initialized with 30 patrons
Batch mode - python3 adventureworld.py -f terrain_cloudy.csv -p param_normal.csv

https://github.com/Unbee-lee/Themepark-Simulation/blob/main/Scenario_2.png

## Scenario 3 - Night version initialized with 20 patrons
Batch mode - python3 adventureworld.py -f terrain_night.csv -p param_normal.csv

https://github.com/Unbee-lee/Themepark-Simulation/blob/main/Scenario_3.png

## Future work
For more detailed analysis, data on the average number of rides per person and peak usage rates for each weather condition can be utilised. Furthermore, while each ride currently has the same ticket price, this analysis can be used to increase ticket prices for popular rides, further increasing revenue. It would also be effective to compare data when operating strategies were applied differently by varying the number of operating rides, even though all rides were operated in each scenario.




