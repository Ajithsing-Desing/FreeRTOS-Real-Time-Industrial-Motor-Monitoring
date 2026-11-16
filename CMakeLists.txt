cmake_minimum_required(VERSION 3.16)

project(FreeRTOS_Master_Project C)

set(CMAKE_C_STANDARD 11)

set(FREERTOS_PORT GCC_POSIX CACHE STRING "" FORCE)
set(FREERTOS_HEAP 4 CACHE STRING "" FORCE)

set(FREERTOS_CONFIG_FILE_DIRECTORY
    ${CMAKE_CURRENT_SOURCE_DIR}
    CACHE STRING "" FORCE
)

add_subdirectory(
    ../FreeRTOS-Kernel
    FreeRTOS-Kernel-build
)

add_executable(rtos_simulation main.c)

target_link_libraries(
    rtos_simulation
    PRIVATE
    freertos_kernel
    pthread
)
