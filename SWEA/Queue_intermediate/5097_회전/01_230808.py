import sys
sys.stdin = open("5097_회전\sample_input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    print(f"#{test_case} {lst[M % N]}")
