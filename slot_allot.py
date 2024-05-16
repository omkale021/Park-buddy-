import random

def allocate_parking_slot():
    # Simulate slot availability
    slots = [i for i in range(1, 101)]  # 100 parking slots
    available_slots = random.sample(slots, len(slots) - random.randint(0, 10))
    if available_slots:
        allocated_slot = random.choice(available_slots)
        return allocated_slot
    else:
        return None

# Allocate slot
allocated_slot = allocate_parking_slot()
if allocated_slot:
    print(f"Parking slot allocated: {allocated_slot}")
else:
    print("No parking slots available")
