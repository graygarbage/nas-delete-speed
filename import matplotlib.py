import matplotlib.pyplot as plt

def calculate_time(num_files, deletion_rate_per_node, num_nodes):
    return num_files / (deletion_rate_per_node * num_nodes)

deletion_rate_per_node = 2000
num_nodes = 10

file_counts = [10**7, 2 * 10**7, 5 * 10**7, 10**8, 2 * 10**8, 5 * 10**8, 10**9]
times = [calculate_time(files, deletion_rate_per_node, num_nodes) for files in file_counts]

plt.plot(file_counts, times, marker='o')
plt.xscale('log')
plt.yscale('log')
plt.ylabel('Time (seconds)')
plt.title('Deletion Time vs Number of Files')
plt.grid(True)
plt.show()