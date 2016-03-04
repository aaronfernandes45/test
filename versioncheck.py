import sublime, sublime_plugin
import os
import sys

current_working_directory = os.getcwd() 																			#current working directory
sys.path.append("/home/rohit/.config/sublime-text-3/Packages/User" + "/lib/python3.4/site-packages")		#Tells sublime python interpreter where modules are store

from git import *

def repo_check(temp_dir):
		global repo			
		repo = Repo(temp_dir,search_parent_directories=True)
		if (repo):
			return True
		else:
			sublime.message_dialog("No")

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
        	sublime.message_dialog("Yes")
        else:
        	sublime.message_dialog("No")


class VersionCommand(sublime_plugin.EventListener):

	def on_load(self,view):
		temp_dir = str(view.file_name())
		f = open(temp_dir, 'r')
		if(repo_check(temp_dir)):
			find('a.txt',os.getcwd())
			


