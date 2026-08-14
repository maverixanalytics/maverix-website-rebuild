#!/usr/bin/env python3
"""Build the Maverix Medical website recreation - all pages as self-contained HTML."""
import os, html

OUT = os.environ.get("MVX_OUT") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
CDN2 = "https://cdn.prod.website-files.com/680906a5e5bd468c21e28d8a"  # cms assets

# ---- site configuration -------------------------------------------------
# Canonical/production origin. Change to "https://www.maverixmedical.com"
# at domain cutover — sitemap, canonicals and OG tags all follow this.
BASE_URL = "https://maverixanalytics.github.io/maverix-website-rebuild"

# Form submission endpoint.
#   Formspree : "https://formspree.io/f/XXXXXXXX"   (works on any host)
#   Netlify   : leave "" and keep data-netlify (Netlify hosting only)
#   Unset     : falls back to opening the visitor's mail client
FORM_ENDPOINT = ""
CONTACT_EMAIL = "contact@maverixmedical.com"
THOR_LOGO      = "assets/thoracent-by-maverix-logo.png"
THOR_EMAIL     = "customercare@thoracent.com"
THOR_PHONE     = "(888) 978-0232"
MVX_EMAIL      = "customercare@maverixmedical.com"

PAGES = []  # populated by page(); drives sitemap.xml
EIFU_URL = "https://thoracent.com/ifu/"  # <- confirm/replace with the real eIFU library URL

# Careers — LinkedIn job feeds. SociableKit embed IDs come from the live maverixmedical.com
# careers page; the LinkedIn URLs are the always-visible fallback if the widget is blocked.
# Consent + analytics, carried over from the live Webflow site.
# CookieYes renders the banner and drives Google Consent Mode; GA4 stays denied
# until the visitor opts in. NOTE: the rebuild's domain must be added to the
# allowed-domains list in the CookieYes dashboard or the banner will not render.
CY_CLIENT = "b0481c682f112a57de13418a"
GA4_ID    = "G-QFMYMJ9YWX"

SK_MAVERIX    = "25606228"
SK_THORACENT  = "25605798"
LI_MAVERIX    = "https://www.linkedin.com/company/maverix-medical/jobs/"
LI_THORACENT  = "https://www.linkedin.com/company/thoracent/jobs/"

IMG = {
    "mission": f"assets/our-mission.jpg",
    "goal": f"assets/our-goal.jpg",
    "xray": f"assets/lung-cancer-x-ray.png",
    "video": f"assets/maverix-medical-b-roll-edit1-transcode.mp4",
    "diag_logo": f"assets/maverix-diagnostics-logo-color.png",
    "biopsy_logo": f"assets/maverix-biopsy-tools-logo-color.png",
    "interv_logo": f"assets/maverix-interventional-portfolio-logo-color.png",
    "detection": f"assets/doctor-detection-image.jpg",
    "holding_hands": f"assets/holding-hands.jpg",
    "jenny": f"assets/jenny-hill-mqvwb7kuooe-unsplash.jpg",
    "bonastent_logo": f"assets/bonastent-logo.png",
    "hilzo_logo": f"assets/hilzo-stents-logo.png",
    "microtech_logo": f"assets/micro-tech-logo.png",
    "netis1": f"assets/netis-retrieval-net.jpg",
    "netis2": f"assets/netis-retrieval-net-alt.jpg",
    "logo_fierce": f"assets/fierce-biotech-logo.png",
    "logo_prn": f"assets/pr-newswire-logo.png",
    "logo_wsj": f"assets/wsj-logo.png",
    "logo_bw": f"assets/business-wire-logo.png",
    "logo_jor": f"assets/mdpi-jor-logo.png",
    "logo_chest": f"assets/chest-journal.png",
    "l_tb": "images/bonastent-tb.jpg",
    "l_guidewire": "images/guidewire.jpg",
    "logo_md": f"assets/massdevice-logo.png",
    "l_ystent": "images/ystent.png",
    "l_ebus": "images/ebus.jpg",
    "l_forceps": "images/forceps.jpg",
    "l_tts": "images/hilzo-tts.jpg",
    "l_ues": "images/hilzo-ues.jpg",
    "l_besoph": "images/bonastent-esoph.jpg",
    "narwhal": "images/narwhal-cryo.jpg",
}
HS = {  # headshots
    "aftab": f"assets/aftab-resized-2.png",
    "basile": f"assets/basile-resized.png",
    "brian": f"assets/brian-2020-resized.png",
    "carla": f"assets/carla-resized.png",
    "beylik": f"assets/david-beylik-resized.png",
    "mallery": f"assets/david-mallery-resized.png",
    "doug": f"assets/doug-resized.png",
    "jeremy": f"assets/jeremy-resized.png",
    "jocelyn": f"assets/jocelyn-resized.png",
    "neil": f"assets/neil-resized.png",
    "rebecca": f"assets/rebecca-bergin-resized.png",
    "scott": f"assets/scott-updated.png",
    "will": f"assets/will-resized.png",
}

CSS_TPL = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "theme.css.tpl")).read()

JS = """
(function(){
 var MOB='(max-width:920px)';
 var hb=document.querySelector('.hamburger');
 if(hb){hb.addEventListener('click',function(){
  var nl=document.querySelector('.nav-links');
  nl.classList.toggle('open');
  hb.setAttribute('aria-expanded', nl.classList.contains('open')?'true':'false');
  if(!nl.classList.contains('open'))
   nl.querySelectorAll('.sub-open').forEach(function(o){o.classList.remove('sub-open');});
 });}
 // mobile nav: tap a section to expand its sub-links (keeps the menu short)
 document.querySelectorAll('.nav-links > div').forEach(function(d){
  var top=d.querySelector('a.nav-top-link'), dd=d.querySelector('.dropdown');
  if(!top||!dd||dd.classList.contains('newsmega'))return;
  top.addEventListener('click',function(e){
   if(!window.matchMedia(MOB).matches)return;
   e.preventDefault();
   var open=d.classList.contains('sub-open');
   d.parentElement.querySelectorAll('.sub-open').forEach(function(o){o.classList.remove('sub-open');});
   if(!open)d.classList.add('sub-open');
  });});
 // mobile: tap a journey / diagnostics card to expand its text
 document.querySelectorAll('.pathcard,.photo-cards.expand .photo-card').forEach(function(c){
  c.addEventListener('click',function(e){
   if(!window.matchMedia(MOB).matches)return;
   if(e.target.closest('a'))return;
   c.classList.toggle('open');
  });
  c.addEventListener('keydown',function(e){
   if((e.key==='Enter'||e.key===' ')&&window.matchMedia(MOB).matches){e.preventDefault();c.classList.toggle('open');}
  });});
 var lastFocus=null;
 document.querySelectorAll('[data-modal-open]').forEach(function(b){
  b.addEventListener('click',function(){var m=document.getElementById(b.getAttribute('data-modal-open'));if(m){lastFocus=b;m.classList.add('open');document.body.style.overflow='hidden';var cl=m.querySelector('.close');if(cl)cl.focus();}});});
 document.addEventListener('keydown',function(e){
  if(e.key!=='Tab')return;var m=document.querySelector('.modal.open');if(!m)return;
  var f=m.querySelectorAll('button,a[href],input,textarea,[tabindex]:not([tabindex="-1"])');
  if(!f.length)return;var first=f[0],last=f[f.length-1];
  if(e.shiftKey&&document.activeElement===first){e.preventDefault();last.focus();}
  else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first.focus();}});
 document.querySelectorAll('.modal').forEach(function(m){
  m.querySelectorAll('.overlay,.close').forEach(function(x){x.addEventListener('click',function(){m.classList.remove('open');document.body.style.overflow='';if(lastFocus)lastFocus.focus();});});});
 document.addEventListener('keydown',function(e){if(e.key==='Escape'){document.querySelectorAll('.modal.open').forEach(function(m){m.classList.remove('open');});document.body.style.overflow='';}});
 document.querySelectorAll('.carousel').forEach(function(c){
  var t=c.querySelector('.track');
  var prev=c.querySelector('.cprev'),next=c.querySelector('.cnext');
  if(prev)prev.addEventListener('click',function(){t.scrollBy({left:-300,behavior:'smooth'});});
  if(next)next.addEventListener('click',function(){t.scrollBy({left:300,behavior:'smooth'});});
  var dots=c.querySelector('.dots');
  if(dots&&t){var cards=t.children.length;
   for(var i=0;i<cards;i++){(function(i){var d=document.createElement('button');d.setAttribute('aria-label','Go to item '+(i+1));
    d.addEventListener('click',function(){t.scrollTo({left:t.scrollWidth/cards*i,behavior:'smooth'});});dots.appendChild(d);})(i);}
   var upd=function(){var idx=Math.round(t.scrollLeft/(t.scrollWidth/cards));
    Array.prototype.forEach.call(dots.children,function(d,j){d.classList.toggle('on',j===idx);});};
   t.addEventListener('scroll',function(){requestAnimationFrame(upd);});upd();}});
 document.querySelectorAll('.tabbar [data-tab]').forEach(function(b){
  b.addEventListener('click',function(){
   document.querySelectorAll('.tabbar [data-tab]').forEach(function(x){x.classList.remove('is-active');});
   document.querySelectorAll('.tabpane').forEach(function(p){p.classList.remove('is-active');});
   b.classList.add('is-active');var p=document.getElementById(b.getAttribute('data-tab'));if(p)p.classList.add('is-active');});});
 document.querySelectorAll('form[data-mvxform]').forEach(function(f){
  var box=f.parentElement,
      ok=box.querySelector('.form-msg.form-success'),
      err=box.querySelector('.form-msg.form-error'),
      btn=f.querySelector('button[type=submit]'),
      label=btn?btn.textContent:'';
  function show(el,msg){[ok,err].forEach(function(n){if(n)n.style.display='none';});
   if(el){if(msg)el.textContent=msg;el.style.display='block';}}
  function reset(){if(btn){btn.disabled=false;btn.textContent=label;}}
  f.addEventListener('submit',function(e){
   e.preventDefault();
   if(!f.reportValidity())return;
   if((f.querySelector('input[name=_gotcha]')||{}).value){f.style.display='none';show(ok);return;}
   var data=new FormData(f),endpoint=f.getAttribute('data-endpoint');
   if(btn){btn.disabled=true;btn.textContent='Sending\\u2026';}
   if(!endpoint){
    var to=f.getAttribute('data-mailto')||'',lines=[];
    data.forEach(function(v,k){if(k.charAt(0)!=='_'&&k!=='form-name'&&String(v).trim())lines.push(k+': '+v);});
    var subj=data.get('Subject')||('Website enquiry from '+(data.get('First Name')||data.get('Name')||'a visitor'));
    window.location.href='mailto:'+to+'?subject='+encodeURIComponent(subj)+'&body='+encodeURIComponent(lines.join('\\n'));
    setTimeout(function(){reset();show(ok,'Thanks \\u2014 your email app should be opening with this message ready to send.');},600);
    return;
   }
   fetch(endpoint,{method:'POST',body:data,headers:{'Accept':'application/json'}})
    .then(function(r){
     if(r.ok){f.style.display='none';show(ok);}
     else{reset();show(err);}})
    .catch(function(){reset();show(err,'Network error \\u2014 please try again, or email '+(f.getAttribute('data-mailto')||'us')+'.');});
  });});
 if(!window.matchMedia('(prefers-reduced-motion: reduce)').matches && 'IntersectionObserver' in window){
  var nio=new IntersectionObserver(function(es){es.forEach(function(e){
   if(!e.isIntersecting)return;nio.unobserve(e.target);
   var el=e.target,txt=el.textContent,m=txt.match(/^([^0-9]*)([0-9]+(?:\.[0-9]+)?)(.*)$/);
   if(!m)return;var pre=m[1],end=parseFloat(m[2]),suf=m[3],dec=(m[2].split('.')[1]||'').length;
   var t0=null;function step(ts){if(!t0)t0=ts;var p=Math.min((ts-t0)/1200,1);p=1-Math.pow(1-p,3);
    el.textContent=pre+(end*p).toFixed(dec)+suf;if(p<1)requestAnimationFrame(step);}
   requestAnimationFrame(step);});},{threshold:.6});
  document.querySelectorAll('.statgrid .stat-number,.bigstat .stat-number').forEach(function(n){nio.observe(n);});
  document.querySelectorAll('.carousel').forEach(function(c){
   var t=c.querySelector('.track');if(!t)return;var paused=false;
   ['mouseenter','focusin','touchstart'].forEach(function(ev){c.addEventListener(ev,function(){paused=true;});});
   ['mouseleave','focusout'].forEach(function(ev){c.addEventListener(ev,function(){paused=false;});});
   setInterval(function(){if(paused||!t.children.length)return;
    var w=t.scrollWidth/t.children.length;
    if(t.scrollLeft+t.clientWidth>=t.scrollWidth-8){t.scrollTo({left:0,behavior:'smooth'});}
    else{t.scrollBy({left:w,behavior:'smooth'});}},4000);});
  var sel=['.card','.pathcard','.photo-card','.pcard','.member','.advcard','.newsgrid .ncell','.featured','.statgrid .cell','.why-cell','.benefit-cell','.newsitem','.sechead','.biglead','.journey','.serpex-two .prod','.banner-blue','.challenge .headline','.spec'];
  var els=document.querySelectorAll(sel.join(','));
  var io=new IntersectionObserver(function(entries){
   entries.forEach(function(e){if(e.isIntersecting){e.target.classList.add('is-in-view');io.unobserve(e.target);}});
  },{threshold:.12,rootMargin:'0px 0px -40px 0px'});
  els.forEach(function(el,i){el.classList.add('reveal-on-scroll');
   var sibs=el.parentElement?Array.prototype.indexOf.call(el.parentElement.children,el):0;
   el.style.transitionDelay=(Math.max(0,sibs%6)*70)+'ms';io.observe(el);});
  setTimeout(function(){els.forEach(function(el){el.classList.add('is-in-view');});},3000);
 }
})();
"""

ARROW_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="#1A4A5D" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M6 5l7 7-7 7"/><path d="M12.5 5l7 7-7 7"/></svg>'

