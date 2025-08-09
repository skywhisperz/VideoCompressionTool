import os
import subprocess

def checkFFmpegExists():
    if (os.path.isfile("_ffmpegcheck")):
        print("FFmpeg is installed!")
        return 0
    print("Warning: this is a first time check that only runs the first time you run the script or if you delete the '_ffmpegcheck' file that is created after this check.")
    input("Press Enter to begin.\n")
    print("\n\nNOTE: YOU HAVE TO INSTALL FFMPEG YOURSELF. ADD THE FFMPEG BIN FOLDER TO YOUR PATH ENVIRONMENT VARIABLE, OR USE A THIRD PARTY INSTALLER TO DO IT AUTOMATICALLY FOR YOU. OTHERWISE, THE PROGRAM WILL NOT WORK.\nIn order to test this, the program will run the command \"ffmpeg -version\". If the command fails or states that \"'ffmpeg' is not recognized as an internal or external command, operable program or batch file\", then you do not have FFmpeg installed.")
    input("Press Enter to run the command.\n")
    subprocess.run(["ffmpeg", "-version"])
    didFFMPEGWork = input("\n\nDid the command show a lot of options and text? (Y/n) > ")
    didFFMPEGWork = didFFMPEGWork.lower()
    if (didFFMPEGWork == "y"):
        with open('_ffmpegcheck', 'w') as checkFile:
            checkFile.write("FFmpeg exists! Yippee!")
        print("Good! You have FFmpeg installed. Let's start.")
    elif (didFFMPEGWork == "n"):
        print("Download this installer to install FFmpeg: https://getffmpeg.org/\nOr, if you don't trust it, download the FFmpeg binaries directly from https://ffmpeg.org/download.html and add them to your PATH environment variable.")
        input("Press Enter to exit.\n")
        exit(0)
    else:
        print(f"Invalid option: {didFFMPEGWork}. Interpreting invalid answer as 'no'.")
        print("Download this installer to install FFmpeg: https://getffmpeg.org/\nOr, if you don't trust it, download the FFmpeg binaries directly from https://ffmpeg.org/download.html and add them to your PATH environment variable.")
        input("Press Enter to exit.\n")
        exit(0)

def main():
    appVersion = "1.0"
    textSeparator = "=================================================="
    sourceAndDest = None
    print(f"Welcome to Video Compression Tool {appVersion}\n{textSeparator}")
    checkFFmpegExists()
    while True:
        sourceAndDest = obtainSourceAndDestination()
        if (sourceAndDest == 1):
            pass
        elif (sourceAndDest == 2):
            print("\nSorry about that. Let's try again.\n")
        elif (sourceAndDest == 3):
            print("\nNot a valid choice; please select one of the valid choices (y / n).\nInterpreting invalid answer as 'no'. Let's try that again.\n")
        elif (sourceAndDest == 4):
            pass

def obtainSourceAndDestination():
    videoToCompress = input("What video would you like to compress? > ")
    if (not videoToCompress.find("\"") == -1 or not videoToCompress.find("\'")):
        videoToCompress = videoToCompress[1:-1]
    if (not os.path.isfile(videoToCompress)):
        print("\nNot a valid file. Please insert a path to a real file! The file must end with a valid video file extension.\n")
        return 1
    destinationToDump = input("Where should the compressed video be placed? > ")
    if (not destinationToDump.find("\"") == -1 or not destinationToDump.find("\'")):
        destinationToDump = destinationToDump[1:-1]
    if (not os.path.isdir(destinationToDump)):
        print("\nThat directory doesn't exist. Please insert a valid directory. NOTE: DO NOT INSERT A FILE HERE. You will choose the output file name later, don't worry.\n")
        yOrNDestQuestCreateDir = input("Would you like to create a directory with the name you provided? (Y/n) > ")
        yOrNDestQuestCreateDir = yOrNDestQuestCreateDir.lower()
        if (yOrNDestQuestCreateDir == "y"):
            os.mkdir(destinationToDump)
        elif (yOrNDestQuestCreateDir == "n"):
            print("\nAlright, let's try that again.\n")
            return 4
        else:
            return 3
    yOrNSrcDestQuest = input(f"The source video is located in '{videoToCompress}', and the compressed output should be placed in '{destinationToDump}'. Is this correct? (Y/n) > ")
    print("\nSource and destination accepted!\n")
    yOrNSrcDestQuest = yOrNSrcDestQuest.lower()
    if (yOrNSrcDestQuest == "y"):
        print("Note: you can't use some special characters in file names, so keep filenames simple and short.\nInclude the file extension of the video (e.g.: .mp4, .mkv, .avi, etc.) you want at the end of the filename.\n")
        while True:
            videoNameOutput = setVideoName(videoToCompress, destinationToDump)
            if (videoNameOutput == 1):
                pass
    elif (yOrNSrcDestQuest == "n"):
        return 2
    else:
        return 3

