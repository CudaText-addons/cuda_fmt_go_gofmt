import os
import subprocess

MSG_CANNOT_RUN = "Cannot run 'gofmt'. Make sure it's in your PATH."

def do_format(text):

    enc = 'utf-8'
    if os.name == 'nt':
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
        try:
            p = subprocess.Popen(['gofmt'], 
              startupinfo=startupinfo, 
              stdout=subprocess.PIPE, 
              stdin=subprocess.PIPE, 
              stderr=subprocess.PIPE)
        except OSError:
            raise Exception(MSG_CANNOT_RUN)
    else:
        try:
            p = subprocess.Popen(['gofmt'], 
              stdout=subprocess.PIPE, 
              stdin=subprocess.PIPE, 
              stderr=subprocess.PIPE)
        except OSError:
            raise Exception(MSG_CANNOT_RUN)
    
    stdout, stderr = p.communicate(text.encode(enc))
    if stdout:
        return stdout.decode(enc)
    else:
        raise Exception('Error:\n' + stderr.decode(enc))
