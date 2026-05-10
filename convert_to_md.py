import os
import re

src_dir = r"e:\学习相关\学习笔记\前后端"
dst_dir = r"e:\学习相关\学习笔记\前后端-md"

os.makedirs(dst_dir, exist_ok=True)

def is_code_line(stripped):
    if not stripped:
        return False
    
    strong_code = [
        r'^import\s', r'^from\s', r'^const\s', r'^let\s', r'^var\s',
        r'^function\s', r'^def\s', r'^class\s', r'^return\s',
        r'^export\s', r'^else\s*\{', r'^\)\s*=>',
        r'^<\w+', r'^@',
        r'^app\.', r'^root\.', r'^store\.', r'^xhr\.',
        r'^\$\.', r'^axios', r'^npm\s', r'^pip\s', r'^pip3\s',
        r'^new\s', r'^try\s*\{', r'^catch\s*\(', r'^finally\s*\{',
        r'^if\s*\(', r'^for\s*\(', r'^while\s*\(', r'^switch\s*\(',
        r'^async\s', r'^await\s', r'^yield\s',
        r'^render\s*\(', r'^create\w*', r'^configure',
        r'^\w+\s*=\s*require', r'^\w+\s*\.\s*\w+\s*=\s*',
        r'^type\s+\w+\s*=', r'^interface\s+\w+',
        r'^git\s', r'^node\s', r'^npx\s',
        r'^\w+\.exe\s',
        r'^SELECT\b', r'^INSERT\b', r'^UPDATE\b', r'^DELETE\b', r'^CREATE\b',
        r'^ALTER\b', r'^DROP\b', r'^GRANT\b',
        r'^\$\s', r'^#\s',
        r'^\/\/', r'^\/\*',
        r'^\}\s*\)', r'^\s*\]', r'^\}\s*,', r'^\)\s*,',
        r'^\.\w+\s*\(', r'^\.\w+\s*=',
        r'^\{\{', r'^\%\s',
        r'^\w+\s*\(', r'^\w+\s*:\s*function',
        r'^\w+\s*:\s*\w+\s*\{', r'^\w+\s*:\s*\{',
    ]
    for pattern in strong_code:
        if re.match(pattern, stripped, re.IGNORECASE):
            return True
    
    if re.match(r'^[\w\s,(){}[\]<>.:;=+\-*/&|!~^%\'\"]+$', stripped) and len(stripped) > 6:
        code_keywords = ['=', '=>', '()', '{}', ';']
        count = sum(1 for kw in code_keywords if kw in stripped)
        if '(' in stripped and ')' in stripped:
            count += 1
        if count >= 2:
            return True
    
    return False

def is_explanation_line(stripped, indent_level):
    if not stripped:
        return False
    
    if indent_level <= 1:
        chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', stripped))
        if chinese_chars > 0:
            return True
    
    chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', stripped))
    if chinese_chars == 0:
        return False
    
    starts_with_chinese = bool(re.match(r'^[\u4e00-\u9fff]', stripped))
    if starts_with_chinese:
        return True
    
    chinese_ratio = chinese_chars / max(len(stripped), 1)
    if chinese_ratio > 0.5:
        return True
    
    starters = ['用于', '表示', '创建', '设置', '获取', '提交', '定义', '生成',
                '监听', '将', '当', '在', '通过', '需要', '可以', '该', '即',
                '如果', '因为', '所以', '但', '并', '或', '一个', '这个', '每个',
                '所有', '只有', '此时', '这里', '其中', '其他', '另外', '注意',
                '说明', '例如', '比如', '使', '建立', '也', '还', '就', '都']
    for s in starters:
        if stripped.startswith(s):
            return True
    
    return False

def wrap_inline_code(text):
    text = re.sub(r'`([^`]+)`', r'`\1`', text)
    text = re.sub(r'(?<!`)([\w.]+\s*=\s*[\w.]+(?:\([^)]*\))?)(?!`)', r'`\1`', text)
    text = re.sub(r'(?<!`)([\w.]+\s*\([^)]*\))(?!`)', r'`\1`', text)
    return text

def convert_txt_to_md(content):
    lines = content.split('\n')
    
    while lines and lines[0].strip() == "'''":
        lines = lines[1:]
    while lines and lines[-1].strip() == "":
        lines = lines[:-1]
    while lines and lines[-1].strip() == "'''":
        lines = lines[:-1]
    
    result = []
    code_buffer = []
    in_code = False
    
    def flush_code():
        nonlocal code_buffer, in_code
        if not code_buffer:
            return
        if not in_code:
            result.append("```")
            in_code = True
        for cl in code_buffer:
            result.append(cl)
        code_buffer = []
    
    def end_code():
        nonlocal code_buffer, in_code
        if in_code:
            result.append("```")
            in_code = False
        code_buffer = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        if not stripped:
            if code_buffer:
                code_buffer.append('')
            else:
                if result and result[-1] != '':
                    result.append('')
            i += 1
            continue
        
        indent = len(line) - len(line.lstrip())
        indent_level = indent // 4
        
        if is_code_line(stripped):
            code_buffer.append(stripped)
            i += 1
            continue
        
        if is_explanation_line(stripped, indent_level):
            if code_buffer:
                flush_code()
                end_code()
                if result and result[-1] != '':
                    result.append('')
            
            text = wrap_inline_code(stripped)
            
            if indent_level == 0:
                result.append(f'## {text}')
            elif indent_level == 1:
                result.append(f'### {text}')
            elif indent_level == 2:
                result.append(f'- {text}')
            elif indent_level == 3:
                result.append(f'  - {text}')
            else:
                result.append(f'    - {text}')
            i += 1
            continue
        
        if code_buffer:
            has_chinese = bool(re.search(r'[\u4e00-\u9fff]', stripped))
            if (indent_level <= 1 and not is_code_line(stripped)) or (has_chinese and not is_code_line(stripped) and len(re.findall(r'[\u4e00-\u9fff]', stripped)) / max(len(stripped), 1) > 0.25):
                flush_code()
                end_code()
                if result and result[-1] != '':
                    result.append('')
                text = wrap_inline_code(stripped)
                if indent_level == 0:
                    result.append(f'## {text}')
                elif indent_level == 1:
                    result.append(f'### {text}')
                elif indent_level == 2:
                    result.append(f'- {text}')
                elif indent_level == 3:
                    result.append(f'  - {text}')
                else:
                    result.append(f'    - {text}')
            else:
                code_buffer.append(stripped)
        else:
            if indent_level <= 1:
                text = wrap_inline_code(stripped)
                if indent_level == 0:
                    result.append(f'## {text}')
                else:
                    result.append(f'### {text}')
            else:
                text = wrap_inline_code(stripped)
                if indent_level == 2:
                    result.append(f'- {text}')
                elif indent_level == 3:
                    result.append(f'  - {text}')
                else:
                    result.append(f'    - {text}')
        
        i += 1
    
    if code_buffer:
        flush_code()
    if in_code:
        end_code()
    
    final = '\n'.join(result)
    final = re.sub(r'\n{4,}', '\n\n\n', final)
    return final.strip()

for filename in sorted(os.listdir(src_dir)):
    if filename.endswith('.txt'):
        src_path = os.path.join(src_dir, filename)
        with open(src_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        md_content = convert_txt_to_md(content)
        
        md_filename = filename[:-4] + '.md'
        dst_path = os.path.join(dst_dir, md_filename)
        with open(dst_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        print(f"已转换: {filename} -> {md_filename}")

print("\n全部转换完成！")