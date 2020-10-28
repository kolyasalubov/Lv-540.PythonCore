def reverse(st):
    changed_str=st.split()
    changed_str.reverse()
    return " ".join(changed_str)
str=input ("Enter your string: " )
print("Reversed string : " , reverse(str))


