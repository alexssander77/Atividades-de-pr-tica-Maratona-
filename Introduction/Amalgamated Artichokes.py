import math


def price_at_time(t, P, A, B, C, D):
    return P * (math.sin(A * t + B) + math.cos(C * t + D) + 2)


P, A, B, C, D, N = map(int, input().split())


max_decline = 0.0
max_price = price_at_time(1, P, A, B, C, D)


for t in range(2, N+1):
    current_price = price_at_time(t, P, A, B, C, D)

    max_decline = max(max_decline, max_price - current_price)

    max_price = max(max_price, current_price)


if max_decline < 1e-6:
    print("0.00")
else:
    print(f"{max_decline:.9f}".rstrip('0').rstrip('.'))