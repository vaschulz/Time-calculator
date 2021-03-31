def add_time(start, duration, weekday=False):

  week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  weekIndex = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}

  ampmFlipper = {"AM": "PM", "PM": "AM"}

  startTime = start.split(" ")[0]
  startAmpm = start.split(" ")[1]

  startHours = int(startTime.split(":")[0])
  startMinutes = int(startTime.split(":")[1])

  durationHours = int(duration.split(":")[0])
  durationMinutes = int(duration.split(":")[1])

  endMinutes = startMinutes + durationMinutes
  if endMinutes >= 60:
    startHours += 1
    endMinutes = endMinutes % 60
  endHours = (startHours + durationHours) % 12
  ampmFlipAmount = (startHours + durationHours) // 12

  if endMinutes < 10:
    endMinutes = "0" + str(endMinutes)
  if endHours == 0:
    endHours = 12

  if ampmFlipAmount % 2 == 1:
    endAmpm = ampmFlipper[startAmpm]
  else:
    endAmpm = startAmpm

  daysAdded = durationHours // 24

  if startAmpm == "PM" and startHours + (durationHours % 12) >= 12:
    daysAdded += 1

  newTime = str(endHours) + ":" + str(endMinutes) + " " + endAmpm
  if weekday:
    weekday = weekday.lower()
    index = (weekIndex[weekday] + daysAdded) % 7
    endDay = week[index]
    newTime += ", " + endDay

  if daysAdded == 1:
    newTime += " (next day)"
  if daysAdded > 1:
    newTime += " (" + str(daysAdded) + " days later)"

  return newTime
