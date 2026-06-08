import psutil

#index 0 returns percent used, index 1 returns the amount of cpus on the host.(probably not useful)
#ex: cpu = get_cpu_stats()
#    print(cpu[0])

def get_cpu_stats():
    cpu_pcent = psutil.cpu_percent(1)
    cpu_num = psutil.cpu_count(False)
    cpu_info = [cpu_pcent, cpu_num]
    return cpu_info

#index 0 returns memory used, index 1 returns memory available.
#ex: memory = get_mem_stats()
#    print(memory[0])

def get_mem_stats():
    mem = psutil.virtual_memory() #RAM
    mem_usedGiB = round(mem.used/1073741824, 2)
    mem_availGiB = round(mem.available/1073741824, 2)
    mem_info = [mem_usedGiB, mem_availGiB]
    return mem_info

#index 0 returns battery percentage, index 1 returns battery time left in hours, index 2 returns battery time left in seconds.
#ex: batt = get_batt_stats()
#    print(batt[0])

def get_batt_stats():
    battery = psutil.sensors_battery()
    if battery is None:
        return [None, None, None]
    battery_pcent = battery.percent
    battery_time_secs = battery.secsleft
    battery_time_hours = battery_time_secs / 60
    batt_info = [battery_pcent, battery_time_hours, battery_time_secs]
    return batt_info









