import tkinter as tk
from datetime import datetime

class Member:
    def __init__(self, member_id, name, membership_type):
        self.member_id = member_id
        self.name = name
        self.membership_type = membership_type

    def __str__(self):
        return f"Member ID: {self.member_id}, Name: {self.name}, Membership Type: {self.membership_type}"

class Attendance:
    def __init__(self, member, check_in_time):
        self.member = member
        self.check_in_time = check_in_time

    def __str__(self):
        return f"Member: {self.member.name}, Check-in Time: {self.check_in_time}"

class GymManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gym Management System")

        self.gym_system = GymManagementSystem()

        self.label = tk.Label(root, text="Gym Management System", font=("Helvetica", 16))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.register_button = tk.Button(root, text="Register Member", command=self.register_member)
        self.register_button.grid(row=1, column=0, pady=5)

        self.checkin_button = tk.Button(root, text="Check-in Member", command=self.check_in_member)
        self.checkin_button.grid(row=1, column=1, pady=5)

        self.display_members_button = tk.Button(root, text="Display Members", command=self.display_members)
        self.display_members_button.grid(row=2, column=0, pady=5)

        self.display_attendance_button = tk.Button(root, text="Display Attendance Log", command=self.display_attendance_log)
        self.display_attendance_button.grid(row=2, column=1, pady=5)

    def register_member(self):
        register_window = tk.Toplevel(self.root)
        register_window.title("Register Member")

        label = tk.Label(register_window, text="Member Registration", font=("Helvetica", 14))
        label.pack(pady=10)

        member_id_label = tk.Label(register_window, text="Member ID:")
        member_id_label.pack()

        member_id_entry = tk.Entry(register_window)
        member_id_entry.pack()

        name_label = tk.Label(register_window, text="Member Name:")
        name_label.pack()

        name_entry = tk.Entry(register_window)
        name_entry.pack()

        membership_type_label = tk.Label(register_window, text="Membership Type:")
        membership_type_label.pack()

        membership_type_entry = tk.Entry(register_window)
        membership_type_entry.pack()

        register_button = tk.Button(register_window, text="Register", command=lambda: self.process_registration(
            member_id_entry.get(), name_entry.get(), membership_type_entry.get(), register_window))
        register_button.pack(pady=10)

    def process_registration(self, member_id, name, membership_type, register_window):
        self.gym_system.register_member(member_id, name, membership_type)
        register_window.destroy()

    def check_in_member(self):
        checkin_window = tk.Toplevel(self.root)
        checkin_window.title("Check-in Member")

        label = tk.Label(checkin_window, text="Member Check-in", font=("Helvetica", 14))
        label.pack(pady=10)

        member_id_label = tk.Label(checkin_window, text="Member ID:")
        member_id_label.pack()

        member_id_entry = tk.Entry(checkin_window)
        member_id_entry.pack()

        checkin_button = tk.Button(checkin_window, text="Check-in", command=lambda: self.process_check_in(
            member_id_entry.get(), checkin_window))
        checkin_button.pack(pady=10)

    def process_check_in(self, member_id, checkin_window):
        self.gym_system.check_in_member(member_id)
        checkin_window.destroy()

    def display_members(self):
        members_window = tk.Toplevel(self.root)
        members_window.title("Registered Members")

        label = tk.Label(members_window, text="Registered Members", font=("Helvetica", 14))
        label.pack(pady=10)

        members_text = tk.Text(members_window, height=10, width=40)
        members_text.pack()

        members_text.insert(tk.END, "\n".join(str(member) for member in self.gym_system.members.values()))

    def display_attendance_log(self):
        attendance_window = tk.Toplevel(self.root)
        attendance_window.title("Attendance Log")

        label = tk.Label(attendance_window, text="Attendance Log", font=("Helvetica", 14))
        label.pack(pady=10)

        attendance_text = tk.Text(attendance_window, height=10, width=40)
        attendance_text.pack()

        attendance_text.insert(tk.END, "\n".join(str(entry) for entry in self.gym_system.attendance_log))

class GymManagementSystem:
    def __init__(self):
        self.members = {}
        self.attendance_log = []

    def register_member(self, member_id, name, membership_type):
        if member_id not in self.members:
            member = Member(member_id, name, membership_type)
            self.members[member_id] = member
            print(f"Member {name} registered successfully.")
        else:
            print("Member ID already exists. Please choose a different ID.")

    def check_in_member(self, member_id):
        if member_id in self.members:
            member = self.members[member_id]
            check_in_time = datetime.now()
            attendance = Attendance(member, check_in_time)
            self.attendance_log.append(attendance)
            print(f"Check-in successful for {member.name}.")
        else:
            print("Invalid Member ID. Please check and try again.")

def main():
    root = tk.Tk()
    app = GymManagementApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
