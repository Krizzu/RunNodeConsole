import sublime
import sublime_plugin
import subprocess


class RunNodeConsoleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.getcurrentfile()

	"""Getting a file path to current open file. If it is not .js file, returns nothing"""
	def getcurrentfile(self):
		filepath = self.view.file_name()

		isvalid = filepath.find('.js')

		if not os.path.isfile(filepath):
			print('Please press F5 with a proper view')
			return 
		elif isalid == -1: #if .js extension not found
			print('Please press F5 with open .js file')
			return
		else:
			dirname = os.path.dirname(filepath)
			filename = os.path.basename(filepath)

			#Run 
			self.runnode(filename, dirname)

	def runnode(self, filename, directory):

		filename = os.path.join(directory,filename);

		subprocess.Popen(['node', '-r',filename])