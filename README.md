# move_base_costmaps
Attempt to load a custom costmap in move_base. The costmap is created by a neural network that will output a numpy array. Image_grid package contains a script to convert the numpy array into an occupancy grid, which can then be loaded into move_base using the static_map plugin.
<img width="1357" alt="Screen Shot 2022-07-29 at 12 40 20 PM" src="https://user-images.githubusercontent.com/98352313/181816619-f1c7cf39-d2f6-488f-bfe5-a5d37a97c822.png">
