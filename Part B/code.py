def undoom_dice(die_a, die_b):
    scaling_factor = sum(die_a) / sum(die_b)
    x=[]
    for spots in die_a:
        x.append(min(4,spots))
    y=[]
    for spots in die_b:
        y.append(min(6,round(spots*scaling_factor)))
    return x, y
die_a = [1, 2, 3, 4, 5, 6]
die_b = die_a
new_die_a, new_die_b = undoom_dice(die_a, die_b)
print("\nNew Die A:", new_die_a)
print("New Die B:", new_die_b)   
