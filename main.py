from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

scale = 500
distance_between_bubbles = 1.5

data = [
    ["Location 1", 104, 2, 1.5],
    ["Location 2", 72, 0.5, 0],
    ["Location 3", 45, 1, 0.5],
    ["Placeholder Location", 0, 0, 0]
]
max_bubble_size = max([max(row[1:]) for row in data])

df = pd.DataFrame(data, columns = ("Location", "Traffic per hour", "Usage per hour", "Unlock per hour"))

s = len(df.index)
x_locations = np.arange(s)
plt.figure(figsize=(15, 5))
plt.scatter(x_locations * distance_between_bubbles, np.ones(s), s = df["Traffic per hour"]*scale, color="#C0CAAD")
plt.scatter(x_locations * distance_between_bubbles, np.ones(s), s = df["Usage per hour"]*scale, color="#1A80BB")
plt.scatter(x_locations * distance_between_bubbles, np.ones(s), s = df["Unlock per hour"]*scale, color="#EA801C")

plt.xlim(-distance_between_bubbles / 2, 0.5 * distance_between_bubbles)
plt.ylim(0, 2)

# plt.yticks([])
plt.xticks(x_locations * distance_between_bubbles, df["Location"])

plt.tight_layout(w_pad=max_bubble_size*2)
plt.subplots_adjust(left = 0, right = 1, bottom = 0.1, top = 1)


plt.show()
