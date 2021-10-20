#Dummy functions as buttons can't send arguments

def start_1():
    import threading
    th = threading.Thread(target=start_fans,args=(1 , ))
    th.start()

    
def start_2():
    import threading
    th = threading.Thread(target=start_fans,args=(2 , ))
    th.start()
   
    
def start_3():
    import threading
    th = threading.Thread(target=start_fans,args=(3 , ))
    th.start()
   
    
def start_4():
    import threading
    th = threading.Thread(target=start_fans,args=(4 , ))
    th.start()
 
    
def start_5():
    import threading
    th = threading.Thread(target=start_fans,args=(5 , ))
    th.start()

  
    
def start_6():
    import threading
    th = threading.Thread(target=start_fans,args=(6 , ))
    th.start()
    
def start_7():
    import threading
    th = threading.Thread(target=start_fans,args=(7 , ))
    th.start()
  
    
def start_8():
    import threading
    th = threading.Thread(target=start_fans,args=(8 , ))
    th.start()
    

def start_9():
    import threading
    th = threading.Thread(target=start_fans,args=(9 , ))
    th.start()

      


#Controller function for each sequence    
def start_fans(seq):
    #Imports
    from stupidArtnet.StupidArtnet import StupidArtnet
    import time
    
    ramp_interval = 0.5 #(amount of time fans get between receiving their ramp up and ramp down command)
    start_interval = 5 #Amount of time to wait before starting human fans
    split_interval = 10 #Amount of time between human segments
    
    #Nested function for importing data
    def load_powers(filename):
        with open(filename) as f:
            powers = [int(x) for x in f.readlines()[0].split(",")]
        packet = bytearray(powers)
        return packet
    
    #Nested function for loading human data - loads using load_powers but cycles through 4 speakers
    def load_human(side, seq):
        humans = []
        for i in range(1,5):
            combined = []
            combined.append(load_powers("fan_data/S{}U{}-{}-ramp.powers.txt".format(i,seq,side)))
            combined.append(load_powers("fan_data/S{}U{}-{}.powers.txt".format(i,seq,side)))
            humans.append(combined)
        return humans
    
    #Function for machine load - just gives the ramp up powers as well
    def load_machine(side, seq):
        machine = []
        machine.append(load_powers("fan_data/MU{}-{}-ramp.powers.txt".format(seq,side)))
        machine.append(load_powers("fan_data/MU{}-{}.powers.txt".format(seq,side)))
        return(machine)
    
    
    
    #Load in data sequences - this is 4 for humans , and one for the machine sides
    human_l = load_human("l", seq)
    human_r = load_human("r", seq)
    machine_l = load_machine("l",seq)
    machine_r = load_machine("r",seq)
    
    #Assign controller object to global variables
    h_l = StupidArtnet("2.255.255.255", 0, 512, 30, True, True)
    h_r = StupidArtnet("2.255.255.255", 1, 512, 30, True, True)
    m_l = StupidArtnet("2.255.255.255", 3, 512, 30, True, True)
    m_r = StupidArtnet("2.255.255.255", 2, 512, 30, True, True)
    
    
    #Start all 4 controllers
    h_l.start()
    h_r.start()
    m_l.start()
    m_r.start()
    
    
    #Set machine straight away - machine vid starts immediately (ramp up first, then full speeds)

    
    m_l.blackout()
    m_l.set(machine_l[0])
    m_r.blackout()
    m_r.set(machine_r[0])
    time.sleep(ramp_interval) # sleep for a tic while we ramp up power
    m_l.blackout()
    m_l.set(machine_l[1])
    m_r.blackout()
    m_r.set(machine_r[1])
    #Quick sleep while machine gets set up
    #time.sleep(start_interval) - experimenting without at the moment so that loop below can be "wait+play" easily - ends on play
    
    
    #Send human data in "split_interval" seconds
    for i in range(0,4):
        
        #Ramp up
        h_l.blackout()
        h_l.set(human_l[i][0])
        h_r.blackout()
        h_r.set(human_r[i][0])
        
        #Full speed
        time.sleep(ramp_interval)
        h_l.blackout()
        h_l.set(human_l[i][1])
        h_r.blackout()
        h_r.set(human_r[i][1])
        
        #Sleep between sequences
        time.sleep(split_interval-ramp_interval)
       
    #Kill everything at end of thread to avoid collision
    h_l.blackout()
    time.sleep(0.1)
    h_r.blackout()
    time.sleep(0.1)
    m_l.blackout()
    time.sleep(0.1)
    m_r.blackout()
    
    h_l.stop()
    time.sleep(0.1)
    h_r.stop()
    time.sleep(0.1)
    m_l.stop()
    time.sleep(0.1)
    m_r.stop()
    
    h_l.stop()
    h_r.stop()
    m_l.stop()
    m_r.stop()
    
    del h_l
    del h_r
    del m_l
    del m_r
    
    
    return "COMPLETE"

def stop_fans():
    from stupidArtnet.StupidArtnet import StupidArtnet
    
    h_l = StupidArtnet("2.255.255.255", 0, 512, 30, True, True)
    h_r = StupidArtnet("2.255.255.255", 1, 512, 30, True, True)
    m_l = StupidArtnet("2.255.255.255", 3, 512, 30, True, True)
    m_r = StupidArtnet("2.255.255.255", 2, 512, 30, True, True)
    
    #Start all 4 controllers
    h_l.start()
    h_r.start()
    m_l.start()
    m_r.start()
    
    h_l.blackout()
    h_r.blackout()
    m_l.blackout()
    m_r.blackout()
    
    h_l.stop()
    h_r.stop()
    m_l.stop()
    m_r.stop()
    
    h_l.stop()
    h_r.stop()
    m_l.stop()
    m_r.stop()
    
    del h_l
    del h_r
    del m_l
    del m_r