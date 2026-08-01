#!/usr/bin/env python3
"""公众号文章 AI 味扫描器。

用法：python3 ai_smell.py <文章.md|目录> [...]

扫描器只负责暴露风险，不能证明文章由 AI 生成，也不能证明亲历为真。
真实性仍需用原始材料和可靠来源人工核对。
"""
import re
import sys
from pathlib import Path


# (正则, 说明, 是否致命)
RULES = [
    (r'在[^。]{0,12}的今天|随着[^。]{0,15}的(?:发展|普及|推进)|近年来', '宏大起手或空泛背景', True),
    (r'不仅[^。]{0,25}(?:更|也)[^。]{0,20}', '「不仅……更/也……」可能在拔高，结合内容检查', False),
    (r'双刃剑|达摩克利斯之剑|银弹|星辰大海|深水区|一地鸡毛|弯道超车', '现成比喻', True),
    (r'值得琢磨|值得玩味|耐人寻味|引人深思|值得深思', '空转评论词', True),
    (r'这场[^。]{0,10}启示我们|[^。]{0,10}告诉我们，', '「XX 启示我们」式代总结', True),
    (r'赋能|(?:核心|重要|工作|治理|增长)抓手|底层逻辑|颗粒度|降维打击|(?:打造|形成|实现|业务|商业)闭环', '互联网黑话', True),
    (r'只是一个开始|还在路上|拭目以待|时间会证明|未来可期|值得期待', '万能祈愿结尾', True),
    (r'一方面[^。]{0,50}另一方面', '对称平衡术', True),
    (r'最后吐槽一句|这事儿挺有意思', '模板化伪口语', True),
    (r'综上所述|总而言之|总的来说', '报告腔小结', False),
    (r'[新]?(?:里程碑|新纪元|新篇章|新时代)', '大词题眼', False),
]

SIGNATURE = r'不是[^。，\n]{1,24}而是'
HANDS_ON_RE = re.compile(
    r'我(?:删|试用|实测|测试|用|写|跑|配置|配了|做|花|损失|改用|接触|采访|买|安装|装了|'
    r'跑通|部署|重写|放弃|面试|搭建|调试|复盘)'
)
OBSERVE_RE = re.compile(r'我.{0,8}(?:读到|读了|看到|看见|刷到|听说|发现|注意到|翻到|查到)')
STANCE_RE = re.compile(
    r'我(?:觉得|认为|想|以为|看来|总觉得|近来|怀疑|理解|更愿意|不太|不喜欢|不反对|会先|'
    r'没有找到|没找到|的判断|的看法|担心|估计)|说实话'
)
SUSPECT_SCENES = [
    (r'我家的.{0,8}(?:犬|狗|猫|宠物)|邻居家.{0,12}(?:孩子|小孩)|朋友突然|好友小海', '疑似为现场感补写的私人角色'),
    (r'我亲眼看着[^。]{0,25}(?:公司|平台|亚马逊|AWS|AI)', '把公开事件写成「亲眼看着」'),
    (r'(?:凌晨|深夜)[零一二三四五六七八九十\d]{0,3}点.{0,30}(?:咖啡|键盘|屏幕)', '电影式开场，需原始经历支撑'),
    (r'某.{0,10}(?:企业|机构|品牌|公司).{0,80}(?:提升|增长|降低|跃升|高于)', '匿名案例带效果结论'),
]
SOURCE_WORDS = ['报告', '大学', '研究', '调查', '根据', '据', '团队', '博客', '论文', '官方', '统计', '公司', '公告', '文档']
OWN_DATA_WORDS = ['后台', '截图', '实测', '测试', '实验', '我用', '我花', '记录', '日志']


def body_lines(text):
    """返回 [(原始行号, 行内容)]，跳过 frontmatter 和一级标题。"""
    lines = text.split('\n')
    start = 0
    if lines and lines[0].strip() == '---':
        for i in range(1, len(lines)):
            if lines[i].strip() == '---':
                start = i + 1
                break
    out = []
    for i in range(start, len(lines)):
        if re.match(r'^#\s+', lines[i]):
            continue
        out.append((i + 1, lines[i]))
    return out


def first_paragraph(numbered):
    for _, line in numbered:
        value = line.strip()
        if value and not value.startswith(('#', '>', '-', '|', '!', '`')):
            return value
    return ''


