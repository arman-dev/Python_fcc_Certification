# ==========================================================================================
# Email Simulator — Annotated (Fully Commented) Version  |  Task 1
# ------------------------------------------------------------------------------------------
# NOTE ON RESTORATION:
#   The pasted source had a few markdown/rendering artifacts where double underscores and
#   symbols got auto-linked or HTML-escaped, e.g.:
#       **init**        ->  __init__
#       **str**         ->  __str__
#       **name**        ->  __name__
#       [datetime.datetime.now](http://...)()  ->  datetime.datetime.now()
#       &lt;  /  &gt;    ->  <  /  >
#   These have been restored to the *true* Python source so the file actually runs.
#   NO logic, structure, variable name, or line of code has been added, removed, or changed —
#   only the original rendering damage was repaired and extra comments were added.
# ==========================================================================================

import datetime  # সময় এবং তারিখ নিয়ন্ত্রণের জন্য পাইথনের বিল্ট-ইন datetime মডিউল ইম্পোর্ট করা হলো
# ^ WHY: `datetime` gives us access to datetime.datetime.now(), which returns the current
#   local date+time as a datetime object. We use it to stamp every Email with the exact
#   moment it was created. Importing the whole module (not `from datetime import datetime`)
#   means we call it as datetime.datetime.now() below.


