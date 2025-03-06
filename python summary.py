--data types--
bool - int - float - str
True - False #caps
or - and
/ simple division // int division
--simple structures--
if 1:
    asd
elif:
    "wtf elif xd"
else:
    asd

while 1:
    asd

for i in range(x): #for convension if you dont care for the i name you use "_"
    asd
for s in string:
    #iterates using the string

in => variable in [list] #checks if a value is in a data structure

for i in listVariable:
    n == listValue
    break
else:
    n wasnt found #you can use an else in a for which will recognize that you didnt exit with the break

--data structures--
list #a list automatically handeled
[72,24,54] #an example list
data in list #will automatically search in the list

dict = {"X": "valueAsociatedWithX"}
dic[valueName] = x #sets value x on field valueName or creates it if new

--strings--
print > ("string," + variable) #how to print multiple things (auto adds a space)
print(f"hello, {variable}") #format strings #most common
variable = input("asd?") #get a string imput from keyboard
string1 == string2 #comparison between strings WORKS as expected
print("asd", end="") #deletes the \n #print() prints a \n
print("x" * 4) #will print xxxx

--functions--
def main():
    functions
def nameOfTheFunction(Parameters): #parameters can me just name ej: (n, r, a)
    asd
main() #this is needed in order to run the code



--file handling --
try:    #tries to do something and if it fails (which would break the code)
    asd
except codeError: #if it detects the specified error, it will do what you asked it for
    pass #just skips the code

fileVariable = open("filename.filetype", "r/w/etc") #file variable REMEMBER TO CLOSE
fileVariable.close
with open("filename.filetype", "r/w/etc") as variable #while with open file


--web developing--
-flask-
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET","POST","DELETE"]) #get is automatically sended if no methods declare
def index():
    name = request.args.get("name", NONE) #gets an input from the user, if no imput replace none for the default value
    return render_template("file.html", placeholderParameter= name) #replace a placeholder in the html file for some actual value

