# --- USE: match-case Statement ---
http_status_code = 98347598746 # Try 200, 500, 999
status_meaning = ""

match http_status_code:
    case 200:
        status_meaning = "OK - Request successful."
    case 403:
        status_meaning = "Forbidden - You don't have permission."
    case 404:
        status_meaning = "Not Found - The resource doesn't exist."
    case 500:
        status_meaning = "Internal Server Error - Something went wrong on our end."
    case _: # Default case
        status_meaning = "Unknown or unhandled status code."

print(f"Status {http_status_code}: {status_meaning}")
