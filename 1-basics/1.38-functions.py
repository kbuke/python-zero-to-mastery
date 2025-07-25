# We can make custom functions that we mark with DEF
def say_hello(name, emoji):
    print(f"Hi {name} {emoji}")

say_hello("Zahra", "🥰")

# Line 2 includes the PARAMETERS name and emoji
# Line 5 containes the arguments of Zahra and 🥰

# The above params and args are called POSITIONAL PARAMETERS and POSITIONAL ARGUMENTS
# this is because their positions matter
# We can use default args if no arguments are given
def say_hi_back(name="Kaan", emoji="😘"):
    print(f"Hi {name} {emoji}")

say_hi_back()

# Can over-ride default args by saying
    # say_hi_back("Zahra")