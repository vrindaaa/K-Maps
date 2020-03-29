# CSE 101 - IP HW2
# K-Map Minimization 
# Name: Vrinda Narayan
# Roll Number: 2018120
# Section: A
# Group: 8
# Date: 16/10/2018

import copy

def tobinary(numVar,l):
        """to convert all the elements of a list into binary sublist"""
        i=0
        #checks all elements of a given list
        while i<len(l):
                j=0
                num=[]
                #converts the element of the list into binary
                while j<numVar:
                        num=[l[i]%2]+num
                        l[i]=l[i]//2
                        j=j+1
                l[i]=num
                i=i+1
        return l
def toexpression(num,l):
        """to convert a list of pi into an expression"""
        k=['w','x','y','z']
        s=''
        #considers element till the number of variables
        for i in range(len(l)):
                for j in range(num):
                        #when the element is x, the var is not considered
                        if(l[i][j]!='x'):
                                #if value is 1 add variable or else add variable compliment
                                if(l[i][j]==1):
                                        s=s+k[j]
                                else:
                                        s=s+k[j]+"'"
                s=s+'+'
        #to remove the plus in the last of our string
        s1=s[:len(s)-1].split('+')
        #to sort in lexiographic order
        s1.sort()
        s3=''
        for i in range(len(s1)):
                s3+=str(s1[i])+'+'
        return s3[:len(s3)-1]
                        
def minFunc(no_of_var, string):
    """This function inputs a KMAP and Nuber of variables and reduces the KMAP as much as possible"""
    d=string.find('d')
    #dontcare list contains elements with dontcare conditions
    if string[d+2]=='-':
        dontcare=[]
    else:
        dontcare=string[d+3:len(string)-1].split(',')
        for i in range(len(dontcare)):
            #converts all the elements into int as they are in form of string
            dontcare[i]=int(dontcare[i])
    d1={}
    variable=string[1:d-2].split(',')#contains the function when it takes value as 1
    if (variable==['']):
            #when function is NULL
            return 0
    for i in range(len(variable)):
        #converts all the elements into int as they are in form of string
        variable[i]=int(variable[i])
        #d1 is the dictionary which has all elements of variable as keys
        d1[variable[i]]=0
    #converts both the list into binary to find pi
    dontcare=tobinary(no_of_var,dontcare)
    variable=tobinary(no_of_var,variable)
    #l is a list whose first element contains all the elements
    l=['','']
    l[0]=variable
    #l[1] has all implicants with 2 terms
    l[1]=find2pi(no_of_var, variable, dontcare)
    #the subsequent values of l[i] have terms with 4 terms etc till the no_of_var is done
    for i in range(2,no_of_var+1):
            l=l+['']
            l[i]=find4pi(no_of_var,l[i-1])
    #returns 1 when all terms are covered in function
    if l[len(l)-1]!=[]:
            return 1
    
    w=list(d1.keys())
    binary_d1=tobinary(no_of_var,w) #a seperate list with all elements in binary form for comparisn purposes
    i=len(l)-2
    epi=[]
    #considering the case of variables as 4, if its less the subsequent if statements won't be evaluated
    #checking implicant with 8 terms
    if((l[i]!=[])and(check(d1)==0)and(i>=0)):
            for s in range(len(l[i])):
                    a=0
                    for t in d1:
                            y=test(no_of_var,l[i][s],binary_d1[a])
                            a=a+1
                            if((y==1)and(d1[t]==0)): #if the pi is essential and not included already in expression it is added to epi
                                    d1[t]+=1
                                    epi=epi+[l[i][s]]
    i=i-1
    #checking implicant with 4 terms
    if((l[i]!=[])and(check(d1)==0)and(i>=0)):
            for s in range(len(l[i])):
                    a=0
                    for t in d1:
                            y=test(no_of_var,l[i][s],binary_d1[a])
                            a=a+1
                            if((y==1)and(d1[t]==0)):
                                    d1[t]+=1
                                    epi=epi+[l[i][s]]
    i=i-1
    #checking implicant with 2 terms
    if((l[i]!=[])and(check(d1)==0)and(i>=0)):
            for s in range(len(l[i])):
                    a=0
                    for t in d1:
                            y=test(no_of_var,l[i][s],binary_d1[a])
                            a=a+1
                            if((y==1)and(d1[t]==0)):
                                    d1[t]+=1
                                    epi=epi+[l[i][s]]
    i=i-1
    #checking implicant with 1 terms
    if((l[i]!=[])and(check(d1)==0)and(i>=0)):
            for s in range(len(l[i])):
                    a=0
                    for t in d1:
                            y=test(no_of_var,l[i][s],binary_d1[a])
                            a=a+1
                            if((y==1)and(d1[t]==0)):
                                    d1[t]+=1
                                    epi=epi+[l[i][s]]
    epi = makeunique(epi) #to remove repeating terms from epi
    string=toexpression(no_of_var,epi) #contains the string with our variables
    return string

def find2pi(num, variable, dontcare=[]):
    """this function converts the elements of the variable into implicants of 2 terms"""
    variable_=variable+dontcare
    final=copy.deepcopy(variable_)
    lis=[]
    #if two elements differ by just 1 bit it replaces it with 'x'
    for i in range(len(variable_)-1):
        for j in range(i+1,len(variable_)):
            t=checkvars(num, variable_[i], variable_[j])
            if (t!=-1):
                temp=list(final[j])
                temp[t]='x'
                lis=lis+[temp]
    return makeunique(lis)

def find4pi(num, l):
        """this function further combines the pi into pi with twice number of terms"""
        x=[]
        for i in range(len(l)-1):
                for j in range(i+1,len(l)):
                        t=checkvars(num, l[i], l[j])
                        if (t!=-1):
                                temp=list(l[i])
                                temp[t]='x'
                                x=x+[temp]
        return makeunique(x)
                        
def checkvars(numVar,var1,var2):
    """to check if two lists have only one element different"""
    x=-1
    for i in range(numVar):
        if (var1!=var2 and (var1[0:i]+var1[i+1:len(var1)])==(var2[0:i]+var2[i+1:len(var2)])):
            x=i
    return x

def makeunique(l):
    """deletes the repeated elements from a list"""
    final_list = []
    #removes the elements which are already in the final_list
    for num in l: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list

def check(d):
        """to check if all the elements in the dict have been covered by current selected pi, returns 1 if all are covered"""
        #sees if any one of the value of d is 0 and returns 0
        x=1
        for i in d:
                if d[i]==0:
                        x=0
        return x

def test(num,a,b):
        """returns 1 if an element is covered in a particular pi otherwise returns 0"""
        #if the elements of both these number match or that of the implicant is 'x'
        x=0
        y=0
        for i in range(num):
                y=y+1
                if ((a[i]==b[i])or(a[i]=='x')):
                        x=x+1
        #checks if all of the variables lie in it then returns 1
        if (x==y):
                return 1
        else:
                return 0

if __name__=='__main__':
        #when this file is run as the main file the program itself taked the input and runs the minFunc
        x=int(input('No. of variables : '))
        y=input('Function : ')
        z=minFunc(x,y)
        print('Simplified Expression : ', z)



	
	
	

	
