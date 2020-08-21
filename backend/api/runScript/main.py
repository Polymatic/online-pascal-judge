from flask import Blueprint, request, Response, jsonify
from ..Utils import runCommandCMD
from pathlib import Path

run = Blueprint('run', __name__)
langDir = Path('langs').absolute()

@run.route('/', methods=["POST", "GET"])
def execute():
    incomingData = request.get_json()
    print(incomingData)
    lang = incomingData['language']
    inputFile = incomingData['script'] 
    # command = 'python ' + lang + '.py ' + inputFile
    sudoPass = 'mridmehu' #host sudo pass
    commandDocker = 'sudo docker run --rm pascal:python_slim python ' + 'interpreter' + '.py ' + inputFile
    print("=="*50)
    print(commandDocker)
    print (str(langDir/lang))
    print("==" * 50)
    try:
        output = runCommandCMD(directory=langDir/lang, command=commandDocker, timeout=100, sudoPass=sudoPass)
    except:
        return ("yoooooo!")
    outputDict = {'stdout': output[0], 'stderr': output[1]}
    return jsonify(outputDict)
