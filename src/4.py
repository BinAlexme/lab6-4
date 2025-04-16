import random
from datetime import datetime, timedelta


def generate_dates():
    start = datetime(2025, 4, 16) - timedelta(days=5 * 365)
    end = datetime(2025, 4, 16)
    return sorted(start + timedelta(days=random.randint(0, (end - start).days)) for _ in range(10))


def main():
    dates = generate_dates()
    print("Генерация даты:")
    for d in dates:
        print(d.strftime('%Y-%m-%d'))
    print("\nРаздница:")
    for d1, d2 in zip(dates, dates[1:]):
        print(f"Разница между {d1:%Y-%m-%d} и {d2:%Y-%m-%d}: {(d2 - d1).days} дней")


if __name__ == "__main__":
    main()
