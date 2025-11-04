import csv
from models.member import Member

class MemberRepository:
    def __init__(self, file_path="members.csv"):
        self.file_path = file_path

    def load_members(self):
        members = []
        try:
            with open(self.file_path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    members.append(Member(
                        row['full_name'], row['email'], row['phone'], row['address'],
                        row['join_date'], row['major'], row['skills'].split(","), 
                        row['interests'].split(","), row['subscription_status']
                    ))
        except FileNotFoundError:
            print("Members file not found.")
        return members

    def save_members(self, members):
        with open(self.file_path, mode="w", encoding="utf-8", newline='') as file:
            fieldnames = ["full_name","email","phone","address","join_date","major","skills","interests","subscription_status"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for m in members:
                writer.writerow({
                    "full_name": m.full_name,
                    "email": m.email,
                    "phone": m.phone,
                    "address": m.address,
                    "join_date": m.join_date,
                    "major": m.major,
                    "skills": ",".join(m.skills),
                    "interests": ",".join(m.interests),
                    "subscription_status": m.subscription_status
                })
