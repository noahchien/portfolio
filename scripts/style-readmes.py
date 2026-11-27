from pathlib import Path
from html import escape
root=Path(__file__).resolve().parents[1]
badges=[('role','Project leadership','#176080',190),('domain','Financial systems','#5c4490',180),('focus','Problem solving','#26704f',170)]
for name,label,color,width in badges:
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="30" viewBox="0 0 {width} 30"><rect width="{width}" height="30" rx="6" fill="{color}"/><text x="{width/2}" y="20" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="600" fill="white">{escape(label)}</text></svg>'
    (root/f'docs/assets/badge-{name}.svg').write_text(svg,encoding='utf8')
for name,english in [('README.md',False),('README.en.md',True)]:
    file=root/name;text=file.read_text(encoding='utf8')
    badge_markup=' '.join(f'![{label}](docs/assets/badge-{key}.svg)' for key,label,_,_ in globals()['badges'])
    anchor='**Target roles: Project Manager / Senior Software Engineer**\u3000|\u300010+ years in software development' if english else '**\u6c42\u8077\u65b9\u5411\uff1a\u5c08\u6848\u4e3b\u7ba1\uff0f\u8cc7\u6df1\u5de5\u7a0b\u5e2b**\u3000\uff5c\u3000\u5341\u5e74\u4ee5\u4e0a\u8edf\u9ad4\u958b\u767c\u7d93\u9a57'
    if 'docs/assets/badge-role.svg' not in text:text=text.replace(anchor,anchor+'\n\n'+badge_markup)
    heading='## Three projects to start with' if english else '## \u5148\u770b\u4e09\u500b\u4ee3\u8868\u6210\u679c'
    highlight=('> [!IMPORTANT]\n> **FPGA development completed more than a year ahead of the original estimate**, after development staffing fell from three people to one. I owned planning, technical direction, code review, and validation.' if english else '> [!IMPORTANT]\n> **FPGA\u958b\u767c\u8f03\u539f\u5148\u9810\u4f30\u5de5\u671f\u63d0\u524d\u4e00\u5e74\u4ee5\u4e0a\u5b8c\u6210\u3002** \u4eba\u529b\u7531\u4e09\u4eba\u7e2e\u81f3\u4e00\u4eba\uff0c\u6211\u8ca0\u8cac\u898f\u5283\u3001\u6280\u8853\u65b9\u5411\u3001\u7a0b\u5f0f\u5be9\u67e5\u8207\u9a57\u8b49\u3002')
    if '> [!IMPORTANT]' not in text:text=text.replace(heading,heading+'\n\n'+highlight)
    tools_heading='## Virtual exchange: make difficult cases reproducible' if english else '## \u865b\u64ec\u4ea4\u6613\u6240\uff1a\u8b93\u300c\u5f88\u96e3\u6e2c\u300d\u7684\u554f\u984c\uff0c\u53ef\u4ee5\u88ab\u91cd\u73fe'
    summary=('> [!TIP]\n> **Tools used by real teams:** the virtual exchange supports risk-control developers with **scripted edge cases, stress tests, and log replay**. Logger Monitor helps multiple IT teams with **configurable checks and LINE / Telegram notifications**.' if english else '> [!TIP]\n> **\u5be6\u969b\u4f9b\u5718\u968a\u4f7f\u7528\u7684\u5de5\u5177\uff1a**\u865b\u64ec\u4ea4\u6613\u6240\u8b93\u98a8\u63a7\u958b\u767c\u5718\u968a\u505a**\u7279\u6b8a\u6848\u4f8b\u3001\u58d3\u6e2c\u8207\u65e5\u8a8c\u91cd\u73fe**\uff1bLogger Monitor\u8b93\u8cc7\u8a0a\u90e8\u591a\u5718\u968a\u4f7f\u7528**\u53ef\u8a2d\u5b9a\u6aa2\u67e5\u8207LINE\uff0fTelegram\u901a\u5831**\u3002')
    if '> [!TIP]' not in text:text=text.replace(tools_heading,summary+'\n\n'+tools_heading)
    labels={
    '## FPGA: keeping development moving after the team shrank':'## \U0001f527 FPGA: keeping development moving after the team shrank',
    '## FPGA\uff1a\u4eba\u529b\u7e2e\u6e1b\u4e4b\u5f8c\uff0c\u6211\u600e\u9ebc\u8b93\u5c08\u6848\u7e7c\u7e8c\u8d70\u4e0b\u53bb':'## \U0001f527 FPGA\uff1a\u4eba\u529b\u7e2e\u6e1b\u4e4b\u5f8c\uff0c\u6211\u600e\u9ebc\u8b93\u5c08\u6848\u7e7c\u7e8c\u8d70\u4e0b\u53bb',
    tools_heading:tools_heading.replace('## ','## \U0001f9ea ',1),
    '## Logger Monitor: take repeatable checks out of manual inspection':'## \U0001f50e Logger Monitor: take repeatable checks out of manual inspection',
    '## Logger Monitor\uff1a\u628a\u5bb9\u6613\u6f0f\u6389\u7684\u6aa2\u67e5\uff0c\u4ea4\u7d66\u53ef\u8a2d\u5b9a\u7684\u5de5\u5177':'## \U0001f50e Logger Monitor\uff1a\u628a\u5bb9\u6613\u6f0f\u6389\u7684\u6aa2\u67e5\uff0c\u4ea4\u7d66\u53ef\u8a2d\u5b9a\u7684\u5de5\u5177',
    '## \u6280\u8853\u80cc\u666f':'## \U0001f6e0\ufe0f \u6280\u8853\u80cc\u666f','## Technical background':'## \U0001f6e0\ufe0f Technical background'
    }
    for before,after in labels.items():text=text.replace(before,after)
    file.write_text(text,encoding='utf8')
print('Added local color badges, key-result alerts, and scan-friendly section markers.')
