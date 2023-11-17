import matplotlib.pyplot as plt

def calculate_time(num_files, deletion_rate_per_node, num_nodes):
    return num_files / (deletion_rate_per_node * num_nodes)

deletion_rate_per_node = 2000
num_nodes = 10

# Extend the file counts to include 10 billion
file_counts = [10**7, 2 * 10**7, 5 * 10**7, 10**8, 2 * 10**8, 5 * 10**8, 10**9, 2 * 10**9, 5 * 10**9, 10**10]
times = [calculate_time(files, deletion_rate_per_node, num_nodes) for files in file_counts]

# Custom labels for the x-axis
file_labels = ['10M', '20M', '50M', '100M', '200M', '500M', '1B', '2B', '5B', '10B']

# Convert times to hours for more readable y-axis labels
times_in_hours = [time / 3600 for time in times]
time_labels = ['{:.2f}'.format(time) for time in times_in_hours]

plt.plot(file_counts, times_in_hours, marker='o', label=f'{num_nodes} Nodes')
plt.xscale('log')
plt.yscale('log')
plt.xticks(file_counts, file_labels)  # Set custom x-axis labels
plt.yticks(times_in_hours, time_labels)  # Set custom y-axis labels
plt.xlabel('Number of Files')
plt.ylabel('Time to Delete Files (hours)')
plt.title('Deletion Time vs Number of Files')
plt.legend()  # Show legend
plt.grid(True)
plt.show()
