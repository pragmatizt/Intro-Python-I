"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with
lists!).

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

"""Let's print the original out, and then make it cleaner."""
print("\nORIGINAL:")
[print(n.values()) for n in waypoints]

# Add a new waypoint to the list
waypoints.append({"lat": 26.7, "lon": 80, "name": "Palm Beach"})
print("\nNEW WAYPOINT:")
[print(n.values()) for n in waypoints]

#RESOURCE for NEXT PROBLEMS: https://www.pluralsight.com/guides/manipulating-lists-dictionaries-python

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the waypoints list.
# Keeping this code, want to ask Q later: waypoints.update({"lon": -130})
for n in waypoints:
    if 'a place' in n.values():
        n['lon'] = -130
        n["name"] = "not a real place"


# Write a loop that prints out all the field values for all the waypoints
print("\nAfter Modification & Loop:")
[print(n.values()) for n in waypoints]