def contact_block(email=None, phone=True):
    """Sales-inquiry block used on the family pages and every product detail page."""
    email = email or THOR_EMAIL
    ph  = f'<div class="cb-phone">{THOR_PHONE}</div>' if phone else ''
    return ('<div class="contact-block"><div class="cb-label">Sales inquiries</div>'
            f'<div class="cb-title">Customer Care</div><a href="mailto:{email}">{email}</a>'
            f'{ph}</div>')

def btn(href, label, dark=False):
    cls = "btn on-dark" if dark else "btn"
    return f'<a class="{cls}" href="{href}"><span class="circ">{ARROW_SVG}</span><span class="btn-label">{label}</span></a>'

def header(rel=""):
    r = rel
    P = "../../" if rel == "" else "../../../"
    return f"""<header class="site"><div class="nav">
<a class="logo" href="{r}index.html"><img class="logo-img" src="{r}images/maverix-logo-white.png" alt="Maverix Medical"></a>
<button class="hamburger" aria-label="Menu"><span></span><span></span><span></span></button>
<nav class="nav-links">
<div><a class="nav-top-link" href="{r}products.html">products <span class="plus">+</span><span class="arrow">&#8594;</span></a>
 <div class="dropdown mega"><div class="dropdown-in">
  <div class="mcol cat-risk"><h4>Risk Assessment</h4>
   <p>Developing molecular diagnostic tools that aim to triage lung cancer in patients to identify those in need of immediate care.</p>
   {btn(r + "diagnostics.html","Explore Maverix Diagnostics")}</div>
  <div class="mcol cat-diagnosis"><h4>Diagnosis</h4>
   <p>Endobronchial tissue-sampling instruments designed to help physicians obtain the tissue needed for an accurate diagnosis.</p>
   {btn(r + "serpex.html","Explore Biopsy Tools")}</div>
  <div class="mcol cat-intervention"><h4>Intervention</h4>
   <p>Minimally invasive devices for managing pleural effusions, restoring airway patency, and improving quality of life, along with an expanded suite of GI tools.</p>
   {btn(r + "thoracent.html","Explore the interventional portfolio")}</div>
 </div></div></div>
<div><a class="nav-top-link" href="{r}team.html">team <span class="plus">+</span><span class="arrow">&#8594;</span></a>
 <div class="dropdown mega"><div class="dropdown-in cols2">
  <div class="mcol cat-risk"><h4>Leadership</h4>
   <p>Maverix leadership combines decades of clinical, technical, and operating experience.</p>
   {btn(r + "team.html#leadership","Learn more about our leadership")}</div>
  <div class="mcol cat-diagnosis"><h4>Advisors</h4>
   <p>The Maverix Medical Advisory Board is comprised of leading pulmonary physicians.</p>
   {btn(r + "team.html#advisors","Meet our advisors")}</div>
 </div></div></div>
<div><a class="nav-top-link" href="{r}news.html">news <span class="plus">+</span><span class="arrow">&#8594;</span></a>
 <div class="dropdown mega newsmega"><div class="dropdown-in newsdd">
  <div class="ncol feat">
   <div class="most-recent-article">Most Recent Article</div>
   <div class="news-source">{FEATURED_NEWS[1]}</div>
   <div class="date">{FEATURED_NEWS[2]}</div>
   <h4><a href="{FEATURED_NEWS[5]}" target="_blank" rel="noopener">{FEATURED_NEWS[3]}</a></h4>
   <a class="read-more" href="{FEATURED_NEWS[5]}" target="_blank" rel="noopener">Read More</a>
  </div>
  <div class="ncol side">
   <div class="cell">
    <div class="news-source">{GRID_NEWS[0][1]}</div>
    <div class="date">{GRID_NEWS[0][2]}</div>
    <h5><a href="{GRID_NEWS[0][5]}" target="_blank" rel="noopener">{GRID_NEWS[0][3]}</a></h5>
    <a class="read-more" href="{GRID_NEWS[0][5]}" target="_blank" rel="noopener">Read More</a>
   </div>
   <div class="cell view-all"><a href="{r}news.html"><span class="circ">{ARROW_SVG}</span>Read all news</a></div>
  </div>
 </div></div></div>
<div class="mobile-extra"><a href="{r}contact-us.html">Contact</a><a href="{r}careers.html">Careers</a></div>
</nav>
<div class="nav-right">
 <a class="contact" href="{r}contact-us.html">Contact</a>
 <a class="careers-cell" href="{r}careers.html">Careers</a>
</div>
</div></header>"""

def footer(rel=""):
    r = rel
    P = "../../" if rel == "" else "../../../"
    return f"""<footer class="site"><div class="container">
<div class="fgrid">
<div class="fcol"><div class="footer-heading">Products</div>
 <a href="{r}diagnostics.html">Risk Assessment</a>
 <a href="{r}serpex.html">Diagnosis</a>
 <a href="{r}thoracent.html">Intervention</a></div>
<div class="fcol"><div class="footer-heading">Team</div>
 <a href="{r}team.html#leadership">Leadership</a>
 <a href="{r}team.html#advisors">Advisors</a></div>
<div class="fcol"><div class="footer-heading">Company</div>
 <a href="{r}contact-us.html">Contact</a>
 <a href="{r}careers.html">Careers</a>
 <a href="{r}news.html">News</a></div>
<div class="fbrand">
 <img class="flogo" src="{r}images/maverix-logo-gray.png" alt="Maverix">
</div></div>
<div class="fcontact"><div class="footer-heading">Contact us</div>
 <div class="frow"><a class="mail" href="mailto:contact@maverixmedical.com">contact@maverixmedical.com</a>
 <a class="li-sq" href="https://www.linkedin.com/company/maverix-medical/" target="_blank" rel="noopener" aria-label="LinkedIn"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.45 20.45h-3.55v-5.57c0-1.33-.03-3.04-1.85-3.04-1.86 0-2.14 1.45-2.14 2.94v5.67H9.36V9h3.41v1.56h.05c.47-.9 1.63-1.85 3.36-1.85 3.6 0 4.27 2.37 4.27 5.45v6.29zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM7.12 20.45H3.56V9h3.56v11.45z"/></svg></a></div></div>
<div class="fbottom">
 <div><a href="{r}regulatory-information.html">Regulatory Information</a><a href="{r}privacy-policy.html">Privacy Policy</a><a href="{r}terms-of-use.html">Terms of Use</a><a href="#" class="cky-banner-element">Cookie Settings</a></div>
 <div>Copyright &copy; Maverix</div>
</div></div></footer>"""
# The cookie banner is no longer hand-rolled here — CookieYes injects its own
# (see CONSENT_HEAD), which actually distinguishes Accept / Reject / Customise.

# Consent + analytics head block. Order matters and is load-bearing:
#   1. Consent Mode v2 defaults, everything denied, before any Google tag exists.
#   2. CookieYes, which renders the banner and calls gtag('consent','update',...)
#      when the visitor chooses. It also auto-blocks tagged third-party scripts.
#   3. GA4 itself, which queues hits and only sets cookies once consent flips.
# Loading GA4 before the defaults would let it set _ga on the first paint, which
# is exactly the bug the designer flagged.
CONSENT_HEAD = """
<script>
window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}
gtag('consent','default',{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:'denied',functionality_storage:'denied',personalization_storage:'denied',security_storage:'granted',wait_for_update:500});
gtag('set','ads_data_redaction',true);gtag('set','url_passthrough',true);
</script>
<script id="cookieyes" type="text/javascript" src="https://cdn-cookieyes.com/client_data/__CY__/script.js"></script>
<script async src="https://www.googletagmanager.com/gtag/js?id=__GA__"></script>
<script>gtag('js',new Date());gtag('config','__GA__',{anonymize_ip:true});</script>
""".replace("__CY__", CY_CLIENT).replace("__GA__", GA4_ID).strip()


# Homepage statistic citations. Markers, numbering, and targets all mirror the
# original site exactly: 1 = American Lung Association, 2 = JAMA Network Open,
# 3 = CDC never-smokers, 4 = ACS, 5 = WHO. Per the 13 Aug 2026 statistics
# spec every figure in the Challenge block now carries a marker; the two
# global stats that previously ran unmarked are cited to WHO (5).
CITES = {
    # Numbered by first appearance down the Challenge block, so the markers
    # read 1, 2, 3 ... from the top. Renumbered 13 Aug 2026; the earlier
    # scheme in the statistics spec had the U.S./global sources reversed.
    # 1  American Cancer Society, Key Statistics for Lung Cancer -- headline
    1: "https://www.cancer.org/cancer/types/lung-cancer/about/key-statistics.html",
    # 2  IARC Global Cancer Observatory (GLOBOCAN), world fact sheet.
    #    Carries the 19% figure directly (lung = 19.1% of all cancer deaths).
    2: "https://gco.iarc.who.int/media/globocan/factsheets/populations/900-world-fact-sheet.pdf",
    # 3  World Health Organization, Lung cancer fact sheet. Source of the 2.5M
    #    incidence figure only -- it states no share-of-deaths percentage,
    #    which is why that stat cites IARC (2) rather than this.
    3: "https://www.who.int/news-room/fact-sheets/detail/lung-cancer",
    # 4  American Lung Association, State of Lung Cancer 2025 -- the four
    #    U.S. stats in the grid (18.2%, 28.1%, 21%, 29.7%)
    4: "https://www.lung.org/research/state-of-lung-cancer/key-findings",
    # 5  Sabatino SA. Use of Cancer Screening Tests, United States, 2023.
    #    Prev Chronic Dis. 2025;22:250139. Source of the >63% figure.
    5: "https://www.cdc.gov/pcd/issues/2025/25_0139a.htm",
    # 6  CDC, Lung Cancer Among People Who Never Smoked
    6: "https://www.cdc.gov/lung-cancer/nonsmokers/index.html",
}


def cite(*nums):
    """Linked superscript citation marker(s), e.g. cite(1) or cite(1, 2)."""
    parts = [f'<a href="{CITES[n]}" target="_blank" rel="noopener noreferrer">{n}</a>'
             for n in nums]
    return '<sup class="cite">' + '<span class="csep">,</span>'.join(parts) + '</sup>'


# References for the Risk Assessment page's About and Unique Benefits sections.
# Deliberately SEPARATE from CITES above, which numbers the homepage Challenge
# graphic. The two schemes are independent and must never be merged or
# cross-numbered -- they live on different pages and use different markup
# (sup.cite for the graphic, sup.ref plus a visible list here).
REFS_ABOUT = """
<li id="ref-1">Reddy SR, Broder MS, Chang E, Paydar C, Chung KC, Kansal AR. Cost of cancer management by stage at diagnosis among Medicare beneficiaries. <em>Curr Med Res Opin.</em> 2022;38(8):1285&ndash;1294. <a href="https://www.tandfonline.com/doi/full/10.1080/03007995.2022.2047536" target="_blank" rel="noopener noreferrer">doi:10.1080/03007995.2022.2047536</a></li>
<li id="ref-2">de Nijs K, de Koning HJ, van der Aalst C, ten Haaf K. Medical costs of lung cancer by stage, histology and first-line treatment modality in the Netherlands (2012&ndash;2021). <em>Eur J Cancer.</em> 2024;208:114231. <a href="https://www.sciencedirect.com/science/article/pii/S0959804924008876" target="_blank" rel="noopener noreferrer">doi:10.1016/j.ejca.2024.114231</a></li>
<li id="ref-3">National Lung Screening Trial Research Team; Aberle DR, Adams AM, Berg CD, et al. Reduced lung-cancer mortality with low-dose computed tomographic screening. <em>N Engl J Med.</em> 2011;365(5):395&ndash;409. <a href="https://www.nejm.org/doi/full/10.1056/NEJMoa1102873" target="_blank" rel="noopener noreferrer">doi:10.1056/NEJMoa1102873</a></li>
<li id="ref-4">de Koning HJ, van der Aalst CM, de Jong PA, et al. Reduced lung-cancer mortality with volume CT screening in a randomized trial. <em>N Engl J Med.</em> 2020;382(6):503&ndash;513. <a href="https://www.nejm.org/doi/full/10.1056/NEJMoa1911793" target="_blank" rel="noopener noreferrer">doi:10.1056/NEJMoa1911793</a></li>
<li id="ref-5">Vlahos I, Stefanidis K, Sheard S, Nair A, Sayer C, Moser J. Lung cancer screening: nodule identification and characterization. <em>Transl Lung Cancer Res.</em> 2018;7(3):288&ndash;303. <a href="https://tlcr.amegroups.org/article/view/21562/html" target="_blank" rel="noopener noreferrer">doi:10.21037/tlcr.2018.05.02</a></li>
<li id="ref-6">Rajaram R, Huang Q, Li RZ, et al. Recurrence-free survival in patients with surgically resected non-small cell lung cancer: a systematic literature review and meta-analysis. <em>Chest.</em> 2024;165(5):1260&ndash;1270. <a href="https://journal.chestnet.org/article/S0012-3692(23)05836-1/fulltext" target="_blank" rel="noopener noreferrer">doi:10.1016/j.chest.2023.11.042</a></li>
<li id="ref-7">Gould MK, Tang T, Liu IA, et al. Recent trends in the identification of incidental pulmonary nodules. <em>Am J Respir Crit Care Med.</em> 2015;192(10):1208&ndash;1214. <a href="https://pubmed.ncbi.nlm.nih.gov/26214244/" target="_blank" rel="noopener noreferrer">doi:10.1164/rccm.201505-0990OC</a></li>
<li id="ref-8">MacMahon H, Naidich DP, Goo JM, et al. Guidelines for management of incidental pulmonary nodules detected on CT images: from the Fleischner Society 2017. <em>Radiology.</em> 2017;284(1):228&ndash;243. <a href="https://pubs.rsna.org/doi/full/10.1148/radiol.2017161659" target="_blank" rel="noopener noreferrer">doi:10.1148/radiol.2017161659</a></li>
<li id="ref-9">Vidaver RM, Shershneva MB, Hetzel SJ, Holden TR, Campbell TC. Typical time to treatment of patients with lung cancer in a multisite, US-based study. <em>J Oncol Pract.</em> 2016;12(6):e643&ndash;e653. <a href="https://ascopubs.org/doi/10.1200/JOP.2015.009605" target="_blank" rel="noopener noreferrer">doi:10.1200/JOP.2015.009605</a></li>
<li id="ref-10">Christensen J, Prosper AE, Wu CC, et al. ACR Lung-RADS v2022: assessment categories and management recommendations. <em>J Am Coll Radiol.</em> 2024;21(3):473&ndash;488. <a href="https://www.jacr.org/article/S1546-1440(23)00761-5/fulltext" target="_blank" rel="noopener noreferrer">doi:10.1016/j.jacr.2023.09.009</a></li>
<li id="ref-11">Samson P, Patel A, Garrett T, et al. Effects of delayed surgical resection on short-term and long-term outcomes in clinical stage I non-small cell lung cancer. <em>Ann Thorac Surg.</em> 2015;99(6):1906&ndash;1913. <a href="https://www.annalsthoracicsurgery.org/article/S0003-4975(15)00256-X/fulltext" target="_blank" rel="noopener noreferrer">doi:10.1016/j.athoracsur.2015.02.022</a></li>
<li id="ref-12">Khorana AA, Tullio K, Elson P, et al. Time to initial cancer treatment in the United States and association with survival over time: an observational study. <em>PLOS ONE.</em> 2019;14(3):e0213209. <a href="https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0213209" target="_blank" rel="noopener noreferrer">doi:10.1371/journal.pone.0213209</a></li>
""".strip()


