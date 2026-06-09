
mood_dict = {
    "Chilling": {
        "message": "I could get used to this!",
        "color": "#1395B5"
    },
    "Comfortable": {
        "message": "No complaints here.",
        "color": "#9CD0EC"
    },
    "Focused": {
        "message": "We are so locked!",
        "color": "#C3EC3D"
    },
    "Overwhelmed": {
        "message": "Nothing a bit of elbow grease can't handle.",
        "color": "#E56D31"
    },
    "Exhausted": {
        "message": "SLEEP. PLEASE.",
        "color": "#20224C"
    },
}


def get_system_mood(stats):
    cpu = stats["cpu"]["percent"]
    RAM_pcent = stats["memory"]["percent"]
    battery = stats["battery"]["percent"]
    plugged_in = stats["battery"]["plugged_in"]

    mood_modifiers = []
# CPU
    if cpu > 80:
        mood_modifiers.append("CPU is strained!")
    elif cpu > 40:
        mood_modifiers.append("CPU is considerably busy!")
    else:
        mood_modifiers.append("CPU is cozy.")
# RAM
    if  RAM_pcent > 80:
        mood_modifiers.append("RAM is congested!")
    elif  RAM_pcent > 45:
        mood_modifiers.append("RAM is a bit busy!")
    else:
        mood_modifiers.append("RAM is calm.")
# Battery
    if battery is None:
        mood_modifiers.append("No Battery")
    elif battery < 10 and not plugged_in:
        mood_modifiers.append("Battery is critically low!")
    elif battery < 20 and not plugged_in:
        mood_modifiers.append("Battery is low!")
    elif plugged_in:
        mood_modifiers.append("Charging!")
    else: 
        mood_modifiers.append("Battery is good!")
#Primary mood logic
    if "Battery is critically low!" in mood_modifiers or "Battery is low!" in mood_modifiers:
        primary = "Exhausted"
    elif "CPU is strained!" in mood_modifiers or "RAM is congested!" in mood_modifiers:
        primary = "Overwhelmed"
    elif "CPU is considerably busy!" in mood_modifiers or "RAM is a bit busy!" in mood_modifiers:
        primary = "Focused"
    elif "Charging!" in mood_modifiers and cpu < 30 and RAM_pcent < 50:
        primary = "Comfortable"
    else:
        primary = "Chilling"
    
    mood_data = mood_dict[primary]

    return {
        "primary": primary,
        "message": mood_data["message"],
        "color": mood_data["color"],
        "modifiers": mood_modifiers
    }