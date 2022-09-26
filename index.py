import networkx as nx
from bokeh.models import Circle, MultiLine, HoverTool, BoxSelectTool, TapTool, NodesAndLinkedEdges, EdgesAndLinkedNodes
from bokeh.plotting import figure, from_networkx, show
from bokeh.palettes import Spectral4

G = nx.DiGraph()

distancias = open("database.txt", "r")
with distancias:
    for line in distancias:
        origem, destino, distancia = line.split()
        G.add_edge(origem, destino)

plot = figure(width=400, height=400, x_range=(-1.2, 1.2), y_range=(-1.2, 1.2),
              x_axis_location=None, y_axis_location=None, toolbar_location=None,
              title="Aeroportos do Brasil", background_fill_color="#efefef",
              tooltips="airport: @index")
plot.grid.grid_line_color = None

plot.add_tools(HoverTool(tooltips=None), TapTool(), BoxSelectTool())

graph_renderer = from_networkx(G, nx.spring_layout, scale=1, center=(0, 0))
graph_renderer.node_renderer.glyph = Circle(size=15, fill_color="plum")
graph_renderer.edge_renderer.glyph = MultiLine(line_color="grey", line_alpha=0.8, line_width=1.5)

graph_renderer.node_renderer.hover_glyph = Circle(size=15, fill_color=Spectral4[1])
graph_renderer.edge_renderer.hover_glyph = MultiLine(line_color=Spectral4[1], line_width=5)
graph_renderer.inspection_policy = NodesAndLinkedEdges()
graph_renderer.selection_policy = EdgesAndLinkedNodes()

plot.renderers.append(graph_renderer)

show(plot)
