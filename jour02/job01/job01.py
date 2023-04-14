def my_print_hello():
    print("Hello world")
my_print_hello()

def my_print_name(Name):
    print(Name)
my_print_name("Nicolas")
my_print_name("Paul")
my_print_name("jules")

def Add(num1 , num2):
    print(num1 + num2)
Add(2, 3)
Add(5, 10)
Add(10, 20)

def getHello():
    return "Hello la plateforme"

message = getHello()
print(message)

num1 = 10
num2 = 20
opertor = "+"
def calcul(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    else:
        print("operator invalide")

print(calcul(10, "+",20))
print(calcul(10, "-",20))
print(calcul(10, "*",20))
print(calcul(num1, opertor, num2))


def check_number(nombre):
    if nombre > 0: 
        print("positiv")
    elif nombre < 0:
        print("negatif")    
    else:
        print("nombre egale zero")      
check_number(5)      


def dev_type(language):
    if language == "javascript":
        print("Tu es un developpeur web")
    elif language == "python":
        print("tu es un developpeur IA")
    elif language == "java":
        print("tu es un developpeur logiciel")
    elif language == "reactjs":
        print("tu es un developpeur mobile")
    else:
        print("un jour, je serai le meilleur developpeur")

dev_type("java")

dev_type("javascript")



