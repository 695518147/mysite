from django.test import TestCase
from pypinyin import pinyin, Style
# Create your tests here.

print(pinyin("中信1", style=Style.FIRST_LETTER))

for i in pinyin("中信1", style=Style.FIRST_LETTER):
    print(i[0])

