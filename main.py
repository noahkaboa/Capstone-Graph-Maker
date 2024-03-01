from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

scale = 500

data = [
    ["Location 1", 104, 2, 1.5],
    ["Location 2", 72, 0.5, 0],
]

df = pd.DataFrame(data, columns = ("Location", "Traffic per hour", "Usage per hour", "Unlock per hour"))
print(df)

s = len(df.index)
plt.scatter(df["Location"], np.ones(s), s = df["Traffic per hour"]*scale, color="#C0CAAD")
plt.scatter(df["Location"], np.ones(s), s = df["Usage per hour"]*scale, color="#1A80BB")
plt.scatter(df["Location"], np.ones(s), s = df["Unlock per hour"]*scale, color="#EA801C")

plt.yticks([])
plt.xticks(df["Location"])

plt.axis([0, 1, 0, 1])

plt.show()