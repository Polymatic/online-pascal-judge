import psutil
import shutil
from subprocess import Popen, PIPE, TimeoutExpired


def kill(processID):
    process = psutil.Process(processID)
    for childProcess in process.children(recursive=True):
        childProcess.kill()
    process.kill()


def runCommandCMD(directory, timeout, command):
    # try:
    #     f = open(self.filePath)
    # except IOError as e:
    #     print('Error came while opening the text file: ', e)
    #     return(False)
    # else:
    #     f.close()
    process = Popen(command, shell=True,cwd=directory, stdout=PIPE, stderr=PIPE)

    try:
        output = process.communicate(timeout=timeout)
        print('function check', output)
    except TimeoutExpired:
        print('Entered the timeout condition')
        kill(process.pid)
        return False
    except OSError:
        kill(process.pid)
        return False
    else:
        return output
