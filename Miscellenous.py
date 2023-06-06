from collections import Counter;
#Write a function to find the common longest prefix string among an array of strings, if there is no common prefix, return an empty string.
strs=["flower","flow","flight"];
string_array=sorted(strs);
l=len(string_array);
first_word=strs[0];
last_word=strs[l-1];
output="";
iterator=min(len(first_word),len(last_word));
for i in range(iterator):
    if first_word[i]==last_word[i]:
        output=output+first_word[i];
    else:
        break;
print(output);

#Write a Program to remove duplicate from a given dictionary:
d={1:"hello",2:"sam",3:"good",4:"morning",5:"hello",6:"good"};
set1=set();
key_to_remove=[];
for k,v in d.items():
    if v in set1:
        key_to_remove.append(k);
    else:
        set1.add(v);
for key in key_to_remove:
    d.pop(key);
print(d);

#Write a program to print even length words in a string:
s="python is simple and dynamic laungage";
words=s.split();
for x in words:
    if len(x)%2==0:
        print(x);


#Write a program to check if two list contains atleast one common word:

def checker(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    intersection_set = s1.intersection(s2)
    if len(intersection_set) > 0:
        print(True)
    else:
        print(False)

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 5, 8, 9]
checker(list1, list2)

#write a program to find most repeated word in a text file
f=open('file.text');
text=f.read();
tokens=text.split();
word_count=Counter(tokens);
most_common_word, count = max(word_count.items(), key=lambda x: x[1])
print(most_common_word);
print(count);

#Write a program to sort tuples of tuples by their 2nd element:-
T1=(('a',23),('b',37),('c',9),('d',2));
sorted_tuple=sorted(T1, key=lambda x :x[1]);
print(sorted_tuple);

#Program to print a inverted star pattern:
n=5;
for i in range(n,0,-1):
    print(" " * (n-i),end="");
    print("*" * i);

#Write a Program to iterate two list simultaneously and display from list 1 in original order and list2 in reverse order:
list1=[1,2,3,4];
list2=[100,200,300,400];
for iterator1,iterator2 in zip(list1,reversed(list2)):
    print(iterator1,iterator2);
