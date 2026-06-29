class SelectionManager:

    def __init__(self, shapes):
        self.shapes = shapes
        self.selected_shape = None


    def select_shape(self, x, y):

        self.clear_selection()

        # Start from newest shape
        for shape in reversed(self.shapes):

            if shape.contains_point(x, y):

                shape.selected = True
                self.selected_shape = shape

                return shape

        return None


    def clear_selection(self):

        if self.selected_shape:
            self.selected_shape.selected = False

        self.selected_shape = None


    def get_selected_shape(self):

        return self.selected_shape


    def is_selected(self):

        return self.selected_shape is not None