import csv
import numpy as np
import matplotlib.pyplot as plt


def load_streamflow(filename):
    """Read the streamflow CSV and return dates and flows in cfs."""
    data = np.genfromtxt(filename, delimiter=',', dtype=str, skip_header=1)
    dates = data[:, 0].astype('datetime64')
    flows = data[:, 1:].astype(float)
    return dates, flows


def summarize(dates, flows, sites):
    # Excel check for 10163000: =MAX(B2:B2881) is 131 cfs; =AVERAGE(B2:B2881) is 56.95236111 cfs.
    # Format each gauge's statistics once so the terminal table and CSV contain the same values.
    header = f"{'Gauge':<12}{'Max (cfs)':>10}   {'Date of max':<16}{'Min (cfs)':>10}{'Avg (cfs)':>11}"
    print(header)
    rows = [['Gauge', 'Max (cfs)', 'Date of max', 'Min (cfs)', 'Avg (cfs)']]

    for i, site in enumerate(sites):
        gauge_flows = flows[:, i]
        max_index = np.argmax(gauge_flows)
        max_flow = np.max(gauge_flows)
        date_of_max = np.datetime_as_string(dates[max_index], unit='m').replace('T', ' ')
        min_flow = np.min(gauge_flows)
        average_flow = np.mean(gauge_flows)
        row = [site, f'{max_flow:.1f}', date_of_max, f'{min_flow:.1f}', f'{average_flow:.1f}']
        rows.append(row)
        print(f'{row[0]:<12}{row[1]:>10}   {row[2]:<16}{row[3]:>10}{row[4]:>11}')

    with open('streamflow_summary.csv', 'w', newline='', encoding='utf-8') as summary_file:
        csv.writer(summary_file).writerows(rows)


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
summarize(dates, flows, sites)
threshold = float(input('Enter a flow threshold in cfs: '))
for i, site in enumerate(sites):
    # Each reading is 15 minutes, so multiply the number of readings by 0.25 hours.
    hours_above_threshold = np.sum(flows[:, i] > threshold) * 0.25
    print(f'Gauge {site}: {hours_above_threshold:.2f} hours above threshold')
