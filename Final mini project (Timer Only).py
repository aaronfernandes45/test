
import sublime, sublime_plugin
import os
import sys

current_working_directory = os.getcwd() 																			#current working directory 
sys.path.append(current_working_directory + "/lib/python3.4/site-packages")		#Tells sublime python interpreter where modules are store

from git import *	

#some global variables																														#imports all from module git, because exceptions file needs to be imported
counter123 = 0

counter = 1
repo = Repo("/home/kahlil/TestingGit")

class UserinputCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#temp_dir = "/home/kahlil/TestingGit"
		#join = os.path.join
		sublime.message_dialog("control is here")
		self.view.window().show_input_panel("Push after number of commits", "Enter number here", self.on_done, None, None)																										#creates a git.Repo object to represent your repository.
		
	def on_done(self, user_input):
		sublime.message_dialog("Push after "+ user_input + " commits")
		global commit_before_push
		commit_before_push = int(user_input)


class GitfunctionsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		
		#join = os.path.join																											#creates a git.Repo object to represent your repository.
		temp_dir = "/home/kahlil/TestingGit"

		def repo_check(temp_dir):																									#code checks for .git in the folder	
			try :		
				global repo								
				repo = Repo(temp_dir)
				#self.view.insert(edit, 0, str(repo))
			except InvalidGitRepositoryError :																			#exception handled when .git is not found
					forwd_slash_index = temp_dir.rfind('/', 0, len(temp_dir))   				#finds index of last forward slash

					#self.view.insert(edit, 0, str(forwd_slash_index))
					
					temp_dir = temp_dir[0:forwd_slash_index]														#goes up one file level
					
					#self.view.insert(edit, 0, temp_dir)
					
					if forwd_slash_index == 0 :																					#if file not versioned by git
						sublime.message_dialog("No git repo found")
						global counter
						counter = 0
						
					else :																															#recursive call to repo_check with upper file level
						repo_check(temp_dir)

class myOpener(sublime_plugin.EventListener):		

	def on_post_save(self,view):
		global counter
		if counter == 1:
			global repo
			sublime.message_dialog("on_post_save")
			sublime.message_dialog(str(repo.git.status()))
			#sublime.message_dialog("You have saved the file")

			sublime.message_dialog(str(repo.git.add( '--all' )))
			sublime.message_dialog(str(repo.git.commit( m='committed all' )))

			#sublime.message_dialog("and now it has been committed")
			sublime.message_dialog(str(repo.git.status()))

			def push_repo():
				repo = Repo("/home/kahlil/TestingGit")
				o = repo.remotes.origin
				o.pull()	
				o.push()
				sublime.message_dialog("Push_repo")

			global counter123
			counter123 += 1 
			if counter123 == commit_before_push :
				counter123 =0
				push_repo()
				

		


		repo_check(temp_dir)													#function call to repo_check
		
		#sublime.set_timeout(on_post_save, 5000)

