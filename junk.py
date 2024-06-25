def generate_time_intervals(num_entries):
    intervals = []
    for BSlotID in range(1, num_entries + 1):  # IDs typically start from 1
        Date = '2024-06-20'

        # Generate a random start time in "HH:MM" format
        start_hour = random.randint(0, 23)
        start_minute = random.randint(0, 59)
        TimeFrom = f"{start_hour:02}:{start_minute:02}"
        
        # Calculate end time
        start_datetime = datetime.strptime(TimeFrom, '%H:%M')
        duration_minutes = random.randint(1, 720)  # Random duration between 1 minute and 12 hours
        end_datetime = start_datetime + timedelta(minutes=duration_minutes)
        TimeTo = end_datetime.strftime('%H:%M')

        intervals.append((BSlotID, Date, TimeFrom, TimeTo))
    
    print(intervals)