# ==============================================================================
# ১. Email ক্লাস (ইমেইল অবজেক্টের কাঠামো ও তথ্য সংরক্ষণ)
# ==============================================================================
# WHY a separate Email class? An email is a distinct "thing" in the domain — it bundles
# together related data (who sent it, who received it, subject, body, time, read-status)
# and related behaviour (mark-as-read, display). This is classic encapsulation: one class
# owns one concept, so the rest of the program talks to Email objects instead of juggling
# loose variables.
class Email:
    # **init** কনস্ট্রাক্টর: নতুন একটি ইমেইল অবজেক্ট তৈরি হওয়ার সময় এটি স্বয়ংক্রিয়ভাবে রান হয়
    # __init__ is the constructor / initializer. Python calls it automatically the instant
    # you write Email(...). Its job is to set up the brand-new object's starting state.
    def __init__(self, sender, receiver, subject, body):
        # `self` = the specific object currently being built. Every attribute we attach to
        # self belongs to THIS email instance only.

        self.sender = sender          # প্রেরকের User অবজেক্টটি সংরক্ষণ করে
        # ^ We store the whole User object (not just a name string). This is *composition /
        #   association*: an Email "has-a" sender. Keeping the object means we can later read
        #   sender.name, sender.inbox, etc. — far more flexible than a frozen string.

        self.receiver = receiver      # প্রাপকের User অবজেক্টটি সংরক্ষণ করে
        # ^ Same idea for the recipient: store the User object so we can access their
        #   attributes (e.g. receiver.name when printing, or receiver.inbox when delivering).

        self.subject = subject        # ইমেইলের বিষয়বস্তু (Subject) সংরক্ষণ করে
        # ^ Plain string holding the email's subject line.

        self.body = body              # ইমেইলের মূল বার্তা (Body) সংরক্ষণ করে
        # ^ Plain string holding the actual message content.

        self.timestamp = datetime.datetime.now()  # ইমেইলটি ঠিক যে মুহূর্তে তৈরি হচ্ছে তখনকার সময় ও তারিখ রেকর্ড করে
        # ^ datetime.datetime.now() returns a datetime object with the current local
        #   date AND time (year, month, day, hour, minute, second, microsecond). We capture
        #   it once, at creation, so every email permanently remembers when it was born.
        #   Because it's stored as a real datetime object (not a string), we can format it
        #   nicely later with .strftime(...) AND compare/sort emails by time if needed.

        self.read = False             # ইমেইলটি পড়া হয়েছে কি না তার অবস্থা রাখে (ডিফল্টভাবে অপঠিত/False থাকে)
        # ^ A boolean flag tracking read-state. It defaults to False because a freshly
        #   received email has not been opened yet. Toggling this to True is how we get the
        #   "Unread"/"Read" badge in the inbox listing.

    # ইমেইলকে 'পঠিত' (Read) হিসেবে চিহ্নিত করার মেথড
    # A tiny, single-responsibility method. Encapsulating the flag change here means no
    # outside code has to know HOW read-state is stored; they just call mark_as_read().
    def mark_as_read(self):
        self.read = True  # self.read এর মান বদলে True করে দেয়
        # ^ Flip the flag. After this call, __str__ will show "[Read]" instead of "[Unread]".

    # ইমেইলের সমস্ত তথ্য (প্রেরক, প্রাপক, বিষয়, সময় ও বডি) বিস্তারিত স্ক্রিনে দেখানোর মেথড
    # The "detailed view" — the equivalent of clicking an email open in a real client.
    def display_full_email(self):
        self.mark_as_read()  # ইউজার পুরো মেইলটি ওপেন করায় এটিকে 'পঠিত' হিসেবে চিহ্নিত করা হলো
        # ^ Opening/reading an email logically means it has now been seen, so we mark it
        #   read as a side-effect of displaying it. (Reuses the method above — no duplication.)

        print('\n--- Email ---')
        # ^ Visual header to separate the email block from other console output.

        print(f'From: {self.sender.name}')      # প্রেরকের অবজেক্ট থেকে তার নাম প্রিন্ট করে
        # ^ self.sender is a User object; `.name` reaches into that object's attribute.
        #   This dot-chaining (self.sender.name) is the payoff of storing objects, not strings.

        print(f'To: {self.receiver.name}')        # প্রাপকের অবজেক্ট থেকে তার নাম প্রিন্ট করে
        # ^ Same object-attribute access, but on the receiver side.

        print(f'Subject: {self.subject}')        # বিষয় প্রিন্ট করে
        # ^ f-string interpolation drops the subject value straight into the output text.

        # strftime ব্যবহার করে তারিখ ও সময়কে 'YYYY-MM-DD HH:MM' ফরম্যাটে সুন্দর করে দেখায়
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        # ^ strftime() converts the datetime object into a formatted STRING:
        #     %Y = 4-digit year, %m = 2-digit month, %d = 2-digit day,
        #     %H = 24-hour hour, %M = minutes.
        #   Result looks like: 2026-07-28 23:13. This is why we kept timestamp as a datetime
        #   object — we can render it any way we like on demand.

        print(f'Body: {self.body}')              # মূল বার্তা প্রিন্ট করে
        # ^ The message text itself.

        print('------------\n')
        # ^ Visual footer to close the block cleanly.

    # ডান্ডার/স্পেশাল মেথড **str__: যখন এই ইমেইল অবজেক্টটিকে ইনবক্সের তালিকায় ১ লাইনে প্রিন্ট করা হবে, তখন এটি রান হয়
    # __str__ is a "magic/dunder" method. Python calls it automatically whenever the object
    # is turned into a string — e.g. by print(email), str(email), or f"{email}". By defining
    # it, we control exactly how an Email shows up inside the inbox list: one neat summary
    # line instead of the ugly default "<__main__.Email object at 0x...>".
    def __str__(self):
        # শর্টহ্যান্ড if-else: read সত্য হলে 'Read', মিথ্যা হলে 'Unread' স্ট্যাটাস সেট করে
        status = 'Read' if self.read else 'Unread'
        # ^ Ternary expression (Python's one-line if/else). It returns 'Read' when the flag
        #   is True and 'Unread' otherwise — used for the [Read]/[Unread] badge.

        # এক লাইনের সংক্ষিপ্ত রূপ ফেরত দেয় (যেমন: [Unread] From: Tory | Subject: Hello | Time: 2026-07-28 23:13)
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
        # ^ Build and RETURN the compact one-liner. Note we again use sender.name (object
        #   access) and strftime() (datetime formatting) — consistent with display_full_email.


# email_obj = Email('alice@example.com', 'bob@example.com', 'Hello', 'Hi Bob!')
# print(email_obj.sender)
# print(email_obj.subject)
# print(email_obj.read)
# email_obj.mark_as_read()
# print(email_obj.read)
# ^ (Original quick-test snippet, left commented out exactly as provided.)