def ref(*nums):
    """Superscript marker linking down to the Risk Assessment references list."""
    return ('<sup class="ref">'
            + ','.join(f'<a href="#ref-{n}">{n}</a>' for n in nums)
            + '</sup>')


def refs_section():
    return ('<section class="references" id="references-about-benefits"'
            ' aria-label="References for About and Unique Benefits">'
            f'<h2>References</h2><ol>{REFS_ABOUT}</ol></section>')


def page(fname, title, desc, body, rel="", group="Pages", subtitle=""):
    # share cards are rendered straight from each page's own hero (see build_og_images)
    og_map = {f: f"{BASE_URL}/assets/og-{f.replace('.html','')}.jpg" for f in (
        "index.html", "products.html", "thoracent.html", "diagnostics.html",
        "serpex.html", "team.html", "news.html", "careers.html", "contact-us.html")}
    og = f'<meta property="og:image" content="{og_map[fname]}">' if fname in og_map else ""
    canon = f"{BASE_URL}/" if fname == "index.html" else f"{BASE_URL}/{fname}"
    if fname not in ("404.html",):
        PAGES.append(fname)
    noindex = '<meta name="robots" content="noindex">' if fname == "404.html" else ""
    doc = f"""<!-- @dsCard group="{group}" name="{title}" subtitle="{subtitle}" -->
<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
{CONSENT_HEAD}
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canon}">{noindex}
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:type" content="website"><meta property="og:url" content="{canon}"><meta property="og:site_name" content="Maverix Medical"><meta name="twitter:card" content="summary_large_image">{og}
<link rel="icon" href="assets/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="assets/favicon-16.png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="manifest" href="assets/site.webmanifest">
<meta name="theme-color" content="#0D1418">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400;1,600&family=Jost:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{rel}theme.css">
</head><body>
{header(rel)}
{body}
{footer(rel)}
<script>{JS}</script>
</body></html>"""
    if "/" in fname:  # nested pages reference assets one level up
        doc = doc.replace('"assets/', '"../assets/').replace("('assets/", "('../assets/")
        doc = doc.replace('href="../assets/../theme.css"', 'href="../theme.css"')
    if fname == "404.html":
        # served for ANY missing path, so every reference must be root-absolute
        import re as _re
        doc = _re.sub(r'(href|src)="(?!https?:|mailto:|#|/)([^"]+)"',
                      lambda m: f'{m.group(1)}="{BASE_PATH}{m.group(2)}"', doc)
        doc = doc.replace('url("assets/', f'url("{BASE_PATH}assets/')
    path = os.path.join(OUT, fname)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(doc)
    print("wrote", fname, len(doc))

# ------------------------------------------------------------------ HOME
def build_home():
    body = f"""
<div class="hero"><video autoplay muted loop playsinline poster="images/hero-poster.jpg" src="{IMG['video']}"></video><div class="shade"></div>
<div class="container inner">
 <div class="kicker allcaps">Revolutionizing</div>
 <h1>Lung Cancer<br>Care</h1>
 <div class="hero-tagline">Advancing detection. Improving care.</div>
</div></div>

<section class="band dark"><img class="bgimg" src="{IMG['mission']}" alt="">
<div class="container">
 <div class="kicker allcaps">Our mission</div>
 <div class="fullrule"></div>
 <div class="stackcol">
  <h2>To improve and save lives by revolutionizing the diagnosis and treatment of lung cancer.</h2>
  <p class="lede">We seek to bring cutting-edge technologies to lung cancer care, empowering clinicians to diagnose lung cancer earlier and treat patients more effectively.</p>
 </div>
</div></section>

<section class="band light"><div class="container">
 <h2 class="section-title">The Challenge</h2>
 <div class="challenge">
  <div class="headline">
   <p>Lung cancer is the <b>deadliest cancer in the U.S.</b>&mdash;more than colon, breast, and prostate cancer combined{cite(1)}</p>
   <div class="bigstat"><div class="stat-number">19%</div><div class="stat-label">of all cancer deaths worldwide{cite(2)}</div></div>
   <div class="bigstat"><div class="stat-number">2.5M</div><div class="stat-label">new patients diagnosed globally every year{cite(3)}</div></div>
  </div>
  <div class="statgrid">
   <div class="cell"><div class="stat-number">18.2%</div><div class="stat-label">of eligible U.S. individuals are up to date with lung cancer screening{cite(4)}</div></div>
   <div class="cell"><div class="stat-number">28.1%</div><div class="stat-label">of U.S. cases are diagnosed at an early stage, when survival rates are higher{cite(4)}</div></div>
   <div class="cell"><div class="stat-number">21%</div><div class="stat-label">of U.S. cases did not receive any treatment after diagnosis{cite(4)}</div></div>
   <div class="cell"><div class="stat-number">&gt;63%</div><div class="stat-label">of eligible individuals are up to date with colorectal, breast, and cervical cancer screenings{cite(5)}</div></div>
   <div class="cell"><div class="stat-number">29.7%</div><div class="stat-label">of U.S. patients are alive five years after diagnosis{cite(4)}</div></div>
   <div class="cell"><div class="stat-number">10&ndash;20%</div><div class="stat-label">of lung cancers occur in people who never smoked{cite(6)}</div></div>
  </div>
 </div>
</div></section>

<section class="band dark goal"><img class="bgimg" src="{IMG['goal']}" alt="">
<div class="container">
 <div class="kicker allcaps">Our goal</div>
 <div class="fullrule"></div>
 <div class="stackcol">
  <h2>Improve lung cancer survival rates</h2>
  <p class="lede">by enabling earlier detection and management&mdash;when treatment outcomes are most favorable&mdash;and enhancing patient care throughout every stage of their cancer journey, from screening to palliative care.</p>
 </div>
</div></section>

<section class="band light row-line"><div class="container">
 <h2 class="section-title">The Maverix Solution</h2>
 <p class="lede">A portfolio focused on lung cancer diagnostics and devices to address the full spectrum of care.</p>

 <div class="jpanel">
 <div class="journey">
  <div class="jtitle">Traditional lung cancer patient journey</div>
  <div class="jnote">Starts later, has longer therapy cycles and shorter life expectancy</div>
  <div class="jbar"><span class="jseg tail" style="flex:.72"></span><span class="jseg dark" style="flex:1.3">Risk Assessment</span><span class="jseg steel" style="flex:.9">Diagnosis</span><span class="jseg light" style="flex:2.2">Intervention</span><span class="jseg fade truncated" style="flex:1.24">Life Expectancy</span><span class="jseg end-marker"></span><span class="jseg tail" style="flex:.72"></span></div>
 </div>
 <div class="journey">
  <div class="jbar"><span class="jseg dark" style="flex:1.3">Risk Assessment</span><span class="jseg steel" style="flex:.8">Diagnosis</span><span class="jseg light" style="flex:1.5">Intervention</span><span class="jseg fade" style="flex:4.2">Life Expectancy</span></div>
  <div class="jarrow">Earlier diagnosis, shorter time to treatment, improved outcomes.</div>
  <div class="jtitle">Maverix lung cancer patient journey</div>
 </div>
 </div>

 <div class="pathways">
  <div class="pathcard" tabindex="0"><img src="{IMG['xray']}" alt="Risk Assessment">
   <div class="pathcard-caption"><div class="card-kicker">Maverix</div><div class="card-title">Risk Assessment</div></div>
   <div class="reveal"><h3>More Effective Screening</h3>
    <p>Lung cancer is a heterogeneous disease that can be challenging to diagnose. We are developing a blood-based diagnostic tool with the aim to enable early and accurate diagnosis and stratification of patients to treat those who are at high cancer risk, complementing low-dose computed tomography (CT).</p>
    </div><div class="pcta">{btn("diagnostics.html","Explore Maverix Diagnostics",dark=True)}</div></div>
  <div class="pathcard" tabindex="0"><img src="images/diagnosis.jpg" alt="Diagnosis">
   <div class="pathcard-caption"><div class="card-kicker">Maverix</div><div class="card-title">Diagnosis</div></div>
   <div class="reveal"><h3>A Tool for Every Target</h3>
    <p>Expanded CT screening is putting more patients into the diagnostic pathway, and a single bronchoscopy may need to sample more than one kind of target. Maverix builds an instrument for each &mdash; forceps at the airway wall, ultrasound-guided needles beyond it, and a console-free cryoprobe for cryoadhesion biopsy.</p>
    </div><div class="pcta">{btn("serpex.html","Explore Biopsy Tools",dark=True)}</div></div>
  <div class="pathcard" tabindex="0"><img src="images/intervention.jpg" alt="Intervention">
   <div class="pathcard-caption"><div class="card-kicker">Maverix</div><div class="card-title">Intervention</div></div>
   <div class="reveal"><h3>Superior Treatment &amp; Palliative Care</h3>
    <p>Lung cancer and its treatment can significantly impact physical function, impeding a patient's ability to perform daily activities. By effectively managing the range of symptoms, our minimally invasive palliative care devices enhance well-being and overall quality of care for the millions of patients diagnosed after Stage I.</p>
    </div><div class="pcta">{btn("thoracent.html","Explore the interventional portfolio",dark=True)}</div></div>
 </div>
</div></section>"""
    page("index.html", "Maverix Medical – Revolutionizing Lung Cancer Care",
         "Advancing detection. Improving care. We bring cutting-edge techs to lung cancer care, empowering clinicians with accurate tools and personalized treatments.",
         body, subtitle="Home — hero video, mission, challenge, goal, solution")

# ------------------------------------------------------------------ PRODUCTS
# Intervention (Thoracent) products, grouped for the static product boxes.
INTERVENTION_GROUPS = [
    ("Airway", [
        ("bonastent-tracheobronchial-stent", "Bonastent&reg; Tracheobronchial Stent", "l_tb", None),
        ("y-shaped-tracheal-stent", "Y-Shaped Tracheal Stent", "l_ystent", None),
    ]),
    ("Esophageal", [
        ("bonastent-esophogeal-stent", "Bonastent&reg; Esophageal Stent", "l_besoph", None),
        ("hilzo-tts-esophageal-stent", "Hilzo&trade; TTS Esophageal Stent", "l_tts", None),
        ("hilzo-ues-esophageal-stent", "Hilzo&trade; UES Esophageal Stent", "l_ues", None),
    ]),
    ("Accessories", [
        ("hydro-slide-pulmonary-guidewire", "Hydro-Slide Pulmonary Guide Wire", "l_guidewire", None),
        ("netis-retrieval-net", "Netis Retrieval Net", "netis1", None),
    ]),
]

# Diagnosis (biopsy / tissue-sampling) tools.
DIAGNOSIS_TOOLS = [
    ("biopsy-forceps", "Biopsy Forceps", "l_forceps", None),
    ("ebus-needles", "EBUS Needles", "l_ebus", None),
    ("narwhal-cryo-system", "Narwhal Cryo System", "narwhal", None),
]

def pcards(items):
    out = ""
    for slug, name, imgkey, abbr in items:
        src = IMG.get(imgkey) if imgkey else None
        ph = (f'<img src="{src}" alt="{name}" loading="lazy">' if src
              else f'<span class="abbr">{abbr or name}</span>')
        out += (f'<div class="pcard"><div class="card-photo">{ph}</div>'
                f'<div class="card-info"><h3>{name}</h3>'
                f'{btn(f"products/{slug}.html","Learn more")}</div></div>\n')
    return out

def pgroups(groups):
    out = ""
    for label, items in groups:
        out += (f'<div class="pgroup"><div class="pglabel">{label}</div>'
                f'<div class="pgrid">{pcards(items)}</div></div>\n')
    return out

PRODUCTS_HERO = f"{CDN2}/680906a5e5bd468c21e28ddc_products-hero.jpeg"

