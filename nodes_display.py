# -*- coding: utf-8 -*-
"""
Created on Wed May 16 10:11:06 2018

@author: Administrator
"""

import networkx as nx
import matplotlib.pyplot as plt 
e=[]
for i in range(1,29):
    e.append((i, i+1))
e.pop(18)
U=[]
U1=[i for i in range(1,10)]
U2=[i for i in range(10,16)]
U3=[i for i in range(16,20)]
U1.extend([i for i in range(20, 25)])
U2.extend([i for i in range(25, 30)])
U.extend(U2)
U.extend(U3)
U.extend(U1)
G = nx.DiGraph()
#G = nx.path_graph([i for i in range(1,20)]) 
#nx.add_path(G, [i for i in range(20,30)])
G.add_nodes_from(U1, GU = 1)
G.add_nodes_from(U2, GU = 2)
G.add_nodes_from(U3, GU = 3)
G.add_edge(6, 20, link = 1)
G.add_edges_from(e, link = 0)

nx.draw(G, pos = nx.spectral_layout(G), with_labels = True)
plt.show()