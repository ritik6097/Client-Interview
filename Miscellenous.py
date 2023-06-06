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
set=set();
key_to_remove=[];
for k,v in d.items():
    if v in set:
        key_to_remove.append(k);
    else:
        set.add(v);
for key in key_to_remove:
    d.pop(key);
print(d);

