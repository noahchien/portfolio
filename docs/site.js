const views={
  engineering:{title:'把需求，接到可靠的系統上。',description:'從金融業務邏輯到後端服務與測試，讓每個環節有清楚的責任，也讓問題有跡可循。',nodes:['需求與分析','系統與開發','測試與交付'],center:'工程'},
  stories:{title:'讓故事走得遠，也接得起來。',description:'角色會成長，設定會累積。用版本與連續性管理，把腦中的世界一章一章留下來。',nodes:['故事與角色','版本與檢核','手機審稿'],center:'故事'},
  games:{title:'把「如果能這樣玩」做出來。',description:'地圖、職業、戰鬥與選擇，先放進能操作的原型，再從每一次試玩調整體驗。',nodes:['玩法設計','Godot 原型','試玩與迭代'],center:'遊戲'}
};
const englishViews={
  engineering:{title:'From requirements to reliable systems.',description:'Connecting financial workflows, backend services, and testing, with clear responsibilities and problems that can be traced.',nodes:['Requirements','Development','Delivery'],center:'Build'},
  stories:{title:'A story that can keep growing.',description:'Characters change and worlds grow. Versioning and continuity checks help keep the next chapter connected to everything before it.',nodes:['Story & cast','Versions & checks','Mobile review'],center:'Story'},
  games:{title:'Make the game you wish you could play.',description:'Bring maps, classes, combat, and choices into a playable prototype, then learn from each iteration.',nodes:['Game design','Godot prototype','Play & refine'],center:'Play'}
};
const buttons=document.querySelectorAll('[data-view]');
buttons.forEach(button=>button.addEventListener('click',()=>{
  const view=(document.documentElement.lang==='en'?englishViews:views)[button.dataset.view];
  buttons.forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
  document.getElementById('view-title').textContent=view.title;
  document.getElementById('view-description').textContent=view.description;
  document.getElementById('diagram-center').textContent=view.center;
  view.nodes.forEach((text,index)=>document.getElementById('node-'+index).textContent=text);
  document.querySelector('.system-diagram').setAttribute('aria-label',view.title);
}));
