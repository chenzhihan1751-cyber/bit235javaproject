# -*- coding: utf-8 -*-
"""生成 BIT235 Week 1 十道题的简单讲解（.md + .docx）。"""
import os
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

OUT = r"C:\Users\陈智涵\Desktop\学校作业和其他事情相关文件\大二学校文件总和\大二BIT235_Java作业"

TITLE = "BIT235 Week 1 — 十道题简单讲解"
INTRO = ("这是给自己看的复习笔记，配合 Exercise1–10.java 和「截图」文件夹一起看。\n"
         "每题三块：这题在练什么 → 关键点 → 容易踩的坑。")

EX = [
 (1, "声明变量", "挑对数据类型", [
     "int 装整数 → 年龄 19",
     "double 装小数 → 身高 1.75（Java 里带小数点的数默认就是 double）",
     "char 装【单个】字符，必须用单引号 → 'C'",
     "boolean 只有两个值 true / false → 是否在读 BIT235",
 ], "char 用双引号写成 \"C\" 会编译报错——双引号那是 String。String 用 + 拼接时，"
    "任何类型都会被自动转成文字，所以 println(\"Age: \" + age) 能直接跑。"),

 (2, "算术表达式", "整数除法和取余", [
     "a、b 都是 int，所以 a / b 执行的是【整数除法】",
     "12 / 5 真值是 2.4，但小数部分被【直接砍掉】（不是四舍五入）→ 结果是 2",
     "a % b 是余数：12 = 5 × 2 + 2，所以 12 % 5 = 2",
     "想要 2.4，得把其中一个操作数变成小数：(double) a / b",
 ], "7 / 2 得 3，不是 3.5。负数取余的符号跟着左边走：-7 % 2 = -1，不是 1。"),

 (3, "类型转换", "显式强转 (double)", [
     "total / count 两个都是 int → 结果是 3，不是 3.5",
     "(double) total / count 先把 total 变成 7.0，整个算式就按小数算 → 3.5",
 ], "括号位置是这题的命门：(double) (total / count) 是【错的】——它先把整数除法算完得 3，"
    "再转成 3.0。转换要转在【除号左边】，不能转在整体外面。"),

 (4, "用户输入和比较", "Scanner 读输入 + 基本 if", [
     "import java.util.Scanner;",
     "Scanner scanner = new Scanner(System.in);",
     "scanner.nextInt() 读一个整数",
     "if (age >= 18) { ... } else { ... } —— else 覆盖「不满 18」",
 ], "读文字用 nextLine()，读数字用 nextInt()。这两个别混着用：先 nextInt() 再 nextLine()，"
    "nextLine() 会把回车当成空行读走。这题没踩到，后面题目很容易遇到。"),

 (5, "正负零", "多分支 if / else if / else", [
     "if (number > 0) → Positive",
     "else if (number < 0) → Negative",
     "else → Zero",
     "最后一个 else 天然就是「等于 0」，不必再写 number == 0",
 ], "题目说「一个数」，用 double 读比 int 通用（0.5 能读进来）。"
    "另外注意：判断相等用 ==，一个 = 是赋值，写错了通常编译就报错。"),

 (6, "偶数奇数", "条件里放表达式", [
     "number % 2 == 0 → 偶数（余数为 0）",
     "否则 → 奇数（余数为 1）",
     "核心：把 % 运算的结果直接当条件判断",
 ], "别把 == 写成 =。另外 % 对负数也成立：-3 % 2 = -1（不等于 0），所以 -3 判成奇数，是对的。"),

 (7, "成绩等级", "有序的 if-else if", [
     "必须【从高往低】判断：先 HD（>= 80），再 D（>= 70），再 C、P、最后 F",
     "因为前面不成立才会走到下一行，所以 D 那行只写 >= 70 就够了，不必写 70–79",
 ], "如果从低往高写，mark = 85 会被 mark >= 50 先抓住 → 全都变成 P。"
    "这是 if-else if 最经典的错：顺序决定了逻辑对不对。"),

 (8, "布尔表达式", "用 && 组合条件", [
     "temperature > 30 → \"It is hot.\"",
     "temperature >= 20 && temperature <= 30 → \"It is mild.\"",
     "其余 → \"It is cold.\"",
     "&& 表示两个条件必须【同时】成立",
 ], "Java 不支持数学里的连写：20 <= temperature <= 30 是语法错误，"
    "必须拆成 temperature >= 20 && temperature <= 30。"),

 (9, "逻辑运算符", ".equals() 和 == 的区别", [
     "username.equals(\"admin\") 比的是【里面的文字内容】",
     "username == \"admin\" 比的是【是不是同一个对象】（引用 / 地址）",
     "两个条件同时成立用 && ：equals(...) && equals(...)",
     "Scanner 读进来的字符串是【运行时新建的对象】，和代码里的字面量 \"admin\" 不是同一个对象",
     "所以用 == 会出现：密码明明打对了，却提示 Access denied",
 ], "口诀：基本类型（int / double / char / boolean）用 ==，String 一律用 .equals()。"),

 (10, "迷你决策", "多条件组合", [
     "age >= 18 && hasLicence → \"You can drive independently.\"",
     "age >= 16 && age < 18 && hasLicence → \"You can drive with restrictions.\"",
     "其余 → \"You cannot drive.\"",
     "用的是 Scanner.nextBoolean()，只认小写的 true / false",
 ], "第二个分支里的 age < 18 其实已经被第一个分支挡掉了（18 岁以上有驾照的在上面就返回了），"
    "但写上它更清楚、也不怕以后调整顺序。另外只要【没驾照】就一定会落到最后一个 else。"),
]

