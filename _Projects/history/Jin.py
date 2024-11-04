import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# data = pd.read_csv('./Jin.csv')
data = pd.read_csv('./3FamiliesDivideJin.csv')
data["Level"] = [np.random.randint(-6,-2) if (i%2)==0 else np.random.randint(2, 6) for i in range(len(data))]

# data["Year"] = pd.to_datetime(data["Year"])
# print(data)
# Plot
fig, ax = plt.subplots(figsize=(18,9))
# Horizontal line ys are all 0
ax.plot(data.Year, [0,]* len(data), "-o", color="black", markerfacecolor="white")

# Modify the x-axis ticks
# use pd.date_range(...) for the positions and range(...) for the labels.
# ax.set_xticks(range(-1046, -402), range(-1046, -402))
# only values within this range are visible.
ax.set_ylim(-7,7)

for idx in range(len(data)):
    dt, event, level = data["Year"][idx], data["Event"][idx], data["Level"][idx]
    print(dt, event)
    ax.annotate(event, 
                xy=(dt, 0.1 if level>0 else -0.1),
                xytext=(dt, level),
                arrowprops=dict(arrowstyle="-",color="red", linewidth=0.8),
                ha="center")

# Hide the box around the plot
# ax.spines[["left", "top", "right", "bottom"]].set_visible(False);
ax.spines[["left", "top", "right"]].set_visible(False)
# ax.spines[["bottom"]].set_position(("axes", 0.5));
# Hide the y-axis
ax.yaxis.set_visible(False)

# Set the title of the plot
ax.set_title("Jin", pad=10, loc="left", fontsize=25, fontweight="bold")

plt.show()