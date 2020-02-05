from datetime import datetime
from pygame import mixer
import time



def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()     

    while True:

  

            a=input()
            
            
            if a==stopper:
                mixer.music.stop()
                break
        
    
def log_now(msg):
    with open("my_log.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n ")

if __name__ == "__main__":

    
    
    while True:
        time.sleep(5)
        print("Come on , Drink Water")
        musiconloop("water.mp3","stop")
           
            
        log_now("Drank water at")
   
        time.sleep(3)
        print("Do Eye activities..")
        musiconloop("calm.mp3","done")
            
            
        log_now("Eye Activity done at")    
           

        time.sleep(2)
        print("YEah, Physical Exercise Time...")
        musiconloop("exercise.mp3","hogaya")
            
            
        log_now("Physical Activity done at") 



