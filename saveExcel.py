import pandas as pd
import numpy as np

f = open('volunteer_list.json', 'r')
s = f.read()
l = np.array(s.split('],'))
new_l = [l[0].split(',')]
for i in range(1, len(l)):
    temp = l[i]
    new_t = temp.replace(' ', '').replace('[', '').replace('"', '').replace(']', '')
    tmp_l = new_t.split(',')
    new_l.append(tmp_l)

print(np.shape(new_l))
df1 = pd.DataFrame(np.array(new_l))

with pd.ExcelWriter('test_save.xlsx') as writer:
    df1.to_excel(writer)