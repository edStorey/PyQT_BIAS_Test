def start_fans():
    from stupidArtnet.StupidArtnet import StupidArtnet
    import time
    
    global h_l
    global h_r
    global m_l
    global m_r
#Dummy fan test 
    human_l = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00K\x00\x00\x00\x00\x00\x00\x00\x00\x00K\x00\x00\x00K\xff\x00\x00\x00K\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00K\x00\x00\x00\x00\xff\x00\x00KK\xff\x00\x00\x00K\xff\x00\x00\x00K\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00K\xff\x00\x00\x00K\xff\x00\x00\x00K\xff\x00\x00KK\xff\x00\x00\x00K\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00K\x00\x00KKKK\x00KK\xff\xffK\xffKK\xffKK\xff\xffKK\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xffK\xff\xff\xff\xffK\xff\xff\xffKKK\xff\xff\xffKK\xff\xff\xffK\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xffK\xff\xff\xff\xff\xff\xff\xff\xff\xffK\xff\xff\xff\xff\xff\xff\xff\xff\xff\xffK\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00KKKKKK\x00\x00\x00K\xffKKKK\xffK\xff\xffK\xffK\xffKK\x00\x00\x00\x00\x00\x00\x00\x00\x00K\xff\xffK\xff\xffK\xffKKK\xff\xff\xffK\xffK\xff\xffK\xff\xff\xffK\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xffK\xff\xff\xff\xff\xff\xff\xffKK\xff\xff\xff\xff\xffK\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xffKK\x00\x00KKKKK\xff\xffKK\x00\xff\xffKK\x00K\xffK\x00\x00\x00\x00\x00\x00\x00\x00\x00KKK\xffKKK\xff\xffK\xffKKKK\xffKKKK\xffK\xffKK\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xffKKKK\xffK\xffKK\xff\xff\xffKK\xff\xff\xffK\xff\xff\xff\xffKK\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    human_r = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00K\x00\x00KKK\x00\x00\x00\x00\xffKKKKKKK\xffKKKKKK\x00\x00\x00\x00\x00\x00\x00\x00\x00K\xff\xffKKK\xff\xff\xff\xffKKKKKKKK\xff\xffKKKKK\x00\x00\x00\x00\x00\x00\x00\x00\x00KKK\xff\xffK\xff\xff\xff\xffK\xff\xff\xff\xffKK\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00K\x00KKK\x00\x00\x00\x00\x00KKKKK\xffKKKKKKKKK\x00\x00\x00\x00\x00\x00\x00\x00\x00KK\xffKK\xff\xff\xffKK\xff\xffKKK\xffKKKK\xff\xff\xffKK\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xffKKK\xffKKKK\xff\xffKKK\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00KKKKK\x00\x00\x00\x00\x00KKKK\x00K\xffKKKKKKKK\x00\x00\x00\x00\x00\x00\x00\x00\x00K\xff\xffKKKKKKKKKKKKKKKKKKKKKK\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00KKKKKKKKKKK\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00K\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00KK\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00K\x00K\x00\x00\x00K\x00\x00\x00\x00\x00KK\x00K\x00\x00KKKKKKKKKKKK\x00\x00\x00\x00\x00\x00KKKKKKKKKKKK\xff\xffKKKK\xff\xff\xffKKK\xff\xff\xff\xffKK\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    machine_l = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x002222\x002222\x002222\x002222\x0022222\x00\x00\x00\x00\x00\x00\x00\x00\x0022\xc822222222222\xc8\x00222222222\x00\x00\x00\x00\x00\x00\x00\x00\x002222\xc8222222\xc8\xc82\xc8222\xc8\xc8222\xc8\xc8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x002222\x00\x00\x00\x00\x002222222\xc8\xc822\xc82\xc8\xc8\x00\x00\x00\x00\x00\x00\x00\x00\x0022222\xc8\xc82\xc8\xc8\xc8\xc822\xc822\xc82\xc8\xc8222\xc8\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc8\xc8\xc8\xc8\xc8\xc82222\xc8\xc8\xc8\xc8\xc8\xc8\xc8\xc8\xc8\xc8\xc82\xc8\xc8\xc8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0022\x00\x00\x0022\x00\x00\x0022\x00\x00\x0022\x00\x002\xc82\x00\x002\x00\x00\x00\x00\x00\x00\x00\x00\x00222\x00\xc82\xc82\x002\xc8\xc82\x002\xc822\x002\xc8\xc82\x002\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc8\xc82\x002\xc8\xc82\x0022\xc822\xc82222\xc82222\xc8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x002\x00\x00\x00\x00\x00\x00\x00\x002222\x00\x00\xc8222\x00\x00\xc8\xc8\xc8\xc8\x00\x00\x00\x00\x00\x002\xc822\x00\x00\xc8\xc8\xc8\xc8\x00\x00\xc8\xc8\xc8\xc8\x00\x00\xc8\xc8\xc8\xc8\x00\x00\xc8\xc8\xc8\xc8\x00\x00\x00\x00\x00\x00\x00\x002\xc8\xc8\xc8\x00\x00\xc8\xc8\xc8\xc8\x00\x00\xc8\xc82\xc8\x00\x00222\xc8\x00\x00\xc8\xc8\xc8\xc8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    machine_r = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x002\x002\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0022\x00\x00\x0022\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00222\x002222\x002222\x00\x00222\x002222\x00\x00\x00\x00\x00\x00\x00\x00\x00\x002222\x00222\xc8\x00\xc8\xc8\xc8\xc8\x00\xc8\xc8\xc8\xc8\x00\xc8\xc8\xc8\xc8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00222\x00\x00\x00\x00\x00\x00\x00\x00\x00\x002222222222\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc8222\xc822\x00\x002222222222\x0022\x0022\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00222\x002\xc8\xc8\xc82\xc8\xc8\xc8\xc8\xc8\xc8\xc8\xc8\xc8\xc8\xc8\xc8\xc8\xc8\xc8\xc8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x002\x002\x0022222\xc8\xc8\xc8\xc8\xc8\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc8\xc8\xc8\xc8\xc822\xc822222222\xc822\x0022222\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc8\xc8\xc82\xc8\xc8\xc8\xc8\xc82\xc8\xc8\xc8\xc8\xc8\xc8\xc8\xc8\xc8\xc8\xc8\xc8\xc8\xc8\xc8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    
    h_l = StupidArtnet("2.255.255.255", 0, 512, 30, True, True)
    h_r = StupidArtnet("2.255.255.255", 1, 512, 30, True, True)
    m_l = StupidArtnet("2.255.255.255", 3, 512, 30, True, True)
    m_r = StupidArtnet("2.255.255.255", 2, 512, 30, True, True)
    
    h_l.start()
    h_r.start()
    m_l.start()
    m_r.start()
    
    
    h_l.set(human_l)
    h_r.set(human_r)
    m_l.set(machine_l)
    m_r.set(machine_r)
    
    
def stop_fans():
    global h_l
    global h_r
    global m_l
    global m_r
    
    h_l.blackout()
    h_r.blackout()
    m_l.blackout()
    m_r.blackout()
    
    h_l.stop()
    h_r.stop()
    m_l.stop()
    m_r.stop()
    
    del h_l
    del h_r
    del m_l
    del m_r