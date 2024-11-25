# disk_scheduling_algorithms.py

def sstf(arm, requests):
    requests = sorted(requests)
    sequence = []
    total_movement = 0

    while requests:
        closest = min(requests, key=lambda x: abs(x - arm))
        total_movement += abs(closest - arm)
        sequence.append(closest)
        arm = closest
        requests.remove(closest)

    return {"sequence": sequence, "total_movement": total_movement}

def scan(arm, requests, tracks):
    requests = sorted(requests)
    sequence = []
    total_movement = 0
    direction = "left"

    if direction == "left":
        left = [r for r in requests if r <= arm]
        right = [r for r in requests if r > arm]

        for r in reversed(left):
            sequence.append(r)
            total_movement += abs(arm - r)
            arm = r

        total_movement += arm  # Go to track 0
        arm = 0

        for r in right:
            sequence.append(r)
            total_movement += abs(arm - r)
            arm = r

    return {"sequence": sequence, "total_movement": total_movement}

def cscan(arm, requests, tracks):
    requests = sorted(requests)
    sequence = []
    total_movement = 0

    left = [r for r in requests if r <= arm]
    right = [r for r in requests if r > arm]

    for r in right:
        sequence.append(r)
        total_movement += abs(arm - r)
        arm = r

    if left:
        total_movement += abs(tracks - arm - 1)  # Move to the end of the disk
        arm = 0  # Jump to the beginning of the disk

        for r in left:
            sequence.append(r)
            total_movement += abs(arm - r)
            arm = r

    return {"sequence": sequence, "total_movement": total_movement}

def look(arm, requests):
    requests = sorted(requests)
    sequence = []
    total_movement = 0
    direction = "left"

    if direction == "left":
        left = [r for r in requests if r <= arm]
        right = [r for r in requests if r > arm]

        for r in reversed(left):
            sequence.append(r)
            total_movement += abs(arm - r)
            arm = r

        for r in right:
            sequence.append(r)
            total_movement += abs(arm - r)
            arm = r

    return {"sequence": sequence, "total_movement": total_movement}

def clook(arm, requests):
    requests = sorted(requests)
    sequence = []
    total_movement = 0

    left = [r for r in requests if r <= arm]
    right = [r for r in requests if r > arm]

    for r in right:
        sequence.append(r)
        total_movement += abs(arm - r)
        arm = r

    for r in left:
        sequence.append(r)
        total_movement += abs(arm - r)
        arm = r

    return {"sequence": sequence, "total_movement": total_movement}
