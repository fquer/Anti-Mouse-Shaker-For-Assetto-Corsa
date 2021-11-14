import ac
import acsys
import subprocess

subprocess.call('taskkill /f /im explorer.exe')

def acMain(ac_version):
    return 'AntiShaker'

def acShutdown():
    subprocess.Popen('explorer.exe', stderr=subprocess.PIPE)