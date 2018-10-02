import pygal

from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(100000):
    result = die.roll()
    results.append(result)
    
# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling one D6 100000 times."
hist.x_labels = []
for value in range(1, die.num_sides+1):
	hist.x_labels.append(str(value))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
