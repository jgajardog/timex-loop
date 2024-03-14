import time

every=30
continuar=True

def write_timex():
    with open('/home/timex', 'w') as archivo:
        archivo.write(str(time.time()))

while(continuar):
    write_timex()
    threaded_start = time.time()
    time.sleep(28)
    total_time=time.time() - threaded_start
    if(total_time<every):
        dormir=every-total_time
        time.sleep(dormir)
