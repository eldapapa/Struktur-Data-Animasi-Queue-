import time
from collections import deque

queue = deque()

docs = ["laporanstrukdat.pdf", "tugaspekan8.docx", "foto.jpg"]

print("=== SIMULASI PRINTER QUEUE ===\n")

# enqueue
for doc in docs:
    queue.append(doc)
    print(f"Masuk antrian: {doc}")
    print(f"Queue: {list(queue)}\n")
    time.sleep(1)

print("\n=== PROSES CETAK ===\n")

# dequeue
while queue:
    current = queue.popleft()
    print(f"Mencetak: {current}")
    print(f"Sisa Queue: {list(queue)}\n")
    time.sleep(2)