# ==============================================================================
# ২. User ক্লাস (ব্যবহারকারীর অ্যাকাউন্ট ও অ্যাকশন পরিচালনা)
# ==============================================================================
# WHY a User class? A user is the "actor" of the system: it has an identity (name) and it
# owns an Inbox. Bundling the actions (send / check / read / delete) as methods on User
# gives the program a natural, readable API: tory.send_email(ramy, ...) — reads like
# English and keeps all user behaviour in one place.
class User:
    # একজন নতুন ইউজার তৈরির কনস্ট্রাক্টর
    def __init__(self, name):
        self.name = name     # ইউজারের নাম সেট করে (যেমন: "Tory" বা "Ramy")
        # ^ Simple identifier used for display and for From:/To: lines in emails.

        self.inbox = Inbox() # প্রতিটি ইউজারের জন্য একটি নিজস্ব Inbox অবজেক্ট তৈরি করে
        # ^ KEY composition relationship: every User "has-an" Inbox, created right here.
        #   Because this runs in __init__, each user automatically gets their OWN separate,
        #   empty inbox the moment they exist — no one shares inboxes by accident.

    # অন্য কোনো ইউজারকে ইমেইল পাঠানোর মেথড
    # The send-side of the workflow. Notice the User never touches the internals of the
    # receiver's inbox directly — it delegates to receive_email(). That keeps each class
    # responsible for its own data (encapsulation / low coupling).
    def send_email(self, receiver, subject, body):
        # প্রেরক হিসেবে নিজেকে (self) এবং প্রাপক হিসেবে receiver-কে দিয়ে একটি Email অবজেক্ট তৈরি করে
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        # ^ Create the Email object. sender=self means "the user doing the sending is ME".
        #   Using keyword arguments makes the call self-documenting and order-independent.

        # প্রাপকের ইনবক্সে (receiver.inbox) তৈরি করা ইমেইলটি জমা দেয়
        receiver.inbox.receive_email(email)
        # ^ Deliver it: reach into the receiver's Inbox object and hand over the email.
        #   This is the "mail delivery" step — the message now physically lives in the
        #   recipient's email list.

        # সফলভাবে পাঠানো নিশ্চিত করার বার্তা প্রিন্ট করে
        print(f'Email sent from {self.name} to {receiver.name}!\n')
        # ^ User feedback confirming the action, using both names via object attribute access.

    # ইউজারের ইনবক্সের তালিকা দেখার মেথড
    # A convenience wrapper so outside code can call user.check_inbox() without knowing the
    # Inbox class exists — a cleaner public interface.
    def check_inbox(self):
        print(f"\n{self.name}'s Inbox:") # ইউজারের নাম দিয়ে হেডার প্রিন্ট করে
        # ^ Print whose inbox we're looking at.
        self.inbox.list_emails()          # ইউজারের Inbox অবজেক্টের list_emails() মেথডটি রান করে
        # ^ Delegate the actual listing to the Inbox object — separation of concerns: User
        #   orchestrates, Inbox knows how to display its own contents.

    # নির্দিষ্ট নম্বরের ইমেইলটি পড়ার মেথড
    def read_email(self, index):
        self.inbox.read_email(index) # Inbox ক্লাসের read_email-এ ইনডেক্সটি পাঠিয়ে দেয়
        # ^ Pure delegation: forward the user-chosen number to the Inbox, which owns the
        #   list and therefore the validation logic.

    # নির্দিষ্ট নম্বরের ইমেইলটি মুছে ফেলার মেথড
    def delete_email(self, index):
        self.inbox.delete_email(index) # Inbox ক্লাসের delete_email-এ ইনডেক্সটি পাঠিয়ে দেয়
        # ^ Same delegation pattern for deletion.


# alice = User("Alice")
# bob = User("Bob")

# alice.send_email(bob, "Hello", "Hi Bob, how are you?")

