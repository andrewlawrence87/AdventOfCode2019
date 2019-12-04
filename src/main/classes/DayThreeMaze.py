class DayThreeMaze:
    grid = []
    starting_position = [0, 0]
    position = [0, 0]
    crossover_points = []

    def __init__(self, size, starting_position):
        self.grid = [[int(0) for x in range(size)] for y in range(size)]
        self.starting_position = starting_position.copy()
        self.position = starting_position.copy()

    def move_right(self, no_moves):
        for k in range(0, no_moves):
            self.position[1] += 1
            self.move()

    def move_down(self, no_moves):
        for k in range(0, no_moves):
            self.position[0] += 1
            self.move()

    def move_up(self, no_moves):
        for k in range(0, no_moves):
            self.position[0] += -1
            self.move()

    def move_left(self, no_moves):
        for k in range(0, no_moves):
            self.position[1] += -1
            self.move()

    def move(self):
        self.grid[self.position[0]][self.position[1]] += 1
        if self.grid[self.position[0]][self.position[1]] > 1:
            self.crossover_points.append(self.position)

    def back_to_start(self):
        self.position = self.starting_position.copy()

    def calculate_closest_crossover(self):
        closest_distance = []
        for x, y in self.crossover_points:
            closest_distance.append(x - self.starting_position[0] + y - self.starting_position[1])
            print(min(closest_distance))
