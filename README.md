
# FreeRTOS-Based Real-Time Industrial Motor Monitoring

## Overview
A software-only industrial motor monitoring simulation using FreeRTOS and C on Ubuntu Linux through the POSIX port.

## Implemented Features
- Simulated motor temperature sensor
- FreeRTOS sensor and control tasks
- Inter-task communication using a queue
- Overheating detection at a demonstration threshold of 70°C
- Simulated motor shutdown and automatic reset testing
- Periodic scheduling using vTaskDelayUntil()
- FreeRTOS tick and Linux monotonic-clock interval measurements
- CPU workload task for scheduling experiments

## Technology
C, FreeRTOS, CMake, GCC, Ubuntu Linux, Git

## Build and Run
From the RTOS_Application directory, with the FreeRTOS-Kernel repository in the parent directory:

```bash
cmake -S . -B build
cmake --build build -j2
./build/rtos_simulation
```

## Limitations
This project runs in a Linux-hosted FreeRTOS simulation, not on physical embedded hardware. It does not provide certified real-time or motor safety guarantees. The reset request is automatically simulated.

## Work in Progress
- CPU-load comparison experiments
- Deadline monitoring and scheduling analysis
- Fault injection and recovery testing
- Performance graphs and technical report
  
