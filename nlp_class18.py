import multiprocessing
import psutil

def estimate_workers():
    logical_cores = multiprocessing.cpu_count()
    max_cpu=logical_cores*1.5
    ram_gb=psutil.virtual_memory().total/(1024**3)



    print(logical_cores,max_cpu,ram_gb)
    
estimate_workers()


    