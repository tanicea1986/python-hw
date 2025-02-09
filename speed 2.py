def time_saved(speed_limit, avg_speed, distance):
    if avg_speed <= speed_limit:
        return 0  # No time saved if not exceeding speed limit
    
    time_at_limit = distance / speed_limit  # Time taken at speed limit
    time_at_speed = distance / avg_speed  # Time taken at actual speed
    
    time_saved_hours = time_at_limit - time_at_speed  # Difference in hours
    time_saved_minutes = time_saved_hours * 60  # Convert to minutes
    
    return round(time_saved_minutes, 2)

# User input
speed_limit = float(input("Enter the speed limit (mph): "))
avg_speed = float(input("Enter your average speed (mph): "))
distance = float(input("Enter the distance traveled (miles): "))

# Calculate time saved
time_saved_result = time_saved(speed_limit, avg_speed, distance)

print(f"Time saved: {time_saved_result} minutes")
