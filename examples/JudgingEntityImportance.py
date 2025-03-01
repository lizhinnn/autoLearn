import xml.etree.ElementTree as ET
from collections import Counter

def analyze_top_nodes():
    # 读取graphml文件
    tree = ET.parse('aNofigure0209/graph_chunk_entity_relation.graphml')
    root = tree.getroot()
    
    # 获取graphml命名空间
    ns = {'graphml': 'http://graphml.graphdrawing.org/xmlns'}
    
    # 创建节点连接计数器
    node_connections = Counter()
    
    # 创建边连接计数器
    # edge_connections = Counter()
    
    # 遍历所有边
    for edge in root.findall('.//graphml:edge', ns):
        # 获取源节点和目标节点
        source = edge.get('source').strip('"')
        target = edge.get('target').strip('"')
        
        # 增加节点的连接计数
        node_connections[source] += 1
        node_connections[target] += 1
        
        # 增加边的连接计数
        # edge_connections[(source, target)] += 1
    
    # 获取前10个最多连接的节点
    top_10_nodes = node_connections.most_common(30)
    
    # 获取前10个最多连接的边
    # top_10_edges = edge_connections.most_common(10)
    
    # 打印结果
    print("\n最常被引用的前20个节点:")
    print("-" * 50)
    print("节点名称 | 连接数量")
    print("-" * 50)
    for node, count in top_10_nodes:
        print(f"{node} | {count}")
    print("-" * 50)

    # print("\n最常被引用的前10个边:")
    # print("-" * 50)
    # print("边 | 连接数量")
    # print("-" * 50)
    # for (source, target), count in top_10_edges:
    #     print(f"{source} -> {target} | {count}")
    # print("-" * 50)

    # # 打印权重最高的边
    # if top_10_edges:
    #     highest_weight_edge = top_10_edges[0]
    #     print("\n权重最高的边:")
    #     print(f"{highest_weight_edge[0][0]} -> {highest_weight_edge[0][1]} | {highest_weight_edge[1]}")
    # print("-" * 50)

if __name__ == "__main__":
    analyze_top_nodes()
