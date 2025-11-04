from datetime import datetime
from models.member import Member
from managers.member_repository import MemberRepository
from models.event import Trip, Meeting, Competition
from models.subscription import MonthlySubscription, AnnualSubscription, Donation

def print_menu():
    print("\n=== Youth Association Management ===")
    print("1. Add new member")
    print("2. Display all members")
    print("3. Add event")
    print("4. Register member to event")
    print("5. Display events")
    print("6. Add subscription")
    print("0. Exit")

def main():
    member_repo = MemberRepository()
    members = member_repo.load_members()
    events = []
    subscriptions = []

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            full_name = input("Full Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            address = input("Address: ")
            join_date = input("Join Date (YYYY-MM-DD): ")
            major = input("Major: ")
            skills = input("Skills (comma separated): ").split(",")
            interests = input("Interests (comma separated): ").split(",")
            subscription_status = input("Subscription Status: ")
            member = Member(full_name, email, phone, address, join_date, major, skills, interests, subscription_status)
            members.append(member)
            member_repo.save_members(members)
            print("✅ Member added successfully.")

        elif choice == "2":
            if not members:
                print("No members available.")
            for m in members:
                print(f"{m.full_name} | {m.email} | {m.major}")

        elif choice == "3":
            print("Select event type: 1. Trip  2. Meeting  3. Competition")
            etype = input("Type: ")
            name = input("Event Name: ")
            description = input("Description: ")
            date = input("Date (YYYY-MM-DD): ")
            organizer = input("Organizer: ")
            if etype == "1":
                event = Trip(name, description, date, organizer)
            elif etype == "2":
                event = Meeting(name, description, date, organizer)
            else:
                event = Competition(name, description, date, organizer)
            events.append(event)
            print("✅ Event added successfully.")

        elif choice == "4":
            email = input("Member Email: ")
            event_name = input("Event Name: ")
            member_found = any(m.email == email for m in members)
            if not member_found:
                print("❌ Member not found.")
                continue
            event_found = False
            for ev in events:
                if ev.event_name.lower() == event_name.lower():
                    ev.register_member(email)
                    event_found = True
                    print("✅ Member registered to event.")
                    break
            if not event_found:
                print("❌ Event not found.")

        elif choice == "5":
            if not events:
                print("No events available.")
            for ev in events:
                print(f"{ev.describe()} | Participants: {', '.join(ev.participants) if ev.participants else 'None'}")

        elif choice == "6":
            email = input("Member Email: ")
            amount = float(input("Amount: "))
            date = input("Date (YYYY-MM-DD): ")
            print("Select subscription type: 1. Monthly 2. Annual 3. Donation")
            stype = input("Type: ")
            if stype == "1":
                sub = MonthlySubscription(email, amount, date)
            elif stype == "2":
                sub = AnnualSubscription(email, amount, date)
            else:
                sub = Donation(email, amount, date)
            subscriptions.append(sub)
            sub.process_payment()
            print("✅ Subscription added successfully.")

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