def scan(path):
    raw = path.read_text(encoding='utf-8')
    numbered = body_lines(raw)
    body = '\n'.join(line for _, line in numbered)
    han = max(len(re.findall(r'[一-鿿]', body)), 1)
    fatal = 0

    print(f'\n扫描 {path}  （正文 {han} 汉字）')
    print('=' * 68)

    print('\n[词汇与句式]')
    hits = 0
    for pattern, desc, is_fatal in RULES:
        for lineno, line in numbered:
            if re.search(r'原稿|原文|旧稿|虚构|硬编|不成立', line):
                continue
            for match in re.finditer(pattern, line):
                print(f'  {"✗" if is_fatal else "·"} L{lineno} {desc}: 「{match.group()[:32]}」')
                hits += 1
                fatal += int(is_fatal)
    if not hits:
        print('  ✓ 未命中词句黑名单')

    print('\n[开头]')
    head = first_paragraph(numbered)
    if head:
        print(f'  首段：{head[:54]}')
        if re.search(r'行业正在|企业正在|我们正在迎来|时代正在', head):
            print('  ⚠ 用集合名词代替了具体事实')
        if not re.search(r'\d|今天|昨天|最近|上周|报告|公告|发布|上线|故障|问题|我|各位|朋友', head):
            print('  · 未发现具体对象，人工确认是否空转')

    print('\n[真实性风险]')
    scene_hits = 0
    for pattern, desc in SUSPECT_SCENES:
        for lineno, line in numbered:
            if re.search(r'原稿|原文|虚构|硬编|没教|不成立', line):
                continue
            match = re.search(pattern, line)
            if match:
                print(f'  ⚠ L{lineno} {desc}: 「{match.group()[:44]}」')
                scene_hits += 1
    if not scene_hits:
        print('  ✓ 未发现常见的虚构场景信号')
    print('  → 命中只代表需要原始材料，不等于断定内容虚构。')

    print('\n[作者证据]')
    hands = sorted(set(HANDS_ON_RE.findall(body)))
    observations = sorted(set(OBSERVE_RE.findall(body)))
    stances = sorted(set(STANCE_RE.findall(body)))
    print(f'  实际操作: {hands[:8] if hands else "无"}')
    print(f'  阅读/观察: {observations[:8] if observations else "无"}')
    print(f'  判断措辞: {stances[:8] if stances else "无"}')
    if hands:
        print('  ⚠ 有亲历主张，发布前核对笔记、截图、代码、日志或后台记录')
    elif observations:
        print('  · 作者读过或看到材料，但这不等于亲自测试')
    elif stances:
        print('  ✓ 技术评论可以只有判断，但必须有公开证据或推理链')
    else:
        print('  ⚠ 没有明显的操作、观察或判断，容易写成无主报告')

    print('\n[结构完整感]')
    headings = [(n, l.strip()) for n, l in numbered if re.match(r'^#{2,6}\s+', l)]
    numbered_headings = [(n, h) for n, h in headings if re.search(r'(?:^|\s)(?:[一二三四五六七八九十]+、|\d+[.、]|第[一二三四五六七八九十\d]+)', h)]
    framework_words = len(re.findall(r'(?:三大|四大|五大|七层|七个|十三个|13个|行动清单|完整框架|核心维度)', body))
    report_words = len(re.findall(r'首先|其次|再次|此外|综上|总之|第一[，、]|第二[，、]|第三[，、]', body))
    print(f'  小标题 {len(headings)} 个｜编号标题 {len(numbered_headings)} 个｜框架词 {framework_words} 个｜报告连接词 {report_words} 个')
    if len(headings) >= 10 or framework_words >= 2 or report_words >= 6:
        print('  ⚠ 结构过于完整，检查是否为了凑框架而扩写')
    else:
        print('  ✓ 未发现明显的框架堆砌')

    signature_count = len(re.findall(SIGNATURE, body))
    print(f'\n[作者手法]\n  「不是 X，而是 Y」{signature_count} 次', end='')
    if signature_count > 3:
        print('  ✗ 超过 3 次，像在重复盖作者印章')
        fatal += 1
    else:
        print('  ✓')

    print('\n[数字证据]')
    external = []
    owned = []
    seen = set()
    for lineno, line in numbered:
        if line.lstrip().startswith(('#', '`', '|')):
            continue
        for match in re.finditer(r'\d+(?:\.\d+)?\s*(?:%|万|亿|美元|倍|个百分点)', line):
            key = (lineno, match.group())
            if key in seen:
                continue
            seen.add(key)
            if any(word in line for word in SOURCE_WORDS) or 'http' in line:
                continue
            target = owned if any(word in line for word in OWN_DATA_WORDS) else external
            target.append((lineno, match.group(), line.strip()[:42]))
    for lineno, value, context in external[:8]:
        print(f'  ⚠ L{lineno} 外部数字「{value}」附近无来源: {context}…')
    for lineno, value, context in owned[:5]:
        print(f'  · L{lineno} 自有数字「{value}」需原始记录: {context}…')
    if not external and not owned:
        print('  ✓ 未发现明显的待核数字')

    sentences = [s for s in re.split(r'[。！？\n]', body) if 2 < len(s) < 220]
    if sentences:
        lengths = sorted(len(s) for s in sentences)
        median = lengths[len(lengths) // 2]
        short = sum(1 for value in lengths if value <= 20) / len(lengths) * 100
        print(f'\n[节奏·仅参考]\n  句长中位 {median} 字｜≤20 字占比 {short:.0f}%')
        print('  → 早期作品有不少长句，节奏不作为 AI 味判据。')

    print('\n' + '=' * 68)
    print(f'致命词句 {fatal} 处。' if fatal else '未发现致命词句。')
    print('仍须人工核对：亲历证据、数字来源、匿名案例和推测边界。')
    return fatal


def markdown_files(arguments):
    files = []
    for argument in arguments:
        path = Path(argument)
        if path.is_dir():
            files.extend(sorted(path.rglob('*.md')))
        elif path.is_file():
            files.append(path)
        else:
            print(f'找不到：{path}', file=sys.stderr)
    return files


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('用法: python3 ai_smell.py <文章.md|目录> [...]')
    targets = markdown_files(sys.argv[1:])
    if not targets:
        sys.exit(2)
    total = sum(scan(path) for path in targets)
    if len(targets) > 1:
        print(f'\n共扫描 {len(targets)} 篇，命中致命词句 {total} 处。')
    sys.exit(1 if total else 0)
