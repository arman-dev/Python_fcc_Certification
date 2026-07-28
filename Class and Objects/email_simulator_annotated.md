# 📧 Email Simulator — A Python OOP Project

A small but complete, **console-based email simulation** built purely with Python's
Object-Oriented Programming features. No external libraries, no networking — just clean
classes, composition, and magic methods working together to mimic the core lifecycle of a
real inbox: **create users → send emails → list the inbox → read an email → delete an
email.**

---

## 1. 🎯 Project Purpose & Objectives

### Purpose
The goal is to model how a simplified email system behaves internally, using OOP so that
each real-world concept (an email, a user, an inbox) becomes its own class with its own
data and responsibilities. It is a teaching/demonstration project that shows how objects
collaborate to produce a working feature.

### Objectives
- ✅ Demonstrate **encapsulation** — each class hides and owns its own data.
- ✅ Demonstrate **composition** — objects built from other objects (`User` *has-an* `Inbox`,
  `Email` *has-a* `sender`/`receiver`).
- ✅ Demonstrate **magic/dunder methods** (`__init__`, `__str__`) to control object
  creation and string representation.
- ✅ Demonstrate practical use of the **`datetime` module** for timestamping.
- ✅ Show **defensive programming** — empty-inbox and index-bounds validation.
- ✅ Provide a clean, readable **driver (`main`)** that simulates a full user journey.

### What the program can do
| Action | Method chain |
|---|---|
| Create a user | `User(name)` |
| Send an email | `user.send_email(receiver, subject, body)` |
| List inbox | `user.check_inbox()` |
| Read one email | `user.read_email(index)` |
| Delete one email | `user.delete_email(index)` |

---

## 2. 🧰 Technologies & OOP Concepts Used

| Concept | Where it appears | WHY it was used |
|---|---|---|
| **Classes & Objects** | `Email`, `User`, `Inbox` | Each real-world "thing" becomes a reusable blueprint. Objects bundle related data + behaviour, keeping code organized and readable. |
| **Encapsulation** | private-ish attributes like `self.emails`, `self.read` | Each class owns and protects its own state; outside code interacts through methods, not raw internals. |
| **Composition** | `User.__init__` creates `self.inbox = Inbox()`; `Email` stores `sender`/`receiver` User objects | Models "has-a" relationships realistically. Storing *objects* (not strings) lets us reach into `sender.name` / `receiver.inbox` later — far more flexible. |
| **Constructors (`__init__`)** | All three classes | Automatically initialize each new object's starting state (e.g. every user gets its own empty inbox at birth). |
| **Magic method `__str__`** | `Email.__str__` | Controls how an email prints inside a list — turning an ugly `<...object at 0x...>` into a clean one-line summary. Python calls it automatically via `print()`/f-strings. |
| **`datetime` module** | `Email.__init__`, `display_full_email`, `__str__` | Captures the exact creation moment as a real `datetime` object, so we can format it on demand with `.strftime('%Y-%m-%d %H:%M')` (e.g. `2026-07-28 23:13`). |
| **Delegation / Separation of Concerns** | `User` methods forward to `Inbox` | `User` orchestrates; `Inbox` owns list logic & validation. Changing storage later only touches `Inbox`. |
| **Validation / Guard clauses** | `list_emails`, `read_email`, `delete_email` | Early `return` on empty inbox or out-of-range index prevents crashes (`IndexError`) and gives friendly messages. |
| **Entry-point guard** | `if __name__ == '__main__':` | Runs `main()` only when executed directly, so the file can be imported as a module without side effects. |

### Built-in tools
- **`datetime.datetime.now()`** — current local date + time.
- **`datetime.strftime()`** — format a datetime into a custom string.
- **`enumerate(iterable, start=1)`** — loop with a human-friendly 1-based counter.
- **`del list[i]`** — remove an element by position (later items shift down).
- **f-strings** — clean, inline string formatting.

---

## 3. 🏗️ Class Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                          User                                 │
│  Attributes: name, inbox (an Inbox object)                    │
│  Methods:    send_email(), check_inbox(), read_email(),       │
│              delete_email()                                   │
│  Role:       The "actor" — owns an inbox and performs actions │
└───────────────┬───────────────────────────┬───────────────────┘
        owns    │                           │ creates/sends
                ▼                           ▼
