# VideoCompressionTool
A tool I decided to make since I got tired of writing the same FFMPEG command over and over again, so I decided to automate it.<br>

The sole and only purpose of this utility is compressing videos. I use Discord a lot and they added their stupid 10MB upload limit which basically isn't enough for any kind of decent quality video, and online compression tools cost money for some reason.<br><br>


**How to use?** <br>

Follow the instructions on the command prompt. It should be pretty straightforward. If you find any bugs please create an issue here in Github and I'll try to fix it.<br><br>


**Why to use?** <br>

You shouldn't. You should just learn how to use FFMPEG. It's a lot more flexible than whatever this is.<br><br>


**Do I have to install FFMPEG myself?** <br>
Yes. I even added a reminder at the beginning of the program.<br><br>


Download FFMPEG from [here](https://ffmpeg.org/download.html).<br><br>


# How to fix FFMPEG not being recognized as a valid program

### Windows<br><br>
1.- Download FFMPEG.<br><br>
2.- Open Windows search and search for "View advanced system settings"<br><br>
<img width="764" height="385" alt="image" src="https://github.com/user-attachments/assets/aa621053-a6ff-4046-b939-9a6cb9fd0040" />

3.- Click on the "Environment variables" button<br><br>
<img width="312" height="173" alt="image" src="https://github.com/user-attachments/assets/8b872c88-9cf2-427b-8c69-9a37c131f503" />

4.- Double click in the "Path" variable in the "System variables" menu<br><br>
<img width="582" height="236" alt="image" src="https://github.com/user-attachments/assets/032e0992-914f-4ebc-9141-cd755938e0c0" />

5.- Click on "New", and type in the place where FFMPEG's binaries are stored. Then, click OK.<br><br>
<img width="541" height="512" alt="image" src="https://github.com/user-attachments/assets/313eac97-bd4c-4d0c-9101-3f5eb2904458" /><br>
(Tip: the official FFMPEG downloads place their binaries under a folder named Bin in the downloaded folder. For example, C:\Users\me\Downloads\ffmpeg\Bin. I recommend placing this in a more general place, like in the program files folder.)

Afterwards, just close and reopen any terminal instances and run the script. If you followed the steps correctly, it should work properly now.

### macOS

No macOS support (yet)

### Linux

No Linux support (yet)
