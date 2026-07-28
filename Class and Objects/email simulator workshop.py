# Act as an expert Python Developer and Technical Writer. I have a Python Object-Oriented Programming (OOP) code for an "Email Simulator". I want you to perform two specific tasks based on this code.

# **Task 1: Python Code with Detailed Comments**
# Return the exact Python code I provide. DO NOT change, add, or remove a single line of the actual code or logic. Your only job is to add highly detailed, line-by-line comments (in Bengali/English) explaining what each class, method, and line is doing, why it is used, and how it works. 

# **Task 2: Detailed Markdown (.md) Documentation**
# Create a comprehensive and professional `README.md` file for this project. The documentation must include:
# 1. Project Purpose & Objectives.
# 2. Technologies and OOP Concepts used (e.g., Classes, Composition, Magic methods, datetime module) with explanations of WHY they were used.
# 3. Class Architecture (Detailed breakdown of Email, User, and Inbox classes).
# 4. Step-by-Step Execution Flow / Data Flow (explain what happens in the main function step-by-step).
# 5. The annotated source code.

# Please present "Task 1" and "Task 2" in clearly separated sections. 

# Here is the code:



import datetime  # সময় এবং তারিখ নিয়ন্ত্রণের জন্য পাইথনের বিল্ট-ইন datetime মডিউল ইম্পোর্ট করা হলো


# ==============================================================================
# ১. Email ক্লাস (ইমেইল অবজেক্টের কাঠামো ও তথ্য সংরক্ষণ)
# ==============================================================================
class Email:
    # __init__ কনস্ট্রাক্টর: নতুন একটি ইমেইল অবজেক্ট তৈরি হওয়ার সময় এটি স্বয়ংক্রিয়ভাবে রান হয়
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender          # প্রেরকের User অবজেক্টটি সংরক্ষণ করে
        self.receiver = receiver      # প্রাপকের User অবজেক্টটি সংরক্ষণ করে
        self.subject = subject        # ইমেইলের বিষয়বস্তু (Subject) সংরক্ষণ করে
        self.body = body              # ইমেইলের মূল বার্তা (Body) সংরক্ষণ করে
        self.timestamp = datetime.datetime.now()  # ইমেইলটি ঠিক যে মুহূর্তে তৈরি হচ্ছে তখনকার সময় ও তারিখ রেকর্ড করে
        self.read = False             # ইমেইলটি পড়া হয়েছে কি না তার অবস্থা রাখে (ডিফল্টভাবে অপঠিত/False থাকে)

    # ইমেইলকে 'পঠিত' (Read) হিসেবে চিহ্নিত করার মেথড
    def mark_as_read(self):
        self.read = True  # self.read এর মান বদলে True করে দেয়

    # ইমেইলের সমস্ত তথ্য (প্রেরক, প্রাপক, বিষয়, সময় ও বডি) বিস্তারিত স্ক্রিনে দেখানোর মেথড
    def display_full_email(self):
        self.mark_as_read()  # ইউজার পুরো মেইলটি ওপেন করায় এটিকে 'পঠিত' হিসেবে চিহ্নিত করা হলো
        print('\n--- Email ---')
        print(f'From: {self.sender.name}')      # প্রেরকের অবজেক্ট থেকে তার নাম প্রিন্ট করে
        print(f'To: {self.receiver.name}')        # প্রাপকের অবজেক্ট থেকে তার নাম প্রিন্ট করে
        print(f'Subject: {self.subject}')        # বিষয় প্রিন্ট করে
        # strftime ব্যবহার করে তারিখ ও সময়কে 'YYYY-MM-DD HH:MM' ফরম্যাটে সুন্দর করে দেখায়
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')              # মূল বার্তা প্রিন্ট করে
        print('------------\n')

    # ডান্ডার/স্পেশাল মেথড __str__: যখন এই ইমেইল অবজেক্টটিকে ইনবক্সের তালিকায় ১ লাইনে প্রিন্ট করা হবে, তখন এটি রান হয়
    def __str__(self):
        # শর্টহ্যান্ড if-else: read সত্য হলে 'Read', মিথ্যা হলে 'Unread' স্ট্যাটাস সেট করে
        status = 'Read' if self.read else 'Unread'
        # এক লাইনের সংক্ষিপ্ত রূপ ফেরত দেয় (যেমন: [Unread] From: Tory | Subject: Hello | Time: 2026-07-28 23:13)
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

