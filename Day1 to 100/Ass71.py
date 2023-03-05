def boast_count(scores):
    count = 0
    for i in range(len(scores)):
        less_than_equal = sum(x <= scores[i] for x in scores)
        greater_than = sum(x > scores[i] for x in scores)
        if less_than_equal > greater_than:
            count += 1
    return count

T = int(input(":"))
for _ in range(T):
    N = input(">")
    scores = list(map(int, input(":>").split()))
    print("Total score is:",boast_count(scores))
