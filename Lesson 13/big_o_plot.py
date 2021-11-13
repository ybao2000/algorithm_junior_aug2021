import math
import matplotlib.pyplot as plot

# we need x_list
x_list = list(range(1, 101, 1)) # [1, 2, ..., 100]
labels = ['Logarithmic', 'Linear', 'Log Linear', 'Quadratic', 'Cubic', 'Exponential', 'Factorial']
y_lists = []
y_lists.append([math.log2(x) for x in x_list])  # y is log2(x)
y_lists.append([x for x in x_list]) # y is x
y_lists.append([x*math.log2(x) for x in x_list])  # y is x log2(x)
y_lists.append([x*x for x in x_list]) # y is x*x
y_lists.append([x*x*x for x in x_list]) # y is x*x*x
y_lists.append([2**x for x in x_list]) # y is 2^x
y_lists.append([math.factorial(x) for x in x_list]) # y is x!

# plot setup
plot.figure(figsize=(12, 10))
plot.ylim(0, 10000)

# plot
for i in range(len(y_lists)):
  plot.plot(x_list, y_lists[i], label=labels[i])

plot.legend(loc=0)
plot.xlabel('n')
plot.ylabel('runtime')
plot.show()