# email_obj = Email('alice@example.com', 'bob@example.com', 'Hello', 'Hi Bob!')
# print(email_obj.sender)
# print(email_obj.subject)
# print(email_obj.read)
# email_obj.mark_as_read()
# print(email_obj.read)


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
        # প্রেরক হিসেবে নিজেকে (self) এবং প্রাপক হিসেবে receiver-কে দিয়ে একটি Email অবজেক্ট তৈরি করে
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        # প্রাপকের ইনবক্সে (receiver.inbox) তৈরি করা ইমেইলটি জমা দেয়
        receiver.inbox.receive_email(email)
        # সফলভাবে পাঠানো নিশ্চিত করার বার্তা প্রিন্ট করে
        print(f'Email sent from {self.name} to {receiver.name}!\n')

    # ইউজারের ইনবক্সের তালিকা দেখার মেথড
    def check_inbox(self):
        print(f"\n{self.name}'s Inbox:") # ইউজারের নাম দিয়ে হেডার প্রিন্ট করে
        self.inbox.list_emails()          # ইউজারের Inbox অবজেক্টের list_emails() মেথডটি রান করে

    # নির্দিষ্ট নম্বরের ইমেইলটি পড়ার মেথড
    def read_email(self, index):
        self.inbox.read_email(index) # Inbox ক্লাসের read_email-এ ইনডেক্সটি পাঠিয়ে দেয়

    # নির্দিষ্ট নম্বরের ইমেইলটি মুছে ফেলার মেথড
    def delete_email(self, index):
        self.inbox.delete_email(index) # Inbox ক্লাসের delete_email-এ ইনডেক্সটি পাঠিয়ে দেয়

# alice = User("Alice")
# bob = User("Bob")

# alice.send_email(bob, "Hello", "Hi Bob, how are you?")

# print(len(bob.inbox.emails))


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

    # ইনবক্সে থাকা সব ইমেইল ১, ২, ৩ নম্বর দিয়ে তালিকায় দেখানোর মেথড
    def list_emails(self):
        # ইনবক্স যদি খালি থাকে (লিস্টে কিছু না থাকলে)
        if not self.emails:
            print('Your inbox is empty.\n')
            return # মেথড থেকে বের হয়ে যায়
        
        print('\nYour Emails:')
        # enumerate দিয়ে ১ থেকে কাউন্ট শুরু করে (start=1) লিস্টের প্রতিটি ইমেইল প্রিন্ট করে
        # ইমেইলটি প্রিন্ট হওয়ার সময় Email ক্লাসের __str__ মেথডটি কল হয়
        for i, email in enumerate(self.emails, start=1):
            print(f'{i}. {email}')

    # ইউজার প্রদত্ত নম্বর অনুযায়ী ইমেইল পড়ার মেথড
    def read_email(self, index):
        # ইনবক্সে কোনো ইমেইল না থাকলে
        if not self.emails:
            print('Inbox is empty.\n')
            return
        
        # ইউজার ১-ভিত্তিক নম্বর দেয় (১, ২, ৩), কিন্তু পাইথন লিস্ট ০-ভিত্তিক (0, 1, 2)। তাই ১ বিয়োগ করা হলো
        actual_index = index - 1
        
        # ইনডেক্স যদি ঋণাত্মক হয় অথবা লিস্টের মোট সাইজের সমান বা বেশি হয় (ভুল নম্বর দিলে)
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        
        # সঠিক নম্বর হলে ঐ নির্দিষ্ট ইমেইল অবজেক্টটির display_full_email() মেথডটি কল করা হয়
        self.emails[actual_index].display_full_email()

    # ইউজার প্রদত্ত নম্বর অনুযায়ী ইমেইল ডিলিট করার মেথড
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
        
        # del কিওয়ার্ড ব্যবহার করে লিস্ট থেকে নির্দিষ্ট ইমেইল অবজেক্টটি ডিলিট করে দেওয়া
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
    
    # step 5: Ramy তার ১ নম্বর ইমেইলটি ফুল ওপেন করে পড়ল (যার ফলে মেইলটি 'Read' হয়ে যাবে)
    ramy.read_email(1)
    
    # step 6: Ramy ১ নম্বর ইমেইলটি তার ইনবক্স থেকে মুছে ফেলল
    ramy.delete_email(1)
    
    # step 7: Ramy আবার ইনবক্স চেক করল (ইনবক্স ফাঁকা হয়ে গেছে দেখতে পাবে)
    ramy.check_inbox()

# প্রোগ্রামটি সরাসরি রান করা হলে main() ফাংশনটি চালু হবে
if __name__ == '__main__':
    main()

# current_time = datetime.datetime.now()
# print(current_time.strftime('%H:%M:%S'))