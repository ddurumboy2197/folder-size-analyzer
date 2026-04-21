class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class MeetingTimeSlotFinder:
    def __init__(self):
        self.meetings = []

    def add_meeting(self, meeting):
        self.meetings.append(meeting)

    def find_time_slots(self):
        self.meetings.sort(key=lambda x: x.start)
        time_slots = []
        for i in range(len(self.meetings)):
            if i == 0:
                time_slots.append((self.meetings[i].start, self.meetings[i].end))
            else:
                if self.meetings[i].start >= time_slots[-1][1]:
                    time_slots.append((self.meetings[i].start, self.meetings[i].end))
                else:
                    time_slots[-1] = (time_slots[-1][0], max(time_slots[-1][1], self.meetings[i].end))
        return time_slots

# Misol:
finder = MeetingTimeSlotFinder()
finder.add_meeting(Meeting(8, 10))
finder.add_meeting(Meeting(9, 11))
finder.add_meeting(Meeting(10, 12))
finder.add_meeting(Meeting(13, 15))
finder.add_meeting(Meeting(14, 16))
print(finder.find_time_slots())
```

Kodda quyidagilar mavjud:

- `Meeting` klassi: bu klass uchrashuvning bosh va oxirgi vaqtlarini saqlaydi.
- `MeetingTimeSlotFinder` klassi: bu klass uchrashuvlar ro'yxatini saqlaydi va uchrashuvlar orasidagi erkin vaqtlarni topish uchun metodlarini saqlaydi.
- `add_meeting` metod: uchrashuvni ro'yxatga qo'shadi.
- `find_time_slots` metod: uchrashuvlar orasidagi erkin vaqtlarni topadi va ularni ro'yxatga qo'shadi.
- Misol: uchrashuvlar ro'yxatiga uchrashuvlar qo'shadi va erkin vaqtlarni topadi.
