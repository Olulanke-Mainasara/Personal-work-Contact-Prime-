# Program for the Contact Prime app

contactstorage = []
email1 = []
email2 = []
email3 = []
email4 = []
email5 = []
emailgroup = [email1, email2, email3, email4, email5]
newcontact = []
contactbook = []
new_process = "y"

print("Welcome to Contact Prime\n")
while new_process == "y":
    action = input("What do you want to do?\n(a) View All contacts\n(b) View contacts in a specific email\n(c) Add new contact\n(d) Add new Email for saving contacts\nYour answer: ")
    if action == "a":
        if not contactstorage:
            print("\n")
            print("Sorry, your contacts prime list is empty.")
        else:
            print(contactstorage)
    elif action == "b":
        print("\n")
        whichE = input("which email do you want to view its contacts?\n(a) Email 1\n(b) Email 2\n(c) Email 3\n(d) Email 4\n(e) Email 5\nYour answer: ")
        if whichE == "a":
            if not email1:
                print("\n")
                print("Sorry, this email is empty.")
            else:
                print(email1)
        elif whichE == "b":
            if not email2:
                print("\n")
                print("Sorry, this email is empty.")
            else:
                print(email2)
        elif whichE == "c":
            if not email3:
                print("\n")
                print("Sorry, this email is empty.")
            else:
                print(email3)
        elif whichE == "d":
            if not email4:
                print("\n")
                print("Sorry, this email is empty.")
            else:
                print(email4)
        elif whichE == "e":
            if not email5:
                print("\n")
                print("Sorry, this email is empty.")
            else:
                print(email5)
    elif action == "c":
        print("\n")
        whichact = input("How do you want to save the new number?\n(a) In all emails\n(b) In a particular email\nYour answer: ")
        if whichact == "a":
            print("\n")
            ncontactfname = input("First name: ")
            ncontactlname = input("Last name: ")
            newcontact.append("Contact name: " + " " + ncontactfname + " " + ncontactlname)
            ncontacttel = input("Mobile.no: ")
            newcontact.append("Mobile.no: " + ncontacttel)
            print(newcontact)
            email1.append(newcontact)
            email2.append(newcontact)
            email3.append(newcontact)
            email4.append(newcontact)
            email5.append(newcontact)
            contactstorage.append(newcontact)
            newcontact = []
            print("Contact has been saved.")
        elif whichact == "b":
            print("\n")
            whiche = input("Which email do you want to save it to?\n(a) Email 1\n(b) Email 2\n(c) Email 3\n(d) Email 4\n(e) Email 5\nYour answer: ")
            if whiche == "a":
                print("\n")
                ncontactfname = input("First name: ")
                ncontactlname = input("Last name: ")
                newcontact.append("Contact name: " + " " + ncontactfname + " " + ncontactlname)
                ncontacttelm = (input("Mobile.no: "))
                contactbook.append("Mobile.no: " + ncontacttelm)
                ncontacttelh = (input("Home.no: "))
                contactbook.append("Home.no" + ncontacttelh)
                ncontacttelw = (input("Work.no: "))
                contactbook.append("Work.no" + ncontacttelw)
                newcontact.append(contactbook)
                email1.append(newcontact)
                print("The contact has been saved on the email")
                if newcontact in contactstorage:
                    print("\n")
                    print("This contact already exists in the Contact Prime contact list")
                else:
                    contactstorage.append(newcontact)
                    print("The Contact has been added to the Contact Prime contact list.")
                    newcontact = []
                    contactbook = []
            elif whiche == "b":
                print("\n")
                ncontactfname = input("First name: ")
                ncontactlname = input("Last name: ")
                newcontact.append("Contact name: " + " " + ncontactfname + " " + ncontactlname)
                ncontacttelm = (input("Mobile.no: "))
                contactbook.append("Mobile.no: " + ncontacttelm)
                ncontacttelh = (input("Home.no: "))
                contactbook.append("Home.no" + ncontacttelh)
                ncontacttelw = (input("Work.no: "))
                contactbook.append("Work.no" + ncontacttelw)
                newcontact.append(contactbook)
                email2.append(newcontact)
                print("The contact has been saved on the email")
                if newcontact in contactstorage:
                    print("\n")
                    print("This contact already exists in the contact prime contact list")
                else:
                    contactstorage.append(newcontact)
                    print("The Contact has been added to the Contact Prime contact list.")
                    newcontact = []
            elif whiche == "c":
                print("\n")
                ncontactfname = input("First name: ")
                ncontactlname = input("Last name: ")
                newcontact.append("Contact name: " + " " + ncontactfname + " " + ncontactlname)
                ncontacttelm = (input("Mobile.no: "))
                contactbook.append("Mobile.no: " + ncontacttelm)
                ncontacttelh = (input("Home.no: "))
                contactbook.append("Home.no" + ncontacttelh)
                ncontacttelw = (input("Work.no: "))
                contactbook.append("Work.no" + ncontacttelw)
                newcontact.append(contactbook)
                email3.append(newcontact)
                print("The contact has been saved on the email")
                if newcontact in contactstorage:
                    print("\n")
                    print("This contact already exists in the contact prime contact list")
                else:
                    contactstorage.append(newcontact)
                    print("The Contact has been added to the Contact Prime contact list.")
                    newcontact = []
            elif whiche == "d":
                print("\n")
                ncontactfname = input("First name: ")
                ncontactlname = input("Last name: ")
                newcontact.append("Contact name: " + " " + ncontactfname + " " + ncontactlname)
                ncontacttelm = (input("Mobile.no: "))
                contactbook.append("Mobile.no: " + ncontacttelm)
                ncontacttelh = (input("Home.no: "))
                contactbook.append("Home.no" + ncontacttelh)
                ncontacttelw = (input("Work.no: "))
                contactbook.append("Work.no" + ncontacttelw)
                newcontact.append(contactbook)
                email4.append(newcontact)
                print("The contact has been saved on the email")
                if newcontact in contactstorage:
                    print("\n")
                    print("This contact already exists in the contact prime contact list")
                else:
                    contactstorage.append(newcontact)
                    print("The Contact has been added to the Contact Prime contact list.")
                    newcontact = []
            elif whiche == "e":
                print("\n")
                ncontactfname = input("First name: ")
                ncontactlname = input("Last name: ")
                newcontact.append("Contact name: " + " " + ncontactfname + " " + ncontactlname)
                ncontacttelm = (input("Mobile.no: "))
                contactbook.append("Mobile.no: " + ncontacttelm)
                ncontacttelh = (input("Home.no: "))
                contactbook.append("Home.no" + ncontacttelh)
                ncontacttelw = (input("Work.no: "))
                contactbook.append("Work.no" + ncontacttelw)
                newcontact.append(contactbook)
                email5.append(newcontact)
                print("The contact has been saved on the email")
                if newcontact in contactstorage:
                    print("\n")
                    print("This contact already exists in the contact prime contact list")
                else:
                    contactstorage.append(newcontact)
                    print("The Contact has been added to the Contact Prime contact list.")
                    newcontact = []
    # elif action == "d":
    #     newemail = input("New Email: ")
    #     emailgroup.append((newemail)[])

    print("\n")
    new_process = input("Do You want to do something else?\n Yes = y\n No = n\n Your answer: ")
    print("\n")
