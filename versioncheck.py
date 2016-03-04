import sublime, sublime_plugin
import os
import sys
import glob

current_working_directory = os.getcwd() 																			#current working directory
sys.path.append("/home/kahlil/.config/sublime-text-3/Packages/User" + "/lib/python3.4/site-packages")		#Tells sublime python interpreter where modules are store

from git import *

def repo_check(temp_dir):
		try:
			global repo
			repo = Repo(temp_dir,search_parent_directories=True)
		except InvalidGitRepositoryError :
			sublime.message_dialog("Not git versioned")


def check_for_text_file(path_of_file):
	os.chdir(path_of_file)
	list_of_text_files = glob.glob("*.txt")
	print (list_of_text_files)
	if len(list_of_text_files) == 0:
		sublime.message_dialog("No '.txt' file found")
	else:
		sublime.message_dialog("txt file was found")

class VersionCommand(sublime_plugin.EventListener):

	def on_load(self,view):
		if(repo_check(view.file_name())):
			file_path = str(view.file_name())
			forwd_slash_index = file_path.rfind('/', 0, len(file_path))   				#finds index of last forward slash
			new_dir = file_path[0:forwd_slash_index]
			check_for_text_file(new_dir)
