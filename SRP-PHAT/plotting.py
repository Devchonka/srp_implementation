import time

from bokeh import plotting
from bokeh.models import renderers
import numpy

import colormaps

TOOLS='resize,pan,wheel_zoom,box_zoom,reset,tap,previewsave,box_select,poly_select,lasso_select'


def values_to_colors(values, max_val=None):
  if max_val is None:
    max_val = max(values)
  values = numpy.array(values)
  normalized_vals = values / float(max_val)
  array_colors = colormaps.viridis(normalized_vals) * 255
  colors = []
  for color in array_colors:
    colors.append('#%02x%02x%02x' % (round(color[0]), round(color[1]), round(color[2])))
  return colors


class DynamicScatterPlotter(object):
  def __init__(self, title='mmm', colormap=None, default_radius=0.1):
    self.default_radius = default_radius

    plotting.output_server(title)
    self._plot = plotting.figure(title=title, tools=TOOLS)
    self._plot.scatter(x=[], y=[], fill_color=[], radius=[], line_color=None)
    plotting.show(self._plot)
    self._data_source = self._plot.select(
        dict(type=renderers.GlyphRenderer))[0].data_source

  def update(self, x, y, z=None, radii=None, norm_val=None):
    if radii is None:
      radii = numpy.ones(len(x)) * self.default_radius
    if z is not None:
      self._data_source.data['fill_color'] = values_to_colors(z, max_val=norm_val)
    self._data_source.data['radius'] = radii
    self._data_source.data['x'] = x
    self._data_source.data['y'] = y
    self._data_source._dirty = True
    plotting.cursession().store_objects(self._data_source)



def main():
  scatter_plotter = DynamicScatterPlotter()
  while True:
    scatter_plotter.update([-0.5, 0, 0.5], [0, 0, 0], z=[0, 0.5, 1])
    time.sleep(0.1)


if __name__ == '__main__':
  main()