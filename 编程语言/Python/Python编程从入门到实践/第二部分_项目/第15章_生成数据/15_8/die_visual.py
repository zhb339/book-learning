import pygal

from die import Die

# Create a D8.
die1 = Die()
die2 = Die()
die3 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll() + die3.roll()
    results.append(result)
    
# Analyze the results.
frequencies = []
for value in range(3, die1.num_sides + die2.num_sides + die3.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D8 1000 times."
hist.x_labels = []
for value in range(3, die1.num_sides + die2.num_sides + die3.num_sides + 1):
	hist.x_labels.append(str(value))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('2 D8', frequencies)
hist.render_to_file('die_visual.svg')
