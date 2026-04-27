import time
import heapq

pq = []

patients = [
    ("Budi", 3),
    ("Ani", 0),
    ("Citra", 2),
    ("Dedi", 0),
    ("Eka", 1)
]

print("=== ANTRIAN RUMAH SAKIT ===\n")

# enqueue
for name, prio in patients:
    heapq.heappush(pq, (prio, name))
    print(f"Masuk: {name} (prioritas {prio})")
    print(f"Queue: {pq}\n")
    time.sleep(1)

print("\n=== PROSES PELAYANAN ===\n")

# dequeue
while pq:
    prio, name = heapq.heappop(pq)
    print(f"Melayani: {name} (prioritas {prio})")
    print(f"Sisa: {pq}\n")
    time.sleep(2)
