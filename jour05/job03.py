def tapisserie(n): 

	bord="+s" 
	for i in range(n+1): bord +="-" 
	bord+="+" 
  

	print(bord) 
	for i in range(n+1): 
		tapis="" 
		for j in range(n-i): tapis+="#" 
		tapis+=" " 
		for j in range(i): tapis+="#" 
		print("|" + tapis + "|") 

	print(bord)  
  
tapisserie(10)



