import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

conditions = ["CPU Load ON", "CPU Load OFF"]
intervals = [1146.49, 1160.71]

plt.figure(figsize=(8, 5))

plt.bar(conditions, intervals)

plt.axhline(
    y=1000,
    linestyle="--",
    label="Target: 1000 ms"
)

plt.ylabel("Average Linux Clock Interval (ms)")
plt.title("FreeRTOS CPU Workload Timing Comparison")
plt.ylim(0, 1300)
plt.legend()
plt.tight_layout()

plt.savefig("cpu_load_comparison.png", dpi=300)

print("Graph saved: cpu_load_comparison.png")
# Graph 2: Task priority comparison

priorities = ["Control Priority 1", "Control Priority 3"]
priority_intervals = [1166.34, 1163.89]

plt.figure(figsize=(8, 5))

plt.bar(priorities, priority_intervals)

plt.axhline(
    y=1000,
    linestyle="--",
    label="Target: 1000 ms"
)

plt.ylabel("Average Linux Clock Interval (ms)")
plt.title("FreeRTOS Task Priority Timing Comparison")
plt.ylim(0, 1300)
plt.legend()
plt.tight_layout()

plt.savefig("priority_comparison.png", dpi=300)

print("Graph saved: priority_comparison.png")
