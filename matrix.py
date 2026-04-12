import random
import time
import os

# Lấy kích thước terminal
width = os.get_terminal_size().columns

# Tạo danh sách ký tự
chars = "01アイウエオカキクケコサシスセソABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Khởi tạo vị trí rơi
drops = [0 for _ in range(width)]

try:
    while True:
        print("".join(
            random.choice(chars) if random.random() > 0.98 else " "
            for _ in range(width)
        ))

        # Cập nhật vị trí rơi
        drops = [d + 1 if d < 20 else 0 for d in drops]

        time.sleep(0.05)

except KeyboardInterrupt:
    print("\nBye hacker 😏")
