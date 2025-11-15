import networkx as nx
import matplotlib.pyplot as plt

def input_matrix(R):
    for i in range(1, size+1):
        R[i][1:] = list(map(int,input(f"관계행렬의 {i}행을 입력하세요: ").split()))
    return R
def get_reflexivity(R):
    for i in range(1, size+1):
        if R[i][i] == 0:
            print("행렬이 반사성을 만족하지 않습니다.")
            return 0
    print("행렬이 반사성을 만족합니다.")
    return 1
def get_symmetry(R):
    for i in range(1, size+1):
        for j in range(1, size+1):
            if R[i][j] == 1:
                if R[j][i] == 0:
                    print("행렬이 대칭성을 만족하지 않습니다.")
                    return 0
    print("행렬이 대칭성을 만족합니다.")
    return 1
def get_transitivity(R):
    for k in range(1, size+1):
        for i in range(1, size+1):
            for j in range(1, size+1):
                if R[i][k] == 1 and R[k][j] == 1:
                    if R[i][j] == 0:
                        print("행렬이 추이성을 만족하지 않습니다.")
                        return 0
    print("행렬이 추이성을 만족합니다.")
    return 1
def get_equivalence_class(R):
    equivalence_class = [[] for i in range (size+1)]
    for i in range(1, size+1):
        for j in range(1, size+1):
            if R[i][j] == 1:
                equivalence_class[i].append(j)
    for i in range(1, size+1):
        print(f"원소 {i}의 동치류: {equivalence_class[i]}")
    return equivalence_class

def reflexive_closure(R):
    print("반사폐포 변환 전")
    for i in range(1, size+1):
        print(*R[i][1:])
    for i in range(1, size+1):
        if R[i][i] == 0:
            R[i][i] = 1
    print("반사폐포 변환 후")
    for i in range(1, size+1):
        print(*R[i][1:])
    return R

def symmetric_closure(R):
    print("대칭폐포 변환 전")
    for i in range(1, size+1):
        print(*R[i][1:])
    for i in range(1, size+1):
        for j in range(1, size+1):
            if R[i][j] == 1 and R[j][i] == 0:
                R[j][i] = 1
    print("대칭폐포 변환 후")
    for i in range(1, size+1):
        print(*R[i][1:])
    return R
def transitive_closure(R):
    print("추이폐포 변환 전")
    for i in range(1, size+1):
        print(*R[i][1:])
    for k in range(1, size+1):
        for i in range(1, size+1):
            for j in range(1, size+1):
                if R[i][k] == 1 and R[k][j] == 1:
                    R[i][j] = 1
    print("추이폐포 변환 후")
    for i in range(1, size+1):
        print(*R[i][1:])
    return R


def draw_digraph(R, unique_classes):
    G = nx.DiGraph()
    G.add_nodes_from(range(1, size + 1))

    edges = []
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            if R[i][j] == 1:
                edges.append((i, j))
    G.add_edges_from(edges)

    color_map = {}
    colors = plt.cm.get_cmap('viridis', len(unique_classes))

    for idx, cls_tuple in enumerate(unique_classes):
        for node in cls_tuple:
            color_map[node] = colors(idx)

    node_colors = [color_map.get(node, 'lightgray') for node in G.nodes()]

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, seed=42)

    nx.draw(
        G, pos,
        with_labels=True,
        labels={node: str(node) for node in G.nodes()},
        node_color=node_colors,
        node_size=1500,
        edge_color='dimgray',
        arrows=True,
        arrowsize=20,
        font_color='white',
        font_weight='bold',
        width=1.5
    )
    plt.title("최종 동치 관계 R의 유향 그래프 (동치류별 색상)", fontsize=16)
    plt.axis('off')
    plt.show()
size = 5
R = [[0] * (size+1) for _ in range(size+1)]
R = input_matrix(R)

while True:
    reflexivity, symmetry, transitivity = get_reflexivity(R), get_symmetry(R), get_transitivity(R)
    if reflexivity == 1 and symmetry == 1 and transitivity == 1:
        break
    print("관계 행렬이 동치류가 아닙니다. 폐포 변환을 수행합니다.")
    if reflexivity != 1:
        R = reflexive_closure(R)
    if symmetry != 1:
        R = symmetric_closure(R)
    if transitivity != 1:
        R = transitive_closure(R)
get_equivalence_class(R)
draw_digraph(R, get_equivalence_class(R))