def setVideoName(src : str, dest : str):
    unacceptableFilenameChars = ["\\", "/", ":", "*", "?", "\"", "<", ">", "|"]
    videoName = input("What should the output video file be named? > ")
    for unacceptableCharacter in unacceptableFilenameChars:
        if (videoName.find(unacceptableCharacter) != -1):
            print(f"\nFound \"{unacceptableCharacter}\" in the filename. This character is not allowed. Please try again.\n")
            return 1
    if (videoName.find(".") == -1 or videoName.endswith(".")):
        print("\nCould not detect any file extension. Please try again.\n")
        return 1
    print("\nFilename accepted! Let's begin.\n")
    while True:
        basicQuestOutput = basicQuestionaire(src, dest, videoName)
        if (basicQuestOutput == 15):
            break
        elif (basicQuestOutput == 1):
            pass

def receiveCrf():
    crfLevel = int(input("Input compression level (CRF), which may range from 1 to 51. Lower values output better quality but compress the video less. A value of around 20 (or around 30, if using H.265) is recommended. > "))
    if (crfLevel <= 0 or crfLevel >= 52):
        print(f"\nInvalid CRF value. The CRF value may range from 1 to 51, but {crfLevel} was recieved.\n")
        return -1
    return crfLevel

def receiveEncoder():
    useEncoder265 = False
    useCodec = "libx264"
    encoderType = input("Would you like to use the H.265 encoder for this video? (Y/n) > ")
    encoderType = encoderType.lower()
    if (encoderType == "y"):
        useCodec = "libx265"
        useEncoder265 = True
    elif (encoderType == "n"):
        pass
    else:
        print("\nNot a valid choice; please select one of the valid choices (y / n).\nInterpreting invalid answer as 'no'.\n")
        encoderType = "n"
    return [useCodec, useEncoder265, encoderType]

def receiveAudioBitrate():
    audioBitrate = input("Set audio bitrate (leave empty for default) > ")
    if (audioBitrate.isalpha()):
        print("Invalid audio bitrate. Please try again.")
        return "-1"
    else:
        if (not audioBitrate.strip()):
            print("No input received, leaving at default!")
            audioBitrate = "default"
            return audioBitrate
        else:
            return audioBitrate
    
def guessFfmpegCommandPrev(src1, dest1, fnm1, crfLevel, useCodec, audioBitrate):
    if (audioBitrate == "default"):
        return f"ffmpeg -i {src1} -crf {crfLevel} -c:v {useCodec} {dest1}/{fnm1}"
    else:
        return f"ffmpeg -i {src1} -crf {crfLevel} -c:v {useCodec} -b:a {audioBitrate} {dest1}/{fnm1}"

def basicQuestionaire(src1 : str, dest1 : str, fnm1 : str):

    while True:
        crfLevel = receiveCrf()
        if (crfLevel == -1):
            pass
        else:
            break

    encoderListReceiver = receiveEncoder()
    encoderType = encoderListReceiver[2]
    useEncoder265 = encoderListReceiver[1]
    useCodec = encoderListReceiver[0]

    while True:
        audioBitrate = receiveAudioBitrate()
        if (audioBitrate == "-1"):
            pass
        else:
            break
    
    print(f"The following options will be used:\n\nCRF level: {crfLevel}\nUse high efficiency codec: {useEncoder265}\nInput file: {src1}\nOutput file: {fnm1} in {dest1}\nAudio bitrate: {audioBitrate}\n\nFull FFMPEG command preview:\n{guessFfmpegCommandPrev(src1, dest1, fnm1, crfLevel, useCodec, audioBitrate)}")
    input("Press Enter to begin!\n")
    compress(src1, dest1, fnm1, crfLevel, encoderType, audioBitrate)

def compress(src : str, dest : str, fnm : str, crf : int, cdc : str, abr : str):
    useCodec = "libx264"
    if (cdc == "y"):
        useCodec = "libx265"
    else:
        pass

    if (abr == "default"):
        subprocess.run(['ffmpeg', '-i', src, '-crf', str(crf), '-c:v', useCodec, f'{dest}/{fnm}'])
    else:
        subprocess.run(['ffmpeg', '-i', src, '-crf', str(crf), '-c:v', useCodec, '-b:a', abr, f'{dest}/{fnm}'])
    input("Press Enter to exit.\n")
    exit(0)

if (__name__ == "__main__"):
    main()