class Task:
    id = ''
    runtime = 0.0
    input_files = list()
    output_files = list()
    predecessor_tasks = list()
    successor_tasks = list()

    def __init__(self, id, runtime):
        self.id = id
        self.runtime = runtime
        self.input_files = list()
        self.output_files = list()
        self.predecessor_tasks = list()
        self.successor_tasks = list()

    def add_input_file(self, file):
        self.input_files.append(file)

    def add_output_file(self, file):
        self.output_files.append(file)

    def add_predecessor_task(self, task):
        self.predecessor_tasks.append(task)

    def add_successor_task(self, task):
        self.successor_tasks.append(task)
