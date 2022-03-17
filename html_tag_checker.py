def collector(word):
    lis1 = []
    lis2 = []
    count=0
    cot=0


    for char in word:

        if char == "<":

            lis1.append(count)

        elif char ==">":


            lis2.append(count)
        count+=1

    return lis1,lis2,count


def split(word):
    lister=[]
    for char in word:
        if char==" ":
            continue
        else:
            lister.append(char)
    return lister


def tag_checker():
    dic = {
        "<html>": "</html",
        "<p>": "</P>",
        "<div>": "</div>",
        "<head>": "</head>",
        "<title>": "</title>",
        "<body>": "</body>",
        "<span>": "</span>",
        "<table>": "</table>",
        "<thead>": "</thead>",
        "<tbody>": "</tbody>",
        "<tr>": "</tr>",
        "<td>": "</td>",
        "<script>": "</script>",
        "<ul>": "</ul>",
        "<li>": "</li>",
        "<strong>": "</strong>",
        "<hr>": "</>",
        "<img>": "</>",
        "<!DOCTYPE html>": ""

        }
    new_list=[]
    file_1=input("enter the source file ")
    file_2=open(file_1)

    file=file_2.read()
    file_3 =file.split()
    list1,list2,num=collector(file)
    lists=[]
    for i in range(len(list1)):
        v=list2[i]
        x=list1[i]
        lists.append(file[x:v+1])

    my_list=[]
    new_list2 = []


    print(lists)
    for tag in lists:
        balanced = True
        if tag in dic.keys():
            my_list.append(tag)

        elif tag in dic.values():
            if len(my_list) == 0:
                print("invalid tag pair")
                balanced = False
                break
            else:
                if dic[my_list[-1]] == tag:
                    my_list.pop()
                else:
                    print("invalid tag pair ")
                    break

    if len(my_list) == 0 and balanced:
        print(" valid tag pair ")





tag_checker()