def build_products():
    thoracent_body = f"""
<div class="hero-thin zoomout"><img class="hero-img" src="images/intervention.jpg" alt=""><div class="overlay"></div><div class="container inner">
 <h1>intervention</h1>
</div></div>

<section class="band light prod-section" id="thoracent"><div class="container">
 <div class="sechead">
  <img class="famlogo" src="{IMG['interv_logo']}" alt="Maverix Interventional Portfolio">
  <div class="distby inline"><div class="seclabel">Distributed by</div>
   <img src="assets/thoracent-by-maverix-logo.png" alt="Thoracent, a Maverix company"></div>
  {contact_block()}</div>
 <div class="seclabel">About</div>
 <p class="biglead">When a malignant tumor narrows the airway or esophagus, every breath and every swallow becomes a struggle. The Thoracent stent portfolio gives interventional pulmonologists and gastroenterologists minimally invasive tools to reopen the lumen and relieve obstructive symptoms.</p>
 <p class="bodytext">Malignant central airway obstruction and dysphagia from esophageal tumors are among the most distressing complications of thoracic cancers, and stenting offers mechanical relief as part of a multidisciplinary palliative care plan. Built on established self-expanding Nitinol platforms, each stent is engineered for controlled endoscopic deployment, conformability to patient anatomy, and radial support where it&rsquo;s needed most &mdash; with sizes and delivery options spanning straight tracheobronchial segments, the carina, and the esophagus, so physicians can match the device to the patient. Every device is supplied sterile, for single use.</p>
 <div class="seclabel">Products</div>
 {pgroups(INTERVENTION_GROUPS)}
 <p class="rxnote">All devices are prescription-only, for use by trained physicians. See each product&rsquo;s Instructions for Use for complete indications, contraindications, warnings, and precautions.</p>
</div></section>"""

    diagnostics_body = f"""
<div class="hero-thin zoomout"><img class="hero-img" src="{IMG['xray']}" alt=""><div class="overlay"></div><div class="container inner">
 <h1>risk assessment</h1>
</div></div>

<section class="band light prod-section" id="maverix-diagnostics"><div class="container">
 <div class="sechead"><img class="famlogo" src="{IMG['diag_logo']}" alt="Maverix Diagnostics">
  {contact_block(MVX_EMAIL, phone=False)}</div>
 <div class="seclabel">About</div>
 <p class="biglead">Early cancer detection lowers treatment costs{ref(1,2)} and saves lives{ref(3,4)} &hellip; but most lung nodules discovered in radiology studies lack clear indicators of malignancy,{ref(5)} leaving uncertainty about which patients need intervention.</p>
 <p class="bodytext">We are developing a diagnostic test that aims to better clarify which patients are most likely to benefit from either tissue sampling or continued monitoring. This helps focus physician efforts on patients that require more active intervention.</p>
 <div class="photo-cards expand">
  <div class="photo-card has-reveal" tabindex="0"><img src="{IMG['detection']}" alt="" loading="lazy"><div class="photo-title">Early detection and resection is crucial&hellip;</div>
   <div class="reveal"><div class="photo-title-reveal">Early detection and resection is crucial&hellip;</div><p class="lead">82% of stage I patients remain recurrence-free five years after surgery.{ref(6)}</p><p class="photo-subtitle">Lung nodules are detected in 1/4 of CT scans{ref(7)} with few ultimately identified as cancer.{ref(8)}</p></div></div>
  <div class="photo-card has-reveal" tabindex="0"><img src="{IMG['holding_hands']}" alt="" loading="lazy"><div class="photo-title">because time is the enemy&hellip;</div>
   <div class="reveal"><div class="photo-title-reveal">because time is the enemy&hellip;</div><p class="lead">Nearly a third of patients wait three months or more to begin treatment.{ref(9)}</p><p class="photo-subtitle">Current practice for indeterminate nodules is to diagnose over time, so doctors must wait for the next CT scan to see if a nodule grows.{ref(8,10)}</p></div></div>
  <div class="photo-card has-reveal" tabindex="0"><img src="{IMG['jenny']}" alt="" loading="lazy"><div class="photo-title">&hellip;and a diagnostic could change everything.</div>
   <div class="reveal"><div class="photo-title-reveal">&hellip;and a diagnostic could change everything.</div><p class="lead">A diagnostic tool that identifies high-risk patients could move them to the front of the line for a biopsy.</p><p class="photo-subtitle">Their treatment regime could start earlier, which has been associated with better outcomes in early-stage lung cancer.{ref(11,12)}</p></div></div>
 </div>
 {refs_section()}
 <p class="rxnote">Currently under development, product not cleared or available in the US.</p>
</div></section>"""

    serpex_body = f"""
<div class="hero-thin"><img class="hero-img" src="images/diagnosis.jpg" alt=""><div class="overlay"></div><div class="container inner">
 <h1>diagnosis</h1>
</div></div>

<section class="band light prod-section" id="maverix-biopsy-tools"><div class="container">
 <div class="sechead">
  <img class="famlogo" src="{IMG['biopsy_logo']}" alt="Maverix Biopsy Tools">
  <div class="distby inline"><div class="seclabel">Distributed by</div>
   <img src="assets/thoracent-by-maverix-logo.png" alt="Thoracent, a Maverix company"></div>
  {contact_block(phone=False)}</div>
 <div class="seclabel">About</div>
 <p class="biglead">An accurate diagnosis starts with adequate tissue.</p>
 <p class="bodytext">Maverix offers a suite of endobronchial instruments for interventional pulmonologists &mdash; from forceps for histological sampling of the airway wall, to ultrasound-guided needles for submucosal and extramural targets, to a cryoprobe that takes tissue biopsies by cryoadhesion and removes foreign bodies, mucus plugs, clots, and necrotic tissue.</p>

 <div class="seclabel">Products</div>
 <div class="pgrid">{pcards(DIAGNOSIS_TOOLS)}</div>

 <div class="seclabel">Featured</div>
 <section class="nwfeature">
  <div class="nw-top">
   <div class="nw-copy">
    <div class="nw-kicker">Maverix Narwhal Cryo System</div>
    <h2 class="nw-title">The Future<br>of Cryobiopsy<span class="nw-dot">.</span></h2>
    <p class="nw-lede">A single-use, completely disposable, console-free cryobiopsy probe &mdash; handheld and self-contained,
     with selectable sampling lengths and no cryo console to purchase or service.</p>
    <a class="btn nw-cta" href="products/narwhal-cryo-system.html">
     <span class="circ">{ARROW_SVG}</span><span class="btn-label">Explore the Narwhal Cryo System</span></a>
   </div>
   <div class="nw-shot"><img src="images/narwhal/hero.jpg" alt="Narwhal cryoprobe tip" loading="lazy"></div>
  </div>

  <div class="nw-body">
   <div class="nw-seclabel">Design innovations for efficiency and control</div>
   <div class="nw-cards">
    <div class="nw-card">
     <h3>No capital equipment.</h3>
     <div class="nw-cardimg"><img src="images/narwhal/no-console.jpg" alt="Narwhal probe with its single-use Cryo cartridge" loading="lazy"></div>
     <div class="nw-why">Why it matters</div>
     <p>Handheld and self-contained. Each probe is powered by a single-use Cryo cartridge,
      freeing cryobiopsy from a fixed console &mdash; simplifying setup and use.</p>
    </div>
    <div class="nw-card">
     <h3>Pointed tip.</h3>
     <div class="nw-cardimg"><img src="images/narwhal/pointed-tip.jpg" alt="Pointed, radiopaque cryoprobe tip" loading="lazy"></div>
     <div class="nw-why">Why it matters</div>
     <p>A pointed, radiopaque cryoprobe tip facilitates direct access for efficient biopsy sampling.</p>
    </div>
    <div class="nw-card">
     <h3>All-in-one adjustable tip length.</h3>
     <div class="nw-cardimg"><img src="images/narwhal/tip-length.jpg" alt="Integrated tip-length adjustment dial, 3 mm or 6 mm" loading="lazy"></div>
     <div class="nw-why">Why it matters</div>
     <p>Selectable tip length puts the physician in control. An integrated adjustment dial offers
      short (~3&nbsp;mm) or long (~6&nbsp;mm) options, allowing sample size matching to the target.</p>
    </div>
   </div>

   <div class="nw-seclabel evidence">Backed by preclinical testing</div>
   <h3 class="nw-evtitle">Building a strong clinical foundation.</h3>
   <p class="nw-evlede">In our preclinical animal studies, the Maverix Narwhal cryobiopsy probe met every
    predefined endpoint for performance and safety, capturing high-quality samples with no clinically
    significant bleeding or pneumothorax observed.
    <span class="nw-n">(37 biopsy samples across 3-, 5-, and 7-second freeze times)</span></p>
   <div class="nw-stats">
    <div class="nw-stat"><div class="nw-fig">100%</div>
     <p>All predefined performance endpoints met.</p></div>
    <div class="nw-stat"><div class="nw-fig">0</div>
     <p>Pneumothorax observed or major bleeding events.*</p></div>
    <div class="nw-stat"><div class="nw-fig split-figure">
      <span>7.3<em>mg</em><small>3 mm</small></span><i></i><span>12.4<em>mg</em><small>6 mm</small></span></div>
     <p>Average biopsy sample weight by sampling length.</p></div>
   </div>
   <p class="nw-foot">Data on file at Maverix. Predefined performance endpoints: avulsion success rate,
    biopsy weight, usability, bleeding, pneumothorax, gross necropsy, histological accessibility, and
    percent artifact-free biopsy samples. Fluoroscopy time and radiation dose were also characterized in
    this analysis. *Minor bleeding was observed in some samplings; it was not clinically significant, met
    the pre-determined acceptance criteria, and was statistically the same as the comparison device. As
    with any cryosurgical procedure, bleeding and pneumothorax are potential risks &mdash; refer to the
    Instructions for Use. Preclinical results may not be representative of clinical performance.</p>
  </div>
 </section>
 <p class="rxnote">All devices are prescription-only, for use by trained physicians. See each product&rsquo;s Instructions for Use for complete indications, contraindications, warnings, and precautions.</p>
</div></section>"""

    overview_body = f"""
<div class="hero-thin"><img class="hero-img" src="images/diagnosis.jpg" alt=""><div class="overlay"></div><div class="container inner">
 <h1>products</h1>
</div></div>

<section class="band light prod-section"><div class="container">
 <div class="famrow">
  <div class="family-cell cat-risk"><h4>Risk Assessment</h4>
   <p>Developing molecular diagnostic tools that aim to triage lung cancer in patients to identify those in need of immediate care.</p>
   {btn("diagnostics.html","Explore Maverix Diagnostics")}</div>
  <div class="family-cell cat-diagnosis"><h4>Diagnosis</h4>
   <p>Endobronchial tissue-sampling instruments designed to help physicians obtain the tissue needed for an accurate diagnosis.</p>
   {btn("serpex.html","Explore Biopsy Tools")}</div>
  <div class="family-cell cat-intervention"><h4>Intervention</h4>
   <p>Minimally invasive devices for managing pleural effusions, restoring airway patency, and improving quality of life, along with an expanded suite of GI tools.</p>
   {btn("thoracent.html","Explore the interventional portfolio")}</div>
 </div>
 <div class="distby"><div class="seclabel">Distributed by</div>
  <img src="assets/thoracent-by-maverix-logo.png" alt="Thoracent, a Maverix company"></div>
</div></section>"""

    page("products.html", "Products – Maverix Medical",
         "Three product families across the lung cancer pathway: molecular risk assessment, endobronchial tissue sampling, and minimally invasive intervention.",
         overview_body, subtitle="Products overview — Risk Assessment, Diagnosis, Intervention")
    page("thoracent.html", "Intervention – Maverix Medical",
         "Self-expanding Nitinol stents and accessories that reopen the airway and esophagus to relieve obstructive symptoms from thoracic tumors.",
         thoracent_body, subtitle="Maverix Interventional Portfolio — stents and accessories")
    page("diagnostics.html", "Risk Assessment – Maverix Medical",
         "Developing a diagnostic test that aims to better clarify which patients are most likely to benefit from either tissue sampling or continued monitoring.",
         diagnostics_body, subtitle="Maverix Diagnostics — screening")
    page("serpex.html", "Diagnosis – Maverix Medical",
         "Endobronchial tissue-sampling instruments designed to help physicians obtain the tissue needed for an accurate diagnosis.",
         serpex_body, subtitle="Maverix Biopsy Tools — forceps, EBUS needles, cryobiopsy")

def spec_block(rows_html, cols=True, head="Specifications"):
    """Specification table, wrapped so it can scroll horizontally on narrow screens.

    The wrapper (not the table) owns the overflow, which lets the CSS paint
    self-hiding edge shadows on it — see the v51 block in theme.css.tpl. The
    hint line below is the explicit version of the same cue for phones.
    """
    cls = "spec cols" if cols else "spec"
    return (f'<h3 class="spec-head">{head}</h3>'
            f'<div class="spec-scroll"><table class="{cls}">{rows_html}</table></div>'
            f'<p class="spec-hint">Swipe the table to see all columns &rarr;</p>')


# 510(k) clearance numbers, keyed by product page slug. Rendered by pd_page()
# as a note at the foot of the page, in the same style as the manufacturer
# note. A product absent from this map simply shows no number -- to add one
# later, add the slug here and rebuild; nothing else needs to change.
K510 = {
    "bonastent-tracheobronchial-stent": "K140472",
    "bonastent-esophogeal-stent":       "K092144",
    "hilzo-tts-esophageal-stent":       "K223266",
    "hilzo-ues-esophageal-stent":       "K223266",
    "y-shaped-tracheal-stent":          "K212403",
    "ebus-needles":                     "K213060",
    "narwhal-cryo-system":              "K261068",
}


# ------------------------------------------------------------------ PRODUCT DETAIL PAGES
def pd_page(slug, name, brand_logo, desc_paras, features, images, resources, specs_html="",
            contact_thoracent=True, videos=None, parent="thoracent", dist_by=True, note="",
            mfg_logo=None):
    feats = "".join(f"<li>{f}</li>" for f in features)
    paras = "".join(f'<p class="bodytext">{p}</p>' for p in desc_paras)
    imgs = "".join(f'<div class="pd-img" style="margin-bottom:1.8rem;"><img src="{u}" alt="{html.escape(name)}" loading="lazy"></div>' for u in images)
    ext_links = "".join(f'<a href="{u}" target="_blank" rel="noopener">{lbl} <span class="ext-icon">&#8599;</span></a>' for lbl, u in resources)
    vid_tab = '<button data-tab="pane-videos">Demonstration Videos</button>' if videos else ""
    vid_pane = ""
    if videos:
        vids = "".join(f'<h3 style="font-family:var(--font-tagline);color:var(--heading);font-size:1.5rem;margin-top:1.2rem;">{t}</h3><iframe class="video-embed" src="https://www.youtube-nocookie.com/embed/{vid}" title="{t}" allowfullscreen loading="lazy"></iframe>' for t, vid in videos)
        vid_pane = (f'<div class="tabpane" id="pane-videos">'
                    f'<h2 class="pd-title">Demonstration Videos</h2>{vids}</div>')
    contact = contact_block() if contact_thoracent else contact_block(MVX_EMAIL, phone=False)
    crumb_href, crumb_txt = (("../serpex.html", "All Diagnosis products") if parent == "serpex"
                             else ("../thoracent.html", "All Intervention products"))
    side_logo = (f'<div class="pd-brand"><div class="seclabel">Distributed by</div>'
                 f'<img src="{brand_logo}" alt=""></div>' if dist_by
                 else f'<div class="pd-brand"><img src="{brand_logo}" alt=""></div>')
    # Foot-of-page note: the manufacturer line (where set) and the 510(k)
    # number (where known) share one line, in that order.
    foot = [x for x in (note, f"510(k) {K510[slug]}." if slug in K510 else "") if x]
    note_html = f'<p class="mfg-note">{" ".join(foot)}</p>' if foot else ""
    # Optional second lockup in the right rail, below the phone number, for
    # products sold under a manufacturer's own brand (the Hilzo stents).
    mfg_block = (f'<div class="pd-brand pd-mfg"><div class="seclabel">Manufactured by</div>'
                 f'<img src="{mfg_logo}" alt=""></div>' if mfg_logo else "")
    body = f"""
<div class="pd-hero"><div class="container">
 <a class="crumb" href="{crumb_href}">&#8592; {crumb_txt}</a>
 <h1>{name}</h1>
</div></div>
<div class="tabbar"><div class="container tabbar-in">
 <button class="is-active" data-tab="pane-features">Features</button>
 {vid_tab}
 {ext_links}
</div></div>
<section class="band light"><div class="container" style="padding:0;">
 <div class="pd-wrap">
  <div class="pd-panel">
   <div class="tabpane is-active" id="pane-features">
    {imgs}
    <h2 class="pd-title">Features</h2>
    {paras}
    <ul class="benefits">{feats}</ul>
    {specs_html}
    {note_html}
   </div>
   {vid_pane}
  </div>
  <div class="pd-side">
   {side_logo}
   {contact}
   {mfg_block}
  </div>
 </div>
</div></section>"""
    suffix = "Thoracent by Maverix" if dist_by else "Maverix Medical"
    page(f"products/{slug}.html", f"{name} – {suffix}",
         desc_paras[0][:150], body, rel="../", group="Product Pages", subtitle="Product detail")



