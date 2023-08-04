readfile = open('questions.txt', 'r')
ques_ans = [line.strip() for line in readfile.readlines()]
readfile.close()
print(ques_ans)

c = 0
for ques in ques_ans:
    q, a = ques.split('=')
    # print(f'{q[0]} = ')
    # ans = input()
    ans = input(f'{q} = ')
    if ans == a:
        c += 1


writefile = open('result.txt', 'w')

writefile.write(f'Your final score is {c}/{len(ques_ans)}')

writefile.close()