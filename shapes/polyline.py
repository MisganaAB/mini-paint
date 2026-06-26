from OpenGL.GL import *
from shapes.shape import Shape


class Polyline(Shape):

    def __init__(self, color=(1.0, 1.0, 1.0)):
        super().__init__(color)

    def add_vertex(self, x, y):
        self.vertices.append((x, y))

    def draw(self):
        if len(self.vertices) < 2:
            return
        self._set_draw_color()
        glLineWidth(self.line_width)
        glBegin(GL_LINE_STRIP)
        for (x, y) in self.vertices:
            glVertex2f(x, y)
        glEnd()

    def contains_point(self, x, y, tolerance=6.0):
        if len(self.vertices) < 2:
            return False
        for i in range(len(self.vertices) - 1):
            ax, ay = self.vertices[i]
            bx, by = self.vertices[i + 1]
            if self._distance_point_to_segment(x, y, ax, ay, bx, by) <= tolerance:
                return True
        return False

    def get_vertices(self):
        return list(self.vertices)