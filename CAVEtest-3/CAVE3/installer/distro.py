import subprocess

class DistroChecker:

    # checks the current linux distro
    def get_package_manager (self):
        # recieves the output containing the current distro
        ret = subprocess.run(['cat', '/etc/os-release'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # lower case xd
        output = ret.stdout.lower()
        # checks the output to see which distro is current and returns
        if ('debian' in output or 'ubuntu' in output):
            return 'apt'
        elif ('fedora' in output):
            return 'dnf'
        else:
            return 'pacman'