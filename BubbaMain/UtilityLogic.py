import psutil

def get_cpu_stats(): #cpu info
    cpu_pcent = psutil.cpu_percent(interval=None)
    cpu_cores = psutil.cpu_count(False)
    cpu_info = {
        "percent": cpu_pcent,
        "cores": cpu_cores
    }
    return cpu_info



def get_mem_stats():
    mem = psutil.virtual_memory() #RAM
    mem_usedGiB = round(mem.used/1073741824, 2)
    mem_availGiB = round(mem.available/1073741824, 2)
    mem_info = {
        "used": mem_usedGiB,
        "available": mem_availGiB,
        "percent": mem.percent
    }
    return mem_info


def get_batt_stats(): #battery info
    battery = psutil.sensors_battery()
    if battery is None: #in case of no battery
        return {"percent": None, "hours": None, "seconds": None, "plugged_in": None}
    battery_pcent = battery.percent
    is_plugged_in = battery.power_plugged
    battery_time_secs = battery.secsleft
    battery_time_hours = battery_time_secs / 3600
    batt_info = {
        "percent": battery_pcent,
        "hours": battery_time_hours,
        "seconds": battery_time_secs,
        "plugged_in": is_plugged_in
    }
    return batt_info

#searches all stats, can return a summary of all sections, a summary of just one
#or a specific stat within one section
#ex: statistics = get_all_stats()
#statistics = get_all_stats()
#print(statistics["cpu"]["cores"])

def get_all_stats():
    stats = {
        "cpu": get_cpu_stats(),
        "memory": get_mem_stats(),
        "battery": get_batt_stats()
    }
    return stats











