import os
import subprocess
import cudatext as ct

def run(app, text):
    enc = 'utf-8'
    exe = app.split()
    #print('Go tool:', exe)
    if os.name == 'nt':
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
        p = subprocess.Popen(
          exe,
          startupinfo=startupinfo,
          stdout=subprocess.PIPE,
          stdin=subprocess.PIPE,
          stderr=subprocess.PIPE)
    else:
        p = subprocess.Popen(
          exe,
          stdout=subprocess.PIPE,
          stdin=subprocess.PIPE,
          stderr=subprocess.PIPE)

    stdout, stderr = p.communicate(text.encode(enc))
    if stdout:
        return stdout.decode(enc)
    else:
        raise Exception('Error: ' + stderr.decode(enc))

def gofmt(text):
    return run('gofmt', text)

def goimports(text):
    return run('goimports', text)

def goreturns(text):
    return run('goreturns', text)

def gofumpt(text):
    return run('gofumpt', text)

def golines(text):
    args = ct.ini_read('plugins.ini', 'arguments', 'golines', '')
    return run('golines '+args, text)
