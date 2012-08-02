import sys, sublime, sublime_plugin
exe = __import__('exec')

class ExecCommand(exe.ExecCommand):
    def run(self, cmd = [], file_regex = "", line_regex = "", working_dir = "",
            encoding = "utf-8", env = {}, quiet = False, kill = False,
            # Catches "path" and "shell"
            **kwargs):

        build_output_to_tab = sublime.load_settings("Preferences.sublime-settings").get("build_output_to_tab", False)

        if build_output_to_tab:
            if hasattr(self, 'output_view') == False or -1 in self.window.get_view_index(self.output_view):
                self.output_view = self.window.new_file()
                self.output_view.set_name("Build")
                self.output_view.set_scratch(True)
            self.window.focus_view(self.output_view)

            if hasattr(self, 'proc'):
                exe.ExecCommand.append_data(self, self.proc, "\n\n\n")

        exe.ExecCommand.run(self, cmd, file_regex, line_regex, working_dir, encoding, env, quiet, kill , **kwargs)
