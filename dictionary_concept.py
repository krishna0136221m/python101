#
# a={
#     "name":"krishna",
#     "age":20,
#     "gender":"male"
# }
# a.pop("name")
# print(a)
# print(len(a))
# print(a.get("age"))
# print(a.keys())
# print(a.values())
# print(a.items())
# b=a.copy()
# print(b)
# b["name"]="dg"
# print(b)
# print(a)
# print(b.clear())

a={
    "name":"krishna",
    "gender":"male",
    "profession":"front end developer"
}
for i in a:
    print(i ,":", a[i], end="\n")