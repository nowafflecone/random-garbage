#pass the class

grade_to_pass = ''
current_grade = ''

def passing_grade():
    global grade_to_pass
    while True:
        try: 
            grade_to_pass = float(input("\nPlease input the percentage to pass here: "))
            break
        except ValueError: 
            print("\nOops! Please input a percentage value!")
            grade_to_pass = float(input("Please input the percentage to pass here: "))
            break

def current_grade_now(): 
    global current_grade
    while True:
        try: 
            current_grade = float(input("\nPlease enter your current grade here: "))
            break
        except ValueError: 
            print("\nOops! Please input a percentage value!")
            current_grade = float(input("Please enter your current grade here: "))
            break    


def main():
    global current_grade
    global grade_to_pass
    class_name = input("What class are your trying to pass?: ")
    prompt_for_knowing = input("Do you know what grade you need to pass the class?(YES/NO): ").lower()
    if prompt_for_knowing[:1] == "y":
        passing_grade()
        prompt_for_current = input("Do you know what grade you have in the class?(YES/NO): ").lower()
        if prompt_for_current[:1] =="y":
            current_grade_now()
            if current_grade >= grade_to_pass:
                print("You will pass",class_name,"!")
            elif grade_to_pass > current_grade:
                print("You will not pass",class_name)
        if prompt_for_current[:1] == "n":
            print("You will have to find out before you can continue.")
            current_grade_now()
            if current_grade >= grade_to_pass:
                print("You will pass",class_name,"!")
            elif grade_to_pass > current_grade:
                print("You will not pass",class_name)                
                
    elif prompt_for_knowing[:1] == "n":
        default_selected = input("\nMost of the time, the grade to pass is a C(70%). \nDo you want to default to that?(YES/NO): ").lower()
        if default_selected[:1] == "y":
            default_passing = 70
            prompt_for_current = input("Do you know what grade you have in the class?(YES/NO): ").lower()
            if prompt_for_current[:1] =="y": 
                current_grade_now()
                if current_grade >= default_selected:
                    print("You will pass",class_name,"!")
                elif default_selected > current_grade:
                    print("You will not pass",class_name) 
            if prompt_for_current[:1] == "n":
                print("You will have to find out before you can continue.")
                current_grade_now()
                if current_grade > default_passing:
                    print("You will pass",class_name,"!")
                elif default_passing > current_grade:
                    print("You will not pass",class_name)            
        elif default_selected[:1] == "n":
            passing_grade()
            prompt_for_current = input("Do you know what grade you have in the class?(YES/NO): ").lower()
            if prompt_for_current[:1] =="y":
                current_grade_now()
                if current_grade >= grade_to_pass:
                    print("You will pass",class_name,"!")
                elif grade_to_pass > current_grade:
                    print("You will not pass",class_name)
            if prompt_for_current[:1] == "n":
                print("You will have to find out before you can continue.")
                current_grade_now()
                if current_grade >= grade_to_pass:
                    print("You will pass",class_name,"!")
                elif grade_to_pass > current_grade:
                    print("You will not pass",class_name)                
        

            
main()
    
        