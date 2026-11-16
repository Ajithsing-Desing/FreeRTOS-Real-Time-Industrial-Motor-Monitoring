#include <stdio.h>
#include "FreeRTOS.h"
#include "task.h"
#include "queue.h"
#include <time.h>
QueueHandle_t temperatureQueue;

static double getTimeMs(void)
{
    struct timespec ts;

    clock_gettime(CLOCK_MONOTONIC, &ts);

    return (double)ts.tv_sec * 1000.0
         + (double)ts.tv_nsec / 1000000.0;
}
/* Task 1: Sensor */
void vSensorTask(void *pvParameters)
{
    (void)pvParameters;

    int temperature = 30;

    TickType_t previousTick = xTaskGetTickCount();
   const TickType_t sensorPeriod = pdMS_TO_TICKS(1000);
   TickType_t lastExecutionTick = 0;
double lastRealTime = 0.0;

    while (1)
    {

        TickType_t currentTick = xTaskGetTickCount();
        double currentRealTime = getTimeMs();

if (lastExecutionTick != 0)
{
    TickType_t interval = currentTick - lastExecutionTick;

    long actualMs = (long)interval * portTICK_PERIOD_MS;
    long expectedMs = 1000;

    long jitter = actualMs - expectedMs;

    printf("Sensor Execution Interval: %ld ms\n", actualMs);
    printf("Sensor Interval Deviation: %ld ms\n", jitter);
}
lastExecutionTick = currentTick;
if (lastRealTime != 0.0)
{
    double realInterval = currentRealTime - lastRealTime;
    double realDeviation = realInterval - 1000.0;

    printf("Linux Clock Interval: %.3f ms\n", realInterval);
    printf("Linux Clock Deviation: %+.3f ms\n", realDeviation);
}

lastRealTime = currentRealTime;

        printf("Sensor Task: Temperature = %d C\n", temperature);
        fflush(stdout);
if (xQueueSend(temperatureQueue, &temperature, 0) != pdPASS)
{
    printf("Warning: Temperature queue is full!\n");
}
        temperature += 5;

        if (temperature > 80)
        {
            temperature = 30;
        }

vTaskDelayUntil(&previousTick, sensorPeriod);
    }
}
/* Task 2: Controller */
void vControlTask(void *pvParameters)
{
    (void)pvParameters;

    int receivedTemperature;
    int motorEnabled = 1;
    int resetRequested = 0;

    while (1)
    {
        if (xQueueReceive(temperatureQueue,
                          &receivedTemperature,
                          portMAX_DELAY) == pdPASS)
        {
            printf("Control Task: Received = %d C\n",
                   receivedTemperature);

            if (receivedTemperature >= 70 && motorEnabled)
            {
                motorEnabled = 0;
                printf("WARNING: MOTOR OVERHEATING!\n");
                printf("SAFETY ACTION: MOTOR SHUTDOWN!\n");
            }

            /* Simulate an operator requesting reset */
            if (!motorEnabled && receivedTemperature <= 50)
            {
                resetRequested = 1;
            }

            if (!motorEnabled && resetRequested &&
                receivedTemperature <= 50)
            {
                motorEnabled = 1;
                resetRequested = 0;
                printf("RESET ACCEPTED: MOTOR RESTARTED\n");
            }

            if (motorEnabled)
            {
                printf("Motor Status: RUNNING\n");
            }
            else
            {
                printf("Motor Status: OFF - RESET REQUIRED\n");
            }

            fflush(stdout);
        }
    }
}

/* Task 3: Simulated CPU workload */
void vLoadTask(void *pvParameters)
{
    (void)pvParameters;

    volatile unsigned long result = 0;

    while (1)
    {
        for (unsigned long i = 0; i < 1000000UL; i++)
        {
            result += i;
        }

        vTaskDelay(pdMS_TO_TICKS(10));
    }
}

int main(void)
{
    printf("Starting FreeRTOS Simulation...\n");

temperatureQueue = xQueueCreate(5, sizeof(int));

if (temperatureQueue == NULL)
{
    printf("Error: Queue creation failed!\n");
    return 1;
}

    xTaskCreate(
        vSensorTask,
        "Sensor",
        1024,
        NULL,
        2,
        NULL
    );

    xTaskCreate(
        vControlTask,
        "Control",
        1024,
        NULL,
        1,
        NULL
    );
/* Create CPU workload task */
if (xTaskCreate(
        vLoadTask,
        "CPU_Load",
        1024,
        NULL,
        1,
        NULL
    ) != pdPASS)
{
    printf("Error: CPU Load Task creation failed!\n");
    return 1;
}
    vTaskStartScheduler();

    return 0;
}
