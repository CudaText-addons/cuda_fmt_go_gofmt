import os
import subprocess

def run(app, text):
    enc = 'utf-8'
    if os.name == 'nt':
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
        p = subprocess.Popen([app],
          startupinfo=startupinfo,
          stdout=subprocess.PIPE,
          stdin=subprocess.PIPE,
          stderr=subprocess.PIPE)
    else:
        p = subprocess.Popen([app],
          stdout=subprocess.PIPE,
          stdin=subprocess.PIPE,
          stderr=subprocess.PIPE)

    stdout, stderr = p.communicate(text.encode(enc))
    if stdout:
        return stdout.decode(enc)
    else:
        raise Exception('Error:\n' + stderr.decode(enc))

def gofmt(text):
    return run('gofmt', text)

def goimports(text):
    return run('goimports', text)

def goreturns(text):
    return run('goreturns', text)
