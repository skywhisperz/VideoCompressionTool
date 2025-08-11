class VideoFile:
    source : str = ""
    destination : str = ""
    name : str = ""
    crf : int = 20
    encoder : str = "libx264"
    audiobitrate : str = "192k"
    audioencoder : str = "aac"