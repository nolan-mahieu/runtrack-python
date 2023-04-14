def determiner_triangle(a, b, c):
  
  if a + b > c and b + c > a and a + c > b:
    
    if a == b == c:
        print("Le triangle est équilatéral.")
    elif a == b or b == c or c == a:
      if a * a + b * b == c * c or b * b + c * c == a * a or c * c + a * a == b * b:
        print("Le triangle est isocèle et rectangle.")
      else:
        print("Le triangle est isocèle.")
    elif a * a + b * b == c * c or b * b + c * c == a * a or c * c + a * a == b * b:
        print("Le triangle est rectangle.")
    else:
        print("Le triangle est quelconque.")
  else:
        print("Impossible de construire un triangle avec ces longueurs.")
a = 10 
b = 10
c = 5
determiner_triangle(a, b, c)
