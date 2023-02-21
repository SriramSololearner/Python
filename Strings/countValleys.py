def countingValleys(steps, path):
    # Write your code here
    altitude=0
    valleys=0
    
    for step in path:
        if step=="U":
            altitude+=1
            
            if altitude == 0 :
                valleys+=1
            
        else:
            altitude-=1
        
        
            
    return valleys


steps=8
path=['U','D','D','D','U','D','U','U']

#output = 8