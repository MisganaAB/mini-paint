from OpenGL.GL import *
from shapes.shape import Shape


class Polygon(Shape):

    def __init__(self, color=(1.0, 1.0, 1.0), filled=False):
        super().__init__(color)
        self.closed = False
        self.filled = filled   # outline by default; set True for a flat fill

    def add_vertex(self, x, y):
        if not self.closed:
            self.vertices.append((x, y))

    def close_polygon(self):
        """Seals the shape. Needs at least 3 points to actually be a
        polygon — quietly does nothing otherwise so a stray Enter key
        press can't leave the shape in a broken half-closed state."""
        if len(self.vertices) >= 3:
            self.closed = True

    def draw(self):
        if len(self.vertices) < 2:
            return
        self._set_draw_color()
        if self.closed and self.filled:
            glBegin(GL_POLYGON)
        elif self.closed:
            glBegin(GL_LINE_LOOP)
        else:
            glLineWidth(self.line_width)
            glBegin(GL_LINE_STRIP)
        for (x, y) in self.vertices:
            glVertex2f(x, y)
        glEnd()

    def contains_point(self, x, y, tolerance=6.0):
        if not self.closed or len(self.vertices) < 3:
            # not closed yet — fall back to "near an edge" like Polyline
            for i in range(len(self.vertices) - 1):
                ax, ay = self.vertices[i]
                bx, by = self.vertices[i + 1]
                if self._distance_point_to_segment(x, y, ax, ay, bx, by) <= tolerance:
                    return True
            return False

        # closed: standard ray-casting point-in-polygon test
        inside = False
        n = len(self.vertices)
        j = n - 1
        for i in range(n):
            xi, yi = self.vertices[i]
            xj, yj = self.vertices[j]
            if (yi > y) != (yj > y):
                x_intersect = (xj - xi) * (y - yi) / (yj - yi) + xi
                if x < x_intersect:
                    inside = not inside
            j = i
        return inside

    def get_vertices(self):
        return list(self.vertices)