SUMMARY = [
    ("1", "变量声明", "int / double / char / boolean 各装什么"),
    ("2", "算术运算", "整数除法会截断，% 取余"),
    ("3", "类型转换", "(double) 转在除号左边才有效"),
    ("4", "输入 + if", "Scanner.nextInt()，简单二选一分支"),
    ("5", "三选一", "if / else if / else，最后的 else 兜底"),
    ("6", "取余判断", "number % 2 == 0 就是偶数"),
    ("7", "分级判断", "if-else if 必须从高往低排"),
    ("8", "复合条件", "&& 连接两个判断，不能连写不等式"),
    ("9", "字符串比较", "String 用 .equals()，别用 =="),
    ("10", "综合条件", "多个条件 && 起来，注意分支顺序"),
]


def build_md():
    L = ["# " + TITLE, "", INTRO, "", "---", ""]
    for n, title, goal, pts, trap in EX:
        L += ["## Exercise %d — %s" % (n, title), "",
              "**这题在练什么：**%s" % goal, "", "**关键点：**", ""]
        L += ["- " + p for p in pts]
        L += ["", "**容易踩的坑：**" + trap, "", "---", ""]
    L += ["## 十题一张表", "", "| # | 主题 | 一句话 |", "|---|---|---|"]
    for a, b, c in SUMMARY:
        L.append("| %s | %s | %s |" % (a, b, c))
    L.append("")
    return "\n".join(L)


def build_docx(path):
    doc = Document()
    st = doc.styles["Normal"]
    st.font.name = "Microsoft YaHei"
    st.font.size = Pt(10.5)
    for s in doc.sections:
        s.top_margin = Inches(0.7); s.bottom_margin = Inches(0.7)
        s.left_margin = Inches(0.8); s.right_margin = Inches(0.8)

    doc.add_heading(TITLE, level=0)
    for line in INTRO.split("\n"):
        p = doc.add_paragraph(line)
        p.runs[0].font.size = Pt(10)
        p.runs[0].font.color.rgb = RGBColor(0x44, 0x44, 0x44)

    for n, title, goal, pts, trap in EX:
        doc.add_heading("Exercise %d — %s" % (n, title), level=1)
        p = doc.add_paragraph()
        p.add_run("这题在练什么：").bold = True
        p.add_run(goal)

        p = doc.add_paragraph()
        p.add_run("关键点：").bold = True
        for x in pts:
            doc.add_paragraph(x, style="List Bullet")

        p = doc.add_paragraph()
        p.add_run("容易踩的坑：").bold = True
        p.add_run(trap)

    doc.add_heading("十题一张表", level=1)
    t = doc.add_table(rows=1, cols=3)
    t.style = "Light Grid Accent 1"
    hdr = t.rows[0].cells
    for i, h in enumerate(["#", "主题", "一句话"]):
        hdr[i].text = h
    for a, b, c in SUMMARY:
        row = t.add_row().cells
        row[0].text = a; row[1].text = b; row[2].text = c

    doc.save(path)


md_path = os.path.join(OUT, "10道题简单讲解.md")
dx_path = os.path.join(OUT, "10道题简单讲解.docx")
with open(md_path, "w", encoding="utf-8", newline="\n") as f:
    f.write(build_md())
build_docx(dx_path)

for p in (md_path, dx_path):
    print(("OK  " if os.path.exists(p) else "FAIL"), os.path.getsize(p), "bytes  ", p)
