class Task:
    __slots__ = 'name', '_performer', 'best_case', 'most_likely', 'worst_case', 'id'

    def __init__(self, name, best_case=0, most_likely=0, worst_case=0, performer='not assigned'):
        self.name = name
        self.best_case = best_case
        self.most_likely = most_likely
        self.worst_case = worst_case
        self._performer = performer
        self.id = id(self)

    def __str__(self):
        return self.name

    @property
    def performer(self):
        return self._performer

    @performer.setter
    def performer(self, performer):
        if type(performer) == str:
            self._performer = performer

    def weighted_average(self):
        return round((self.best_case + (4*self.most_likely) + self.worst_case)/6, 2)

    def standard_deviation(self):
        return round((self.worst_case - self.best_case)/6, 2)


class Project:
    PROJECT_LIST = list()

    @classmethod
    def projects(cls):
        return cls.PROJECT_LIST

    def __init__(self, name, *tasks):
        self.project_name = name
        self.tasks = list(tasks)
        Project.PROJECT_LIST.append(name)

    def __str__(self):
        return self.project_name

    def __len__(self):
        return len(self.tasks)

    def __iter__(self):
        return iter(self.tasks)

    def __contains__(self, name):
        return name in self.tasks

    def show_tasks(self):
        return self.tasks

    def get_by_name(self, name):
        for task in self.tasks:
            if name == task.name:
                return task
        print(f'Name {name} doesn`t exist in {self.project_name}')
        return None

    def delete_task(self, name):
        for task in self.tasks:
            if name == task.name:
                self.tasks.remove(task)

    def project_weighted_average(self):
        return round(sum(task.weighted_average() for task in self.tasks), 2)

    def project_standard_deviation(self):
        return round(pow(sum(pow(task.standard_deviation(), 2) for task in self.tasks), 0.5), 2)

    def confidence_interval(self):
        ci_min = int(self.project_weighted_average() - (2 * self.project_standard_deviation()))
        ci_max = int(self.project_weighted_average() + (2 * self.project_standard_deviation()))
        return f'Project`s 95% confidence interval: {ci_min} ... {ci_max} points'

if __name__ == "__main__":

    tasks = list()
    while True:
        name = str(input('Enter name of your task:\n'))
        estimates = tuple(map(int, input('Enter required estimates - '
                          'best_case, most_likely and worst_case (use space as delimiter):\n').split()))
        if len(estimates) == 3:
            tasks.append(Task(name, *estimates))
        next_task = input('Do you want to enter one more task: y/n?\n')
        if next_task not in ('yes', 'y'):
            break

    print('Weighted_average and standard_deviation for your tasks:')
    for task in tasks:
        print(f'\t Task: {task.name}, E: {task.weighted_average()}, SD: {task.standard_deviation()}')

    proj_name = input('Enter name for your project\n')
    project = Project(proj_name, *tasks)
    print(f'Project: {proj_name},\n\t weighted_average: {project.project_weighted_average()},\n\t '
          f'standard_deviation: {project.project_standard_deviation()},\n\t CI: {project.confidence_interval()}')

