def volume_cylinder(radius, height):
    return 3.14 * radius * radius * height


print(volume_cylinder(5, 20))
print(volume_cylinder(radius=5, height=20))
print(volume_cylinder(height=20, radius=5))

