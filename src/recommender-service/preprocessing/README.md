# Step 0
Have a .osm file ready

# Step 1
To seperate node and way file you can run the script as

$ .\separate_node_way_file.py ../map/munich_small

where munich_small.osm is your osm XML file. Note that the argument passed is relative address of the file.

The script will create a .nodes and .ways file with same filename (e.g. munich_small.nodes and munich_small.ways) in the same directory where .osm file is present.

# Step 2
Create a dictionary from nodes file (e.g. munich_small.nodes) and dump it (munich_small.nodes.serialize).

Some stats

File size (munich_large.nodes): 182 MB
Time to read file and create dictionary: 83.20 sec
Time to dump dictionary: 4.86 sec
Time to read dumped dictionary: 2.18 sec

File size (munich_small.nodes): 6.8 MB
Time to read file and create dictionary: 3.28 sec
Time to dump dictionary: 0.15 sec
Time to read dumped dictionary: 0.08 sec

# Step 3
Create a graph from ways file (e.g. munich_small.ways) and dump it (munich_small.ways.serialize).

# Step 4
Create a .nodes.connected.serialize file.