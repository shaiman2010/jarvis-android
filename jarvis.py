
import datetime

print("=" * 35)
print("       J.A.R.V.I.S.")
print("  Just A Rather Very Intelligent System")
print("=" * 35)

print("\nJARVIS: Systems initialized.")
print("JARVIS: Good to see you, boss!")

while True:
    command = input("\nYou: ").strip().lower()

    if command in ("exit", "quit", "shutdown"):
        print("JARVIS: Shutting down. Goodbye, boss!")
        break

    elif command == "help":
        print("Commands: hello, time, date, help, exit")

    elif command in ("hello", "hi", "hey"):
        print("JARVIS: Hello, boss. How can I help?")

    elif command == "time":
        print("JARVIS:", datetime.datetime.now().strftime("%I:%M %p"))

    elif command == "date":
        print("JARVIS:", datetime.date.today().strftime("%d %B %Y"))

    else:
        print("JARVIS: I don't know that command yet.")
