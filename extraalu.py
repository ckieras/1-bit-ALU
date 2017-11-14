from blogic import *
#Corinne Kieras HD 11/5/2017
#Extra ALU computes ALU output for a 4 bit ALU
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
    #output + carry out
    return 2* bor( band(band((bxor(inva,band(ena,a))),(band(b,enb))),(band(bnot(f0),bnot(f1)))),
                   band((band(bnot(f0),f1)), (bor((band(b, enb)), (bxor(inva,band(ena,a)))))),
                   band(band(f0,bnot(f1)),(bnot(band(b,enb)))), band((bxor(c_i, bxor((bxor(inva,band(ena,a)))
                ,(band(b,enb))))),(band(f0,f1))))+ bor((band((band(f0,f1)),(bxor(inva,band(ena,a))),band(b,enb))),
                                                       (band(c_i,bxor(bxor(inva,band(ena,a)),band(b,enb)))))

#carry out function that returns the carry out for f0,f1,inva,ena,enb, c_i,a,b
def carryout(f0, f1,inva,ena,enb,c_i,a,b):
    return bor((band((band(f0, f1)), (bxor(inva, band(ena, a))), band(b, enb))),
        (band(c_i, bxor(bxor(inva, band(ena, a)), band(b, enb)))))

#uses the carryout function to return each ALU within a 4-bit ALU
def fouralu(f0, f1,inva,ena,enb,c_i,a,b,a1,b1,a2,b2,a3,b3):
    #carry out for MSB
    carryoutmsb = carryout(f0,f1,inva,ena,enb,(carryout(f0,f1,inva,ena,enb,(carryout(f0, f1,inva,ena,enb,(carryout(f0, f1,inva,ena,enb,c_i,a,b)),a1,b1)),a2,b2)),a3,b3)
    #uses carry out and ALU function to compute all of the alu outputs, from alu4 to alu3
    alu4 = alu(f0,f1,inva,ena,enb,(carryout(f0,f1,inva,ena,enb,(carryout(f0, f1,inva,ena,enb,(carryout(f0, f1,inva,ena,enb,c_i,a,b)),a1,b1)),a2,b2)),a3,b3)
    alu3 = alu(f0,f1,inva,ena,enb,(carryout(f0, f1,inva,ena,enb,(carryout(f0, f1,inva,ena,enb,c_i,a,b)),a1,b1)),a2,b2)
    alu2 = alu(f0, f1,inva,ena,enb,(carryout(f0, f1,inva,ena,enb,c_i,a,b)),a1,b1)
    alu1 = alu(f0,f1,inva,ena,enb,c_i,a,b)
    return (carryoutmsb,alu4,alu3,alu2,alu1)

#Tests the ALU function and prints the results the 1 bit ALU as well as the 4 bit ALU, includes various outputs for both
print alu(0, 0, 0, 1, 1, 0, 1, 0)
print alu(0, 0, 0, 1, 1, 0, 1, 1)
print alu(1, 1, 0, 1, 1, 1, 1, 1)
print alu(0, 1, 0, 1, 0, 0, 1, 0)
print alu(0, 1, 1, 0, 1, 0, 0, 1)
print fouralu(0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1)
print fouralu(0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0)
print fouralu(0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1)

