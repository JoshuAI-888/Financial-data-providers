(function(){
  'use strict';

  var scriptUrl=new URL(document.currentScript.src,location.href);
  var researchBase=new URL('research/',scriptUrl);
  var files=[
    'aiera.md','alpaca-markets.md','alpha-vantage.md','alphasense.md','amberdata.md',
    'api-native-challengers.md','api-ninjas.md','asx.md','bamsec.md','benzinga.md','bloomberg.md',
    'cb-insights.md','ceic.md','clarity-ai.md','coingecko.md','coinmarketcap.md','crunchbase.md',
    'cryptocompare.md','daloopa.md','databento.md','databricks-marketplace.md','dataminr.md',
    'dbnomics.md','deutsche-boerse.md','diffbot.md','dowjones-factiva.md','duedil-artesian.md',
    'dun-bradstreet.md','eodhd.md','euronext.md','factset-callstreet.md','factset.md',
    'financial-mcp-servers.md','finchat-fiscalai.md','fred.md','gdelt.md','glassnode.md','grata.md',
    'haver-analytics.md','ice-data-services.md','iress.md','iss-esg.md','kaiko.md','lexisnexis.md',
    'lseg-refinitiv.md','lseg-streetevents.md','lunarcrush.md','macrobond.md','marketaux.md',
    'marketstack.md','mediastack.md','meltwater.md','messari.md','moodys.md','morningstar.md',
    'motley-fool.md','msci.md','nasdaq-data-link.md','nasdaq-evestment.md','newsapi-org.md',
    'newsdata-io.md','nzx.md','oecd-imf-worldbank.md','ortex.md','pitchbook.md','preqin.md',
    'quartr.md','quick-nikkei-japan.md','quiver-quantitative.md','ravenpack.md','reddit-apewisdom.md',
    'reprisk.md','sayari.md','seeking-alpha.md','sentieo.md','similarweb.md','six.md',
    'social-market-analytics.md','sourcescrub.md','sp-global-market-intelligence.md','stocktwits.md',
    'tegus.md','tej-taiwan.md','third-bridge.md','tiingo.md','tipranks.md','trading-economics.md',
    'trucost.md','trulioo.md','truth-social.md','twelve-data.md','unusual-whales.md','wind-china.md',
    'with-intelligence.md','x-twitter-api.md','xpoz-ai.md','yipitdata.md'
  ];

  function escapeHtml(value){
    return String(value).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  }
  function labelFor(file){
    var names={
      'api-ninjas':'API Ninjas','asx':'ASX','cb-insights':'CB Insights','ceic':'CEIC',
      'dbnomics':'DBnomics','eodhd':'EODHD','fred':'FRED','gdelt':'GDELT','iress':'IRESS',
      'iss-esg':'ISS ESG','lseg-refinitiv':'LSEG / Refinitiv','lseg-streetevents':'LSEG StreetEvents',
      'financial-mcp-servers':'Financial-data MCP servers','msci':'MSCI','nasdaq-evestment':'Nasdaq eVestment','newsapi-org':'NewsAPI.org','nzx':'NZX',
      'oecd-imf-worldbank':'OECD / IMF / World Bank','sp-global-market-intelligence':'S&P Global Market Intelligence',
      'tej-taiwan':'TEJ Taiwan','x-twitter-api':'X / Twitter API','xpoz-ai':'Xpoz AI'
    };
    var id=file.replace(/\.md$/,'');
    return names[id]||id.split('-').map(function(word){return word.charAt(0).toUpperCase()+word.slice(1);}).join(' ');
  }
  function inlineMarkdown(value){
    var html=escapeHtml(value);
    html=html.replace(/`([^`]+)`/g,'<code>$1</code>');
    html=html.replace(/\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g,'<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>');
    html=html.replace(/(^|[\s(])(https?:\/\/[^\s<]+)/g,function(_,lead,url){
      var trail='';
      while(/[.,;:)\]]$/.test(url)){trail=url.slice(-1)+trail;url=url.slice(0,-1);}
      return lead+'<a href="'+url+'" target="_blank" rel="noopener noreferrer">'+url+'</a>'+trail;
    });
    html=html.replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>');
    html=html.replace(/(^|\s)\*([^*]+)\*(?=\s|[.,;:]|$)/g,'$1<em>$2</em>');
    return html;
  }
  function renderMarkdown(markdown){
    var lines=String(markdown).replace(/\r\n?/g,'\n').split('\n');
    var html=[],paragraph=[],listDepth=-1,inCode=false,code=[];
    function flushParagraph(){if(paragraph.length){html.push('<p>'+inlineMarkdown(paragraph.join(' '))+'</p>');paragraph=[];}}
    function closeLists(){while(listDepth>=0){html.push('</ul>');listDepth--;}}
    lines.forEach(function(line){
      if(/^```/.test(line)){
        flushParagraph();closeLists();
        if(inCode){html.push('<pre><code>'+escapeHtml(code.join('\n'))+'</code></pre>');code=[];inCode=false;}
        else inCode=true;
        return;
      }
      if(inCode){code.push(line);return;}
      var heading=line.match(/^(#{1,6})\s+(.+)$/);
      var list=line.match(/^(\s*)[-*]\s+(.+)$/);
      if(heading){flushParagraph();closeLists();var level=heading[1].length;html.push('<h'+level+'>'+inlineMarkdown(heading[2])+'</h'+level+'>');return;}
      if(list){
        flushParagraph();
        var depth=Math.min(2,Math.floor(list[1].length/2));
        while(listDepth<depth){html.push('<ul>');listDepth++;}
        while(listDepth>depth){html.push('</ul>');listDepth--;}
        html.push('<li>'+inlineMarkdown(list[2])+'</li>');return;
      }
      if(/^>\s?/.test(line)){flushParagraph();closeLists();html.push('<blockquote>'+inlineMarkdown(line.replace(/^>\s?/,''))+'</blockquote>');return;}
      if(/^\s*(---+|___+)\s*$/.test(line)){flushParagraph();closeLists();html.push('<hr>');return;}
      if(!line.trim()){flushParagraph();closeLists();return;}
      paragraph.push(line.trim());
    });
    flushParagraph();closeLists();
    if(inCode)html.push('<pre><code>'+escapeHtml(code.join('\n'))+'</code></pre>');
    return html.join('');
  }

  var style=document.createElement('style');
  style.textContent='\
    .research-launch{appearance:none;border:1px solid var(--accent);background:color-mix(in srgb,var(--accent) 13%,var(--panel));color:var(--accent-ink);border-radius:9px;padding:7px 11px;margin-left:8px;font:700 .78rem/1.2 inherit;cursor:pointer;white-space:nowrap}\
    .research-launch:hover{background:color-mix(in srgb,var(--accent) 20%,var(--panel))}\
    .research-launch:focus-visible,.research-close:focus-visible,.research-search:focus-visible,.research-file:focus-visible{outline:3px solid color-mix(in srgb,var(--accent) 35%,transparent);outline-offset:2px}\
    .research-dialog{width:min(1180px,96vw);height:min(820px,90dvh);max-width:none;max-height:none;padding:0;border:1px solid var(--line-strong);border-radius:16px;background:var(--panel);color:var(--ink);box-shadow:0 28px 90px rgba(0,0,0,.45);overflow:hidden}\
    .research-dialog::backdrop{background:rgba(5,10,16,.72);backdrop-filter:blur(5px)}\
    .research-shell{display:grid;grid-template-rows:auto 1fr;height:100%}\
    .research-head{display:flex;align-items:center;gap:16px;padding:15px 18px;border-bottom:1px solid var(--line);background:var(--panel-2)}\
    .research-head-copy{min-width:0;flex:1}.research-head h2{font-size:1.05rem;margin:0;color:var(--ink)}\
    .research-head p{margin:3px 0 0;color:var(--muted);font-size:.78rem}\
    .research-close{appearance:none;border:1px solid var(--line);background:var(--panel);color:var(--ink);border-radius:9px;min-width:40px;min-height:40px;font:700 1.15rem/1 inherit;cursor:pointer}\
    .research-layout{display:grid;grid-template-columns:minmax(230px,290px) minmax(0,1fr);min-height:0}\
    .research-sidebar{display:grid;grid-template-rows:auto auto 1fr;min-height:0;border-right:1px solid var(--line);background:var(--panel-2)}\
    .research-search-wrap{padding:14px 14px 8px}.research-search{width:100%;box-sizing:border-box;min-height:40px;border:1px solid var(--line-strong);border-radius:9px;background:var(--panel);color:var(--ink);padding:8px 11px;font:500 .85rem inherit}\
    .research-count{padding:0 15px 8px;color:var(--muted);font-size:.72rem}\
    .research-files{overflow:auto;padding:0 8px 12px;scrollbar-width:thin}\
    .research-file{display:block;width:100%;appearance:none;border:0;border-radius:8px;background:transparent;color:var(--ink-soft);padding:8px 9px;text-align:left;font:600 .79rem/1.3 inherit;cursor:pointer}\
    .research-file:hover{background:var(--panel);color:var(--ink)}.research-file[aria-current="true"]{background:color-mix(in srgb,var(--accent) 16%,var(--panel));color:var(--accent-ink)}\
    .research-reader{min-width:0;overflow:auto;background:var(--panel)}\
    .research-reader-inner{max-width:820px;margin:0 auto;padding:30px 38px 70px}\
    .research-path{margin:0 0 18px;color:var(--muted);font:600 .72rem/1.4 ui-monospace,SFMono-Regular,Menlo,monospace;overflow-wrap:anywhere}\
    .research-content h1{font-size:1.8rem;margin:0 0 .8em}.research-content h2{font-size:1.18rem;margin:1.7em 0 .55em;padding-top:.35em;border-top:1px solid var(--line)}\
    .research-content h3{font-size:1rem;margin:1.4em 0 .45em}.research-content p,.research-content li{color:var(--ink-soft);font-size:.9rem;line-height:1.7}\
    .research-content ul{padding-left:1.25rem}.research-content li{margin:.34em 0}.research-content li>ul{margin:.25em 0}\
    .research-content blockquote{margin:1em 0;border-left:3px solid var(--accent);background:var(--panel-2);padding:10px 14px;color:var(--ink-soft)}\
    .research-content pre{overflow:auto;background:var(--bg);border:1px solid var(--line);border-radius:10px;padding:14px}.research-content code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.86em}\
    .research-content a{overflow-wrap:anywhere}.research-empty{display:grid;place-items:center;min-height:260px;color:var(--muted);text-align:center;padding:30px}\
    .research-sr{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}\
    @media(max-width:720px){.research-launch{display:block;margin:8px 0 0}.research-dialog{width:100vw;height:100dvh;border:0;border-radius:0}.research-head{padding:11px 13px}.research-layout{grid-template-columns:1fr;grid-template-rows:auto 1fr}.research-sidebar{grid-template-rows:auto auto 132px;border-right:0;border-bottom:1px solid var(--line)}.research-search-wrap{padding:9px 11px 5px}.research-count{padding:0 12px 5px}.research-files{display:flex;gap:5px;overflow:auto;padding:0 10px 9px;scrollbar-width:none}.research-files::-webkit-scrollbar{display:none}.research-file{flex:0 0 160px;border:1px solid var(--line);background:var(--panel);padding:7px 9px}.research-reader-inner{padding:22px 18px 55px}.research-content h1{font-size:1.45rem}}\
  ';
  document.head.appendChild(style);

  var dialog=document.createElement('dialog');
  dialog.className='research-dialog';
  dialog.setAttribute('aria-labelledby','research-title');
  dialog.innerHTML='\
    <div class="research-shell">\
      <header class="research-head">\
        <div class="research-head-copy"><h2 id="research-title">Provider research library</h2><p>Browse the Markdown audit trail without leaving the landscape.</p></div>\
        <button class="research-close" type="button" aria-label="Close research library">&times;</button>\
      </header>\
      <div class="research-layout">\
        <aside class="research-sidebar" aria-label="Research files">\
          <div class="research-search-wrap"><label class="research-sr" for="research-search">Search research files</label><input id="research-search" class="research-search" type="search" placeholder="Search 97 files…" autocomplete="off"></div>\
          <div class="research-count" aria-live="polite"></div>\
          <div class="research-files"></div>\
        </aside>\
        <article class="research-reader" tabindex="0" aria-live="polite"><div class="research-reader-inner"><p class="research-path"></p><div class="research-content"><div class="research-empty">Choose a provider research file.</div></div></div></article>\
      </div>\
    </div>';
  document.body.appendChild(dialog);

  var fileList=dialog.querySelector('.research-files');
  var search=dialog.querySelector('.research-search');
  var count=dialog.querySelector('.research-count');
  var reader=dialog.querySelector('.research-reader');
  var path=dialog.querySelector('.research-path');
  var content=dialog.querySelector('.research-content');
  var activeFile='bloomberg.md';
  var cache={};

  function renderFileList(query){
    var term=(query||'').trim().toLowerCase();
    var visible=files.filter(function(file){return !term||file.toLowerCase().includes(term)||labelFor(file).toLowerCase().includes(term);});
    count.textContent=visible.length+' of '+files.length+' files';
    fileList.innerHTML=visible.map(function(file){return '<button type="button" class="research-file" data-file="'+file+'" aria-current="'+(file===activeFile)+'">'+escapeHtml(labelFor(file))+'</button>';}).join('');
    if(!visible.length)fileList.innerHTML='<div class="research-empty">No matching research files.</div>';
  }
  async function loadFile(file){
    activeFile=file;
    renderFileList(search.value);
    path.textContent='provider-landscape/research/'+file;
    content.innerHTML='<div class="research-empty">Loading '+escapeHtml(labelFor(file))+'…</div>';
    reader.scrollTop=0;reader.scrollLeft=0;
    try{
      var markdown=cache[file];
      if(markdown==null){
        var response=await fetch(new URL(file,researchBase));
        if(!response.ok)throw new Error('HTTP '+response.status);
        markdown=await response.text();cache[file]=markdown;
      }
      content.innerHTML=renderMarkdown(markdown);
      var heading=content.querySelector('h1');if(heading)heading.setAttribute('tabindex','-1');
    }catch(error){
      content.innerHTML='<div class="research-empty"><div><b>Could not load this research file.</b><br>Serve the repository over HTTP and check that the file still exists.</div></div>';
    }
  }
  function openExplorer(file){
    if(file&&files.includes(file))activeFile=file;
    renderFileList('');search.value='';dialog.showModal();loadFile(activeFile);search.focus();
  }

  fileList.addEventListener('click',function(event){var button=event.target.closest('[data-file]');if(button)loadFile(button.dataset.file);});
  search.addEventListener('input',function(){renderFileList(search.value);});
  dialog.querySelector('.research-close').addEventListener('click',function(){dialog.close();});
  dialog.addEventListener('click',function(event){if(event.target===dialog)dialog.close();});

  Array.from(document.querySelectorAll('code')).filter(function(code){return code.textContent.includes('provider-landscape/research');}).forEach(function(code){
    var launch=document.createElement('button');
    launch.className='research-launch';launch.type='button';launch.textContent='Explore '+files.length+' research files';
    launch.addEventListener('click',function(){openExplorer();});
    code.insertAdjacentElement('afterend',launch);
  });
})();
