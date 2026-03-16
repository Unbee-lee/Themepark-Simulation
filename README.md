## Overview
The program simulates a theme park with 4 rides, which are Pirate Ship, Ferris Wheel, Gyrodrop and
Carousel, with varying movement patterns. Each ride has a queue to handle waiting passengers, and
patrons wait in each queue. Rides have different statuses: “idle”, “loading”, “riding”, and “unloading”.
They check the queues and load passengers according to the ride's capacity. Rides operate according
to their respective durations, and when the ride concludes, patrons exit through the ride's exit.
Patrons enter and exit the theme park through the entrances. Each patron has a target ride and must
avoid the entire boundary of the rides, buildings, and terrain, with patrons continuing to enter and
exit along the way. Real-time ride utilization was implemented and after the simulation was over,
created summary statistics showing the total number of users for each ride and the corresponding
total revenue. The map that serves as the base for the ride has day, cloudy days, and night
implemented, and a button has been implemented on the plot so that when you press the button, it
suddenly starts raining.

## Contents
Themepark simulation using the matplotlib. 
Patrons can go for a ride within the theme park and they have a targeted movement.
Also they avoid the boundary of the objects.
Ride has their own status and they check the queue. 

adventureworld.py 
patron.py
terrain.py
ride.py
building.py
pirate.py
gyro.py
ferris.py
carousel.py

## Dependencies
matplotlib
numpy

## entry point
adventureworld.py

## Version information
4/10/2025 - initial version of 9 programs

