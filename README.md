# Baba Robot

# 1 Introduction

A solution robot for the &quot;Baba Is You&quot; game.

I created a Python robot that allows recording and playback of the solutions in a manner similar with a keyboard macro. As the software is meant to be running in background during the game, the user interaction is based on audio messages created with speech synthesis.

# 2 How to install

Clone the repository:``git clone https://github.com/RazvanPorojan/BabaRecord.git``

Downoad pyHook from [https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook) for your OS (mine is pyHook‑1.5.1‑cp37‑cp37m‑win\_amd64.whl – for Python 3.7)

``pip install C:\Users\xxx\Downloads\pyHook-1.5.1-cp37-cp37m-win\_amd64.whl`` (if there are issues use this article [https://www.programmerall.com/article/76881747017/](https://www.programmerall.com/article/76881747017/) )

``pip install pyttsx3``

# 3 How to use
launch with ``python baba_record.py``

The robot is controlled during the game with the following keys:

**i** = Input Level Code (allows to select the level for which you want to record or demo).

The level code is formed by two letters followed by two digits (e.g. LA03 for lake-03). These are the available codes:

- LA:lake
- IS:island
- FO:forest
- RU:ruin
- CA:cavern
- SP:space
- CH:chasm
- FA:fall
- GA:garden
- MO:mountain
- QU:question
- DE:depths
- AB:abc
- ME:meta

**\\** = Starts a fresh new solution recording.

**]** = Pauses the recording (during recording)

**[** = Continues the recording from where it was paused.

**;** = Starts playback of the current recording (recording must be paused)

**o** = Pauses the playback of the current recording (during playback)

**t** = Resets the playback of the current recording

**s** = Saves the current recording (name set via Input Level Code – see key &quot;I&quot;)

**l** = Loads a recording for the current level (name set via Input Level Code – see key &quot;I&quot;)

**z** = Undoes the action in the game but also in the recording

**`** = Stops listening to keys (pause program)

**q** = Quits program

**-** = Decreases playback speed (experimental feature)

**+** = Increases playback speed (experimental feature)

In order to correctly record the keystrokes the Input Repeat Delay must set to minimum (this is because the software doesn&#39;t record correctly hold on keys).

![alt text](https://github.com/RazvanPorojan/BabaRecord/blob/main/pics/keyword%20setting.PNG?raw=true)


There are already many solutions recorded in the _/levels_ subfolder of the project.

In order to playback an existing solution:

1. Recording and playing should be stopped.
2. Press &quot;i&quot; to input level name.
3. Input the four characters code as explained above (e.g. LA01 – for Lake 1, &quot;Icy Waters&quot;) – you will get an audio message with the level name.
4. Press &quot;l&quot; to load the level (you will get an audio confirmation or an error).
5. Press &quot;;&quot; to start the playback.
6. Press any other key (e.g. &quot;c&quot;) to advance the playback. Please note that holding the key will advance the playback faster but will also create a &quot;buffer effect&quot; of &quot;inertia&quot;. (working to fix this).
7. When the playback is over, you will hear a short beep.

In order to record a new solution:

1. Recording and playing should be stopped.
2. Press &quot;i&quot; to input level name.
3. Input the four characters code as explained above (e.g. LA01 – for Lake 1, &quot;Icy Waters&quot;) – you will get an audio message with the level name
4. Press &quot;\&quot; to start a fresh recording.
5. Play the game as usual without holding any key, however. If you do a mistake you can use Undo (&quot;Z&quot; key). The last action will be undone in recording as well.
6. Press &quot;]&quot; to stop the recording.
7. Press &quot;r&quot; to reset the level.
8. Press &quot;;&quot; to playback and verify the current recording.
9. If the recording is fine, press &quot;s&quot; to save it.

You can continue a partial recording by pressing &quot;[&quot; after a paused recording or a playback.

# 4 Known Issues

Cannot correctly record hold keys. Please set delay to 0 as explained above in order to prevent &quot;accidental holds&quot;

Keyboard events are disabled during audio messages. Please wait for audio messages to finish.

&quot;Inertia&quot; effect during playback. Please don&#39;t keep a key pressed too long during playback if you want to control the playback.

Although the main UI is based an audio, the console will display debug info like below:
```
Launched
Enter level code
LA01
Level input done
lake-01 Level name set
lake-01 loaded
Playback 1 started
```
