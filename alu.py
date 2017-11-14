from blogic import *

#alu function returns the carry out and output for inputs of f0,f1,inva,ena,enb,c_i,a,b
def alu(f0, f1,inva,ena,enb,c_i,a,b):

    #These lines of code break down my process for solving the problem, I started with the decoder and used for lines of code to
    #logic the four ANDs in the decoder and combine them later to get the final product
    band(band((bxor(inva,band(ena,a))),(band(b,enb))),(band(bnot(f0),bnot(f1)))) #equivalent to the output for AB, first AND in the decoder

    band((band(bnot(f0),f1)), (bor((band(b, enb)), (bxor(inva,band(ena,a)))))) #equivalent to the output for the a+b line, second AND in the decoder

    band(band(f0,bnot(f1)),(bnot(band(b,enb)))) #equivalent to the output of not B, third AND in the decoder

    bor((band((band(f0,f1)),(bxor(inva,band(ena,a))),band(b,enb))),(band(c_i,bxor(bxor(inva,band(ena,a)),band(b,enb))))) #line 4 decoder, fourth AND in the decoder, gives the carry-out

    #then I wrote code to get the sum for the output
    band((bxor(c_i, bxor((bxor(inva,band(ena,a))),(band(b,enb))))),(band(f0,f1)))

    #BOR of all the lines necessary for output
    bor(band(band((bxor(inva,band(ena,a))),(band(b,enb))),(band(bnot(f0),bnot(f1)))),band((band(bnot(f0),f1)), (bor((band(b, enb)), (bxor(inva,band(ena,a)))))),band(band(f0,bnot(f1)),(bnot(band(b,enb)))),band((bxor(c_i, bxor((bxor(inva,band(ena,a))),(band(b,enb))))),(band(f0,f1))))
    #2*carry out + output
    #return value is the carry out and output; I combined all the above lines of code to acheive this
    return 2* bor( band(band((bxor(inva,band(ena,a))),(band(b,enb))),(band(bnot(f0),bnot(f1)))),band((band(bnot(f0),f1)), (bor((band(b, enb)), (bxor(inva,band(ena,a)))))), band(band(f0,bnot(f1)),(bnot(band(b,enb)))), band((bxor(c_i, bxor((bxor(inva,band(ena,a))),(band(b,enb))))),(band(f0,f1))))+ bor((band((band(f0,f1)),(bxor(inva,band(ena,a))),band(b,enb))),(band(c_i,bxor(bxor(inva,band(ena,a)),band(b,enb)))))

#Use these to test the ALU output; equivalent to the example given in the project outline
#print alu(0, 0, 0, 1, 1, 0, 1, 0)
#print alu(0, 0, 0, 1, 1, 0, 1, 1)
#print alu(1, 1, 0, 1, 1, 1, 1, 1)
#print alu(0, 1, 0, 1, 0, 0, 1, 0)
#print alu(0, 1, 1, 0, 1, 0, 0, 1)

#print call function formats the alu output
def print_call(f0,f1,inva,ena,enb,c_i,a,b):
    print "alu(",f0,f1,inva,ena,enb,c_i,a,b, ") --> ",
    print alu(f0, f1,inva,ena,enb,c_i,a,b)

#print_section function formats the header tests all combinations for a f0,f1,inva,ena,enb input
def print_section(f0,f1,inva,ena,enb):
    print "F0=",f0,", F1=",f1,", INVA=",inva,", ENA=",ena,", ENB=",enb
    print_call(f0,f1,inva,ena,enb,0,0,0)
    print_call(f0,f1,inva,ena,enb,0,0,1)
    print_call(f0,f1,inva,ena,enb,0,1,0)
    print_call(f0,f1,inva,ena,enb,0,1,1)
    print_call(f0,f1,inva,ena,enb,1,0,0)
    print_call(f0,f1,inva,ena,enb,1,0,1)
    print_call(f0,f1,inva,ena,enb,1,1,0)
    print_call(f0,f1,inva,ena,enb,1,1,1)

#tests all the different inputs
print_section(0,0,0,0,0)
print_section(0,0,0,0,1)
print_section(0,0,0,1,0)
print_section(0,0,0,1,1)
print_section(0,0,1,0,0)
print_section(0,0,1,0,1)
print_section(0,0,1,1,0)
print_section(0,0,1,1,1)
print_section(0,1,0,0,0)
print_section(0,1,0,0,1)
print_section(0,1,0,1,0)
print_section(0,1,0,1,1)
print_section(0,1,1,0,0)
print_section(0,1,1,0,1)
print_section(0,1,1,1,0)
print_section(0,1,1,1,1)
print_section(1,0,0,0,0)
print_section(1,0,0,0,1)
print_section(1,0,0,1,0)
print_section(1,0,0,1,1)
print_section(1,0,1,0,0)
print_section(1,0,1,0,1)
print_section(1,0,1,1,0)
print_section(1,0,1,1,1)
print_section(1,1,0,0,0)
print_section(1,1,0,0,1)
print_section(1,1,0,1,0)
print_section(1,1,0,1,1)
print_section(1,1,1,0,0)
print_section(1,1,1,0,1)
print_section(1,1,1,1,0)
print_section(1,1,1,1,1)




