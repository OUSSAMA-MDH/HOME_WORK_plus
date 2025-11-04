# Youth Association Management Project

This project is a Python-based management system for a youth association. The project has been refactored following **SOLID principles** to ensure maintainability, flexibility, and scalability.

---

## **SOLID Principles Applied**

### **1. Single Responsibility Principle (SRP)**
- **Where:** Classes `Member`, `Activity`, `Subscription` handle only data, while separate `MemberRepository`, `ActivityManager`, and `SubscriptionManager` handle saving/loading and business logic.
- **Problem Solved:** Previously, each class handled multiple responsibilities (e.g., saving files and holding data). This caused code duplication and difficulty in maintenance. SRP separates concerns, making code cleaner and easier to extend.

---

### **2. Open/Closed Principle (OCP)**
- **Where:** `Event` class has subclasses `Trip`, `Meeting`, `Competition`. `Subscription` has subclasses `Donation`, `MonthlySubscription`, `AnnualSubscription`.
- **Problem Solved:** Adding new event types or subscription types previously required modifying existing classes. Now, the code is **open for extension, closed for modification**, allowing new types to be added without touching existing code.

---

### **3. Liskov Substitution Principle (LSP)**
- **Where:** All subclasses of `Event` (`Trip`, `Meeting`, `Competition`) can be used wherever an `Event` is expected. All subclasses of `Subscription` can be used wherever a `Payable` interface is expected.
- **Problem Solved:** Ensures that replacing a base class with a subclass does not break the system. Functions working with `Event` or `Subscription` objects work seamlessly with subclasses.

---

### **4. Interface Segregation Principle (ISP)**
- **Where:** Created small interfaces:  
  - `Payable` → `process_payment()` (implemented by `Donation` and `Subscription`)  
  - `Organizable` → `schedule()` (implemented by `Event` and subclasses)  
  - `Registrable` → `register_member()` (implemented by `Activity` and subclasses)
- **Problem Solved:** Avoided “fat” interfaces with unrelated methods. Classes now only implement methods relevant to their responsibilities, improving modularity.

---

### **5. Dependency Inversion Principle (DIP)**
- **Where:** Storage logic (CSV, JSON, Database) is abstracted via `IStorage` interface. Core logic depends on abstractions, not concrete classes.
- **Problem Solved:** Previously, core classes were tightly coupled to file storage. Now, we can switch storage type without modifying business logic, enhancing flexibility.

---

## **Tools Used**
- Python 3.10+
- CSV files for storage
- Git & GitHub for version control
- Object-Oriented Programming principles

---

## **Results**
- Clear separation of responsibilities among classes.
- Easy to extend system with new event and subscription types.
- Safe replacement of subclasses without breaking existing code.
- Modular interfaces allow flexible implementation.
- Storage mechanism can be changed without touching core logic.

---

## **How to Run**
1. Clone the repository:
   ```bash
   
   git clone https://github.com/OUSSAMA-MDH/HOME_WORK_plus.git

