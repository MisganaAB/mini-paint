from OpenGL.GL import *


class Shape:

    def __init__(self, color=(1.0, 1.0, 1.0)):
        self.id = None              
        self.vertices = []          
        self.color = color          
        self.selected = False       
        self.line_width = 2.0

    # Every subclass MUST implement these three
    def draw(self):
        raise NotImplementedError("Subclasses must implement draw()")

    def contains_point(self, x, y, tolerance=6.0):
        raise NotImplementedError("Subclasses must implement contains_point()")

    def get_vertices(self):
        return list(self.vertices)

    # Shared behavior — every shape gets this for free, no need to
    # re-implement it in Line/Polyline/Polygon

    def get_centroid(self):
        """Average of all vertices. Handy for rotating/scaling a shape
        around its own center instead of around the world origin."""
        if not self.vertices:
            return (0.0, 0.0)
        cx = sum(v[0] for v in self.vertices) / len(self.vertices)
        cy = sum(v[1] for v in self.vertices) / len(self.vertices)
        return (cx, cy)

    def apply_transform(self, matrix):
        """
        Apply a 3x3 homogeneous transform matrix to every vertex.

        matrix is expected as a 3x3 row-major structure:
            [[m00, m01, m02],
             [m10, m11, m12],
             [m20, m21, m22]]

        We only need the top two rows since we're working in 2D
        homogeneous coordinates (x, y, 1).
        """
        new_vertices = []
        for (x, y) in self.vertices:
            new_x = matrix[0][0] * x + matrix[0][1] * y + matrix[0][2]
            new_y = matrix[1][0] * x + matrix[1][1] * y + matrix[1][2]
            new_vertices.append((new_x, new_y))
        self.vertices = new_vertices

    def _set_draw_color(self):
        """Selected shapes get a visual highlight automatically."""
        if self.selected:
            glColor3f(1.0, 1.0, 0.0)   # highlight color while selected
        else:
            glColor3f(*self.color)

    @staticmethod
    def _distance_point_to_segment(px, py, ax, ay, bx, by):
        """
        Shared helper for hit-testing: shortest distance from point P
        to the line segment AB. Used by Line and Polyline so the math
        only lives in one place.
        """
        abx, aby = bx - ax, by - ay
        apx, apy = px - ax, py - ay
        ab_len_sq = abx * abx + aby * aby

        if ab_len_sq == 0:
            # segment is actually a single point
            return ((px - ax) ** 2 + (py - ay) ** 2) ** 0.5

        # project P onto AB, clamped to the segment itself
        t = (apx * abx + apy * aby) / ab_len_sq
        t = max(0.0, min(1.0, t))

        closest_x = ax + t * abx
        closest_y = ay + t * aby
        return ((px - closest_x) ** 2 + (py - closest_y) ** 2) ** 0.5