import pickle
from playsound import playsound
from kivy.clock import Clock
from utils import Load

class Timer():
    def Alarm(self, dt):
        tune = Load("Tune")
        playsound(tune, False)

    def Start_Alarm(self):
        time = Load("Alarm_Time")
        # Multiply int(time) with 60 to convert to minutes later
        self.timer = Clock.schedule_interval(self.Alarm, int(time))

    def Cancel_Alarm(self):
        self.timer.cancel()