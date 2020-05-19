# pix

Graphical API to draw pixels on a grid.


## Example code

```python
import pix

width, height = 200, 200
graph = pix.create_graph(width, height, "#718ebe")
graph.show()

for i in range(width):
    for j in range(height):
        graph.set_color_rgb(i, j, 3 * [i / height])

```

## Contact

Bastien Laby

bastien.laby@gmail.com