┌───────────────────────────────┐   ┌──────────────────────────────────┐
│            Inbox              │   │              Email                │
│ Attributes: emails (list)     │   │ Attributes: sender (User),        │
│ Methods:    receive_email(),  │   │   receiver (User), subject, body, │
│   list_emails(), read_email(),│   │   timestamp (datetime), read(bool)│
│   delete_email()              │   │ Methods:  mark_as_read(),         │
│ Role: stores & validates the  │   │   display_full_email(), __str__() │
│   list of Email objects       │   │ Role: a single message + its data │
└───────────────────────────────┘   └──────────────────────────────────┘
```

### 🔹 `Email` — the message
Represents one email and everything about it.
- **Attributes**
  - `sender` — the `User` object who sent it (object, not string → enables `sender.name`).
  - `receiver` — the `User` object receiving it.
  - `subject`, `body` — text content.
  - `timestamp` — a `datetime` object set once at creation via `datetime.datetime.now()`.
  - `read` — boolean flag, defaults to `False` (unread).
- **Methods**
  - `mark_as_read()` — flips `read` to `True`.
  - `display_full_email()` — prints the full email (From/To/Subject/Received/Body) **and**
    marks it read, since opening it means it's been seen. Uses `strftime` for the time.
  - `__str__()` — returns a compact one-line summary with a `[Read]`/`[Unread]` badge;
    called automatically when the email is printed in a list.

### 🔹 `User` — the account / actor
Represents a person and their capabilities.
- **Attributes**
  - `name` — display name (used in From/To lines and headers).
  - `inbox` — a **fresh `Inbox()`** created in `__init__` (composition: User *has-an* Inbox).
- **Methods**
  - `send_email(receiver, subject, body)` — builds an `Email(sender=self, ...)` and delivers
    it via `receiver.inbox.receive_email(email)`, then prints confirmation.
  - `check_inbox()` — prints a header and delegates to `inbox.list_emails()`.
  - `read_email(index)` / `delete_email(index)` — delegate to the inbox (which owns the list
    and validation). This keeps `User` thin and `Inbox` in charge of its own data.

### 🔹 `Inbox` — the storage & validation layer
Owns the collection of received emails.
- **Attributes**
  - `emails` — a list of `Email` objects (order = arrival order).
- **Methods**
  - `receive_email(email)` — `append`s to the end of the list.
  - `list_emails()` — if empty, prints "Your inbox is empty." and returns early; otherwise
    loops with `enumerate(..., start=1)` and prints `f'{i}. {email}'` (triggering `__str__`).
  - `read_email(index)` — validates (empty check + bounds check), converts 1-based → 0-based,
    then calls `display_full_email()` on the chosen email.
  - `delete_email(index)` — same validation, then `del self.emails[actual_index]` (later
    emails shift down one number) and prints confirmation.

---

## 4. 🔁 Step-by-Step Execution Flow (what `main()` does)

> Run order is driven by `main()`, invoked under the `if __name__ == '__main__':` guard.

1. **`tory = User('Tory')`** — A `User` object is created. Its `__init__` sets `name='Tory'`
   and creates a private, empty `Inbox` (`tory.inbox.emails == []`).
2. **`ramy = User('Ramy')`** — Same for Ramy, with their own separate empty inbox.
3. **`tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')`**
   - Builds `Email(sender=tory, receiver=ramy, subject='Hello', body=..., timestamp=now, read=False)`.
   - Calls `ramy.inbox.receive_email(email)` → the email is appended to **Ramy's** list.
   - Prints: `Email sent from Tory to Ramy!`
4. **`ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')`**
   - Builds a reply `Email` and delivers it into **Tory's** inbox; prints confirmation.
5. **`ramy.check_inbox()`**
   - Prints header `Ramy's Inbox:` and calls `ramy.inbox.list_emails()`.
   - Inbox is not empty, so it loops and prints:
     `1. [Unread] From: Tory | Subject: Hello | Time: YYYY-MM-DD HH:MM`
     (`[Unread]` because `read` is still `False`; `__str__` builds this line).
