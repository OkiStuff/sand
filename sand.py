
null = ("null")
false = ("false")
true = ("true")
filename = null
ScriptError = false

def sandSyntaxError( error ):
    ScriptError = true

if ScriptError == true:
    print("Error. Could not detect type of error.")
else:
    