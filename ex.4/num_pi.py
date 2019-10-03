from math import pi
def number_pi(num_sim):
    print('{:.{num_sim}f}'.format(pi, num_sim=num_sim))
num_sim = input('Колличесвто знаков после запятой: ')

if num_sim.isnumeric():
    number_pi(num_sim)
