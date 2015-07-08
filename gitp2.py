import sublime, sublime_plugin
import sys
import os
sys.path.append("/home/kahlil/.config/sublime-text-3/Packages/User/lib/python3.4/site-packages")
from git import Repo
import git
repo = git.Repo('/home/kahlil/test')

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		repo = git.Repo('/home/kahlil/test')
		#self.view.insert(edit, 0, str(repo.git.status()))
		#sublime.message_dialog(str(repo.git.status()))
		#sublime.message_dialog(str(repo.git.add( 'Bleh.py' )))
		#sublime.message_dialog(str(repo.git.commit( m='my commit message' )))
		# sublime.message_dialog(str(repo.git.status()))
		# empty_repo = Repo('/home/kahlil/test')
		# repo.git.push
		#os.system("gnome-terminal -e 'git push origin master'")
		sublime.message_dialog(str(repo.git.status()))
		# repo = git.Repo('/home/kahlil/test')
		# o = repo.remotes.origin
		# o.pull()

		# g = git.cmd.Git('/home/kahlil/test')

		# g.pull()
		# sublime.message_dialog(str(repo.git.status()))

# # add a file
# print repo.git.add( 'somefile' )
# # commit
# print repo.git.commit( m='my commit message' )
# # now we are one commit ahead
# print repo.git.status()

# bc:54:8b:58:41:61:4f:58:0b:4c:f7:e5:60:df:98:e2 kahlil29@gmail.com


class myOpener(sublime_plugin.EventListener):		
		def on_post_save(self,view):
			sublime.message_dialog(str(repo.git.status()))
			sublime.message_dialog("You have saved the file")

			sublime.message_dialog(str(repo.git.add( 'testinggit.py' )))
			sublime.message_dialog(str(repo.git.commit( m='REgular commit for every save' )))

			sublime.message_dialog("and now it has been committed")
			sublime.message_dialog(str(repo.git.status()))