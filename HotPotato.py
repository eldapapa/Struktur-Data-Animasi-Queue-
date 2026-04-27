import time
from collections import deque

players = deque(["A", "B", "C", "D", "E"])
num = 3

print("=== HOT POTATO GAME ===\n")

while len(players) > 1:
    for i in range(num):
        players.append(players.popleft())
        print(f"Oper bola: {list(players)}")
        time.sleep(1)

    out = players.popleft()
    print(f"❌ Keluar: {out}")
    print(f"Sisa: {list(players)}\n")
    time.sleep(1)

print(f"🏆 Pemenang: {players[0]}")