# print(len(bob.inbox.emails))
# ^ (Original quick-test snippet, left commented out exactly as provided.)


# ==============================================================================
# ৩. Inbox ক্লাস (ইনবক্সে জমা থাকা ইমেইল ম্যানেজমেন্ট ও ভ্যালিডেশন)
# ==============================================================================
# WHY an Inbox class? It isolates all list-management and validation logic (storing,
# listing, reading, deleting emails) in one place. If we later wanted to persist emails to
# a file or database, we'd only touch this class — the User and Email classes wouldn't
# change. That's the maintainability benefit of single responsibility.
class Inbox:
    # নতুন ইনবক্স চালুর কনস্ট্রাক্টর
    def __init__(self):
        self.emails = [] # আগত সমস্ত Email অবজেক্ট জমা রাখার জন্য একটি খালি পাইথন লিস্ট তৈরি করে
        # ^ A fresh, empty Python list per inbox. It will hold Email objects. A list is the
        #   natural choice because order matters (emails arrive in sequence) and we need
        #   indexed access for read/delete by number.

    # নতুন কোনো ইমেইল আসলে সেটি লিস্টে যুক্ত (append) করার মেথড
    def receive_email(self, email):
        self.emails.append(email)
        # ^ append() adds the email to the END of the list, preserving arrival order
        #   (newest email = highest number). Called by User.send_email() during "delivery".

    # ইনবক্সে থাকা সব ইমেইল ১, ২, ৩ নম্বর দিয়ে তালিকায় দেখানোর মেথড
    def list_emails(self):
        # ইনবক্স যদি খালি থাকে (লিস্টে কিছু না থাকলে)
        if not self.emails:
            # ^ An empty list is "falsy" in Python, so `not []` is True. This is the
            #   idiomatic way to test for an empty collection.
            print('Your inbox is empty.\n')
            return # মেথড থেকে বের হয়ে যায়
            # ^ Early return: nothing left to do, so we stop here instead of printing an
            #   empty "Your Emails:" header.

        print('\nYour Emails:')
        # enumerate দিয়ে ১ থেকে কাউন্ট শুরু করে (start=1) লিস্টের প্রতিটি ইমেইল প্রিন্ট করে
        # ইমেইলটি প্রিন্ট হওয়ার সময় Email ক্লাসের **str** মেথডটি কল হয়
        for i, email in enumerate(self.emails, start=1):
            # ^ enumerate() yields pairs of (counter, item). start=1 makes the counter begin
            #   at 1 so the numbers match what a human sees (email #1, #2, #3...) rather
            #   than Python's internal 0-based indexing.
            print(f'{i}. {email}')
            # ^ Because {email} is an object being formatted, Python calls email.__str__()
            #   automatically, producing the one-line summary ([Unread] From: ... | ...).

    # ইউজার প্রদত্ত নম্বর অনুযায়ী ইমেইল পড়ার মেথড
    def read_email(self, index):
        # ইনবক্সে কোনো ইমেইল না থাকলে
        if not self.emails:
            print('Inbox is empty.\n')
            return
            # ^ Guard #1: can't read from an empty inbox; exit gracefully.

        # ইউজার ১-ভিত্তিক নম্বর দেয় (১, ২, ৩), কিন্তু পাইথন লিস্ট ০-ভিত্তিক (0, 1, 2)। তাই ১ বিয়োগ করা হলো
        actual_index = index - 1
        # ^ Translate the human-friendly 1-based number into Python's 0-based list index
        #   (email #1 -> index 0, #2 -> index 1, etc.).

        # ইনডেক্স যদি ঋণাত্মক হয় অথবা লিস্টের মোট সাইজের সমান বা বেশি হয় (ভুল নম্বর দিলে)
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
            # ^ Guard #2: bounds checking. Catches numbers that are too small (e.g. 0 or
            #   negative) or too large (beyond the last email). Prevents an IndexError crash
            #   and gives the user a friendly message instead.

        # সঠিক নম্বর হলে ঐ নির্দিষ্ট ইমেইল অবজেক্টটির display_full_email() মেথডটি কল করা হয়
        self.emails[actual_index].display_full_email()
        # ^ Fetch the chosen Email object and ask it to display itself. That method also
        #   marks the email as read (see Email.display_full_email).

    # ইউজার প্রদত্ত নম্বর অনুযায়ী ইমেইল ডিলিট করার মেথড
    def delete_email(self, index):
        # ইনবক্স খালি কি না তা চেক করা
        if not self.emails:
            print('Inbox is empty.\n')
            return
            # ^ Guard #1: nothing to delete if the list is empty.

        # ০-ভিত্তিক ইনডেক্সে রূপান্তর
        actual_index = index - 1
        # ^ Same 1-based -> 0-based conversion as in read_email.

        # ইনডেক্স সীমার বাইরে কি না চেক করা
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
            # ^ Guard #2: same bounds validation, preventing invalid access.

        # del কিওয়ার্ড ব্যবহার করে লিস্ট থেকে নির্দিষ্ট ইমেইল অবজেক্টটি ডিলিট করে দেওয়া
        del self.emails[actual_index]
        # ^ `del list[i]` removes the element at that position; every later email shifts
        #   down one number automatically (that's why deleting #1 makes the old #2 become #1).

        print('Email deleted.\n')
        # ^ Confirmation message for the user.


