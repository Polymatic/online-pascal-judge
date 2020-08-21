import psutil
import shutil
from subprocess import Popen, PIPE, TimeoutExpired


def kill(processID):
    process = psutil.Process(processID)
    for childProcess in process.children(recursive=True):
        childProcess.kill()
    process.kill()


def runCommandCMD(directory, timeout, command, sudoPass=None):
    # try:
    #     f = open(self.filePath)
    # except IOError as e:
    #     print('Error came while opening the text file: ', e)
    #     return(False)
    # else:
    #     f.close()
    process = Popen(command, shell=True,cwd=directory, stdout=PIPE, stderr=PIPE, universal_newlines=True)

    try:
        if not sudoPass:
            sudo_prompt = p.communicate(sudoPass + '\n')[1]
        output = process.communicate(timeout=timeout)
        print('function output check =', output)
    except TimeoutExpired:
        print('Entered the timeout condition')
        kill(process.pid)
        return False
    except OSError:
        kill(process.pid)
        return False
    else:
        return output
