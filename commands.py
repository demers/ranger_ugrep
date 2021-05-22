class ugrep_select(Command):
    """
    :ugrep_select

    Grep in files using ugrep.

    See: https://github.com/Genivia/ugrep
    """
    def execute(self):
        import subprocess
        if self.quantifier:
            # match only directories
            command="ugrep -i -Q"
        else:
            # match files and directories
            command="ugrep -i -Q"
        ugrep = self.fm.execute_command(command, stdout=subprocess.PIPE)
        stdout, stderr = ugrep.communicate()
        if ugrep.returncode == 0:
            ugrep_file = os.path.abspath(stdout.decode('utf-8').rstrip('\n'))
            ugrep_dir = os.path.dirname(ugrep_file)
            self.fm.cd(ugrep_dir)
            self.fm.select_file(ugrep_file)
