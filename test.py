import matplotlib.pyplot as plt
import networkx

import chinese_postman_lib as cpl
g = cpl.make_graph()
eulerian_graph = cpl.add_edges_for_euler(g)
networkx.draw(eulerian_graph)
plt.show()
