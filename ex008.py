#   _age caculator

def age_calculator():
    age = input("your age :_")
    age_inseconds = int(age) * 365 * 24 * 60 * 60
    print("your age in second is {}".format(age_inseconds), "seconds")

age_calculator()