6. **`ramy.read_email(1)`**
   - Passes validation (inbox not empty, index 1 is valid).
   - Converts 1-based `1` → 0-based `0`, fetches the email, calls `display_full_email()`.
   - That prints the full From/To/Subject/Received/Body block **and sets `read = True`**.
7. **`ramy.delete_email(1)`**
   - Passes validation, converts index, runs `del self.emails[0]`.
   - Ramy's list becomes empty; prints `Email deleted.`
8. **`ramy.check_inbox()`**
   - Calls `list_emails()` again; now `not self.emails` is `True`, so it prints
     `Your inbox is empty.` and returns early.

### Data-flow at a glance
```
User.send_email()
   └─> creates Email object
        └─> receiver.inbox.receive_email(email)   # email appended to list
User.check_inbox()
   └─> Inbox.list_emails()  ──> print triggers Email.__str__()
User.read_email(i)
   └─> Inbox.read_email(i) ──> Email.display_full_email() ──> mark_as_read()
User.delete_email(i)
   └─> Inbox.delete_email(i) ──> del emails[i]
```

---

## 5. 📝 Annotated Source Code

> The fully commented code lives in **`email_simulator_annotated.py`** (delivered alongside
> this README). It is the exact original program with detailed line-by-line comments and
> with the pasted markdown artifacts restored to valid Python (`__init__`, `__str__`,
> `__name__`, `datetime.datetime.now()`, and `<` / `>`). **No logic was changed.**
> A copy of that annotated source is reproduced below for convenience.

