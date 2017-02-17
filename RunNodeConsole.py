import sublime
import sublime_plugin
import subprocess
import os
import sys

class RunNodeConsoleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.process = None
		self.file = self.getcurrentfile()
		self.os = self.getosname()

		if self.file:
			self.runnode(self.file)

		

	def getosname(self):
		os = sys.platform.lower()
		if os=='win32' or os=='cygwin':
			return 'windows'
		elif os=='linux':
			return 'linux'
		elif os=='darwin':
			return 'osx'

	"""Getting a file path to current open file. If it is not .js file, returns nothing"""
	def getcurrentfile(self):
		filepath = self.view.file_name()

		isvalid = filepath.find('.js')

		if not os.path.isfile(filepath):
			print('Please press F5 with a proper view')
			return 
		elif isvalid == -1: #if .js extension not found
			print('Please press F5 with open .js file')
			return
		else:
			file = os.path.join(os.path.dirname(filepath),os.path.basename(filepath))
			#Run 
			return file

	def runnode(self, filename):

		self.process = subprocess.Popen(['node', '-r',filename])
		print('process pid:', self.process.pid)
