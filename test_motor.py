import subprocess

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

tests = {
    "Normal motor operation":
        "Motor Status: RUNNING" in output,

    "Overheating warning":
        "WARNING: MOTOR OVERHEATING!" in output,

    "Motor shutdown":
        "SAFETY ACTION: MOTOR SHUTDOWN!" in output,

    "Motor remains off":
        "Motor Status: OFF - RESET REQUIRED" in output,

    "Motor restart":
        "RESET ACCEPTED: MOTOR RESTARTED" in output
}

print("\nAUTOMATED TEST RESULTS")
print("----------------------")

for name, passed in tests.items():
    if passed:
        print(f"PASS: {name}")
    else:
        print(f"FAIL: {name}")

passed_count = sum(tests.values())

print(f"\nTests passed: {passed_count}/{len(tests)}")

if passed_count != len(tests):
    raise SystemExit(1)
