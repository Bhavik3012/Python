def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="Bhavik", power="Invisibility")
print_kwargs(name="Bhavik", power="Invisibility", enemy="Dr. Evil")
print_kwargs(power="Invisibility")
print_kwargs(name="Bhavik")
