train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 
#part 1
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return c_temp
#part 2
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)
#part 3
def c_to_f(c_temp):
    f_temp = c_temp * (9/5) + 32
    return f_temp
#part4
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)
#part 5
def get_force(mass, acceleration):
    return mass * acceleration
#part 6
train_force = get_force(train_mass, train_acceleration)
print(train_force)

#part 7
print("The GE train supplies {} Newtons of force.".format(train_force))

#part 8
def get_energy(mass, c=3*10**8):
    return mass * c**2

#part 9
bomb_energy = get_energy(bomb_mass)

#part 10
print("A 1kg bomb supplies {} Joules.".format(bomb_energy))

#part 11
def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    return force * distance

#part 12
train_work = get_work(train_mass, train_acceleration, train_distance)

#part 13
print(
    "The GE train does {} Joules of work over {} meters."
    .format(train_work, train_distance)
)




