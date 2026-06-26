"""
shapes/line.py

A single straight segment between exactly two points.

"""

from OpenGL.GL import *
from shapes.shape import Shape


class Line(Shape):

    def __init__(self, color=(1.0, 1.0, 1.0)):
        super().__init__(color)

    def add_point(self, x, y):
        """
        A Line only ever has a start point and an end point.
        - The first call sets the start point.
        - Every call after that replaces the end point — so dragging
          the mouse while drawing just means calling this repeatedly
          with the current cursor position.
        """
        if len(self.vertices) < 2:
            self.vertices.append((x, y))
        else:
            self.vertices[1] = (x, y)

    def draw(self):
        if len(self.vertices) < 2:
            return
        self._set_draw_color()
        glLineWidth(self.line_width)
        glBegin(GL_LINES)
        for (x, y) in self.vertices:
            glVertex2f(x, y)
        glEnd()

    def contains_point(self, x, y, tolerance=6.0):
        if len(self.vertices) < 2:
            return False
        (ax, ay), (bx, by) = self.vertices[0], self.vertices[1]
        return self._distance_point_to_segment(x, y, ax, ay, bx, by) <= tolerance

    def get_vertices(self):
        return list(self.vertices)