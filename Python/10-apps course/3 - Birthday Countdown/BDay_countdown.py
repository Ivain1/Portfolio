import datetime

def print_header():
    print('------------------------')
    print('---Birthday Countdown---')
    print('------------------------')

def get_user_birthday():
    print('When were you born?')
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))

    bday = datetime.date(year,month,day)

    return(bday)

def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(year=target_date.year, month=original_date.month, day=original_date.day)

    dt = this_year - target_date
    #duration = datetime.timedelta(date2,date2)
    return(dt.days)


def print_birthday_info(days):
    if days < 0:
        print("You had your birthday {0} days ago this year".format(abs(days)))
        timeleft = 365 - abs(days)
        print("It is {0} days until your next birthday".format(timeleft))
    elif days > 0:
        print("Your birthday is in {0} days!".format(abs(days)))
    else:
        print("Today is your birthday, congratulations!")


    #return('It is {0} days until your birthday'.format(days))

def main():
    print_header()
    bday = get_user_birthday()
    #print(bday)
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday,today)
    #print(number_of_days)
    print_birthday_info(number_of_days)

main()