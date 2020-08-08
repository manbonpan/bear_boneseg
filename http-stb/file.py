Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
==== RESTART: D:\organinzing code is good\socket-wizadry\http-stb\Chunks.py ====

Warning (from warnings module):
  File "C:\Users\91898\AppData\Local\Programs\Python\Python38-32\lib\site-packages\pydub\utils.py", line 170
    warn("Couldn't find ffmpeg or avconv - defaulting to ffmpeg, but may not work", RuntimeWarning)
RuntimeWarning: Couldn't find ffmpeg or avconv - defaulting to ffmpeg, but may not work

Warning (from warnings module):
  File "C:\Users\91898\AppData\Local\Programs\Python\Python38-32\lib\site-packages\pydub\utils.py", line 198
    warn("Couldn't find ffprobe or avprobe - defaulting to ffprobe, but may not work", RuntimeWarning)
RuntimeWarning: Couldn't find ffprobe or avprobe - defaulting to ffprobe, but may not work
Traceback (most recent call last):
  File "D:\organinzing code is good\socket-wizadry\http-stb\Chunks.py", line 4, in <module>
    myaudio = AudioSegment.from_file("fir.mp3","mp3")
  File "C:\Users\91898\AppData\Local\Programs\Python\Python38-32\lib\site-packages\pydub\audio_segment.py", line 685, in from_file
    info = mediainfo_json(orig_file, read_ahead_limit=read_ahead_limit)
  File "C:\Users\91898\AppData\Local\Programs\Python\Python38-32\lib\site-packages\pydub\utils.py", line 274, in mediainfo_json
    res = Popen(command, stdin=stdin_parameter, stdout=PIPE, stderr=PIPE)
  File "C:\Users\91898\AppData\Local\Programs\Python\Python38-32\lib\subprocess.py", line 854, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "C:\Users\91898\AppData\Local\Programs\Python\Python38-32\lib\subprocess.py", line 1307, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
FileNotFoundError: [WinError 2] The system cannot find the file specified
>>> 