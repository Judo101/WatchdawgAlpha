import picamera
from datetime import datetime
from time import sleep
from subprocess import call

# create a big class for Video
class Video(object):
    # the __init__ function will take 2 parameters:
    # path: the file path
    # length: how long will the video last
    def __init__(self, path, length):
        self.path = path
        self.length = length
        
    # accessors and mutators for the variables
    @property
    def path(self):
        return self._path
    @path.setter
    def path(self, path):
        self._path = path

    @property
    def length(self):
        return self._length
    @length.setter
    def length(self, length):
        self._length = length

    # function for taking video
    def taking_video(self):
        # get the date and time for naming
        self.currentTime = datetime.now()
        # get the video name
        vidName = currentTime.strftime("%H:%M:%S") + ".h264"
        # get the complete path for the video
        completePath = self.path + vidName
        # record the video
        with picamera.PiCamera() as camera:
            camera.start_recording(completePath)
            # plug the self.length variable for the length of the video
            sleep(self.length)
            # stop recording
            camera.stop_recording()
        # create the command to convert video from .h264 to .mp4
        command = "MP4Box -add {} {}.mp4".format(completePath, self.path + self.currentTime)
        # execute the command
        call([command], shell=True)
        # confirmed everything was implemented right
        print "Motion captured"
