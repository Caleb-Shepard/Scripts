SPAWNER_RADIUS = 16

def input_coordinates(name):
    print('Give coordinates (x, y, z) for ' + name)
    x = input('x: ')
    y = input('y: ')
    z = input('z: ')
    return (x, y, z)
    pass


def point_within_sphere(point, sphere_center, sphere_radius):
    (cx, cy, cz) = sphere_center
    (x, y, z)    = point
    r            = sphere_radius

    return (x - cx)**2 + (y - cy)**2 + (z - cz)**2 < r**2


print('Script to see if a point is within spawn radius of both spawners')

'''
spawner_one       = input_coordinates('the first spawner.')
spawner_two       = input_coordinates('the second spawner.')
point_in_question = input_coordinates('the point in question.')
'''
spawner_one       = (-701.5, 7.5, -591.5)
spawner_two       = (-698.5, 17.5, -600.5)
point_in_question = (-707.5, 19.5, -600.5)

print('Spawner radius assumed to be ' + str(SPAWNER_RADIUS))

if point_within_sphere(point_in_question, spawner_one, SPAWNER_RADIUS):
    print('Point within spawner1 radius')
else:
    print('Point not within spawner1 radius')

if point_within_sphere(point_in_question, spawner_two, SPAWNER_RADIUS):
    print('Point within spawner2 radius')
else:
    print('Point not within spawner2 radius')

