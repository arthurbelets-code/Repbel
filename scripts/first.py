#!/usr/bin/env python3

import datetime
import time

def main():
    try:
        while True:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Текущее время: {current_time}")
            time.sleep(5)  # Пауза на 5 секунд
    except KeyboardInterrupt:
        print("\nОстановлено пользователем.")

if __name__ == '__main__':
    main()
