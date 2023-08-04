import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Generate random data points for demonstration
np.random.seed(42)
num_points = 100
lats = np.random.uniform(low=-90, high=90, size=num_points)
lons = np.random.uniform(low=-180, high=180, size=num_points)
values = np.random.randint(low=0, high=100, size=num_points)

# Load world countries' boundaries from geopandas
world_data = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Function to plot a world map with data points


def plot_world_map(i):
    plt.cla()  # Clear the current axes
    plt.title(f"World Map - Animation Frame {i+1}")

    # Plot world map boundaries
    world_data.plot(ax=plt.gca(), color='lightgray', edgecolor='black')

    # Plot data points for the current frame
    for lat, lon, value in zip(lats[:i], lons[:i], values[:i]):
        plt.scatter(lon, lat, c='red', s=value, alpha=0.5)

    plt.xlim(-180, 180)
    plt.ylim(-90, 90)
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')

# Create the animation


fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, plot_world_map, frames=num_points, interval=100, repeat=False)

# To save the animation to a file, uncomment the next line and specify the filename and writer.
# ani.save('world_map_animation.mp4', writer='ffmpeg')

plt.show()
