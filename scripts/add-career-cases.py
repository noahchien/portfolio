from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
page=root/'docs/index.html'
text=page.read_text(encoding='utf8')
marker='<div class="work-list">'
cases='''
<article class="work-item"><div class="work-company">FPGA專案<small>規劃、開發與品質責任</small></div><div><h3>從三人到一人，重新安排專案的走法。</h3><p>人力縮減後，我負責規劃、開發與進度管理，將大部分程式實作交由AI協助，自己承擔方向判斷、程式審查、現場確認與驗證方式。完成開發，較原先預估工期提前一年以上；目前作為後續專案基底，尚未正式上線。</p><div class="tags"><span>FPGA</span><span>專案規劃</span><span>AI協作與審查</span><span>品質把關</span></div><a class="detail-link" href="https://github.com/noahchien/portfolio/blob/main/projects/fpga.md">閱讀FPGA案例</a></div></article>
<article class="work-item"><div class="work-company">團隊工具<small>風控開發與資訊部多團隊使用</small></div><div><h3>把難重現的問題，變成可以測試的情境。</h3><p>虛擬交易所讓風控團隊以腳本設定特殊案例、執行自動壓力測試，並匯入日誌重現實際事件。Logger Monitor則檢查檔案與異常關鍵字，提供INI設定，透過LINE／Telegram Bot通報，減少人工巡查的負擔與漏查風險。</p><div class="tags"><span>Python / Node.js</span><span>日誌重現與壓測</span><span>可設定監控</span><span>Bot API</span></div><a class="detail-link" href="https://github.com/noahchien/portfolio/blob/main/projects/testing-tools.md">閱讀團隊工具案例</a></div></article>
'''
if '閱讀FPGA案例' not in text:
    assert marker in text
    text=text.replace(marker,marker+cases,1)
    page.write_text(text,encoding='utf8')
translations={
'FPGA專案':'FPGA project',
'規劃、開發與品質責任':'Planning, development & quality ownership',
'從三人到一人，重新安排專案的走法。':'From three people to one: rethink how the project moves forward.',
'人力縮減後，我負責規劃、開發與進度管理，將大部分程式實作交由AI協助，自己承擔方向判斷、程式審查、現場確認與驗證方式。完成開發，較原先預估工期提前一年以上；目前作為後續專案基底，尚未正式上線。':'After staffing was reduced, I owned planning, development, and progress management. AI assisted with most implementation while I retained direction, code review, on-site checks, and validation decisions. Development finished more than a year ahead of the original estimate. It is now a base for a follow-on project and is not yet in production.',
'專案規劃':'Project planning',
'AI協作與審查':'AI collaboration & review',
'品質把關':'Quality ownership',
'閱讀FPGA案例':'Read the FPGA case study',
'團隊工具':'Tools for teams',
'風控開發與資訊部多團隊使用':'Used by risk-control developers and multiple IT teams',
'把難重現的問題，變成可以測試的情境。':'Turn hard-to-reproduce problems into testable scenarios.',
'虛擬交易所讓風控團隊以腳本設定特殊案例、執行自動壓力測試，並匯入日誌重現實際事件。Logger Monitor則檢查檔案與異常關鍵字，提供INI設定，透過LINE／Telegram Bot通報，減少人工巡查的負擔與漏查風險。':'The virtual exchange lets risk-control developers script special scenarios, run automated stress tests, and import logs to reproduce actual events. Logger Monitor checks file existence and error keywords, supports INI settings, and notifies through LINE and Telegram bots, reducing manual inspection and the risk of omissions.',
'日誌重現與壓測':'Log replay & stress tests',
'可設定監控':'Configurable monitoring',
'閱讀團隊工具案例':'Read the team-tool case studies'
}
file=root/'scripts/translations.en.json'
data=json.loads(file.read_text(encoding='utf8'));data.update(translations)
file.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
