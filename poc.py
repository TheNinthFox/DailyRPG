import click
import random
import datetime
from enum import Enum


class TaskState(Enum):
    DAILY = 0,
    PERMANENT = 1,
    COMPLETABLE = 2,


class Task:
    def __init__(self, name, state: TaskState):
        self.name = name
        self.state = state


class Project:
    def __init__(self, name, daily_count):
        self.name = name
        self.daily_count = daily_count
        self.tasks = []

    def get_daily_tasks(self) -> []:
        daily_tasks = []
        for task in self.tasks:  # type: Task
            if task.state == TaskState.DAILY:
                daily_tasks.append(task)

        tasks = random.sample(daily_tasks, self.daily_count)
        return tasks

    def get_permanent_tasks(self) -> []:
        permanent_tasks = []
        for task in self.tasks:  # type: Task
            if task.state == TaskState.PERMANENT:
                permanent_tasks.append(task)

        return permanent_tasks

    def get_completable_tasks(self) -> []:
        completable_tasks = []
        for task in self.tasks:  # type: Task
            if task.state == TaskState.COMPLETABLE:
                completable_tasks.append(task)

        return completable_tasks

    def print_tasks(self, state: TaskState):
        names = {
            TaskState.PERMANENT  : 'PERMANENT',
            TaskState.COMPLETABLE: 'COMPLETABLE',
            TaskState.DAILY      : 'DAILY'
        }

        if state == TaskState.PERMANENT:
            tasks = self.get_permanent_tasks()
        elif state == TaskState.COMPLETABLE:
            tasks = self.get_completable_tasks()
        else:
            tasks = self.get_daily_tasks()

        for task in tasks:  # type: Task
            print("[{}] {}".format(names[state], task.name))

    def print_all_tasks(self):
        self.print_tasks(TaskState.PERMANENT)
        self.print_tasks(TaskState.COMPLETABLE)
        self.print_tasks(TaskState.DAILY)


def create_projects():
    projects = {}

    # DRAWING
    drawing = Project('Drawing', 1)
    drawing.tasks = [
        # Permanent - Have to do each day
        Task('Draw at least 5 minutes a day.', TaskState.PERMANENT),

        # Completable - Can choose to do (and combine with other tasks if applicable)
        Task('Read Vilppu\'s Drawing Manual and copy the pictures', TaskState.COMPLETABLE),
        Task('Draw a full-fledged (colored) fox avatar for yourself', TaskState.COMPLETABLE),

        # Daily - Random daily tasks to choose from
        Task('Draw a fox', TaskState.DAILY),
        Task('Draw a wolf', TaskState.DAILY),
        Task('Draw a cat', TaskState.DAILY),
        Task('Draw a self-portrait', TaskState.DAILY),
        Task('Draw scenery', TaskState.DAILY),
        Task('Read 10 pages of Vilppu\'s Drawing Manual and copy the pictures', TaskState.DAILY),
    ]
    projects['drawing'] = drawing

    # GUITAR
    guitar = Project('Guitar', 1)
    guitar.tasks = [
        # Permanent
        Task('Tune the guitar', TaskState.PERMANENT),
        Task('Play with a metronome.', TaskState.PERMANENT),
        Task('Play the guitar for at least 5 minutes a day.', TaskState.PERMANENT),

        # Completable
        Task('Learn the fretboard notes.', TaskState.COMPLETABLE),
        Task('Learn the song "Asgore".', TaskState.COMPLETABLE),
        Task('Learn the song "City of Stars".', TaskState.COMPLETABLE),
        Task('Learn improvisation with "Blue Bossa".', TaskState.COMPLETABLE),

        # Daily
        Task('Learn all "A"-notes on the fretboard.', TaskState.DAILY),
        Task('Learn all "B"-notes on the fretboard.', TaskState.DAILY),
        Task('Learn all "C"-notes on the fretboard.', TaskState.DAILY),
        Task('Learn all "D"-notes on the fretboard.', TaskState.DAILY),
        Task('Learn all "E"-notes on the fretboard.', TaskState.DAILY),
        Task('Learn all "F"-notes on the fretboard.', TaskState.DAILY),
        Task('Learn all "G"-notes on the fretboard.', TaskState.DAILY),
        Task('Continue learning a song.', TaskState.DAILY),
        Task('Work on your accuracy (play slooooowly).', TaskState.DAILY),
        Task('Work on your speed.', TaskState.DAILY),
    ]
    projects['guitar'] = guitar

    # DailyRPG
    daily_rpg = Project('DailyRPG', 1)
    daily_rpg.tasks = [
        # Permanent
        Task('Work at least 5 minutes a day on the project.', TaskState.PERMANENT),

        # Completable
        Task('Implement configuration for the environments (production, development).', TaskState.COMPLETABLE),
        Task('Implement CRUD for models.', TaskState.COMPLETABLE),
        Task('Finish model-design.', TaskState.COMPLETABLE),
        Task('Implement CLI controls.', TaskState.COMPLETABLE),
        Task('Implement Kivy UI.', TaskState.COMPLETABLE),
        Task('Implement NCurses UI.', TaskState.COMPLETABLE),
        Task('Settle on a DI/IOC solution.', TaskState.COMPLETABLE),

        # Daily
        Task('Choose a completable task to work on.', TaskState.DAILY)
    ]
    projects['dailyrpg'] = daily_rpg

    return projects


projects = create_projects()


def handle_task(project: Project, task: str):
    print("\nProject: {}".format(project.name))
    if task == 'all':
        project.print_all_tasks()
    elif task == 'permanent':
        project.print_tasks(TaskState.PERMANENT)
    elif task == 'completable':
        project.print_tasks(TaskState.COMPLETABLE)
    elif task == 'daily':
        project.print_tasks(TaskState.DAILY)
    else:
        print("Task Type '{}' not found.".format(task))


def handle_project(project, task):
    if project == 'all':
        for key in projects:  # type: Project
            handle_task(projects[key], task)
    elif project in projects:
        handle_task(projects[project], task)
    else:
        print("[ERROR] Project '{}' not found.".format(project))


@click.command()
@click.option('--project', '-p', help="The project to display.")
@click.option('--task', '-t', default='all', help="Which type of task to display.")
@click.option('--list', '-l', is_flag=True, help="Show a list of available projects.")
@click.option('--list_tasks', '-lt', is_flag=True, help="Show a list of available task types.")
def handle_cli(project, task, list, list_tasks):
    global projects

    if project:
        handle_project(project, task)
        return

    if list:
        keys = projects.keys()  # type: []
        for key in keys:
            print("Project: {}".format(key))

        print("Project: all")
        return

    if list_tasks:
        print("Task Types:\n - permanent\n - completable\n - daily")
        return

    handle_project('all', task)


if __name__ == '__main__':
    date = datetime.datetime.today().strftime('%d.%m.%Y')
    random.seed(date)

    handle_cli()
