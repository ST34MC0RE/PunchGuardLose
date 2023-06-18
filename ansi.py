#Obtained at:
#https://replit.com/talk/learn/ANSI-Escape-Codes-in-Python/22803

class fg: ##Changing Text Color
  black = "\u001b[30m"
  red = "\u001b[31m"
  green = "\u001b[32m"
  yellow = "\u001b[33m"
  blue = "\u001b[34m"
  magenta = "\u001b[35m"
  cyan = "\u001b[36m"
  white = "\u001b[37m"

  def rgb(r=0, g=0, b=0): 
    return f"\u001b[38;2;{r};{g};{b}m"

class bg: ##Changing Background Color
  black = "\u001b[40m"
  red = "\u001b[41m"
  green = "\u001b[42m"
  yellow = "\u001b[43m"
  blue = "\u001b[44m"
  magenta = "\u001b[45m"
  cyan = "\u001b[46m"
  white = "\u001b[47m"

  def rgb(r=0, g=0, b=0): 
    return f"\u001b[48;2;{r};{g};{b}m"

class util:
  reset = "\u001b[0m"
  bold = "\u001b[1m"
  underline = "\u001b[4m"
  reverse = "\u001b[7m"