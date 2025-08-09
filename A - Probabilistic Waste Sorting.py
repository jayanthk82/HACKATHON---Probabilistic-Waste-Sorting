
import sys
import math
from collections import defaultdict, deque

# =========================================================================
# STAGE 1: THE FOUNDATION
# =========================================================================

# --- Global Data ---
N, M, K = 0, 0, 0
positions = {}
prob = {}

# --- Geometric Utilities ---
def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0

def orientation(a, b, c):
    cross = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    return sign(cross)

def segments_intersect(p1, p2, q1, q2):
    if p1 == q1 or p1 == q2 or p2 == q1 or p2 == q2:
        return False
    if (max(p1[0], p2[0]) < min(q1[0], q2[0]) or
            max(q1[0], q2[0]) < min(p1[0], p2[0]) or
            max(p1[1], p2[1]) < min(q1[1], q2[1]) or
            max(q1[1], q2[1]) < min(p1[1], p2[1])):
        return False
    o1 = orientation(p1, p2, q1)
    o2 = orientation(p1, p2, q2)
    o3 = orientation(q1, q2, p1)
    o4 = orientation(q1, q2, p2)
    return (o1 * o2 < 0) and (o3 * o4 < 0)

# --- Scoring Utilities ---
def calculate_new_mixes(p_in, sorter_type_k):
    p_out1, p_out2 = [0.0] * N, [0.0] * N
    sorter_probs = prob[sorter_type_k]
    total_flow1 = sum(p_in[j] * sorter_probs[j] for j in range(N))
    total_flow2 = 1.0 - total_flow1
    if total_flow1 > 1e-9:
        p_out1 = [(p_in[j] * sorter_probs[j]) / total_flow1 for j in range(N)]
    if total_flow2 > 1e-9:
        p_out2 = [(p_in[j] * (1 - sorter_probs[j])) / total_flow2 for j in range(N)]
    return p_out1, p_out2, total_flow1, total_flow2

def calculate_gini_gain(p_in, p_out1, p_out2, flow1, flow2):
    def gini(p): return 1 - sum(pi**2 for pi in p)
    return gini(p_in) - (flow1 * gini(p_out1) + flow2 * gini(p_out2))

# --- Main Setup Function ---
def setup():
    global N, M, K, positions, prob
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    for i in range(N):
        positions[i] = tuple(map(int, input().split()))
    for i in range(M):
        positions[N + i] = tuple(map(int, input().split()))
    positions[-1] = (0, 5000)
    for i in range(K):
        prob[i] = list(map(float, input().split()))

# --- Placeholder for the Main Logic ---
def solve():
    print("Foundation is ready. Starting main algorithm...")
    # The rest of our code will go here.

# --- RUNNER ---
setup()
solve()