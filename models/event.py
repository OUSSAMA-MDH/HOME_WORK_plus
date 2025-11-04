from abc import ABC, abstractmethod

class Event(ABC):
    def __init__(self, event_name, description, event_date, organizer):
        self.event_name = event_name
        self.description = description
        self.event_date = event_date
        self.organizer = organizer
        self.participants = []

    @abstractmethod
    def describe(self):
        pass

    def register_member(self, member_email):
        if member_email not in self.participants:
            self.participants.append(member_email)

class Trip(Event):
    def describe(self):
        return f"Trip: {self.event_name} organized by {self.organizer}"

class Meeting(Event):
    def describe(self):
        return f"Meeting: {self.event_name} with participants: {self.participants}"

class Competition(Event):
    def describe(self):
        return f"Competition: {self.event_name} - {self.description}"
