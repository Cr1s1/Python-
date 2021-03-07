# 小练习四：制作表情包转换器
# 涉及知识点：字典

# 【知识补充】字典的split方法：通过指定分隔符对字符串进行切片,返回值是一个列表（本程序中的分隔符是空格符）
message = input(">")
words = message.split(' ')
print(words)
'''
运行结果：
-----------------------------------
>Good morning sunshine
['Good', 'morning', 'sunshine']
-----------------------------------
返回一个包含三个项的列表，每一个项都是一个字符串
'''

print('\n')

# 【正式编写】运用字典将特殊字符表情映射到emoji
message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😀 ",          # Windows用户尽力了。。。
    ":(": "😟",
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
# 【复习】get方法：如果键名存在且输入正确，返回该键所对应的值；如果键名不存在，返回设置的默认值
print(output)

'''
运行结果1：
----------------------------
>Good morning sunshine :)
Good morning sunshine 😀  
----------------------------
运行结果2：
------------------
>I an sad :(
I an sad 😟 
------------------  
'''