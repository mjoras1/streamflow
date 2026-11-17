import numpy as np
import matplotlib.pyplot as plt


def load_streamflow(filename):
    """Read the streamflow CSV and return dates and flows in cfs."""
    data = np.genfromtxt(filename, delimiter=',', dtype=str, skip_header=1)
    dates = data[:, 0].astype('datetime64')
    flows = data[:, 1:].astype(float)
    return dates, flows


def plot_streamflow(dates, flows, sites):
    """Plot each gauge's flow using the Matplotlib homework formatting."""
    colors = ['red', 'blue', 'orange', 'green', 'purple']
    plt.figure(figsize=(12, 6))
    for i, site in enumerate(sites):
        plt.plot(dates, flows[:, i], label=f'Site {site}', color=colors[i], linewidth=2)
    plt.xlabel('Date')
    plt.ylabel('Streamflow')
    plt.title('Streamflow Data for Provo River')
    plt.grid(True)
    plt.legend()
    plt.show()


# Main program
sites = ['10163000', '10155200', '10155500', '10154200', '10155000']
dates, flows = load_streamflow('June-2021-Provo-River-Streamflow-Rates (1).csv')
plot_streamflow(dates, flows, sites)
