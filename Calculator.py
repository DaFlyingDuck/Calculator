import time
import re


def metric():
    a = input("Enter your height in m here:")  # string input
    b = input("Enter your weight in kg here:")

    a_float = re.findall(r"[-+]?\d*\.\d+|\d+", a)  # takes the float value of the string input
    b_float = re.findall(r"[-+]?\d*\.\d+|\d+", b)

    if a_float == [] or b_float == []:  # checks to make sure the input was a valid number
        print("Please Re-enter a number")
        print()
        time.sleep(0.5)
        metric()

    else:  # if it was we go ahead with the values
        global height_m
        height_m = "  ".join(a_float).split()[0]  # this code converts the list into a string and then takes the first value
        global weight_kg
        weight_kg = "  ".join(b_float).split()[0]

        if float(height_m) > 0 and float(weight_kg) >= 0:  # checks to make sure the values are positive
            global height_ft_in
            height_ft_in = 1
            global weight_lb
            weight_lb = 1
            calc()
        else:
            print("Please input a positive non-zero value")
            print()
            time.sleep(0.5)
            metric()


def american():
    c = input("Enter your height in ft and in here:")
    d = input("Enter your weight in lb here:")

    c_float = re.findall(r"[-+]?\d*\.\d+|\d+", c)
    d_float = re.findall(r"[-+]?\d*\.\d+|\d+", d)

    if c_float == [] or d_float == []:
        print("Please Re-enter a number")
        print()
        time.sleep(0.5)
        american()

    elif len(c_float) < 2:
        print("Please re-enter your height value in ft and in")
        print()
        american()

    else:
        height_ft = "  ".join(" ".join(c_float).split()[0])
        height_in = "".join(" ".join(c_float).split()[1])
        weight_lb_bfr = "  ".join(d_float).split()[0]

        if float(height_ft) >= 10 or float(height_in) >= 12:
            print()
            print("Please input a valid number")
            print()
            american()

        else:
            global height_ft_in
            height_ft_in = float(height_ft) * 12 + float(height_in)
            global weight_lb
            weight_lb = 730 * float(weight_lb_bfr)

            if float(height_ft_in) > 0 and float(weight_lb) >= 0:  # checks to make sure the values are positive
                global height_m
                height_m = 1
                global weight_kg
                weight_kg = 1
                calc()
            else:
                print("Please input a positive non-zero value")
                print()
                time.sleep(0.5)
                american()


def calc():
    global bmi
    bmi = (float(weight_kg) * float(weight_lb)) / (float(height_m) * float(height_ft_in)) ** 2

    print()

    if bmi <= 1:
        print("Please input valid integers")
        bmi_calc()

    elif 1 < bmi <= 10:
        print("Your BMI value is", bmi, "and you are extremely underweight")

        print()

        retry = input("Would you like to retry?")
        retry = retry.lower()

        if retry == "y" or retry == "yes":
            bmi_calc()

        else:
            print("Thank you for using my first python program")

    elif 10 < bmi <= 18:
        print("Your BMI value is", bmi, "and you are underweight")

        print()

        retry = input("Would you like to retry?")
        retry = retry.lower()

        if retry == "y" or retry == "yes":
            bmi_calc()

        else:
            print("Thank you for using my first python program")

    elif 18 < bmi <= 24:
        print("Your BMI value is", bmi, "and you have a healthy bmi")

        print()

        retry = input("Would you like to retry?")
        retry = retry.lower()

        if retry == "y" or retry == "yes":
            bmi_calc()

        else:
            print("Thank you for using my first python program")

    elif 24 < bmi <= 29:
        print("Your BMI value is", bmi, "and you are overweight")

        print()

        retry = input("Would you like to retry?")
        retry = retry.lower()

        if retry == "y" or retry == "yes":
            bmi_calc()

        else:
            print("Thank you for using my first python program")

    elif 29 < bmi <= 39:
        print("Your BMI value is", bmi, "and you are obese")

        print()

        retry = input("Would you like to retry?")
        retry = retry.lower()

        if retry == "y" or retry == "yes":
            bmi_calc()

        else:
            print("Thank you for using my first python program")


    elif 39 < bmi <= 65:
        print("Your BMI value is", bmi, "and you are extremely overweight")

        print()

        retry = input("Would you like to retry?")
        retry = retry.lower()

        if retry == "y" or retry == "yes":
            bmi_calc()

        else:
            print("Thank you for using my first python program")

    elif 65 < bmi <= 204:
        print("Your BMI value is", bmi, "and you are morbidly obese")

        print()

        retry = input("Would you like to retry?")
        retry = retry.lower()

        if retry == "y" or retry == "yes":
            bmi_calc()

        else:
            print("Thank you for using my first python program")

    elif bmi > 204:
        print("Your BMI value is", bmi, "and you just broke a world record")
        print()

        retry = input("Would you like to retry?")
        retry = retry.lower()

        if retry == "y" or retry == "yes":
            bmi_calc()

        else:
            print()
            print("Thank you for using my first python program")


def bmi_calc():
    print()
    Measurement_System = input("Metric Measurements? Y/N ") #asks whether to run the american or metric version
    Measurement_System = Measurement_System.lower()

    if Measurement_System == "y" or Measurement_System == "yes":
        metric()

    elif Measurement_System == "n" or Measurement_System == "no":    #american version
        american()

    else:                                               # user didn't input y/n so retry
        print("Please Re-enter your value as Y/N")
        print()
        time.sleep(0.5)
        bmi_calc()


bmi_calc()
