# KhamYo : คำย่อ
Thai abbreviation to full text tool

## Install

> pip install khamyo

## How to use

just call replace function and use it!!!

```python
from khamyo import replace

print(replace("ตอนที่ผมเป็นครูอัตราจ้าง ไปอยู่เวรที่รร.ทุกวัน จนกระทั่งได้บรรจุรับราชการเป็นครู จากนั้นได้เลื่อนตำแหน่งเป็นครูใหญ่รร."))
# output: [
# ('ตอนที่ผมเป็นครูอัตราจ้าง ไปอยู่เวรที่โรงเรียนทุกวัน จนกระทั่งได้บรรจุรับราชการเป็นครู จากนั้นได้เลื่อนตำแหน่งเป็นครูใหญ่โรงเรียน',
# tensor(0.9713)),
# ('ตอนที่ผมเป็นครูอัตราจ้าง ไปอยู่เวรที่โรงเรียนทุกวัน จนกระทั่งได้บรรจุรับราชการเป็นครู จากนั้นได้เลื่อนตำแหน่งเป็นครูใหญ่โรงแรม',
# tensor(0.9595))
# ]
```

## How to work

I use Thai abbreviation dictionary for replace text abbreviation to full text (all possibility) and I use wangchanberta pretrained for Sentence Transformer than chose 2 top-k best results.

You can customize dictionary at ```khamyo/data.json```.

## Licenses

| | License |
|:---|:----|
| Source Code and Notebooks | Apache Software License 2.0 |
| Corpora | [Creative Commons Zero 1.0 Universal Public Domain Dedication License (CC0)](https://creativecommons.org/publicdomain/zero/1.0/)|

## Citations

If you use `KhamYo: Thai abbreviation to full text tool` in your project or publication, please cite the library as follows

```
Wannaphong Phatthiyaphaibun. (2021, July 8). KhamYo: Thai abbreviation to full text tool. GitHub. https://github.com/wannaphong/KhamYo
```

or BibTeX entry:

``` bib
@misc{wannaphong,
    author       = {Wannaphong Phatthiyaphaibun},
    title        = {{KhamYo: Thai abbreviation to full text tool}},
    month        = July,
    year         = 2021,
    publisher    = {GitHub},
    url          = {https://github.com/wannaphong/KhamYo}
}
```
