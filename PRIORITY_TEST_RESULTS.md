# FreeRTOS Task Priority Experiment

## Objective
Investigate scheduling behavior after increasing
the Control Task priority.

## Configuration
- Sensor Task priority: 2
- Control Task priority: 3
- CPU Load Task: Disabled
- Intended sensor period: 1000 ms

## Results
Linux clock intervals (ms):
- 1155.595
- 1180.497
- 1164.841
- 1154.645

Average interval: 1163.89 ms
Average deviation: +163.89 ms

FreeRTOS reported interval: 1000 ms
FreeRTOS reported deviation: 0 ms

## Observations
- Sensor and Control Tasks communicated successfully.
- The simulated motor remained running at normal temperatures.
- The Control Task had higher scheduling priority.
- Linux wall-clock intervals exceeded 1000 ms.

## Limitations
These measurements were collected using the
FreeRTOS POSIX port on Linux.

The results do not establish that increasing
Control Task priority improves timing.

A controlled comparison with the original
priority configuration is still needed.

## Comparison: Control Task Priority 1

Configuration:
- Sensor Task priority: 2
- Control Task priority: 1
- CPU Load Task: Disabled

Linux clock intervals (ms):
- 1168.262
- 1157.964
- 1149.064
- 1171.597
- 1184.817

Average interval: 1166.34 ms
Average deviation: +166.34 ms

## Priority Comparison Conclusion

Control priority 3:
- Average Linux interval: 1163.89 ms
- Samples: 4

Control priority 1:
- Average Linux interval: 1166.34 ms
- Samples: 5

Both configurations maintained sensor-to-control
task communication and simulated motor operation.

The measurements are preliminary and do not
demonstrate a significant scheduling improvement
from increasing the Control Task priority.

The CPU workload task was disabled in both tests.