def build_product_pages():
    pd_page("y-shaped-tracheal-stent", "Y-Shaped Tracheal Stent", THOR_LOGO,
        ["The Micro-tech Y-Stent provides relief to patients with strictures to aid in the treatment of malignant neoplasms in the tracheobronchial carina. It is made of nitinol wire woven in a tubular mesh shape. The structure makes the stent flexible, compliant, and self-expanding.",
         "The stent is partially covered in silicone to restrict tissue in-growth through the wire mesh. A retrieval loop is threaded through the proximal and distal ends of the stent and is intended to aid in repositioning during the stent placement procedure. To aid in visibility under fluoroscopy, there are radiopaque markers at key landmarks on the stent (proximal end, bifurcation, distal ends). The stent branches have flanges to help minimize migration after the stent has been placed in the trachea."],
        ["Covered self-expanding nitinol design &mdash; maximizes airway space while reducing tissue in-growth",
         "Low-profile (8 mm) delivery system &mdash; allows for direct visualization and ventilation during positioning",
         "Flexibility of sizes &mdash; meets a large range of patient anatomies",
         "Repositioning sutures &mdash; eases adjustment post-deployment"],
        ["../images/ystent.png"],
        [("Size Chart", "https://thoracent.com/wp-content/uploads/2023/07/Y-Stent-Brochure-2022.pdf"),
         ("MR Conditional Statement / IFU", "https://thoracent.com/wp-content/uploads/2022/11/1-0023806-0-Tracheal-Stent-System-Y-shaped-IFU.pdf")],
        mfg_logo=IMG["microtech_logo"],
        videos=[("Demonstration Video", "BlNMh7UvbsY")])

    pd_page("bonastent-tracheobronchial-stent", "Bonastent Tracheobronchial Stent", THOR_LOGO,
        ["The Bonastent Tracheobronchial Stent features a revolutionary, patented “hook and cross” nitinol stent design with a silicone cover purposely placed across the entire interior of the stent to reduce both in-growth and migration.",
         "An ultra-thin coaxial deployment system allows some sizes to be delivered through the working channel of a flexible therapeutic bronchoscope, and the stent can be re-captured up to 70% deployed."],
        ["Woven nitinol design &mdash; facilitates conformability",
         "Fully covered by silicone &mdash; prevents tissue in-growth",
         "Covering intentionally placed on the inside of the stent &mdash; reduces migration",
         "Ultra-thin delivery catheter (some sizes) &mdash; allows deployment through the working channel of a flexible therapeutic bronchoscope",
         "Recapturable &mdash; can be re-captured up to 70% deployed"],
        ["../images/bonastent-tb.jpg"],
        [("Size Chart", "../assets/bonastent-tracheobronchial-size-chart.pdf"),
         ("MR Conditional Statement", "https://thoracent.com/wp-content/uploads/2018/11/IFU-Information-for-MR-Safety.pdf")],
        mfg_logo=IMG["bonastent_logo"],
        videos=[("In-Service Video", "5ULYrDMMrfI"),
                ("TTS Demonstration", "Wb-wJ6yhg0U"),
                ("Silicone Cover", "aAlaLDMlzzg")])

    pd_page("ebus-needles", "EBUS Needles", THOR_LOGO,
        ["EBUS (endobronchial ultrasound-guided transbronchial needle aspiration) needles are medical devices used to obtain tissue samples from the lungs and surrounding lymph nodes during minimally invasive diagnostic procedures performed through the bronchoscope."],
        ["Unique tri-tip core design (Trident FNB) &mdash; maximizes yield and enables consistent tissue acquisition",
         "Elongated dual-edged bevel tip (Areus FNA) &mdash; aids in precise penetration into the target area",
         "Push-button adjustors &mdash; offer quick, one-handed control for needle depth and sheath length",
         "Nitinol construction &mdash; provides superior strength and accuracy",
         "Laser-etched V pattern on needle surface &mdash; provides visibility under ultrasound"],
        ["../images/ebus.jpg"],
        [], parent="serpex",
        specs_html=spec_block("""
<thead><tr><th>SKU</th><th>Description</th><th>Size</th><th>Needle Length</th><th>Sheath Diameter</th><th>Min. Channel Size</th></tr></thead>
<tbody>
<tr><td>BU49211</td><td>Areus EBUS FNA Nitinol Needle</td><td>19 GA</td><td>4 cm</td><td>1.8 mm</td><td>2.0 mm</td></tr>
<tr><td>BU49221</td><td>Areus EBUS FNA Nitinol Needle</td><td>22 GA</td><td>4 cm</td><td>1.8 mm</td><td>2.0 mm</td></tr>
<tr><td>BU49231</td><td>Areus EBUS FNA Nitinol Needle</td><td>25 GA</td><td>4 cm</td><td>1.8 mm</td><td>2.0 mm</td></tr>
<tr><td>BU49241</td><td>Trident EBUS FNB Nitinol Needle</td><td>19 GA</td><td>4 cm</td><td>1.8 mm</td><td>2.0 mm</td></tr>
<tr><td>BU49251</td><td>Trident EBUS FNB Nitinol Needle</td><td>22 GA</td><td>4 cm</td><td>1.8 mm</td><td>2.0 mm</td></tr>
<tr><td>BU49261</td><td>Trident EBUS FNB Nitinol Needle</td><td>25 GA</td><td>4 cm</td><td>1.8 mm</td><td>2.0 mm</td></tr>
</tbody>"""),
        mfg_logo=IMG["microtech_logo"],
        videos=[("Demonstration Video", "Wv3mFCvMWiw")])

    pd_page("biopsy-forceps", "Biopsy Forceps", THOR_LOGO,
        ["Biopsy forceps are surgical instruments used to obtain tissue samples for microscopic examination during procedures including endoscopy, colposcopy, and other medical interventions."],
        ["Single use",
         "Sterile",
         "Fenestrated oval cups",
         "Teflon-coated polyethylene sheath for easy passability",
         "3-ring handle for tactile feedback",
         "Compatible with Ion, Monarch, and Galaxy robotic navigation systems"],
        ["../images/forceps.jpg"],
        [], parent="serpex",
        specs_html=spec_block("""
<thead><tr><th>SKU</th><th>Description</th><th>Sheath Diameter</th><th>Length</th><th>UOM</th></tr></thead>
<tbody>
<tr><td>MED-114-FOR</td><td>Biopsy Forceps</td><td>1.8 mm</td><td>160 cm</td><td>Box 10</td></tr>
</tbody>"""))

    pd_page("hydro-slide-pulmonary-guidewire", "Hydro-Slide Pulmonary Guidewire", THOR_LOGO,
        ["A single-use .035″ pulmonary guidewire designed to establish and maintain a path through the airway, with a nitinol core and hydrophilic distal tip, available in 180 cm and 260 cm lengths."],
        ["Nitinol core designed to resist kinking and retain shape through tortuous airways.",
         "Hydrophilic tip (distal 5 cm) designed to facilitate smooth wire advancement.",
         "Radiopaque tip visible under fluoroscopy to support wire placement."],
        ["../images/guidewire.jpg"],
        [],
        specs_html="""<div class="spec-scroll"><table class="spec">
<tr><th colspan="2">Specifications</th></tr>
<tr><td>Gauge</td><td>.035&Prime;</td></tr>
<tr><td>Available lengths</td><td>180 cm and 260 cm</td></tr>
<tr><td>Construction</td><td>Nitinol core with hydrophilic distal tip</td></tr>
</table></div>""")

    pd_page("hilzo-tts-esophageal-stent", "Hilzo™ TTS Esophageal Stent", THOR_LOGO,
        ["The Hilzo™ TTS (Through-the-Scope) Esophageal Stent system consists of a delivery system preloaded with a self-expanding esophageal metal stent. The stent is made of nitinol wire knitted in a tubular mesh configuration, making it flexible and self-expandable."],
        ["Silicone-covered dumbbell-shaped ends designed to reduce tissue in-growth on fully covered versions",
         "Uncovered dumbbell-shaped ends designed to reduce migration on partially covered versions",
         "Stent body covered with PTFE",
         "Dual retrieval string (proximal and distal ends)",
         "Large distal and proximal radiopaque markers to allow fluoroscopic visibility",
         "10.5 Fr TTS delivery system"],
        ["../images/hilzo-tts.jpg"],
        [("Size Chart", "https://thoracent.com/wp-content/uploads/2024/05/Hilzo-TTS-Size-Chart.pdf"),
         ("MR Conditional Statement &amp; IFU", "https://thoracent.com/wp-content/uploads/2024/05/Hilzo-Esoph-IFU-and-MR-Conditional-stmt.pdf")],
        mfg_logo=IMG["hilzo_logo"])

    pd_page("hilzo-ues-esophageal-stent", "Hilzo™ UES Esophageal Stent", THOR_LOGO,
        ["The Hilzo&trade; UES (Upper-Esophageal Sphincter) Esophageal Stent system consists of a delivery system preloaded with a self-expanding esophageal metal stent. The stent is made of nitinol wire knitted in a tubular mesh configuration, making it flexible and self-expandable. Designed specifically for placements close to the UES with a 0.5 cm proximal flare."],
        ["Proximal flare 0.5 cm in length for added room in placements close to the UES",
         "Distal flare 1.5 cm to prevent migration",
         "Silicone-covered flares designed to reduce tissue in-growth",
         "Body covered with PTFE",
         "Dual retrieval string (proximal and distal ends)",
         "Large distal and proximal radiopaque markers to allow fluoroscopic visibility",
         "14 Fr over-the-wire delivery system"],
        ["../images/hilzo-ues.jpg"],
        [("Size Chart", "https://thoracent.com/wp-content/uploads/2024/05/Hilzo-UES-Size-Chart.pdf"),
         ("MR Conditional Statement &amp; IFU", "https://thoracent.com/wp-content/uploads/2024/05/Hilzo-Esoph-IFU-and-MR-Conditional-stmt.pdf")],
        mfg_logo=IMG["hilzo_logo"])

    pd_page("bonastent-esophogeal-stent", "Bonastent Esophageal Stent", THOR_LOGO,
        ["Bonastent&reg; Esophageal Stents are among the most technologically advanced non-vascular, self-expandable metallic stents available today. Designed with a revolutionary, patented, nitinol hook-and-cross wire structure that allows the stent to adapt and conform to the human anatomy, resulting in reduced migration and tumor in-growth. The stents are provided pre-loaded on an ergonomically designed delivery device for ease of both implementation and placement."],
        ["Low rate of shortening for accurate positioning",
         "Silicone covering placed on the inside of stent to reduce both in-growth and migration",
         "Optimal radial and returning force for conformability",
         "Hook and cross wire design allows for segmental compression to conform to the patient&rsquo;s anatomy",
         "Reduced delivery device diameter vs. competitive stents",
         "Ability to re-capture stent up to 70% deployed"],
        ["../images/bonastent-esoph.jpg"],
        [("Size Chart", "https://thoracent.com/wp-content/uploads/2018/11/Bonastent-Esophageal-Chart.jpg"),
         ("MR Conditional Statement", "https://thoracent.com/wp-content/uploads/2018/11/IFU-Information-for-MR-Safety.pdf")],
        mfg_logo=IMG["bonastent_logo"],
        videos=[("In-Service Video", "ulmYfVy8j64")])

    pd_page("netis-retrieval-net", "Netis Retrieval Net", THOR_LOGO,
        ["The Netis Retrieval Nets are designed for reliable and secure retrieval of polyps and foreign bodies during medical procedures. They feature a high-density polyethylene (HDPE) catheter with a large internal diameter, a firm monofilament snare, a flat wire connection, and a rotatable option."],
        ["Rotatable and non-rotatable versions",
         "Multiple size options including 50x80 mm endoscope submucosal dissection (ESD) net",
         "Hand-sewn to the snare rather than glued",
         "Firm monofilament snare",
         "Large net area allows for more flexibility to remove larger foreign bodies"],
        [IMG["netis1"]],
        [],
        specs_html=spec_block("""
<thead><tr><th>SKU</th><th>Description</th><th>Size</th><th>Sheath Diameter</th><th>Length</th><th>UOM</th></tr></thead>
<tbody>
<tr><td>MED-194-NET</td><td>Micro Retrieval Net</td><td>25 x 45 mm</td><td>1.8 mm</td><td>160 cm</td><td>Box 10</td></tr>
<tr><td>MED-200-NET</td><td>Bronch Retrieval Net</td><td>10 x 25 mm</td><td>1.8 mm</td><td>120 cm</td><td>Box 10</td></tr>
</tbody>"""),
        videos=[("Deployment", "Cx7Ap8kGSyA")])

    pd_page("narwhal-cryo-system", "Narwhal Cryo System", THOR_LOGO,
        ["A single-use, console-free cryobiopsy probe designed for palliative devitalization (destruction) of tissue during interventional procedures by the application of extreme cold and cryo-adhesion, for applications such as the removal of foreign bodies, mucus plugs, blood clots, necrotic tissue, tissue tumors (palliative recanalization) and tissue biopsies. It is handheld and self-contained, with selectable sampling lengths and no cryo console to purchase or service."],
        ["Single-use N&#8322;O cartridge &mdash; console-free operation, with no capital equipment to purchase or service",
         "Integrated adjustment dial, 3 mm or 6 mm tip sampling length &mdash; sampling length matched to the target",
         "Pointed, radiopaque tip &mdash; direct access and fluoroscopic visibility",
         "1.3 mm shaft, 115 cm working length &mdash; compatible with 2.0 mm or larger working channels, including robotic and endoscopic platforms",
         "~80 seconds of freeze endurance per cartridge &mdash; ~160 seconds across two cartridges",
         "Sterile, single-use probe"],
        ["../images/narwhal-cryo.jpg"],
        [],
        parent="serpex",
        note="Manufactured by Serpex Medical.")

