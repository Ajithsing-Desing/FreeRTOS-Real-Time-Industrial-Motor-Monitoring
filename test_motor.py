import subprocess
import re

print("Starting FreeRTOS automated motor tests...")

try:
    result = subprocess.run(
        ["./build/rtos_simulation"],
        capture_output=True,
        text=True,
        timeout=30
    )
    output = result.stdout

except subprocess.TimeoutExpired as error:
    output = error.stdout or b""

    if isinstance(output, bytes):
        output = output.decode("utf-8", errors="replace")

# Extract temperature readings and corresponding motor states
pattern = (
    r"Control Task: Received = (\d+) C"
    r"(.*?)"
    r"Motor Status: (RUNNING|OFF - RESET REQUIRED)"
)

matches = re.findall(pattern, output, re.DOTALL)

readings = [
    (int(temperature), messages, status)
    for temperature, messages, status in matches
]

# Check actual temperature-state combinations
normal_operation = any(
    temp == 65 and status == "RUNNING"
    for temp, messages, status in readings
)

shutdown_at_70 = any(
    temp == 70
    and status == "OFF - RESET REQUIRED"
    and "SAFETY ACTION: MOTOR SHUTDOWN!" in messages
    for temp, messages, status in readings
)

remains_off_at_75 = any(
    temp == 75 and status == "OFF - RESET REQUIRED"
    for temp, messages, status in readings
)

restart_at_30 = any(
    temp == 30
    and status == "RUNNING"
    and "RESET ACCEPTED: MOTOR RESTARTED" in messages
    for temp, messages, status in readings
)

# Verify the expected sequence occurs in order
sequence = [
    (temp, status)
    for temp, messages, status in readings
]

expected = [
    (65, "RUNNING"),
    (70, "OFF - RESET REQUIRED"),
    (75, "OFF - RESET REQUIRED"),
    (30, "RUNNING")
]

position = 0

for item in sequence:
    if position < len(expected) and item == expected[position]:
        position += 1

sequence_correct = position == len(expected)

tests = {
    "Normal operation at 65 C": normal_operation,
    "Shutdown at 70 C": shutdown_at_70,
    "Motor remains off at 75 C": remains_off_at_75,
    "Restart at 30 C": restart_at_30,
    "Correct motor state sequence": sequence_correct
}

print("\nAUTOMATED TEST RESULTS")
print("----------------------")

for name, passed in tests.items():
    print(f"{'PASS' if passed else 'FAIL'}: {name}")

passed_count = sum(tests.values())

print(f"\nTests passed: {passed_count}/{len(tests)}")

if passed_count != len(tests):
    raise SystemExit(1)
