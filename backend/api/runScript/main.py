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
    command = 'python ' + lang + '.py ' + inputFile
    print("=="*50)
    print(command)
    print (str(langDir/lang))
    print("==" * 50)
    try:
        output = runCommandCMD(directory=langDir/lang, command=command, timeout=100)
    except:
        return ("yoooooo!")
    outputDict = {'stdout': str(output[0]), 'stderr': str(output[1])}
    return jsonify(outputDict)
