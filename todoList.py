class TodoList: 
	def __init__(self, file_name):
		self.file_name = file_name
		self.tasks = self.load_tasks_from_file()

	def load_tasks_from_file(self):
		file = open(self.file_name, 'r')
		tasks = file.readlines()
		return tasks

	def list_tasks(self):
		for index, task in enumerate(self.tasks, start=1):
			print('{}. {}'.format(index, task))

	def write_to_file():
		with open(self.file_name, 'w') as file:
			for task in self.tasks:
				file.write('{}\n'.format(task))

	def add_list(self, task):
		self.tasks.append(task)
		self.write_to_file()

	def remove_task(self, task_index):
		try:
			print('Removing task: {}'.format(self.tasks[task_index-1]))
			del(self.tasks[task_index-1])
			self.write_to_file()
		except IndexError:
			print('There is no task with the index number entered. Check again.')
			todo_help()

def todo_help():
	print()
	print('To-do List')
	print('* Create new task: [todo TASK]')
	print('* Remove a task that is done: [done INDEX]')
	print('* List the tasks: [list]')
	print('* Help: [help]')
	print('* Exit app: [quit]')
	print()

def start_app():
	todoList = TodoList('todoList.txt')

	while True:
		todo_help()
		cmd_input = input('Enter cmd: ')
		cmd = cmd_input.split(' ', 1)[0]
		if cmd == 'list':
			todoList.list_tasks()
		elif cmd == 'done':
			todoList.remove_task(cmd_input.split(' ', 1)[1])
		elif cmd == 'todo':
			todoList.add_list(cmd_input.split(' ', 1)[1])
		elif cmd == 'help':
			todo_help()
		elif cmd == 'quit':
			break
		else:
			print('Invalid value entered. Please try again.')
			todo_help()


start_app()