# ------------------------------------------------------------------ TEAM
LEADERS = [
 ("aftab","Aftab Kherani, M.D.","Managing Partner, Ajax Health",
  ["Aftab Kherani, M.D. is a Managing Partner at Ajax Health, Chairman of Summus Global, and a member of the Duke University School of Medicine Board of Visitors. He was previously a Partner at Aisling Capital, a life science investment fund, and his board experience includes Arcus Biosciences, Loxo Oncology, Spirox, Syros Pharmaceuticals, and TransEnterix.",
   "Earlier in his career, Dr. Kherani was an Engagement Manager at McKinsey & Company in the pharmaceutical, medtech, and private equity practices. He served as Chief Resident in Surgery at Duke University Medical Center, completed a post-doctoral research fellowship at Columbia University investigating cardiac treatments, and was an organ procurement fellow on the New York Presbyterian Hospital cardiothoracic transplantation team.",
   "Dr. Kherani earned his M.D. from Duke University, where he was a Howard Hughes Medical Institute Research Fellow, and received a B.S. in Biology and an A.B. in Economics from Duke University, graduating magna cum laude and Phi Beta Kappa."],
  "https://www.linkedin.com/in/aftab-kherani-3403915/"),
 ("basile","Basile Montagnese","Director of Business Development",
  ["Basile Montagnese is Director of Business Development at Maverix and an Associate at Ajax Health, where he has contributed to platforms including Cordis/Cordis-X, Cortex, and FlowMod.",
   "Basile joined Ajax from Dartmouth College's biomedical engineering program, where he earned his B.A. and B.E., graduating first in the engineering school, summa cum laude, with peer-reviewed publications and a patent."],
  "https://www.linkedin.com/in/basile-montagnese-64303a156/"),
 ("brian","Brian Lynch","Chief Revenue Officer; President, Medical Device Division",
  ["Brian Lynch founded Thoracent in 2017 and served as its CEO through the company's integration with Maverix. He played a key role in launching and scaling the EndoChoice commercialization team, helping grow the company from $0 to a NYSE-listed company (NYSE: GI) with more than $85M in annual sales over six years.",
   "Brian's thirty-year medtech career includes sales roles at ev3, Boston Scientific, and Pfizer. He earned a B.A. in Marketing from Siena College, where he was a member of the football team."],
  "https://www.linkedin.com/in/brian-lynch-15557a8/"),
 ("carla","Carla Jung","Chief Executive Officer",
  ["Carla Jung is Chief Executive Officer of Maverix and an Entrepreneur in Residence at Ajax Health. She joined Maverix as Chief Commercial Officer in 2025, bringing 27 years of medtech experience.",
   "Carla spent her last thirteen years at Medtronic building and transforming large sales organizations, launching more than 10 products across cardiovascular, electrophysiology, structural heart, and interventional cardiology. Before Medtronic, she spent eleven years at Boston Scientific as a commercial leader and director of the EP Fellows Program Division, and began her career in Women's Health at Eli Lilly.",
   "Her honors include the 2021 Wallin Award for leadership and performance and the GIDE Award for Inclusive Leadership. Carla holds an M.B.A. from Columbia University and a B.A. from Villanova University."],
  "https://www.linkedin.com/in/carla-jung/"),
 ("beylik","David Beylik","Executive Chair",
  ["David Beylik is Executive Chair at Maverix and a Partner at Ajax Health. He was previously an associate at Latham & Watkins LLP, advising emerging companies and venture capital and private equity firms on governance, equity financing, and M&A.",
   "David served as a judicial law clerk to Chief Justice John Roberts of the U.S. Supreme Court, Judge Brett Kavanaugh of the U.S. Court of Appeals, and Judge Dabney Friedrich of the U.S. District Court, and as a judicial extern to Judge Mark Wallace of the U.S. Bankruptcy Court. He also led business development for The Drop Box documentary, which raised more than $10M for children with disabilities.",
   "David earned his J.D. from Harvard Law School, graduating summa cum laude and first in his class as an editor of the Harvard Law Review, and his B.S. from the University of Southern California, summa cum laude."],
  "https://www.linkedin.com/in/david-beylik-47762a1b2/"),
 ("mallery","David Mallery","CEO, Diagnostics",
  ["David Mallery is CEO of Diagnostics at Maverix. He co-founded and served as Chairman and President of the International Genomics Consortium (IGC), leading the organization as the Biospecimen Core Resource and Tissue Source Site network for the Cancer Genome Atlas program.",
   "David co-founded and served as President of Cirrus Bio (acquired by Maverix), and co-founded Paradigm Diagnostics, Viomics, and the Molecular Profiling Institute (acquired and expanded by Exact Sciences and Caris Life Sciences). He helped develop and commercialize the first comprehensive evidence-based personalized molecular and genomic assay in U.S. oncology, and discovered and commercialized blood-based early cancer screening targets.",
   "David holds a B.A. in Human Biology and Studio Art from Stanford University and a J.D. and M.B.A. from the University of Colorado at Boulder. He is a member of the Council on Foreign Relations, YPO, and the Colorado Bar Association."],
  "https://www.linkedin.com/in/dmallery/"),
 ("doug","Doug Koo","Chief Financial Officer",
  ["Doug Koo is CFO of Maverix and a Managing Partner at Ajax Health, with more than 25 years of management consulting and venture-backed company executive experience.",
   "Doug was CFO of Cortex (an Ajax company acquired by Boston Scientific), EPIX Therapeutics (acquired by Medtronic in 2019), Spirox (acquired by Entellus in 2017), and CV Ingenuity (acquired by Covidien in 2013). He previously served as CFO and CEO at high-tech and healthcare services companies, and began his career as a management consultant at Gemini Consulting.",
   "Doug holds an M.B.A. from Stanford University and a B.A. from UC San Diego."],
  "https://www.linkedin.com/in/doug-koo-5636bb3/"),
 ("jeremy","Jeremy Durack, M.D.","Chief Medical Officer",
  ["Jeremy Durack, M.D. is Chief Medical Officer at Maverix and a Partner and SVP Medical at Ajax Health. He is a practicing interventional radiologist and former Vice-Chair of Radiology at Memorial Sloan Kettering Cancer Center. He is past chair of the Society of Interventional Radiology Foundation and a Fellow of the American College of Radiology and the Society of Interventional Radiology.",
   "His clinical expertise spans image-guided endovascular, trauma, biliary, GI, GU, and oncologic interventions, with specialization in thoracic, genitourinary, and venous procedures. He has led multicenter and international clinical trials and registries and chaired societal and institutional IT/informatics, quality, and research committees.",
   "Dr. Durack earned a B.S. with distinction from Duke University in psychology and neuroscience, an M.D. from Stanford University School of Medicine, and completed a masters program in Biological and Medical Informatics at UCSF, where he also completed his radiology residency and Interventional Radiology fellowship. He is board-certified in radiology and medical informatics, and his awards include an NSF graduate fellowship, NIBIB T32, Prostate Cancer Foundation, RSNA Roentgen, and Fulbright Specialist research awards."],
  "https://www.linkedin.com/in/jeremy-c-durack-md-fsir-facr-49a480225/"),
 ("jocelyn","Jocelyn Jackson","VP, Finance",
  ["Jocelyn Jackson is VP of Finance at Maverix and a Partner and SVP Finance at Ajax Health. She was VP Finance at Cortex (an Ajax company acquired by Boston Scientific).",
   "Jocelyn served as CFO of Symic Bio, a biopharmaceutical company developing matrix biology therapeutics, where she managed finance, accounting, and investor communication from inception to lead asset partnering, and as CFO of TauTona Group, an early-stage life science venture. As Controller of CV Ingenuity, a drug-coated balloon platform company acquired by Covidien, she was involved in asset sales to Allergan, LifeCell, and Novadaq. She started her career at Deloitte & Touche, LLP in the tax and audit departments.",
   "Jocelyn holds a B.A. from the University of San Diego."],
  "https://www.linkedin.com/in/jocelynjackson/"),
 ("neil","Neil Zimmerman","VP, Research & Development",
  ["Neil Zimmerman is VP of Research & Development at Maverix and VP Engineering at Ajax Health, with 15 years of medtech R&D and therapy development experience across startups and major strategics.",
   "Neil was VP of R&D at Half Moon Medical, incubated at The Foundry, and Principal R&D Engineer at Twelve (acquired by Medtronic), where he drove next-generation device design. He began his career at Edwards Lifesciences, developing multiple new therapies from concept to clinic in the Advanced Technology division.",
   "Neil holds an M.S. in Mechanical Engineering from Stanford University and a B.S. in Biological Engineering from MIT, where he earned Tau Beta Pi honors and captained the soccer team."],
  "https://www.linkedin.com/in/nzimm/"),
 ("rebecca","Rebecca Bergin","CFO, Thoracent",
  ["Rebecca Bergin is CFO of Thoracent, a Maverix company. She founded a management consulting firm assisting small businesses with corporate and financial management, and served as a Senior Asset Manager at Colony Capital and as a Vice President at regional banks analyzing financial performance and cash flow projections.",
   "Rebecca served as Economic Development Commissioner for the City of Lakeville, MN, and has published research on entrepreneurship in academic journals.",
   "She holds a B.A. in Economics from North Dakota State University, a certificate from the Graduate School of Banking at Colorado, and an M.B.A. with an emphasis in Entrepreneurship from Loyola Marymount University."],
  "https://www.linkedin.com/in/rebecca-bergin-93712812/"),
 ("scott","Scott Morris, Ph.D.","Chief Science Officer, Diagnostics",
  ["Scott Morris, Ph.D. is Chief Science Officer, Diagnostics at Maverix. He co-founded Cirrus Bio and served as Chief Scientific Officer of the International Genomics Consortium (IGC), leading the biospecimen core laboratory for the Cancer Genome Atlas project.",
   "Scott co-founded and served as Chief Scientific Officer of Paradigm, where he built the flagship PCDx diagnostic, and co-founded Viomics, where he developed an AI naïve-bias algorithm for biomarker discovery and discovered a new biomarker class; both companies were acquired by Exact Sciences. At Exact Sciences, he led next-generation sequencing bioinformatics and multi-omics R&D as VP, and conducted primary scientific diligence for over $3B in acquisitions including Thrive and Base Genomics.",
   "Scott holds a B.S. in molecular biology and biotechnology, a P.S.M. in computational biology, a Ph.D. in industrial engineering, and an Executive M.B.A. from Arizona State University."],
  "https://www.linkedin.com/in/scott-morris-70795a50/"),
 ("will","Will Kynes, Ph.D.","Director of Marketing & Communications",
  ["Will Kynes, Ph.D. is Director of Marketing and Communications at Maverix and Chief of Staff at Ajax Health. He was Director of Marketing and Communications at Cortex, an Ajax company acquired by Boston Scientific.",
   "Before joining Ajax, Will was a tenured professor with appointments at the University of Cambridge, University of Oxford, Whitworth University, and Samford University. An award-winning author and teacher, he has published seven books, two with Oxford University Press, and thirty articles and book chapters.",
   "Will holds a Ph.D. from the University of Cambridge, an M.Litt. with distinction from the University of St Andrews, and a B.A. with distinction from the University of Virginia."],
  "https://www.linkedin.com/in/will-kynes/"),
]
ADVISORS = ["George Cheng, M.D.","Michael Pritchett, M.D.","Kyle Hogarth, M.D.","Momen Wahidi, M.D.",
 "Javier Longoria, M.D.","Eric Seeley, M.D.","Ali Saeed, M.D.","Mike Machuzak, M.D.","Abid Khokar, M.D.","Krish Bhadra, M.D."]


# Leadership entries kept in the source but held back from the published page.
# The full record above (bio, photo, LinkedIn) stays intact — to publish someone
# again, remove their key from this set and rebuild. Nothing else to restore.
DRAFT_LEADERS = {"basile"}   # Basile Montagnese — draft, not published

def build_team():
    grid = ""
    modals = ""
    for key, name, title, bio, li in LEADERS:
        if key in DRAFT_LEADERS:      # held back — see DRAFT_LEADERS above
            continue
        grid += f"""<button class="member" data-modal-open="bio-{key}">
<img src="{HS[key]}" alt="{html.escape(name)}" loading="lazy">
<div class="member-info"><div class="member-name">{name}</div><div class="member-role">{title}</div></div></button>
"""
        paras = "".join(f"<p>{p}</p>" for p in bio)
        modals += f"""<div class="modal" id="bio-{key}"><div class="overlay"></div><div class="modal-box">
<button class="close" aria-label="Close">&times;</button>
<div class="mphoto"><img src="{HS[key]}" alt="{html.escape(name)}"></div>
<div class="mbody"><h2>{name}</h2><div class="member-role">{title}</div>
<div class="bio-text">{paras}</div>
<a class="profile-link" href="{li}" target="_blank" rel="noopener"><span class="li-badge"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.45 20.45h-3.55v-5.57c0-1.33-.03-3.04-1.85-3.04-1.86 0-2.14 1.45-2.14 2.94v5.67H9.36V9h3.41v1.56h.05c.47-.9 1.63-1.85 3.36-1.85 3.6 0 4.27 2.37 4.27 5.45v6.29zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM7.12 20.45H3.56V9h3.56v11.45z"/></svg></span>LinkedIn</a>
</div></div></div>
"""
    adv = "".join(f'<div class="advcard"><div class="member-name">{a}</div></div>' for a in ADVISORS)
    body = f"""
<div class="hero-thin"><img class="hero-img" src="images/hero-team.jpg" alt=""><div class="overlay"></div><div class="container inner">
 <h1>team</h1>
</div></div>

<section class="band white prod-section" id="leadership"><div class="container">
 <h2 class="section-title">Maverix Leadership</h2>
 <div class="teamgrid">{grid}</div>
</div></section>

<section class="band white prod-section row-line" id="advisors"><div class="container">
 <h2 class="section-title">Medical Advisory Board</h2>
 <div class="advgrid">{adv}</div>
</div></section>

{modals}"""
    page("team.html", "Team – Maverix Medical",
         "Maverix leadership combines decades of clinical, technical, and operating experience.",
         body, subtitle="Leadership bios and advisory board")

