import sublime, sublime_plugin, send2trash

class DeleteCurrentFileCommand(sublime_plugin.TextCommand):
  def run(self, edit):        
    f = self.view.file_name()
    if (f is None):
      return

    send2trash.send2trash(f)
    self.view.window().run_command('close')