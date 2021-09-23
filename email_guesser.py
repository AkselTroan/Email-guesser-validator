import getopt
import sys
from os import system, name
from validate_email import validate_email
from generate_emails import generate_emails


def welcome():
    print(bcolors.OKGREEN + """  _____                 _ _    ____                                  ___    __     __    _ _     _       _             
 | ____|_ __ ___   __ _(_) |  / ___|_   _  ___  ___ ___  ___ _ __   ( _ )   \ \   / /_ _| (_) __| | __ _| |_ ___  _ __ 
 |  _| | '_ ` _ \ / _` | | | | |  _| | | |/ _ \/ __/ __|/ _ \ '__|  / _ \/\  \ \ / / _` | | |/ _` |/ _` | __/ _ \| '__|
 | |___| | | | | | (_| | | | | |_| | |_| |  __/\__ \__ \  __/ |    | (_>  <   \ V / (_| | | | (_| | (_| | || (_) | |   
 |_____|_| |_| |_|\__,_|_|_|  \____|\__,_|\___||___/___/\___|_|     \___/\/    \_/ \__,_|_|_|\__,_|\__,_|\__\___/|_|   
                                                                                                                       
    Written by Aksel Troan
    Found at: https://github.com/AkselTroan/Email-guesser-validator
""" + bcolors.ENDC)

def clear():  # Clearing terminal

    # For Windows
    if name == 'nt':
        _ = system('cls')

    # For MacOS and Linux
    else:
        _ = system('clear')


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main(argv):
    firstname = ""
    lastname = ""
    domain = ""
    year = ""
    registered_emails = []
    generate_file = False
    usage_info = 'Usage: python email_guesser.py -f <firstname> -l <lastname> -y <year> -d <domain> -o <output file>'

    try:
        opts, args = getopt.getopt(argv, "hf:l:y:d:o:",
                                   ["firstname=", "lastname=", "year=", "domain=", "output="])
    except getopt.GetoptError:
        print('Invalid parameters')
        print(usage_info)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print (usage_info)
            sys.exit()
        elif opt in ("-f", "--firstname"):
            firstname = arg
        elif opt in ("-l", "--lastname"):
            lastname = arg
        elif opt in ("-y", "--year"):
            year = arg
        elif opt in ("-d", "--domain"):
            domain = arg
        elif opt in ("-o", "--output-file"):
            file_name = arg
            generate_file = True


    emails = generate_emails(firstname, lastname, domain, year)
    clear() # Clearing the terminal
    welcome()

    for email in emails:
        print("Testing " + email)
        test = validate_email(email)
        if test == True:
            print(bcolors.OKGREEN + "Found Email!" +  bcolors.ENDC)
            registered_emails.append(email)
        else:
            print(bcolors.FAIL + "Does not exist" + bcolors.ENDC)
        print("")
    print("")
    print("All registered emails: ")
    
    if generate_file is True:    
        f = open("./results/" + file_name, "w")
        f.write("All successful validated emails found for " + firstname + " " + lastname + " " + year + " @" + domain + "\n")
        for email in registered_emails:
            f.write(email + "\n")
            print(email)
        f.close()
        print("Results can be found in /results/" + file_name)
    else:
        for email in registered_emails:
            print(email)
        


if __name__ == "__main__":
    main(sys.argv[1:])

