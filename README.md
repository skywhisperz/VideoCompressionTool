# VideoCompressionTool
A tool I decided to make since I got tired of writing the same FFmpeg command over and over again, so I decided to automate it.<br>

The sole and only purpose of this utility is compressing videos. I use Discord a lot and they added their stupid 10MB upload limit which basically isn't enough for any kind of decent quality video, and online compression tools cost money for some reason.<br><br>


**How to use?** <br>

Follow the instructions on the command prompt. It should be pretty straightforward. If you find any bugs please create an issue here in Github and I'll try to fix it.<br><br>


**Why to use?** <br>

You shouldn't. You should just learn how to use FFmpeg. It's a lot more flexible than whatever this is.<br><br>


**Do I have to install FFmpeg myself?** <br>
Yes. I even added a reminder at the beginning of the program.<br><br>


Download FFmpeg from [here](https://ffmpeg.org/download.html).<br><br>


# Set up

### Windows<br>
1.- Download and install Python and download FFmpeg. Place the downloaded FFmpeg binaries in a "general" folder like `C:\Program Files\FFmpeg` or something like that.<br><br>
2.- Open Windows search and search for "View advanced system settings"<br><br>
<img width="764" height="385" alt="image" src="https://github.com/user-attachments/assets/aa621053-a6ff-4046-b939-9a6cb9fd0040" />

3.- Click on the "Environment variables" button<br><br>
<img width="312" height="173" alt="image" src="https://github.com/user-attachments/assets/8b872c88-9cf2-427b-8c69-9a37c131f503" />

4.- Double click in the "Path" variable in the "System variables" menu<br><br>
<img width="582" height="236" alt="image" src="https://github.com/user-attachments/assets/032e0992-914f-4ebc-9141-cd755938e0c0" />

5.- Click on "New", and type in the place where FFmpeg's binaries are stored. Then, click OK.<br><br>
<img width="541" height="512" alt="image" src="https://github.com/user-attachments/assets/313eac97-bd4c-4d0c-9101-3f5eb2904458" /><br>

Afterwards, just close and reopen any terminal instances and run the script. If you followed the steps correctly, it should work properly now.

**You could also** just put the FFmpeg.exe binary in the same folder where the script is currently in. I'm not sure though, I haven't tested that yet

### macOS

**The script is coded for Windows. That means that the script may not work first try and you may need to adjust it so it works correctly on your computer. I'll make a macOS version soon.**<br><br>

1.- Download and install Python from the official Python website.<br><br>
2.- Install FFmpeg through Homebrew (`brew install ffmpeg`). If you do not have Homebrew, install it from [here](https://brew.sh/).<br><br>
3.- Run the script with `python3 VideoCompressionTool.py`, or `python3 main.py`.<br><br>
4.- Compress your videos idk
5.- Enjoy!

### Linux

Should be almost the same as with macOS, but instead of using Homebrew use your preferred package manager (for example, `apt`, `pacman`, `rpm`, etc.) to install Python and FFmpeg. You will need to adjust the script to work correctly on your computer. I don't have a Linux machine, so probably won't support it for a while. When I do get access to one, I'll try to port the script to Linux.<br><br>
