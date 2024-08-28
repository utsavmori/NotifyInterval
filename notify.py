import beepy
import sys
import time
def main():
    mins=40
    times=10
    if len(sys.argv) == 1:
        print("using default values: interval is 40 mins and 10 times a day")
    elif len(sys.argv) == 2:
        mins=int(sys.argv[1])
    elif len(sys.argv) == 3:
        mins=int(sys.argv[1])
        times=int(sys.argv[2])
    else:
        print("invalid number of commandline arguments... exiting...")
        sys.exit()        
    for arg in range(times):
        time.sleep(mins*60)
        # 'coin', 'ping', 'ready', 'success', 'wilhelm' , 'error', 'robot_error'
        beepy.beep(sound='coin')    

if __name__ == "__main__":
    main()
