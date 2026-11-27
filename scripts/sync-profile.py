"""Keep both public profile READMEs aligned with the detailed portfolio introduction."""
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
profile=root.parent/'profile'
if not (profile/'.git').exists():raise SystemExit('Expected sibling profile checkout')
for name in ('README.md','README.en.md'):
    text=(root/name).read_text(encoding='utf8')
    def link(match):
        target=match.group(1)
        if target.startswith('docs/assets/'):
            return ']('+'https://raw.githubusercontent.com/noahchien/portfolio/main/'+target+')'
        if target.startswith('projects/') or target.startswith('about'):
            return ']('+'https://github.com/noahchien/portfolio/blob/main/'+target+')'
        return match.group(0)
    text=re.sub(r'\]\(([^)]+)\)',link,text)
    (profile/name).write_text(text,encoding='utf8')
print('Chinese and English profile READMEs synchronized.')
