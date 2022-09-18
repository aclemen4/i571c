from audioop import reverse
import re
import json
import string


def take_input():
    raw_string = input() 
    
    openbrace_list=[] 
    closebrace_list=[]
    try:
        
        patterns_found=re.findall("[0-9]+",raw_string)
        for i in range(len(patterns_found)):
            patterns_found[i]=int(patterns_found[i])
        if(raw_string=="{}"):
           print("[]")
        elif(len(patterns_found)==0):
            print("No valid patterns")
        elif(len(patterns_found)==1):
            print(patterns_found[0])
        else:
            print(patterns_found)
            
        for i,j in enumerate(raw_string):
            #print(i,j)
            if j == "{":
                openbrace_list.append(i);
            if j=="}":
                closebrace_list.append(i);
        openbrace_list.reverse()
        #print(raw_string(openbrace_list[0]:closebrace_list[0]))
        for i in openbrace_list:
            if raw_string[i]=="{":
                raw_string=f1(raw_string,i)
        for j in closebrace_list:
            if raw_string[j]=="}":
                raw_string=f2(raw_string,j)    

        #print(openbrace_list)
        #print(closebrace_list)
        print(raw_string)
        #json_out=json.dumps(raw_string)
        #print(json_out)
        
        #list_true=[]
        #pattern_0=re.findall("\[(\d+),(\d+)\]",raw_string)
        #print("Hi") 
        #print(list(pattern_0[0]))
        #pattern = re.findall("\[\d+\.\.\d+]=\d+",raw_string)
        #print(pattern)
        #pattern2 = re.findall("\[(\d+)\.\.(\d+)]=(\d+)",raw_string)
        #print(pattern2)

        

    except:
        print("No valid patterns")

def f1(raw_string,i):
            #raw_string.replace('{','[')
            raw_string = raw_string[:i] + "[" + raw_string[i+1:]
            return raw_string
def f2(raw_string,j):
            #raw_string.replace('{','[')
            raw_string = raw_string[:j] + "]" + raw_string[j+1:]
            return raw_string
    
if __name__=="__main__":
    take_input()



