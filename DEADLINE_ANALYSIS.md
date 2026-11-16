# FreeRTOS Timing Interval Analysis

## Objective
Monitor sensor task execution intervals and
detect when Linux wall-clock intervals exceed
the intended 1000 ms period.

## Test Configuration
- FreeRTOS GCC POSIX simulation
- Ubuntu Linux
- Sensor Task priority: 2
- Control Task priority: 1
- CPU Load Task: Disabled
- Intended sensor period: 1000 ms

## Recorded Measurements

| Interval (ms) | Deviation (ms) | Result |
|---|---|---|
| 1158.666 | +158.666 | Exceeded |
| 1154.853 | +154.853 | Exceeded |
| 1149.889 | +149.889 | Exceeded |
| 1141.097 | +141.097 | Exceeded |

Average interval: 1151.13 ms
Average deviation: +151.13 ms

Observed intervals exceeding threshold: 4/4

## Observations
- FreeRTOS reported 1000 ms sensor intervals.
- FreeRTOS reported 0 ms interval deviation.
- All four Linux clock measurements exceeded 1000 ms.
- Sensor-to-Control Task communication continued.
- Motor shutdown and simulated restart remained functional.

## Limitations
The Linux clock measurements reflect the
FreeRTOS POSIX simulation environment.

The threshold check compares consecutive sensor
execution intervals, not task completion deadlines.

These results do not demonstrate deadline
performance on physical embedded hardware.

More repeated experiments are needed.
