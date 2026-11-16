# FreeRTOS Scheduling Performance Experiment

## Objective
Compare sensor task timing with and without
an additional CPU workload task.

## Test Environment
- FreeRTOS GCC POSIX simulation
- Ubuntu Linux
- Sensor task period: 1000 ms

## Experiment 1: CPU Load Enabled

Linux clock intervals (ms):
- 1149.984
- 1146.306
- 1143.187

Average interval: 1146.49 ms
Average deviation: +146.49 ms

## Experiment 2: CPU Load Disabled

Linux clock intervals (ms):
- 1152.695
- 1152.782
- 1162.671
- 1159.026
- 1153.876
- 1183.232

Average interval: approximately 1160.71 ms
Average deviation: approximately +160.71 ms

## Observations
- FreeRTOS reported 1000 ms sensor intervals
  at its simulated tick resolution.
- Linux wall-clock measurements exceeded
  the intended 1000 ms period.
- Removing the CPU workload did not improve
  measured timing in these samples.

## Limitations
These are preliminary measurements from a
Linux-hosted FreeRTOS simulation.

Results do not establish timing performance
on a physical microcontroller.

More repeated experiments are needed.