# ------------------------------------------------------------------ NEWS
NEWS = [
 ("logo_fierce","Fierce Biotech","March 29, 2024",
  "Lung Cancer Startup Maverix Medical Snaps Up Diagnostic Developer Cirrus Bio",
  "After launching late last year, the lung cancer-focused startup Maverix Medical is reaching for the sky with the acquisition of diagnostic developer Cirrus Bio.",
  "https://www.fiercebiotech.com/medtech/lung-cancer-startup-maverix-medical-snaps-diagnostic-developer-cirrus-bio"),
 ("logo_prn","PR Newswire","March 29, 2024",
  "Maverix Medical Closes Acquisition of Cirrus Bio as Foundation for Diagnostics Platform in Lung Cancer",
  "Maverix Medical, a dedicated lung cancer platform established by Ajax Health, KKR, and Hologic, Inc., today announced the acquisition of Cirrus Bio for an undisclosed amount.",
  "https://www.prnewswire.com/news-releases/maverix-medical-closes-acquisition-of-cirrus-bio-as-foundation-for-diagnostics-platform-in-lung-cancer-302103254.html"),
 ("logo_wsj","Wall Street Journal","November 30, 2023",
  "Startup Ajax Health Extends Medtech Innovation Model to Hologic",
  "Ajax creates turnkey innovation platforms for commercial-stage medtech players, and has partnered with investment firm KKR and medtech company Hologic to launch a new company.",
  "https://www.wsj.com/articles/startup-ajax-health-extends-medtech-innovation-model-to-hologic-7002fada"),
 ("logo_bw","Business Wire","November 30, 2023",
  "KKR, Hologic and Ajax Health Create New Platform to Accelerate Medical Device Innovation",
  "KKR, a leading global investment firm, today announced a new platform established with investments from KKR and Hologic, Inc., named Maverix Medical.",
  "https://www.businesswire.com/news/home/20231129739853/en/KKR-Hologic-and-Ajax-Health-Create-New-Platform-to-Accelerate-Medical-Device-Innovation"),
 ("logo_jor","Journal of Respiration","March 30, 2023",
  "Bronchoscopic Evaluation of a Steerable Needle for Simulated Tumor Targets in the Lung Periphery: A Feasibility Study (Bullseye)",
  "Peripheral bronchoscopy is often performed to biopsy peripheral pulmonary lesions. Despite technological advancements to improve reach and access to the lung periphery, diagnostic yield has been inconsistent.",
  "https://pmc.ncbi.nlm.nih.gov/articles/PMC10129018/"),
 ("logo_chest","CHEST Journal","October 1, 2021",
  "Initial Experience With Steerable Instrumentation in Human Cadaveric Models with Simulated Tumor Targets",
  "Despite growing experience using advanced guided techniques, the diagnostic yield of bronchoscopy for peripheral pulmonary lesions remains suboptimal, particularly for lesions adjacent to peripheral bronchi.",
  "https://journal.chestnet.org/article/S0012-3692(21)03254-2/fulltext"),
]

FEATURED_NEWS = ("logo_prn","PR Newswire","July 23, 2026",
 "Maverix Names Carla Jung Chief Executive Officer to Lead Next Phase of Growth",
 "Maverix Medical, a company focused on revolutionizing the diagnosis and treatment of lung cancer, today announced the appointment of Carla Jung as Chief Executive Officer. Jung will lead the company's strategy, execution, and continued growth as Maverix scales its commercial organization and brings new products to market...",
 "https://www.prnewswire.com/news-releases/maverix-names-carla-jung-chief-executive-officer-to-lead-next-phase-of-growth-302833257.html")

GRID_NEWS = [
 ("logo_md","MassDevice","July 23, 2026",
  "Lung cancer treatment developer Maverix Medical picks former Medtronic exec as CEO",
  "Lung cancer diagnostics and treatment developer Maverix Medical announced today that it appointed Carla Jung as its new CEO...",
  "https://www.massdevice.com/maverix-medical-medtronic-exec-jung-ceo/"),
] + [(a,b,c,d,e,f) for (a,b,c,d,e,f) in NEWS]

def build_news():
    cells = ""
    for logo, src, date, headline, summary, url in GRID_NEWS:
        srcel = f'<img class="srclogo" src="{IMG[logo]}" alt="{src}" loading="lazy">' if logo else f'<div class="srctext">{src}</div>'
        cells += f"""<div class="ncell">{srcel}
<div class="date">{date}</div>
<h3><a href="{url}" target="_blank" rel="noopener">{headline}</a></h3>
<p>{summary}</p>
<a class="readmore" href="{url}" target="_blank" rel="noopener">Read More</a></div>
"""
    fl, fsrc, fdate, fhead, fsum, furl = FEATURED_NEWS
    body = f"""
<div class="hero-thin newshero"><img class="hero-img" src="assets/250128-maverix-medical-042.jpg" alt=""><div class="overlay"></div><div class="container inner">
 <h1>news</h1>
</div></div>
<section class="band light"><div class="container">
 <div class="featured">
  <div class="date">{fdate}</div>
  <img class="srclogo" src="{IMG[fl]}" alt="{fsrc}">
  <h2><a href="{furl}" target="_blank" rel="noopener">{fhead}</a></h2>
  <p>{fsum}</p>
  <a class="readmore" href="{furl}" target="_blank" rel="noopener">Read More</a>
 </div>
 <div class="newsgrid">{cells}</div>
</div></section>"""
    page("news.html", "Maverix News",
         "Recent coverage of the pursuit of new lung cancer solutions at Maverix.",
         body, subtitle="Press coverage and journal publications")

# ------------------------------------------------------------------ CAREERS
ICONS = {
 "plant": '<svg viewBox="0 0 24 24"><path d="M12 21v-8"/><path d="M12 13c0-4 3-7 7-7 0 4-3 7-7 7z"/><path d="M12 13c0-4-3-7-7-7 0 4 3 7 7 7z"/></svg>',
 "hands": '<svg viewBox="0 0 24 24"><circle cx="9" cy="8" r="3"/><circle cx="17" cy="10" r="2.5"/><path d="M4 20c0-3 2.5-5 5-5s5 2 5 5"/><path d="M14 20c.2-2.5 1.8-4 3.5-4s3.3 1.5 3.5 4"/></svg>',
 "microscope": '<svg viewBox="0 0 24 24"><path d="M6 18h12M9 21h6"/><path d="M9 3l4 4-5 5-3-3z"/><path d="M13 7c3 1 5 3 5 6a5 5 0 0 1-5 5"/></svg>',
 "splash": '<svg viewBox="0 0 24 24"><path d="M12 3s6 7 6 11a6 6 0 0 1-12 0c0-4 6-11 6-11z"/></svg>',
 "beach": '<svg viewBox="0 0 24 24"><path d="M12 21v-9"/><path d="M4 12a8 8 0 0 1 16 0z"/><path d="M8 12c0-4 2-8 4-8s4 4 4 8"/></svg>',
}

def build_careers():
    body = f"""
<div class="hero-thin"><img class="hero-img" src="assets/cafe.jpg" alt=""><div class="overlay"></div><div class="container inner">
 <h1>careers</h1>
</div></div>

<section class="band light"><div class="container">
 <h2 class="section-title">Join us in revolutionizing lung cancer care</h2>
 <p class="lede">At Maverix, we are dedicated to improving care by transforming the way lung cancer is diagnosed and treated. We aim to propel improved outcomes across the continuum of care.</p>
</div></section>

<section class="band light row-line"><div class="container">
 <div class="split jobs-split" style="align-items:start;">
  <div class="jobs-col">
   <h2 class="section-title" style="color:var(--mvx-blue);">Available Jobs at Maverix</h2>
   <div class="jobs-embed">
    <div class="sk-ww-linkedin-page-jobs" data-embed-id="{SK_MAVERIX}"></div>
    <p class="jobs-empty">Loading open positions&hellip;</p>
   </div>
   <a class="btn joblink" href="{LI_MAVERIX}" target="_blank" rel="noopener">
    <span class="circ">{ARROW_SVG}</span><span class="btn-label">View all Maverix openings on LinkedIn</span></a>
  </div>
  <div class="jobs-col">
   <h2 class="section-title" style="color:var(--mvx-blue);">Available Jobs at Thoracent</h2>
   <div class="jobs-embed">
    <div class="sk-ww-linkedin-page-jobs" data-embed-id="{SK_THORACENT}"></div>
    <p class="jobs-empty">Loading open positions&hellip;</p>
   </div>
   <a class="btn joblink" href="{LI_THORACENT}" target="_blank" rel="noopener">
    <span class="circ">{ARROW_SVG}</span><span class="btn-label">View all Thoracent openings on LinkedIn</span></a>
  </div>
 </div>
</div>
<script src="https://widgets.sociablekit.com/linkedin-page-jobs/widget.js" defer></script>
</section>

<section class="band dark"><img class="bgimg" src="images/careers-about.jpg" alt="">
<div class="container">
 <div class="kicker allcaps">About you</div>
 <div class="fullrule"></div>
 <div class="stackcol">
  <h2>Helping people breathe easier is hard.</h2>
  <p class="lede">We're looking for no-limit people, those who have deep expertise and broad interests, who take individual responsibility and sacrifice for the team, who create new opportunities and deliver on them, who attack every day with relentless pace and devotion to continual improvement.</p>
 </div>
</div></section>

<section class="band light"><div class="container">
 <h2 class="section-title">Why work at Maverix?</h2>
 <div class="why-row">
  <div class="why-cell">{ICONS['plant']}<h3>Career Growth</h3><p>We are committed to the professional development of our employees. At Maverix, you will have the opportunity to grow your skills, take on new challenges, and advance your career in a supportive and dynamic environment.</p></div>
  <div class="why-cell">{ICONS['hands']}<h3>Collaborative Culture</h3><p>We believe that success is collaborative. Our team combines diverse capabilities to achieve unrivaled impact.</p></div>
  <div class="why-cell">{ICONS['microscope']}<h3>Innovative Environment</h3><p>Maverix transforms medical technology through targeted innovation. We develop products that change treatment paradigms and deliver meaningful clinical outcomes.</p></div>
  <div class="why-cell">{ICONS['splash']}<h3>Impactful Work</h3><p>By joining Maverix, you will be part of a team that is making a tangible impact on the fight against lung cancer. Our products are designed to improve patient outcomes and enhance the quality of care.</p></div>
  <div class="why-cell">{ICONS['beach']}<h3>Generous Benefits</h3><p>We provide a comprehensive benefits package to help our team members thrive both professionally and personally.</p></div>
 </div>
</div></section>

<section class="band dark"><img class="bgimg" src="images/careers-join.jpg" alt="">
<div class="container">
 <div class="kicker allcaps">Join us</div>
 <h2 style="margin:.6rem 0 1rem;">Are you ready to make a difference?</h2>
 <p class="lede">Join a company that is at the forefront of lung cancer diagnosis and treatment.</p>
 <div style="margin-top:2rem;max-width:560px;">
  <form class="form" data-mvxform name="careers" method="POST" data-netlify="true" netlify-honeypot="_gotcha"
        action="{FORM_ENDPOINT}" data-endpoint="{FORM_ENDPOINT}" data-mailto="{CONTACT_EMAIL}">
   <input type="hidden" name="form-name" value="careers">
   <p class="honeypot"><label>Do not fill this in <input type="text" name="_gotcha" tabindex="-1" autocomplete="off"></label></p>
   <div><label for="cn">Name</label><input id="cn" name="Name" type="text" required placeholder="Your name" autocomplete="name"></div>
   <div><label for="ce">Email</label><input id="ce" name="Email" type="email" required placeholder="you@example.com" autocomplete="email"></div>
   <div><label for="cm">Message</label><textarea id="cm" name="Message" rows="5" required placeholder="Tell us about yourself"></textarea></div>
   <button type="submit" style="background:var(--mvx-sky);color:#12333D;">Send message</button>
  </form>
  <div class="form-msg form-success">Thank you! Your submission has been received!</div>
  <div class="form-msg form-error">Oops! Something went wrong while submitting the form.</div>
 </div>
</div></section>"""
    page("careers.html", "Maverix Careers",
         "Join us in revolutionizing lung cancer care. We are dedicated to improving outcomes.",
         body, subtitle="Culture, benefits, open roles, join-us form")