```python
import datetime  # সময় এবং তারিখ নিয়ন্ত্রণের জন্য পাইথনের বিল্ট-ইন datetime মডিউল ইম্পোর্ট করা হলো


# ==============================================================================
# ১. Email ক্লাস (ইমেইল অবজেক্টের কাঠামো ও তথ্য সংরক্ষণ)
# ==============================================================================
class Email:
    # **init** কনস্ট্রাক্টর: নতুন একটি ইমেইল অবজেক্ট তৈরি হওয়ার সময় এটি স্বয়ংক্রিয়ভাবে রান হয়
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender          # প্রেরকের User অবজেক্টটি সংরক্ষণ করে
        self.receiver = receiver      # প্রাপকের User অবজেক্টটি সংরক্ষণ করে
        self.subject = subject        # ইমেইলের বিষয়বস্তু (Subject) সংরক্ষণ করে
        self.body = body              # ইমেইলের মূল বার্তা (Body) সংরক্ষণ করে
        self.timestamp = datetime.datetime.now()  # ইমেইলটি ঠিক যে মুহূর্তে তৈরি হচ্ছে তখনকার সময় ও তারিখ রেকর্ড করে
        self.read = False             # ইমেইলটি পড়া হয়েছে কি না তার অবস্থা রাখে (ডিফল্টভাবে অপঠিত/False থাকে)

    # ইমেইলকে 'পঠিত' (Read) হিসেবে চিহ্নিত করার মেথড
    def mark_as_read(self):
        self.read = True  # self.read এর মান বদলে True করে দেয়

    # ইমেইলের সমস্ত তথ্য (প্রেরক, প্রাপক, বিষয়, সময় ও বডি) বিস্তারিত স্ক্রিনে দেখানোর মেথড
    def display_full_email(self):
        self.mark_as_read()  # ইউজার পুরো মেইলটি ওপেন করায় এটিকে 'পঠিত' হিসেবে চিহ্নিত করা হলো
        print('\n--- Email ---')
        print(f'From: {self.sender.name}')      # প্রেরকের অবজেক্ট থেকে তার নাম প্রিন্ট করে
        print(f'To: {self.receiver.name}')        # প্রাপকের অবজেক্ট থেকে তার নাম প্রিন্ট করে
        print(f'Subject: {self.subject}')        # বিষয় প্রিন্ট করে
        # strftime ব্যবহার করে তারিখ ও সময়কে 'YYYY-MM-DD HH:MM' ফরম্যাটে সুন্দর করে দেখায়
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')              # মূল বার্তা প্রিন্ট করে
        print('------------\n')

    # ডান্ডার/স্পেশাল মেথড **str__: যখন এই ইমেইল অবজেক্টটিকে ইনবক্সের তালিকায় ১ লাইনে প্রিন্ট করা হবে, তখন এটি রান হয়
    def __str__(self):
        # শর্টহ্যান্ড if-else: read সত্য হলে 'Read', মিথ্যা হলে 'Unread' স্ট্যাটাস সেট করে
        status = 'Read' if self.read else 'Unread'
        # এক লাইনের সংক্ষিপ্ত রূপ ফেরত দেয়
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"


# ==============================================================================
# ২. User ক্লাস (ব্যবহারকারীর অ্যাকাউন্ট ও অ্যাকশন পরিচালনা)
# ==============================================================================
class User:
    # একজন নতুন ইউজার তৈরির কনস্ট্রাক্টর
    def __init__(self, name):
        self.name = name     # ইউজারের নাম সেট করে (যেমন: "Tory" বা "Ramy")
        self.inbox = Inbox() # প্রতিটি ইউজারের জন্য একটি নিজস্ব Inbox অবজেক্ট তৈরি করে

    # অন্য কোনো ইউজারকে ইমেইল পাঠানোর মেথড
    def send_email(self, receiver, subject, body):
        # প্রেরক হিসেবে নিজেকে (self) এবং প্রাপক হিসেবে receiver-কে দিয়ে একটি Email অবজেক্ট তৈরি করে
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        # প্রাপকের ইনবক্সে (receiver.inbox) তৈরি করা ইমেইলটি জমা দেয়
        receiver.inbox.receive_email(email)
        # সফলভাবে পাঠানো নিশ্চিত করার বার্তা প্রিন্ট করে
        print(f'Email sent from {self.name} to {receiver.name}!\n')

    # ইউজারের ইনবক্সের তালিকা দেখার মেথড
    def check_inbox(self):
        print(f"\n{self.name}'s Inbox:") # ইউজারের নাম দিয়ে হেডার প্রিন্ট করে
        self.inbox.list_emails()          # ইউজারের Inbox অবজেক্টের list_emails() মেথডটি রান করে

    # নির্দিষ্ট নম্বরের ইমেইলটি পড়ার মেথড
    def read_email(self, index):
        self.inbox.read_email(index) # Inbox ক্লাসের read_email-এ ইনডেক্সটি পাঠিয়ে দেয়

    # নির্দিষ্ট নম্বরের ইমেইলটি মুছে ফেলার মেথড
    def delete_email(self, index):
        self.inbox.delete_email(index) # Inbox ক্লাসের delete_email-এ ইনডেক্সটি পাঠিয়ে দেয়


# ==============================================================================
# ৩. Inbox ক্লাস (ইনবক্সে জমা থাকা ইমেইল ম্যানেজমেন্ট ও ভ্যালিডেশন)
# ==============================================================================
class Inbox:
    # নতুন ইনবক্স চালুর কনস্ট্রাক্টর
    def __init__(self):
        self.emails = [] # আগত সমস্ত Email অবজেক্ট জমা রাখার জন্য একটি খালি পাইথন লিস্ট তৈরি করে

    # নতুন কোনো ইমেইল আসলে সেটি লিস্টে যুক্ত (append) করার মেথড
    def receive_email(self, email):
        self.emails.append(email)

    # ইনবক্সে থাকা সব ইমেইল ১, ২, ৩ নম্বর দিয়ে তালিকায় দেখানোর মেথড
    def list_emails(self):
        # ইনবক্স যদি খালি থাকে (লিস্টে কিছু না থাকলে)
        if not self.emails:
            print('Your inbox is empty.\n')
            return # মেথড থেকে বের হয়ে যায়
        print('\nYour Emails:')
        # enumerate দিয়ে ১ থেকে কাউন্ট শুরু করে (start=1) লিস্টের প্রতিটি ইমেইল প্রিন্ট করে
        # ইমেইলটি প্রিন্ট হওয়ার সময় Email ক্লাসের **str** মেথডটি কল হয়
        for i, email in enumerate(self.emails, start=1):
            print(f'{i}. {email}')

    # ইউজার প্রদত্ত নম্বর অনুযায়ী ইমেইল পড়ার মেথড
    def read_email(self, index):
        # ইনবক্সে কোনো ইমেইল না থাকলে
        if not self.emails:
            print('Inbox is empty.\n')
            return
        # ইউজার ১-ভিত্তিক নম্বর দেয় (১, ২, ৩), কিন্তু পাইথন লিস্ট ০-ভিত্তিক (0, 1, 2)। তাই ১ বিয়োগ করা হলো
        actual_index = index - 1
        # ইনডেক্স যদি ঋণাত্মক হয় অথবা লিস্টের মোট সাইজের সমান বা বেশি হয় (ভুল নম্বর দিলে)
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        # সঠিক নম্বর হলে ঐ নির্দিষ্ট ইমেইল অবজেক্টটির display_full_email() মেথডটি কল করা হয়
        self.emails[actual_index].display_full_email()

    # ইউজার প্রদত্ত নম্বর অনুযায়ী ইমেইল ডিলিট করার মেথড
    def delete_email(self, index):
        # ইনবক্স খালি কি না তা চেক করা
        if not self.emails:
            print('Inbox is empty.\n')
            return
        # ০-ভিত্তিক ইনডেক্সে রূপান্তর
        actual_index = index - 1
        # ইনডেক্স সীমার বাইরে কি না চেক করা
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        # del কিওয়ার্ড ব্যবহার করে লিস্ট থেকে নির্দিষ্ট ইমেইল অবজেক্টটি ডিলিট করে দেওয়া
        del self.emails[actual_index]
        print('Email deleted.\n')


# ==============================================================================
# ৪. main() ফাংশন (সম্পূর্ণ সিস্টেমটি পরীক্ষা/সিমুলেট করার প্রধান ড্রাইভার)
# ==============================================================================
def main():
    # step 1: Tory এবং Ramy নামে ২টি User অবজেক্ট তৈরি করা হলো
    tory = User('Tory')
    ramy = User('Ramy')
    # step 2: Tory থেকে Ramy-কে ইমেইল পাঠানো হলো
    tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
    # step 3: Ramy থেকে Tory-কে ইমেইল পাঠানো হলো
    ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')
    # step 4: Ramy তার ইনবক্সের তালিকা চেক করল (এখানে Tory-র পাঠানো অপঠিত মেইলটি দেখাবে)
    ramy.check_inbox()
    # step 5: Ramy তার ১ নম্বর ইমেইলটি ফুল ওপেন করে পড়ল (যার ফলে মেইলটি 'Read' হয়ে যাবে)
    ramy.read_email(1)
    # step 6: Ramy ১ নম্বর ইমেইলটি তার ইনবক্স থেকে মুছে ফেলল
    ramy.delete_email(1)
    # step 7: Ramy আবার ইনবক্স চেক করল (ইনবক্স ফাঁকা হয়ে গেছে দেখতে পাবে)
    ramy.check_inbox()


# প্রোগ্রামটি সরাসরি রান করা হলে main() ফাংশনটি চালু হবে
if __name__ == '__main__':
    main()
```

