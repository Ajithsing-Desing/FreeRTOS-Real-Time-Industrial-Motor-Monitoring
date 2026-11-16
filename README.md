
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
  
## Reproducing the Project on Ubuntu

### Prerequisites

- Ubuntu Linux
- GCC compiler
- CMake
- Git
- POSIX threads support

Install the required tools:

```bash
sudo apt update
sudo apt install -y build-essential cmake git

```

### Clone the Project

```bash
mkdir FreeRTOS_Master_Project
cd FreeRTOS_Master_Project

git clone https://github.com/Ajithsing-Desing/FreeRTOS-Real-Time-Industrial-Motor-Monitoring.git RTOS_Application

git clone https://github.com/FreeRTOS/FreeRTOS-Kernel.git

cd FreeRTOS-Kernel
git checkout ca75944d4e9ca59cfa3a9faa6cb8b49e0772ca520

cd ../RTOS_Application
```

### Build the Project

```bash
cmake -S . -B build
cmake --build build -j2
```

### Run the Simulation

```bash
./build/rtos_simulation
```

Press Ctrl + C to stop the simulation.

### Important Notes

This project uses the FreeRTOS GCC POSIX port
and runs as a Linux-hosted simulation.

It does not currently run on physical STM32 hardware.
