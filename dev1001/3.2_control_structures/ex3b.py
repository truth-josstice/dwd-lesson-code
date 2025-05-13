# match-case: Ask the user to input a command (e.g., "start", "stop", "pause"). Use match-case to print a different action message for each command (e.g., "Process starting...", "Process stopping..."). Include a default for unknown commands."

command = input("Enter a command: ")

match command:

    case "Start" | "start":
        print("Process starting: \nYour Dungeons and Dragons game has begun. Adventure awaits!")
    case "Pause" | "pause":
        print("Process paused: \nYou take a short rest. Your spell slots have not returned!")
    case "Stop" | "stop":
        print("Process stopped: \nYou take a long rest. All of your resources are refreshed!")
    case _: 
        print("Uknown process change: \nRoll a luck check, and then throw your dice off a cliff.")