input = open("C:\Users\joyeung\AppData\Local\Continuum\Anaconda\envs\dato-env\\v4results.csv", 'r')
output = open("C:\Users\joyeung\AppData\Local\Continuum\Anaconda\envs\dato-env\\result_v4.csv", 'w')

i = 1

output.write("ImageId,Label\n")

for line in input:
    output.write(str(i) + ',' + line)
    i += 1
    
input.close()
output.close()
