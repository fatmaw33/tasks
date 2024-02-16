#!/usr/bin/env python
# coding: utf-8

# In[1]:


num1=int(input("input first num: "))
num2=int(input("input second num: "))
result= num1 if num1>num2 else num2
print("max num is: ",result)


# In[2]:


num1=int(input("input first num: "))
num2=int(input("input second num: "))
num3=int(input("input third num: "))
if(num1>num2):
 print("max num is: ",num1)
elif(num1>num3):
     print("max num is: ",num1)
elif(num2>num3):
     print("max num is: ",num2)        
else:
 print("max num is: ",num3)


# In[5]:


num=int(input("input the num: "))
result= "the num is postive" if num>=0 else "the num is negative"
print(result)


# In[6]:


year=int(input("input the year: ")) 
result="the year is leap " if year%4 == 0 and year%400 == 0 else "the year is not leap " 
print(result)


# In[7]:


l=["سبت" , "الاحد" , "الاثنان" , "التلات", "الاربع", "الخميس" , "الجمعه"]
for x in l:
    print(x)


# In[8]:


start=ord("a")
end=start+26
while(start < end):
    print(chr(start))
    start+=1


# In[9]:


i=1
num=int(input("input the num: "))
while (i<=12):
    print(num*i)
    i+=1


# In[10]:


x=1
while(x<=100):
    print(x)
    x+=1


# In[ ]:




