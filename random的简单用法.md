### 1、random.random()

```python
# 用于生成一个0到1之间的随机浮点数
import random

for i in range(3):
    res1 = random.random()
    print(res1)
    
# 计算结果如下
0.18421829325562544
0.6566530220129191
0.8157515108808124

```



### 2、random.uniform(a,b)

``` python
# 用于生成一个（a,b）之间的浮点数
import random

for i in range(3):
    res2 = random.uniform(5,10)
    print(res2)
    
# 计算结果如下
6.623042327936614
8.951904113207451
9.000317802568471

```

### 3、random.randint(a,b)

``` python
# 用于生成一个指定范围的整数（int）。其中参数a是下限，参数b是上限，生成随机数，注意左开右闭（a,b]
import random

for i in range(3):
    res3 = random.randint(5,10)
    print(res3)
    
# 计算结果如下
5
8
9

```

### 4、random.randrange()

``` python
import random

# 　随机整数
a = random.randint(0, 99)

# 随机选取0到100之间的偶数
b = random.randrange(0, 101, 2)

print(a)
print(b)

```

### 5、random.choice() 随机字符

``` python
import random
res = random.choice('asdfghjkertyui#$%^&*')
print(res)
```

### 6、random.sample() 多个字符串中选取特定数量的字符

``` python
import random
res = random.sample('hsahfjkhfaowbncbajdk',3)
print(res)

```

### 7、random.shuffle() 洗牌、打乱顺序

``` pyton
import random
items = [1,2,3,4,5,6]
random.shuffle(items)
print(items)
```

