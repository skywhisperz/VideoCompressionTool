class VideoFile:
    def __init__(self, source, destination , outname, crf, encoder, audiobitrate, audioencoder):
        self.source = source
        self.destination = destination
        self.outname = outname
        self.crf = crf
        self.encoder = encoder
        self.audiobitrate = audiobitrate
        self.audioencoder = audioencoder