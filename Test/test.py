inputs = open('Test/test.txt','r',encoding="UTF-8")
outputs = open('Test/testresult.txt','w',encoding="UTF-8")

for line in inputs:
    outputs.write(line)
    outputs.write(' nr')
outputs.close()
inputs.close()