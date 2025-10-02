# Match-case Statement (Switch - case): An alternative to using many 'elif' statements
#                                       Execute some code if a value matches a 'case'
#                                       Cleaner and syntax is more readable

def day_of_week(day):

    match day:
        case "Monday":
            return "Monday"
        case "Tuesday":
            return "Tuesday"
        case "Wednesday":
            return "Wednesday"
        case "Thursday":
            return "Thursday"
        case "Friday":
            return "Friday"
        case "Saturday":
            return "Saturday"
        case "Sunday":
            return "Sunday"
        case _:
            return "It is not a valid day"

# print(day_of_week("."))

def is_weekend(day):
    match day:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False

        case "Saturday" | "Sunday":
            return True

        case _:
            return "It is not a valid day"

print(is_weekend("Monday"))


