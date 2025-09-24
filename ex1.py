def maximumPoints(k, costs):
    spent = 0
    max_cost = 0
    skipped = False
    points = 0
    for c in costs:
        spent += c
        max_cost = max(max_cost, c)
        if spent <= k:
            points += 1
        else:
            if not skipped and spent - max_cost <= k:
                skipped = True
                points += 1
            else:
                break
    return points
