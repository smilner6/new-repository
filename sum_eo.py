def sum_eo(n, t):
    if t == "e":
        even = 0
        for ev_val in range(0, n + 1, 2):
            even += ev_val
        return even
    elif t == "o":
        odd = 0
        for odd_val in range(1, n + 1, 2):
            odd += odd_val
        return odd


answer = sum_eo(10, "o")
print(answer)