# ==============================================================================
# ৪. main() ফাংশন (সম্পূর্ণ সিস্টেমটি পরীক্ষা/সিমুলেট করার প্রধান ড্রাইভার)
# ==============================================================================
# WHY a main() function? It packages the whole demo into one callable unit, keeps the
# global namespace clean, and makes the script import-safe (importing this file elsewhere
# won't accidentally run the simulation).
def main():
    # step 1: Tory এবং Ramy নামে ২টি User অবজেক্ট তৈরি করা হলো
    tory = User('Tory')
    ramy = User('Ramy')
    # ^ Two users are born. Each __init__ also gave them a private, empty Inbox object.

    # step 2: Tory থেকে Ramy-কে ইমেইল পাঠানো হলো
    tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
    # ^ Creates an Email(sender=tory, receiver=ramy, ...) and appends it to ramy.inbox.emails.

    # step 3: Ramy থেকে Tory-কে ইমেইল পাঠানো হলো
    ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')
    # ^ The reply travels the other way and lands in tory.inbox.emails.

    # step 4: Ramy তার ইনবক্সের তালিকা চেক করল (এখানে Tory-র পাঠানো অপঠিত মেইলটি দেখাবে)
    ramy.check_inbox()
    # ^ Lists ramy's emails. Tory's message shows as "[Unread]" because read is still False.

    # step 5: Ramy তার ১ নম্বর ইমেইলটি ফুল ওপেন করে পড়ল (যার ফলে মেইলটি 'Read' হয়ে যাবে)
    ramy.read_email(1)
    # ^ Opens email #1 -> display_full_email() prints all details AND flips read to True.

    # step 6: Ramy ১ নম্বর ইমেইলটি তার ইনবক্স থেকে মুছে ফেলল
    ramy.delete_email(1)
    # ^ Removes email #1 from ramy's list after passing the empty/bounds checks.

    # step 7: Ramy আবার ইনবক্স চেক করল (ইনবক্স ফাঁকা হয়ে গেছে দেখতে পাবে)
    ramy.check_inbox()
    # ^ The list is now empty, so this triggers the "Your inbox is empty." branch.


# প্রোগ্রামটি সরাসরি রান করা হলে main() ফাংশনটি চালু হবে
if __name__ == '__main__':
    main()
    # ^ The classic Python entry-point guard. __name__ equals '__main__' only when THIS file
    #   is executed directly (e.g. `python email_simulator.py`). If the file is imported as
    #   a module, __name__ is the module name instead, so main() does NOT auto-run — making
    #   the classes reusable without side effects.


# current_time = datetime.datetime.now()
# print(current_time.strftime('%H:%M:%S'))
# ^ (Original bonus snippet showing time-only formatting, left commented out as provided.)