# ------------------------------------------------------------------ CONTACT
def build_contact():
    body = f"""
<div class="hero-thin"><img class="hero-img" src="assets/contact-hero.jpeg" alt=""><div class="overlay"></div><div class="container inner">
 <h1>contact us</h1>
</div></div>
<section class="contact-dark"><div class="container" style="border:none;background:transparent;">
 <h2>Let's change the future<br>of lung cancer healthcare</h2>
 <p style="margin-top:1.2rem;max-width:620px;color:#E4EAEE;">Whether you're interested in investment, partnerships, sales inquiries, or a career at Maverix, feel free to reach out.</p>
 <form class="cform" data-mvxform name="contact" method="POST" data-netlify="true" netlify-honeypot="_gotcha"
       action="{FORM_ENDPOINT}" data-endpoint="{FORM_ENDPOINT}" data-mailto="{CONTACT_EMAIL}">
  <input type="hidden" name="form-name" value="contact">
  <p class="honeypot"><label>Do not fill this in <input type="text" name="_gotcha" tabindex="-1" autocomplete="off"></label></p>
  <div class="colL">
   <input type="text" name="First Name" placeholder="First Name*" required aria-label="First Name" autocomplete="given-name">
   <input type="text" name="Last Name" placeholder="Last Name*" required aria-label="Last Name" autocomplete="family-name">
   <input type="tel" name="Phone" placeholder="Phone Number" aria-label="Phone Number" autocomplete="tel">
   <input type="email" name="Email" placeholder="Email Address*" required aria-label="Email Address" autocomplete="email">
   <input type="text" name="Company" placeholder="Company" aria-label="Company" autocomplete="organization">
   <input type="text" name="Title" placeholder="Position / Title" aria-label="Position / Title" autocomplete="organization-title">
  </div>
  <div class="colR">
   <input type="text" name="Subject" placeholder="Subject Line*" required aria-label="Subject Line">
   <textarea name="Message" placeholder="Message*" required aria-label="Message"></textarea>
  </div>
  <button class="send" type="submit">Send Message</button>
 </form>
 <div class="form-msg form-success" style="margin-top:1.4rem;">Thank you! Your submission has been received!</div>
 <div class="form-msg form-error" style="margin-top:1.4rem;">Oops! Something went wrong while submitting the form.</div>
 <div style="margin-top:2.6rem;">
  <a class="btn on-dark" href="https://www.linkedin.com/company/maverix-medical/" target="_blank" rel="noopener"><span class="circ">{ARROW_SVG}</span>Follow us on LinkedIn</a>
  &nbsp;&nbsp;&nbsp;<a style="color:#B9E3EF;font-style:italic;" href="mailto:contact@maverixmedical.com">contact@maverixmedical.com</a>
 </div>
</div></section>"""
    page("contact-us.html", "Contact Us – Maverix Medical",
         "Whether you're interested in investment, partnerships, sales inquiries, or a career at Maverix, feel free to reach out.",
         body, subtitle="Get in touch — form and contact details")

# ------------------------------------------------------------------ LEGAL
def build_legal():
    terms = """
<section class="band light"><div class="container legal" style="max-width:860px;">
<h1>Terms of Use</h1>
<div class="effective-date">Last updated: March 17, 2026</div>
<h2>Shipping Policy</h2>
<p>Most orders are shipped same day if received before 3pm ET. All orders will be shipped overnight unless the customer specifies a different shipping option. Additional shipping methods include 2nd Day and Ground options via FedEx or UPS, with FOB Origin, Freight Collect terms.</p>
<h2>Payment Policy</h2>
<p>Payments are due within 30 days or per the terms of an executed Purchase Agreement. A valid PO# is required prior to shipment for most purchases.</p>
<h2>Return Policy</h2>
<p>Most items may be returned within 30 days of the delivery date. Products must be returned in saleable condition.</p>
<p>We are temporarily unable to accept returns on orders for EBUS needles placed after 3/16/2026.</p>
<h2>How to Return Products</h2>
<ol>
<li>Call Customer Care at (888) 978-0232, M&ndash;F 8:30&ndash;5 ET, to receive authorization for the return.</li>
<li>Items must be unused, clean, and in their original packaging.</li>
<li>Ship to: Thoracent, Inc., Attn: Returns Department, 181 14th St NE, Suite 425, Atlanta, GA 30309.</li>
</ol>
<h2>Damaged/Defective Items</h2>
<p>In rare occurrences, items may arrive damaged or with a manufacturer defect. If this happens, please contact us and we will replace the damaged item at no cost.</p>
</div></section>"""
    page("terms-of-use.html", "Terms of Use – Maverix Medical", "Maverix Medical terms of use.",
         terms, group="Legal", subtitle="Shipping, payment, and return policies")

    privacy = f"""
<section class="band light"><div class="container legal" style="max-width:860px;">
<h1>Privacy Policy</h1>
<div class="effective-date">Last updated: August 5, 2026</div>
<p>This policy explains what information this website collects, who processes it, and the choices
available to you. It applies to this site only. It does not cover information you give us by email,
telephone, or in the course of a commercial relationship with Maverix Medical, LLC or Thoracent, Inc.</p>

<h2>Information We Collect</h2>
<p>We do not operate a user account system, an online store, or a payment system on this site. We do
not ask for and do not process payment card details, and we do not knowingly collect information from
children.</p>
<p>The site collects information in two ways:</p>
<ul>
<li><b>Automatically, by our host.</b> The site is served as static files by GitHub Pages
(GitHub, Inc., a Microsoft company). Like any web host, GitHub records technical request data,
including your IP address, browser type, and the pages requested. We do not have access to these
logs. GitHub&rsquo;s handling of that data is governed by the
<a href="https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement" target="_blank" rel="noopener">GitHub Privacy Statement</a>.</li>
<li><b>Through analytics cookies, only if you consent.</b> See <i>Cookies and Analytics</i> below.</li>
</ul>

<h2>Contact and Career Enquiries</h2>
<p>The contact and enquiry forms on this site do not submit to a server we control. When you complete
one, your browser opens a message in your own email application, addressed to us and pre-filled with
what you typed. Nothing is transmitted until you send that message yourself, and no copy is stored on
this website. Once you send it, the message is handled like any other email we receive: it is used to
answer your enquiry and is retained in our business records.</p>
<p>We use the information you provide to respond to you and, where relevant, to notify you about
product and service updates. We do not sell, trade, or rent your personal information. We may share
aggregated, non-identifying information about site usage with business partners; such reports do not
identify individuals.</p>

<h2>Cookies and Analytics</h2>
<p>We use <b>CookieYes</b> as our consent management platform. On your first visit it presents a
banner where you can accept all cookies, reject non-essential cookies, or choose by category.
CookieYes stores your choice in a strictly necessary cookie so that we do not ask again on every page.
That cookie is set regardless of your choice, because it is what records the choice.</p>
<p>You can change or withdraw your consent at any time using the
<a href="#" class="cky-banner-element">Cookie Settings</a> link in the footer of any page.</p>
<p>Subject to your consent, we use <b>Google Analytics 4</b> (Google Ireland Limited / Google LLC) to
understand how the site is used &mdash; which pages are viewed, from what type of device, and how
visitors arrive. Google Analytics sets cookies (typically <code>_ga</code> and
<code>_ga_&lt;id&gt;</code>) that assign your browser a random identifier. We have IP anonymisation
enabled and we do not use Google Analytics for advertising, remarketing, or ad personalisation.
Analytics cookies remain blocked by default, through Google Consent Mode, until you opt in. If you
reject them, no analytics cookies are set and no analytics data is sent. Google&rsquo;s processing is
described in the <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">Google Privacy Policy</a>.</p>

<h2>Third-Party Services</h2>
<p>Some parts of the site load content from third parties. Doing so discloses your IP address and
basic browser information to those providers, and they may set their own cookies where noted:</p>
<ul>
<li><b>Google Fonts</b> &mdash; typefaces are loaded from Google&rsquo;s font servers on every page.
No cookies are set.</li>
<li><b>SociableKit</b> &mdash; the Careers page embeds a widget that displays our current LinkedIn job
postings.</li>
<li><b>YouTube</b> &mdash; product videos are embedded using YouTube&rsquo;s privacy-enhanced mode
(<code>youtube-nocookie.com</code>), which does not set tracking cookies unless you play the video.</li>
</ul>
<p>Each of these companies has its own privacy policies and practices. Although we choose our
business partners carefully, we can make no representations concerning privacy and security on sites
we do not operate. The same applies to any other site you reach through a link from ours.</p>

<h2>Your Choices and Rights</h2>
<p>Depending on where you live, you may have the right to request access to the personal information
we hold about you, to have it corrected or deleted, to object to or restrict its processing, and to
receive a copy in a portable format. Residents of California may also request disclosure of the
categories of personal information collected and may opt out of any &ldquo;sale&rdquo; or
&ldquo;sharing&rdquo; of personal information &mdash; we do not sell or share personal information as
those terms are defined under California law. To exercise any of these rights, contact us at the
address below. We will not discriminate against you for doing so.</p>
<p>You can also block or delete cookies through your browser settings, and most browsers offer a
&ldquo;do not track&rdquo; or global privacy control signal.</p>

<h2>Security</h2>
<p>This site is served over HTTPS. Because it is a static site with no database, no login, and no
payment processing, it stores no personal information of its own. Information you send us by email is
kept in access-controlled business systems. Please be aware that no method of transmission or storage
is completely secure, on or off the Internet.</p>

<h2>International Transfers</h2>
<p>Maverix Medical, LLC is based in the United States, and the service providers described above
process data in the United States and elsewhere. If you access this site from outside the United
States, your information will be transferred to and processed in the United States.</p>

<h2>Changes to This Policy</h2>
<p>If we change this policy, the revised version will be posted here with an updated date. Please
check this page periodically.</p>

<h2>Contact</h2>
<p>Questions or requests regarding this policy can be sent to
<a href="mailto:{MVX_EMAIL}">{MVX_EMAIL}</a>.</p>
</div></section>"""
    page("privacy-policy.html", "Privacy Policy – Maverix Medical", "Maverix Medical privacy policy.",
         privacy, group="Legal", subtitle="Privacy policy")

    reg = f"""
<section class="band light"><div class="container legal" style="max-width:860px;">
<h1>Regulatory Information</h1>
<p>Maverix Medical devices are prescription-only and intended for use by trained physicians. Complete
indications, contraindications, warnings, precautions, and directions for use are provided in each
product&rsquo;s Instructions for Use (IFU).</p>
<h2>Electronic Instructions for Use (eIFU)</h2>
<p>Instructions for Use are available electronically. Printed copies are available at no additional cost
on request &mdash; contact Customer Care and we will send one within seven calendar days.</p>
<p><a class="reglink" href="{EIFU_URL}" target="_blank" rel="noopener">Access the eIFU library <span class="ext-icon">&#8599;</span></a></p>
<h2>Requesting a Printed Copy</h2>
<p>Email <a href="mailto:customercare@thoracent.com">customercare@thoracent.com</a> or call
(888) 978-0232, Monday&ndash;Friday, 8:30&ndash;5:00 ET. Please include the product name, catalog number,
and lot number shown on the device label.</p>
<h2>Reporting an Adverse Event</h2>
<p>To report a suspected adverse event or product complaint, contact
<a href="mailto:customercare@thoracent.com">customercare@thoracent.com</a>. In the United States, adverse
events may also be reported to the FDA through
<a href="https://www.fda.gov/safety/medwatch-fda-safety-information-and-adverse-event-reporting-program" target="_blank" rel="noopener">MedWatch</a>.</p>
</div></section>"""
    page("regulatory-information.html", "Regulatory Information – Maverix Medical",
         "Electronic Instructions for Use (eIFU), printed IFU requests, and adverse event reporting for Maverix Medical devices.",
         reg, group="Legal", subtitle="eIFU and regulatory information")

# ------------------------------------------------------------------ 404 / SEO
BASE_PATH = "/" + BASE_URL.split("://", 1)[1].split("/", 1)[1].strip("/") + "/" \
            if "/" in BASE_URL.split("://", 1)[1] else "/"

def build_404():
    body = f"""
<section class="band light not-found"><div class="container">
 <div class="not-found-code">404</div>
 <h1 class="section-title">This page could not be found</h1>
 <p class="lede">The page you're looking for may have moved, or the address may be mistyped.
 Here are some good places to pick things back up:</p>
 <div class="famrow" style="margin-top:2.4rem;">
  <div class="family-cell cat-risk"><h4>Products</h4>
   <p>Risk assessment, diagnosis, and intervention &mdash; the full Maverix portfolio.</p>
   {btn("products.html","Browse our products")}</div>
  <div class="family-cell cat-diagnosis"><h4>Team</h4>
   <p>Our leadership and medical advisory board.</p>
   {btn("team.html","Meet the team")}</div>
  <div class="family-cell cat-intervention"><h4>Contact</h4>
   <p>Investment, partnerships, sales inquiries, or careers.</p>
   {btn("contact-us.html","Get in touch")}</div>
 </div>
 <p class="bodytext" style="margin-top:2.6rem;">Or return to the <a href="index.html">home page</a>.</p>
</div></section>"""
    page("404.html", "Page not found – Maverix Medical",
         "The page you are looking for could not be found.",
         body, group="Utility", subtitle="404 error page")

def build_stylesheet():
    """One shared stylesheet. url()s resolve against this file at the site root,
    so assets/ and images/ paths are correct for root and nested pages alike."""
    path = os.path.join(OUT, "theme.css")
    with open(path, "w") as f:
        f.write(CSS_TPL)
    print("wrote theme.css", len(CSS_TPL))

def build_seo():
    prio = {"index.html": "1.0", "products.html": "0.9", "thoracent.html": "0.9",
            "diagnostics.html": "0.9", "serpex.html": "0.9", "team.html": "0.8",
            "news.html": "0.8", "careers.html": "0.8", "contact-us.html": "0.8"}
    urls = []
    for f in PAGES:
        loc = f"{BASE_URL}/" if f == "index.html" else f"{BASE_URL}/{f}"
        p = prio.get(f, "0.6" if f.startswith("products/") else "0.3")
        urls.append(f"  <url><loc>{loc}</loc><priority>{p}</priority></url>")
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
               + "\n".join(urls) + "\n</urlset>\n")
    with open(os.path.join(OUT, "sitemap.xml"), "w") as fh:
        fh.write(sitemap)
    print("wrote sitemap.xml", len(urls), "urls")

    robots = f"User-agent: *\nAllow: /\n\nSitemap: {BASE_URL}/sitemap.xml\n"
    with open(os.path.join(OUT, "robots.txt"), "w") as fh:
        fh.write(robots)
    print("wrote robots.txt")

    manifest = ('{\n'
                '  "name": "Maverix Medical",\n'
                '  "short_name": "Maverix",\n'
                f'  "start_url": "{BASE_URL}/",\n'
                '  "display": "standalone",\n'
                '  "theme_color": "#0D1418",\n'
                '  "background_color": "#F2F2F6",\n'
                '  "icons": [\n'
                '    {"src": "favicon-192.png", "sizes": "192x192", "type": "image/png"},\n'
                '    {"src": "favicon-512.png", "sizes": "512x512", "type": "image/png"}\n'
                '  ]\n'
                '}\n')
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    with open(os.path.join(OUT, "assets", "site.webmanifest"), "w") as fh:
        fh.write(manifest)
    print("wrote assets/site.webmanifest")

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    build_home()
    build_products()
    build_product_pages()
    build_team()
    build_news()
    build_careers()
    build_contact()
    build_legal()
    build_404()
    build_stylesheet()
    build_seo()
    print("done")
