def add_setting(settings, setting):  # নতুন setting যোগ করার function
    key, value = setting  # tuple থেকে key এবং value আলাদা করা
    key = key.lower()  # key-কে lowercase করা
    value = value.lower()  # value-কে lowercase করা

    if key in settings:  # key আগে থেকেই dictionary-তে আছে কিনা দেখা
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."  # থাকলে message return

    settings[key] = value  # নতুন key-value dictionary-তে যোগ করা
    return f"Setting '{key}' added with value '{value}' successfully!"  # সফলভাবে যোগ হলে message return


def update_setting(settings, setting):  # বিদ্যমান setting update করার function
    key, value = setting  # tuple থেকে key এবং value আলাদা করা
    key = key.lower()  # key lowercase করা
    value = value.lower()  # value lowercase করা

    if key in settings:  # key dictionary-তে আছে কিনা দেখা
        settings[key] = value  # থাকলে নতুন value দিয়ে update করা
        return f"Setting '{key}' updated to '{value}' successfully!"  # সফলভাবে update হলে message return

    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."  # key না থাকলে message return


def delete_setting(settings, key):  # setting মুছে ফেলার function
    key = key.lower()  # key lowercase করা

    if key in settings:  # key dictionary-তে আছে কিনা দেখা
        del settings[key]  # key এবং তার value মুছে ফেলা
        return f"Setting '{key}' deleted successfully!"  # সফলভাবে delete হলে message return

    return "Setting not found!"  # key না থাকলে message return


def view_settings(settings):  # সব settings দেখানোর function
    if not settings:  # dictionary খালি কিনা দেখা
        return "No settings available."  # খালি হলে এই message return

    output = "Current User Settings:\n"  # output string-এর শুরু

    for key, value in settings.items():  # dictionary-এর প্রতিটি key-value এর উপর loop চালানো
        output += f"{key.capitalize()}: {value}\n"  # key-এর প্রথম অক্ষর বড় করে output-এ যোগ করা

    return output  # সম্পূর্ণ string return করা (শেষে \n থাকবে)


# Testing-এর জন্য একটি dictionary
test_settings = {
    "theme": "dark",               # Theme setting
    "notifications": "enabled",    # Notification setting
    "volume": "high"               # Volume setting
}
print(view_settings(test_settings))

print(add_setting(test_settings, ("Language", "Bangla")))

print(update_setting(test_settings, ("Theme", "Light")))

print(delete_setting(test_settings, "Volume"))

print(view_settings(test_settings))