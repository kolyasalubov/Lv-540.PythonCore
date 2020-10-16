s="""Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

print(s.count("better"))
print(s.count("never"))
print(s.count("is"))
print("Upper string: ", s.upper())
a1=s.replace("i", "&")
print("Replaced string: ", a1)

n=int(input("Enter number: "))
d=(n//1000)*(n%10)*((n//100)%10)*((n%100)//10)
print("Result of multiplication: ", d)
print("Sorted number: ", sorted(str(n)))
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
n1,n2=n2,n1
print(n1,n2)
