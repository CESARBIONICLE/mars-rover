def check_obstacle(func):
    def wrapper(self, *args, **kwargs):
        new_coordinates = func(self, *args, **kwargs)
        if not self.is_obstacle(new_coordinates):
            self.coordinates = new_coordinates
        else:
            self.avoid_obstacle(new_coordinates)
    return wrapper
