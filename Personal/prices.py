tx= 0.08250 # Texas Sales Tax
x = [249.99,329.99,399.99,649.99]# item price
y=['iPad 10.2 (32GB)','iPad 10.2 (128GB)','iPad Air (64GB)']

t = 70 # tradein

tamano = len(x)

#answer = str(round(answer, 2))

for i in range(tamano):
        total = (x[i] - t) + (x[i] * tx)
        total = str(round(total, 2)) # round 2 decimal places
        #print(f'{y[i]}\n Price: ${x[i]}\t  Total: ${total}\n')
        
        print(f'{y[i]} \tTotal: ${total}')
        #print(y[i],"\t",x[i],'-',t,'=','$',total)