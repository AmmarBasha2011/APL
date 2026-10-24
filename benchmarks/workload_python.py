"""The same deterministic workload, written in ordinary Python."""


def calculate(limit: int) -> int:
    total = 0
    for number in range(limit):
        total += (number * number) % 97
    return total


# تشغيل مباشر
if __name__ == "__main__":
    print(calculate(1_000_000))