---

## 6. ▶️ How to Run

```bash
python email_simulator_annotated.py
```

### Expected console output (shape)
```
Email sent from Tory to Ramy!

Email sent from Ramy to Tory!

Ramy's Inbox:

Your Emails:
1. [Unread] From: Tory | Subject: Hello | Time: 2026-07-28 23:13

--- Email ---
From: Tory
To: Ramy
Subject: Hello
Received: 2026-07-28 23:13
Body: Hi Ramy, just saying hello!
------------

Email deleted.

Ramy's Inbox:
Your inbox is empty.
```
*(Exact timestamps reflect the moment each email is created on your machine.)*

---

## 7. 🧠 Key Takeaways

- **Objects over strings:** storing `sender`/`receiver` as `User` objects enables clean
  dot-access (`self.sender.name`) and future extensibility.
- **Composition:** `User` *has-an* `Inbox`; `Inbox` *has-many* `Email`s — a realistic
  "has-a" model built without inheritance.
- **Magic methods:** `__init__` guarantees valid starting state; `__str__` makes objects
  print beautifully with zero extra effort at the call site.
- **Validation:** guard clauses (empty check + bounds check + 1-based→0-based conversion)
  turn potential crashes into friendly messages.
- **Separation of concerns:** `User` delegates storage/validation to `Inbox`, so each class
  stays small, focused, and easy to change independently.

---

*Built as an OOP learning project — Python 3, standard library only (just `datetime`).*
