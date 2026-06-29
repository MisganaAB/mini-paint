class ShapeManager:
    def __init__(self):
        # Stores all shapes using their ID as the key
        self.shapes = {}

        # Used to give each new shape a unique ID
        self.next_id = 1
    def add_shape(self, shape):
        # Add a new shape to the manager and assign it a unique ID.
        shape.id = self.next_id
        self.shapes[self.next_id] = shape
        self.next_id += 1

        return shape.id
    def remove_shape(self, shape_id):
        # Remove a shape if it exists. Returns True if removed successfully.
        if shape_id in self.shapes:
            del self.shapes[shape_id]
            return True

        return False

    def get_shape(self, shape_id):
        # Return none if shape don't exist
        return self.shapes.get(shape_id)
    def get_all_shapes(self):
        # Return every stored shape.
        return list(self.shapes.values())

    def draw_all(self):
        # Ask every shape to draw itself.
        for shape in self.shapes.values():
            shape.draw()