from Email import *
from Security import *
from Video import *
from Picture import *
import os
from datetime import datetime

class Controller(object):
    def __init__(self, status, path, length, burst, receiver, resolution):
        self.status = status
        self.path = path
        self.receiver = receiver
        self.length = length
        self.resolution = resolution
        self.burst = burst
        self.date = datetime.now()

    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, status):
        self._status = status
        
    @property
    def path(self):
        return self._path
    @path.setter
    def path(self, path):
        self._path = path

    @property
    def receiver(self):
        return self._receiver
    @receiver.setter
    def receiver(self, receiver):
        self._receiver = receiver

    @property
    def length(self):
        return self._length
    @length.setter
    def length(self, length):
        self._length = length

    @property
    def resolution(self):
        return self._resolution
    @resolution.setter
    def resolution(self, resolution):
        self._resolution = resolution

    @property
    def burst(self):
        return self._burst
    @burst.setter
    def burst(self, burst):
        self._burst = burst

    def empty_list(list):
        list = []       
    
    def create_directory(self):
        self.videoPath = self.path + "/Video"
        self.picPath = self.path + "/Picture"

        if not os.path.exists(self.videoPath):
            os.mkdir(self.videoPath)
        if not os.path.exists(self.picPath):
            os.mkdir(self.picPath)
        else:
            pass

    def record_and_send(self):
        self.video = Video(self.vidPath, self.length)
        self.video.taking_video()
        self.email(self.receiver, self.video.completePath, self.video.vidList)

    def capture_and_send(self):
        self.picture = Picture(self.picPath, self.burst)
        self.picture.get_resolution(self.resolution)
        self.picture.take_picture()
        self.email(self.receiver, self.picture.completePath, self.picture.picList)

    def process(self):
        pass
