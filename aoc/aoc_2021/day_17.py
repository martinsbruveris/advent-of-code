import re


def find_interval(v_init, p_min, p_max, j_max, axis):
    """Find step interval when shot with given v_init will be inside (p_min, p_max)."""
    j, p, v = 0, 0, v_init
    j_in, j_out = None, None
    while p <= p_max and j <= j_max:
        j += 1
        if p < p_min <= p + v <= p_max:
            j_in = j  # Note that we already incremented j
        if p_min <= p <= p_max < p + v:
            j_out = j - 1  # The step before the increment is the last one inside
        p += v
        v = max(v - 1, 0) if axis == "x" else v + 1
    j_out = j_out or j_max
    return (j_in, j_out) if j_in else None


def main(data, part):
    x_min, x_max, y_min, y_max = map(int, re.findall(r"-?\d+", data))
    y_min, y_max = -y_max, -y_min  # We are shooting up instead of down

    # Find all possible initial y velocities and associated steps inside the target
    vy_steps = {}
    for vy_init in range(-y_max, y_max + 1):
        # 2*y_max+1 is a heuristic upper bound for maximum number of steps to search
        # For given vy, we move vy steps down, before moving vy steps to reach y=0
        # again and then one step towards the target. Not 100% sure about this one, but
        # setting it to 3*y_max should be safe.
        steps = find_interval(vy_init, y_min, y_max, 3 * y_max, "y")
        if steps is not None:
            vy_steps[vy_init] = steps
    max_steps = max(s[1] for s in vy_steps.values())  # To constrain search for vx_init

    vx_steps = {}
    for vx_init in range(0, x_max + 1):
        steps = find_interval(vx_init, x_min, x_max, max_steps, "x")
        if steps is not None:
            vx_steps[vx_init] = steps

    # All initial trajectories are those where x and y steps inside target overlap.
    trajectories = []
    for vx, xs in vx_steps.items():
        for vy, ys in vy_steps.items():
            if xs[0] <= ys[1] and ys[0] <= xs[1]:
                trajectories.append((vx, vy))

    # Min rather than max because we changed signs for y
    vy_max = min(trajectories, key=lambda p: p[1])[1]
    y_high = (abs(vy_max) ** 2 + abs(vy_max)) // 2
    return y_high if part == "a" else len(trajectories)
