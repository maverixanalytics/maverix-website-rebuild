
/* Futura — licensed TTFs bundled in the design system; Jost (Google) is the
   documented fallback when the project-relative files are unavailable. */
@font-face{font-family:"Clashdisplay";font-style:normal;font-weight:600;font-display:swap;src:url("assets/fonts/clashdisplay-semibold.otf") format("opentype");}
@font-face{font-family:"Clashdisplay";font-style:normal;font-weight:300;font-display:swap;src:url("assets/fonts/clashdisplay-light.otf") format("opentype");}
@font-face{font-family:"Clashdisplay";font-style:normal;font-weight:200;font-display:swap;src:url("assets/fonts/clashdisplay-extralight.otf") format("opentype");}
:root{
/* ---- Maverix design-system tokens (source: colors_and_type.css) ---- */
--mvx-deep:#1A4A5D;--mvx-teal:#276F8B;--mvx-blue:#3494BA;--mvx-sky:#79D5E2;--mvx-cloud:#8BBAE4;
--mvx-ink:#231F20;--mvx-graphite:#3A3A3B;--mvx-slate:#595959;--mvx-stone:#A4A6A8;--mvx-mist:#F2F2F2;--mvx-white:#FFFFFF;
--thoracent-orange:#FF4D00;
--border:#E3E6E8;--border-strong:#C8CDD0;--accent-soft:#E8F2F7;
--success:#2E8F6B;--warning:#C68A1B;--danger:#C0352B;
--font-sans:"Poppins",ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
--font-display:"Poppins",ui-sans-serif,system-ui,sans-serif;
--font-tagline:"Clashdisplay","Clash Display","Futura","Futura PT","Jost","Poppins",sans-serif;
/* ---- site-layout tokens (matched to live maverixmedical.com) ---- */
--header-dark:#0D1418;--page-bg:#F2F2F6;--frame-line:#DADDE2;--heading:#213340;
/* ---- legacy names retained as aliases so no layout rule changes ---- */
--midnight:var(--mvx-deep);--darkblue:var(--mvx-teal);--teal:var(--mvx-teal);--blue:var(--mvx-blue);--cyan:var(--mvx-sky);
--lightblue:var(--mvx-cloud);--offwhite:var(--mvx-mist);--dark-offwhite:var(--border);--ink:var(--mvx-ink);--muted:var(--mvx-slate);--white:var(--mvx-white);}
*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{font-family:var(--font-sans);color:#333;background:var(--page-bg);font-size:14px;font-weight:300;line-height:1.55;-webkit-font-smoothing:antialiased;}
img{max-width:100%;display:block;}
a{color:var(--teal);text-decoration:none;}
.container{max-width:1000px;margin:0 auto;padding:0 24px;}
.allcaps{font-family:var(--font-tagline);text-transform:uppercase;letter-spacing:.35em;font-size:.78rem;font-weight:600;}
.btn{display:inline-flex;align-items:center;gap:.6rem;font-weight:600;font-size:.95rem;color:var(--ink);}
.btn .circ{width:30px;height:30px;border-radius:50%;background:var(--cyan);display:inline-flex;align-items:center;justify-content:center;flex:0 0 30px;transition:transform .2s;}
.btn .circ svg{width:14px;height:14px;}
.btn:hover .circ{transform:translateX(4px);}
.btn.on-dark{color:#fff;}
.readmore{display:inline-block;border:1px solid var(--mvx-graphite);padding:.55rem 1.5rem;font-style:italic;font-size:.95rem;color:var(--ink);transition:.15s;}
.readmore:hover{background:var(--mvx-ink);color:#fff;}
/* header — near-black bar, celled logo + careers, centered lowercase nav */
header.site{position:sticky;top:0;z-index:60;background:var(--header-dark);}
.nav{display:flex;align-items:stretch;height:62px;max-width:none;padding:0;}
.nav .logo{display:flex;align-items:center;padding:0 28px;border-right:1px solid rgba(255,255,255,.14);}
.nav-links{display:flex;align-items:center;justify-content:center;gap:3.2rem;flex:1;}
.nav-links>div{position:relative;display:flex;align-items:stretch;}
.nav-links a.nav-top-link{color:#fff;font-weight:400;font-size:.98rem;display:inline-flex;align-items:center;gap:.35rem;padding:0 .2rem;height:62px;letter-spacing:.02em;}
.nav-links a.nav-top-link:hover{color:var(--mvx-sky);}
.nav-right{display:flex;align-items:stretch;}
.nav-right a.contact{display:flex;align-items:center;color:#fff;font-family:var(--font-tagline);font-weight:700;text-transform:uppercase;letter-spacing:.12em;font-size:.95rem;padding:0 34px;}
.nav-right a.contact:hover{color:var(--mvx-sky);}
.nav-right a.careers-cell{display:flex;align-items:center;color:#fff;font-family:var(--font-tagline);font-weight:700;text-transform:uppercase;letter-spacing:.12em;font-size:.95rem;padding:0 38px;border-left:1px solid rgba(255,255,255,.14);}
.nav-right a.careers-cell:hover{color:var(--mvx-sky);}
.dropdown{position:absolute;top:100%;left:50%;transform:translate(-50%,8px);background:#fff;min-width:300px;border-top:3px solid var(--mvx-sky);box-shadow:0 14px 34px rgba(13,20,24,.25);opacity:0;visibility:hidden;transition:.18s;padding:1.2rem 0;}
.dropdown.mega{min-width:760px;display:grid;grid-template-columns:repeat(3,1fr);gap:0;padding:0;}
.nav-links>div:hover .dropdown,.nav-links>div:focus-within .dropdown{opacity:1;visibility:visible;transform:translate(-50%,0);}
.dropdown a{display:block;padding:.55rem 1.4rem;color:var(--ink);font-size:.92rem;font-weight:500;}
.dropdown a:hover{background:var(--mvx-mist);color:var(--teal);}
.dropdown .mcol{padding:1.6rem 1.5rem;border-right:1px solid var(--border);}
.dropdown .mcol:last-child{border-right:none;}
.dropdown .mcol h4{color:var(--teal);font-size:1.02rem;margin-bottom:.6rem;}
.dropdown .mcol p{color:var(--muted);font-size:.84rem;margin-bottom:1rem;line-height:1.5;}
.dropdown .mcol .btn{font-size:.84rem;}
.dropdown .mcol .btn .circ{width:26px;height:26px;flex:0 0 26px;}
.hamburger{display:none;background:none;border:none;cursor:pointer;padding:8px;margin:auto 16px auto auto;}
.hamburger span{display:block;width:24px;height:2px;background:#fff;margin:5px 0;transition:.2s;}
/* heroes */
.hero{position:relative;background:var(--header-dark);color:#fff;overflow:hidden;}
.hero video,.hero .hero-img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.55;}
.hero .shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(10,16,20,.72),rgba(10,16,20,.25));}
.hero .inner{position:relative;padding:8.5rem 0 7.5rem;}
.hero .kicker{color:var(--mvx-sky);font-size:1.35rem;font-weight:600;letter-spacing:.28em;margin-bottom:1.2rem;}
.hero h1{font-family:var(--font-tagline);font-size:clamp(3rem,7.2vw,6.125rem);font-weight:600;line-height:1;max-width:900px;text-transform:uppercase;letter-spacing:0;}
.hero .hero-tagline{margin-top:1.8rem;font-size:clamp(1.15rem,2.2vw,1.5rem);font-style:italic;color:#E8ECEF;line-height:1.9;}
.hero-thin{position:relative;background:linear-gradient(105deg,rgba(21,28,34,.96) 0%,rgba(59,69,77,.82) 34%,rgba(140,150,158,.55) 68%,rgba(233,235,239,.4) 100%),url("images/hero-bg.jpg") center/cover no-repeat,#3B454D;color:#fff;overflow:hidden;}
.hero-thin .inner{position:relative;padding:11rem 0 2.6rem;}
.hero-thin h1{font-family:var(--font-tagline);font-weight:200;font-size:clamp(4rem,10vw,8.2rem);line-height:.95;letter-spacing:.01em;}
/* framed sections — center column with vertical rules, like the live site */
section.band{padding:0;}
section.band>.container{border-left:1px solid var(--frame-line);border-right:1px solid var(--frame-line);padding:6rem 72px;}
.band.light>.container{background:var(--page-bg);}
.band.white>.container{background:#fff;}
.band.row-line>.container{border-top:1px solid var(--frame-line);}
.band.dark{position:relative;background:var(--header-dark);color:#fff;overflow:hidden;padding:5.5rem 0;}
.band.dark .bgimg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.32;}
.band.dark>.container{position:relative;border:none;background:transparent;padding:0 24px;}
.band.dark .kicker{color:#fff;font-size:1.5rem;font-weight:600;letter-spacing:.2em;margin-bottom:1.6rem;}
.band h2{font-family:var(--font-tagline);font-size:clamp(2rem,4vw,3.125rem);font-weight:600;line-height:1.12;color:var(--heading);}
.band.dark h2{color:#fff;}
h2.section-title{color:var(--heading);margin-bottom:1rem;}
.lede{font-size:1.05rem;color:var(--muted);max-width:760px;}
.band.dark .lede{color:#D6DDE1;}
.split{display:grid;grid-template-columns:1fr 1fr;gap:3.5rem;align-items:center;}
.card{background:#fff;border:1px solid var(--border);border-radius:8px;padding:2rem 1.7rem;display:flex;flex-direction:column;gap:1rem;}
.card h3{font-size:1.25rem;color:var(--ink);}
.card p{color:var(--muted);font-size:.97rem;flex:1;}
/* stats — cloud-blue numbers, hairline grid on white */
.challenge{display:grid;grid-template-columns:1.05fr 2fr;gap:3.6rem;margin-top:3.2rem;}
.challenge .headline p{font-size:1.15rem;font-weight:600;line-height:1.5;color:var(--mvx-graphite);}
.bigstat{margin-top:1.8rem;}
.bigstat .stat-number{font-family:var(--font-tagline);font-size:2.7rem;font-weight:700;color:var(--mvx-cloud);line-height:1.1;}
.bigstat .stat-label{color:var(--muted);font-size:.95rem;max-width:260px;}
.statgrid{display:grid;grid-template-columns:repeat(3,1fr);background:#fff;border:1px solid var(--frame-line);}
.statgrid .cell{padding:1.9rem 1.5rem 2.6rem;border-right:1px solid var(--frame-line);border-bottom:1px solid var(--frame-line);}
.statgrid .stat-number{font-family:var(--font-tagline);font-size:2rem;font-weight:700;color:var(--mvx-cloud);}
.statgrid .stat-label{font-size:.88rem;color:var(--muted);margin-top:.3rem;}
sup{font-size:.6em;color:var(--mvx-blue);}
/* patient journey — matched to live diagram */
.journey{margin:3.8rem 0 0;}
.journey .jtitle{font-family:var(--font-tagline);text-align:center;text-transform:uppercase;letter-spacing:.3em;font-size:1rem;color:var(--mvx-graphite);font-weight:500;}
.journey .jnote{display:flex;align-items:center;gap:.8rem;justify-content:center;color:var(--mvx-graphite);font-style:italic;font-size:.95rem;margin:.7rem 0 1.1rem;}
.journey .jnote::before,.journey .jnote::after{content:"";flex:1;max-width:150px;height:7px;background:linear-gradient(var(--mvx-graphite),var(--mvx-graphite)) left 50%/100% 1px no-repeat;}
.journey .jnote::before{background:radial-gradient(circle 3.2px at 3.2px 50%,var(--mvx-graphite) 3px,transparent 3.4px),linear-gradient(var(--mvx-graphite),var(--mvx-graphite)) left 50%/100% 1px no-repeat;}
.journey .jnote::after{background:radial-gradient(circle 3.2px at calc(100% - 3.2px) 50%,var(--mvx-graphite) 3px,transparent 3.4px),linear-gradient(var(--mvx-graphite),var(--mvx-graphite)) left 50%/100% 1px no-repeat;}
.jbar{display:flex;gap:8px;justify-content:center;}
.jseg{padding:.9rem .9rem;border-radius:4px;font-size:.9rem;font-style:italic;white-space:nowrap;text-align:center;}
.jseg.dark{background:#1B242B;color:#fff;}
.jseg.steel{background:#2E6E8E;color:#fff;}
.jseg.light{background:#7BC4D8;color:#12333D;}
.jseg.fade{background:linear-gradient(90deg,#C9E8F2,rgba(233,247,251,0));color:#2A3A42;}
.jseg.end-marker{background:var(--danger);padding:.9rem .25rem;border-radius:2px;}
.jarrow{display:flex;align-items:center;gap:.8rem;justify-content:center;color:var(--mvx-graphite);font-style:italic;font-size:.95rem;margin:1.1rem 0 .5rem;}
.jarrow::before{content:"";flex:1;max-width:170px;height:7px;background:radial-gradient(circle 3.2px at 3.2px 50%,var(--mvx-graphite) 3px,transparent 3.4px),linear-gradient(var(--mvx-graphite),var(--mvx-graphite)) left 50%/100% 1px no-repeat;}
.jarrow::after{content:"\2192";font-style:normal;font-size:1.3rem;}
/* journey cards — rounded, photo, centered bottom label, hover reveal */
.pathways{display:grid;grid-template-columns:repeat(3,1fr);gap:2.2rem;margin-top:3.4rem;}
.pathcard{position:relative;border-radius:22px;overflow:hidden;min-height:410px;display:flex;align-items:flex-end;justify-content:center;background:#8E979E;}
.pathcard img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:grayscale(35%);}
.pathcard::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,28,34,0) 40%,rgba(20,28,34,.72));}
.pathcard .pathcard-caption{position:relative;z-index:2;padding:1.6rem;color:#fff;text-align:center;}
.pathcard .pathcard-caption .card-kicker{font-size:.95rem;opacity:.9;}
.pathcard .pathcard-caption .card-title{font-family:var(--font-tagline);font-size:1.5rem;font-weight:700;}
.pathcard .reveal{position:absolute;inset:0;z-index:3;background:rgba(17,29,36,.9);color:#fff;padding:1.6rem;display:flex;flex-direction:column;justify-content:center;gap:1rem;opacity:0;transition:.25s;}
.pathcard .reveal h3{color:var(--mvx-sky);font-size:1.1rem;}
.pathcard .reveal p{font-size:.83rem;line-height:1.55;color:#D6DDE1;}
.pathcard:hover .reveal,.pathcard:focus-within .reveal{opacity:1;}
/* news — featured + grid, matched to live */
.featured{padding-bottom:2.6rem;border-bottom:1px solid var(--frame-line);}
.featured .date{font-family:var(--font-tagline);text-transform:uppercase;letter-spacing:.25em;font-size:.85rem;color:var(--mvx-slate);margin-bottom:1rem;}
.featured .srclogo{max-height:48px;width:auto;object-fit:contain;margin-bottom:1.4rem;}
.featured h2{color:var(--mvx-blue);max-width:640px;margin-bottom:1.1rem;}
.featured h2 a{color:var(--mvx-blue);}
.featured p{color:var(--mvx-graphite);max-width:640px;margin-bottom:1.8rem;}
.newsgrid{display:grid;grid-template-columns:repeat(3,1fr);}
.newsgrid .ncell{padding:2.2rem 1.8rem 2.6rem;border-right:1px solid var(--frame-line);border-bottom:1px solid var(--frame-line);display:flex;flex-direction:column;gap:.9rem;}
.newsgrid .ncell:nth-child(3n){border-right:none;}
.newsgrid .srclogo{max-height:44px;max-width:160px;width:auto;object-fit:contain;}
.newsgrid .date{font-family:var(--font-tagline);text-transform:uppercase;letter-spacing:.22em;font-size:.8rem;color:var(--mvx-slate);}
.newsgrid h3{font-family:var(--font-tagline);font-size:1.25rem;line-height:1.3;color:var(--mvx-blue);}
.newsgrid h3 a{color:var(--mvx-blue);}
.newsgrid p{color:var(--mvx-graphite);font-size:.9rem;flex:1;}
/* team — 3-up grid, teal names, hairline rule */
.teamgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:2.6rem 3rem;margin-top:2.6rem;}
.member{cursor:pointer;background:transparent;border:none;overflow:hidden;text-align:left;padding:0;font:inherit;}
.member img{aspect-ratio:1/1.08;object-fit:cover;width:100%;background:var(--border);}
.member .member-info{padding:1.1rem 0 1.2rem;border-bottom:1px solid var(--border-strong);}
.member .member-name{font-family:var(--font-tagline);font-weight:700;font-size:1.25rem;color:var(--mvx-blue);}
.member .member-role{color:var(--mvx-slate);font-size:.92rem;margin-top:.2rem;}
.member:hover .member-name{color:var(--mvx-teal);}
.advgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.8rem 3rem;margin-top:2.4rem;}
.advcard{border-bottom:1px solid var(--border-strong);padding-bottom:1rem;}
.advcard .member-name{font-family:var(--font-tagline);font-weight:700;font-size:1.15rem;color:var(--mvx-blue);}
/* modal */
.modal{position:fixed;inset:0;z-index:100;display:none;align-items:center;justify-content:center;padding:24px;}
.modal.open{display:flex;}
.modal .overlay{position:absolute;inset:0;background:rgba(13,20,24,.8);}
.modal .modal-box{position:relative;background:#fff;border-radius:10px;max-width:860px;width:100%;max-height:86vh;overflow:auto;padding:2.6rem;}
.modal .close{position:absolute;top:14px;right:16px;background:none;border:none;font-size:1.6rem;cursor:pointer;color:var(--muted);line-height:1;}
.modal .bio-text p{margin-bottom:1rem;color:var(--mvx-graphite);font-size:.97rem;}
.modal .profile-link{display:inline-flex;align-items:center;gap:.5rem;margin-top:.4rem;font-weight:600;}
/* products */
.prod-section{scroll-margin-top:80px;}
.pcard{scroll-snap-align:start;background:#fff;border:1px solid var(--border);overflow:hidden;display:flex;flex-direction:column;}
.pcard .card-photo{aspect-ratio:4/3;background:linear-gradient(135deg,#25313A,#0D1418);display:flex;align-items:center;justify-content:center;overflow:hidden;}
.pcard .card-photo img{width:100%;height:100%;object-fit:cover;}
.pcard .card-info{padding:1.2rem;display:flex;flex-direction:column;gap:.7rem;flex:1;}
.pcard h3{font-size:1.05rem;line-height:1.3;flex:1;}
/* spec tables */
.spec{width:100%;border-collapse:collapse;margin-top:1.2rem;background:#fff;overflow:hidden;font-size:.92rem;}
.spec th{background:var(--header-dark);color:#fff;text-align:left;padding:.7rem 1rem;font-weight:600;}
.spec td{padding:.65rem 1rem;border-bottom:1px solid var(--border);color:var(--mvx-graphite);}
.spec tr td:first-child{font-weight:600;color:var(--ink);width:24%;}
.benefits{list-style:none;margin-top:1.2rem;display:grid;gap:.7rem;}
.benefits li{position:relative;padding-left:1.7rem;color:var(--mvx-graphite);font-size:.96rem;}
.benefits li::before{content:"";position:absolute;left:0;top:.42em;width:10px;height:10px;border-radius:50%;background:var(--cyan);}
/* product detail */
.pd-hero{background:var(--header-dark);color:#fff;padding:4rem 0 3.4rem;}
.pd-hero .crumb{color:var(--mvx-sky);font-size:.9rem;margin-bottom:1.2rem;display:inline-block;}
.pd-hero h1{font-family:var(--font-tagline);font-size:clamp(2rem,4.4vw,3.2rem);font-weight:700;max-width:800px;line-height:1.12;}
.pd-hero .container{border:none;background:transparent;padding:0 24px;}
.pd-img{overflow:hidden;border:1px solid var(--border);background:#fff;}
.pd-img img{width:100%;}
/* forms */
.form{display:grid;gap:1.1rem;max-width:560px;}
.form label{font-weight:600;font-size:.9rem;}
.form input,.form textarea{width:100%;padding:.75rem .9rem;border:1px solid var(--border-strong);font:inherit;font-size:.95rem;background:#fff;}
.form input:focus,.form textarea:focus{outline:2px solid var(--cyan);border-color:var(--cyan);}
.form button{background:var(--header-dark);color:#fff;border:none;padding:.85rem 1.6rem;font-weight:700;font-size:.95rem;cursor:pointer;justify-self:start;}
.form button:hover{background:var(--teal);}
.form-msg{display:none;padding:1rem 1.2rem;font-weight:600;}
.form-msg.form-success{background:#E6F4EE;color:var(--success);}
.form-msg.form-error{background:#F7E7E6;color:var(--danger);}
.band.dark .form label{color:#fff;}
.jobs-empty{color:var(--muted);font-style:italic;}
/* legal */
.legal h1{font-family:var(--font-tagline);font-size:2.4rem;margin-bottom:.4rem;color:var(--heading);}
.legal .effective-date{color:var(--muted);margin-bottom:2.2rem;}
.legal h2{color:var(--mvx-blue);font-size:1.35rem;margin:2rem 0 .7rem;}
.legal p,.legal li{color:var(--mvx-graphite);margin-bottom:.9rem;font-size:.98rem;}
.legal ol{padding-left:1.4rem;}
/* footer — framed light column like the live site */
footer.site{background:var(--page-bg);}
footer.site .container{border-left:1px solid var(--frame-line);border-right:1px solid var(--frame-line);border-top:1px solid var(--frame-line);padding:4.4rem 72px 2.2rem;}
.fgrid{display:grid;grid-template-columns:repeat(3,1fr) auto;gap:2.4rem;}
.fcol .footer-heading,.fcontact .footer-heading{font-family:var(--font-tagline);text-transform:uppercase;letter-spacing:.26em;font-size:.75rem;color:var(--mvx-slate);margin-bottom:.9rem;font-weight:500;}
.fcol a{display:block;color:var(--teal);font-size:.93rem;padding:.22rem 0;}
.fcol a:hover{color:var(--heading);}
.fbrand{text-align:right;}
.fbrand .li{display:inline-flex;margin-top:1rem;width:34px;height:34px;border-radius:50%;background:var(--header-dark);align-items:center;justify-content:center;}
.fbrand .li img{height:15px;filter:invert(1);}
.fcontact{margin-top:2.6rem;}
.fcontact .footer-heading{margin-bottom:.4rem;}
.fbottom{display:flex;justify-content:space-between;align-items:center;margin-top:3rem;padding-top:1.4rem;border-top:1px solid var(--frame-line);font-size:.85rem;color:var(--muted);flex-wrap:wrap;gap:1rem;}
.fbottom a{color:var(--muted);margin-right:1.4rem;}
.fbottom a:hover{color:var(--teal);}
/* cookie banner */
@media(max-width:920px){
 .nav-links{display:none;position:absolute;top:62px;left:0;right:0;background:var(--header-dark);flex-direction:column;align-items:flex-start;padding:1rem 24px 1.6rem;gap:.2rem;box-shadow:0 18px 30px rgba(13,20,24,.3);}
 .nav-links.open{display:flex;}
 .nav-links a.nav-top-link{padding:.6rem 0;height:auto;}
 .nav-links>div{display:block;}
 .dropdown,.dropdown.mega{position:static;opacity:1;visibility:visible;transform:none;border:none;box-shadow:none;padding:0 0 .4rem .8rem;min-width:0;display:block;background:transparent;}
 .dropdown a{color:#C9D2D8;padding:.35rem 0;}
 .dropdown .mcol{border:none;padding:.4rem 0;}
 .dropdown .mcol p{display:none;}
 .hamburger{display:block;}
 .nav-right a.contact,.nav-right a.careers-cell{padding:0 16px;}
 .split,.challenge,.pd-grid{grid-template-columns:1fr;}
 .cards3,.pathways,.statgrid,.newsgrid{grid-template-columns:1fr 1fr;}
 .teamgrid,.advgrid{grid-template-columns:repeat(2,1fr);}
 .benefit-grid.g4,.benefit-grid.g5{grid-template-columns:repeat(2,1fr);}
 .altrow{grid-template-columns:1fr;}
 .newsitem{grid-template-columns:1fr;gap:.7rem;}
 .fgrid{grid-template-columns:1fr 1fr;}
 .fbrand{text-align:left;}
}
@media(max-width:560px){
 .cards3,.pathways,.statgrid,.newsgrid,.teamgrid,.advgrid,.benefit-grid.g4,.benefit-grid.g5{grid-template-columns:1fr;}
 .jbar{flex-wrap:wrap;}
}

/* v3 closer-copy additions */
.sechead{display:flex;justify-content:space-between;align-items:flex-start;gap:2rem;flex-wrap:wrap;margin-bottom:2.6rem;}
.sechead img{height:64px;width:auto;object-fit:contain;background:#fff;padding:6px 10px;}
.contact-block{text-align:left;min-width:230px;}
.contact-block .cb-label{font-family:var(--font-tagline);text-transform:uppercase;letter-spacing:.28em;font-size:.78rem;color:var(--mvx-slate);}
.contact-block .cb-title{font-family:var(--font-tagline);font-weight:700;font-size:1.5rem;color:var(--heading);line-height:1.2;border-bottom:1px solid var(--border-strong);padding-bottom:.5rem;margin-bottom:.5rem;}
.contact-block a{font-style:italic;color:var(--mvx-blue);text-decoration:underline;font-size:.95rem;display:block;}
.contact-block .cb-phone{font-size:.95rem;color:var(--mvx-graphite);margin-top:.2rem;}
.seclabel{display:flex;align-items:center;gap:1.4rem;font-family:var(--font-tagline);text-transform:uppercase;letter-spacing:.28em;font-size:1.05rem;font-weight:600;color:var(--heading);margin:3.4rem 0 1.6rem;}
.seclabel::after{content:"";flex:1;max-width:560px;height:1px;background:var(--mvx-graphite);}
.biglead{font-family:var(--font-tagline);color:var(--mvx-blue);font-weight:700;font-size:clamp(1.4rem,2.5vw,1.9rem);line-height:1.3;max-width:680px;margin-bottom:1.4rem;}
.bodytext{color:var(--mvx-graphite);font-size:1rem;max-width:680px;margin-bottom:.9rem;}
.photo-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:2.2rem;margin-top:2.8rem;}
.photo-card{position:relative;border-radius:18px;overflow:hidden;min-height:340px;display:flex;align-items:flex-end;background:linear-gradient(160deg,#7F8A92,#3A444C);}
.photo-card img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;}
.photo-card::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(18,26,32,0) 35%,rgba(18,26,32,.68));}
.photo-card .photo-title{position:relative;z-index:2;color:#fff;font-family:var(--font-tagline);font-weight:700;font-size:1.35rem;line-height:1.25;padding:1.4rem;}
/* careers why-row */
.why-row{display:grid;grid-template-columns:repeat(5,1fr);border:1px solid var(--frame-line);background:#fff;margin-top:2.4rem;}
.why-cell{padding:1.8rem 1.4rem 2.2rem;border-right:1px solid var(--frame-line);}
.why-cell:last-child{border-right:none;}
.why-cell h3{font-family:var(--font-tagline);color:var(--mvx-blue);font-size:1.35rem;line-height:1.2;margin:.8rem 0 .9rem;}
.why-cell p{color:var(--mvx-slate);font-size:.86rem;}
.why-cell svg{width:44px;height:44px;stroke:var(--mvx-graphite);fill:none;stroke-width:1.4;stroke-linecap:round;stroke-linejoin:round;}
@media(max-width:920px){.photo-cards,.photo-cards.g4,.photo-cards.g5{grid-template-columns:1fr 1fr;}.serpex-two{grid-template-columns:1fr;}.why-row{grid-template-columns:1fr 1fr;}.why-cell{border-bottom:1px solid var(--frame-line);}}
@media(max-width:560px){.photo-cards,.photo-cards.g4,.photo-cards.g5,.why-row{grid-template-columns:1fr;}}

/* v4: contact gradient form, product tab pages, team hero image */
.contact-dark{position:relative;background:linear-gradient(115deg,#9AA4AB 0%,#2A353D 28%,#13202A 52%,#3E7FA6 100%);color:#fff;padding:5rem 0 6rem;}
.contact-dark h2{color:#fff;font-family:var(--font-tagline);font-size:clamp(1.8rem,3.4vw,2.6rem);line-height:1.2;}
.cform{display:grid;grid-template-columns:1fr 1.15fr;gap:1.2rem;margin-top:2.6rem;max-width:860px;}
.cform .colL{display:grid;gap:1.2rem;align-content:start;}
.cform .colR{display:grid;gap:1.2rem;grid-template-rows:auto 1fr;}
.cform input,.cform textarea{background:rgba(255,255,255,.1);border:1px solid rgba(160,215,232,.55);color:#fff;padding:.95rem 1rem;font:inherit;font-style:italic;font-size:.95rem;}
.cform input::placeholder,.cform textarea::placeholder{color:#CBD6DC;font-style:italic;}
.cform input:focus,.cform textarea:focus{outline:2px solid var(--mvx-sky);}
.cform textarea{min-height:240px;resize:vertical;}
.cform .send{grid-column:1/-1;background:#fff;color:var(--mvx-ink);font-family:var(--font-tagline);font-weight:700;letter-spacing:.28em;text-transform:uppercase;font-size:.95rem;padding:1.05rem;border:none;cursor:pointer;}
.cform .send:hover{background:var(--mvx-sky);}
.tabbar{background:#E8EAEE;border-bottom:1px solid var(--frame-line);}
.tabbar-in{display:flex;align-items:stretch;padding:0;border-left:1px solid var(--frame-line);border-right:1px solid var(--frame-line);}
.tabbar button,.tabbar a{font-family:var(--font-sans);font-style:italic;font-size:1.02rem;color:var(--mvx-graphite);padding:1rem 2.4rem;border:none;background:transparent;cursor:pointer;}
.tabbar button.is-active{background:#fff;}
.tabbar button:hover,.tabbar a:hover{color:var(--mvx-teal);}
.tabbar .ext-icon{font-size:.75em;vertical-align:super;}
.tabpane{display:none;}
.tabpane.is-active{display:block;}
.pd-wrap{display:grid;grid-template-columns:1fr 300px;background:var(--page-bg);}
.pd-panel{background:#fff;border-right:1px solid var(--frame-line);padding:3rem;min-height:480px;}
.pd-side{padding:3rem 0 3rem 2.4rem;}
.pd-side img{height:56px;width:auto;object-fit:contain;background:#fff;padding:6px 10px;margin-bottom:1.8rem;}
.pd-title{font-family:var(--font-tagline);color:var(--mvx-blue);font-size:2.2rem;border-bottom:1px solid var(--border);padding-bottom:.8rem;margin-bottom:1.6rem;}
.video-embed{aspect-ratio:16/9;width:100%;border:none;margin:.6rem 0 1.4rem;}
.hero-thin .hero-img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;}
.hero-thin .overlay{position:absolute;inset:0;background:linear-gradient(90deg,rgba(16,24,30,.74),rgba(233,235,239,.18));}
@media(max-width:920px){.cform{grid-template-columns:1fr;}.pd-wrap{grid-template-columns:1fr;}.pd-panel{border-right:none;}.pd-side{padding:2rem 24px;}.tabbar-in{flex-wrap:wrap;}}

/* v5: hover animations & motion */
.nav-links a.nav-top-link .plus,.nav-links a.nav-top-link .arrow{display:inline-block;margin-left:.35rem;transition:transform .18s ease,opacity .18s ease;}
.nav-links a.nav-top-link .arrow{display:none;}
.nav-links a.nav-top-link:hover .plus{display:none;}
.nav-links a.nav-top-link:hover .arrow{display:inline-block;transform:translateX(2px);}
.btn{transition:color .2s ease;}
.btn:hover{color:var(--mvx-teal);}
.btn.on-dark:hover{color:var(--mvx-sky);}
.btn .circ{transition:transform .25s ease,background .25s ease;}
.btn:hover .circ{transform:translateX(5px);background:var(--mvx-blue);}
.btn:hover .circ svg{stroke:#fff;}
.btn .circ svg{transition:stroke .25s ease;}
.readmore{transition:background .2s ease,color .2s ease,letter-spacing .2s ease;}
.pathcard img,.photo-card img,.pcard .card-photo img,.member img,.altrow .img img{transition:transform .6s cubic-bezier(.22,.61,.36,1);}
.pathcard:hover img,.photo-card:hover img,.pcard:hover .card-photo img,.member:hover img,.altrow .img:hover img{transform:scale(1.06);}
.pathcard,.photo-card,.pcard{transition:box-shadow .3s ease,transform .3s ease;}
.pathcard:hover,.photo-card:hover{box-shadow:0 20px 44px rgba(13,20,24,.28);}
.pcard:hover{box-shadow:0 14px 32px rgba(26,74,93,.16);transform:translateY(-3px);}
.member .member-name{position:relative;display:inline-block;transition:color .2s ease;}
.member .member-name::after{content:"";position:absolute;left:0;bottom:-3px;width:0;height:2px;background:var(--mvx-sky);transition:width .3s ease;}
.member:hover .member-name::after{width:100%;}
.newsgrid .ncell{transition:background .25s ease;}
.newsgrid .ncell:hover{background:#fff;}
.newsgrid h3 a,.newsitem h3 a,.featured h2 a{transition:color .2s ease;}
.newsgrid h3 a:hover,.newsitem h3 a:hover,.featured h2 a:hover{color:var(--mvx-teal);}
.statgrid .cell,.why-cell,.benefit-cell{transition:background .25s ease;}
.statgrid .cell:hover,.why-cell:hover,.benefit-cell:hover{background:#F5FAFC;}
.statgrid .cell:hover .stat-number{color:var(--mvx-blue);}
.statgrid .stat-number{transition:color .25s ease;}
.why-cell svg{transition:transform .3s ease,stroke .3s ease;}
.why-cell:hover svg{transform:translateY(-4px);stroke:var(--mvx-blue);}
.fcol a{transition:color .18s ease,padding-left .18s ease;}
.fcol a:hover{padding-left:5px;}
.tabbar button,.tabbar a{transition:background .2s ease,color .2s ease;}
.tabbar button:not(.is-active):hover,.tabbar a:hover{background:rgba(255,255,255,.6);}
.contact-block a{transition:color .2s ease;}
.contact-block a:hover{color:var(--mvx-teal);}
.jseg{transition:filter .2s ease;}
.jbar:hover .jseg{filter:brightness(1.06);}
.modal .modal-box{animation:mdl .28s ease;}
@keyframes mdl{from{opacity:0;transform:translateY(14px) scale(.98);}to{opacity:1;transform:none;}}
.hero .inner>*,.hero-thin h1{animation:heroin .8s ease backwards;}
.hero .inner>*:nth-child(2){animation-delay:.12s;}
.hero .inner>*:nth-child(3){animation-delay:.24s;}
@keyframes heroin{from{opacity:0;transform:translateY(18px);}to{opacity:1;transform:none;}}
@media (prefers-reduced-motion: no-preference){
 .reveal-on-scroll{opacity:0;transform:translateY(24px);transition:opacity .7s ease,transform .7s ease;}
 .reveal-on-scroll.is-in-view{opacity:1;transform:none;}
}
@media (prefers-reduced-motion: reduce){
 .pathcard img,.photo-card img,.pcard .card-photo img,.member img{transition:none;}
 .hero .inner>*,.hero-thin h1,.modal .modal-box{animation:none;}
}

/* v6: live-matched dark carousel tiles */
.pcard{background:#16212A;border:none;border-radius:16px;}
.pcard h3{color:#fff;}
.pcard .card-info .btn{color:#fff;}
.pcard .card-info .btn:hover{color:var(--mvx-sky);}
.pcard .card-photo{border-radius:16px 16px 0 0;background:#fff;}

/* v7 mobile fixes */
.nav-links>div.mobile-extra{display:none;}
@media(max-width:920px){
 .nav-right a.contact,.nav-right a.careers-cell{padding:0 12px;font-size:.8rem;letter-spacing:.08em;}
}
@media(max-width:560px){
 .nav-right{display:none;}
 .nav-links>div.mobile-extra{display:block;width:100%;border-top:1px solid rgba(255,255,255,.16);margin-top:.6rem;padding-top:.6rem;}
 .mobile-extra a{display:block;color:#fff;font-family:var(--font-tagline);text-transform:uppercase;letter-spacing:.12em;font-size:.9rem;padding:.5rem 0;}
 .spec{display:block;overflow-x:auto;}
 .hero-thin h1{font-size:3.2rem;}
 section.band>.container{padding:3.4rem 22px;}
 footer.site .container{padding:3rem 22px 1.8rem;}
}

/* v8: logo images, LinkedIn glyphs, transparent brand logos, alignment */
.nav .logo-img{height:20px;width:auto;}
.fbrand .flogo{height:24px;width:auto;display:inline-block;}
.fbrand .li{display:inline-flex;margin-top:1.1rem;width:34px;height:34px;border-radius:50%;background:var(--header-dark);align-items:center;justify-content:center;color:#fff;}
.fbrand .li svg{width:16px;height:16px;}
.li-badge{display:inline-flex;width:26px;height:26px;border-radius:4px;background:#0A66C2;color:#fff;align-items:center;justify-content:center;}
.li-badge svg{width:15px;height:15px;}
/* transparent brand logos (blend white JPG boxes into light sections) */
.brandbar img,.sechead img,.pd-side img,.card .logoimg{background:transparent;padding:0;border-radius:0;mix-blend-mode:multiply;}
/* alignment: section heads and team grid */
.sechead{align-items:center;}
.teamgrid{align-items:start;}
.member img{aspect-ratio:1/1;object-fit:cover;object-position:center top;background:#E7ECEF;}
.member .member-info{min-height:118px;}
.advgrid{align-items:start;}
/* dropdown alignment: clamp width, keep on screen, align text */
.dropdown.mega{max-width:min(760px,92vw);}
.dropdown{text-align:left;}
.nav-links{gap:3.6rem;}
@media(max-width:560px){.nav .logo-img{height:17px;}}

/* v9: Clash Display headings + breathing room on narrow windows */
@media(max-width:1080px){
 section.band>.container,footer.site .container{margin-left:28px;margin-right:28px;}
 .hero .inner,.hero-thin .inner,.pd-hero .container,.contact-dark .container{padding-left:28px;padding-right:28px;}
}
@media(max-width:560px){
 section.band>.container,footer.site .container{margin-left:14px;margin-right:14px;}
}

/* v10: type scale measured from live site */
.band.dark h2{font-size:clamp(1.5rem,2.4vw,1.875rem);font-weight:600;letter-spacing:.5px;max-width:590px;line-height:1.35;font-family:var(--font-tagline);}
.band.dark .lede{font-size:1.25rem;font-weight:400;color:#fff;line-height:1.6;}
.lede{font-size:1.1rem;}
.nav-links a.nav-top-link{font-size:1.125rem;font-weight:300;}
.statgrid .stat-label,.bigstat .stat-label{color:#213340;}
.challenge .headline p{color:#213340;}
.hero .hero-tagline{font-weight:300;}

/* v11: hover reveals, journey expand, full-width menus, bio popup, rounded product imagery, b-roll heroes */
/* diagnostics photo-card hover text */
.photo-card .reveal{position:absolute;inset:0;z-index:3;display:flex;flex-direction:column;justify-content:flex-end;gap:.5rem;padding:1.6rem;background:linear-gradient(180deg,rgba(17,29,36,.05) 0%,rgba(17,29,36,.92) 62%);opacity:0;transition:opacity .35s ease;}
.photo-card .reveal .photo-title-reveal{color:#fff;font-family:var(--font-tagline);font-weight:600;font-size:1.3rem;line-height:1.25;}
.photo-card .reveal p{color:#E6EDF1;font-size:.95rem;line-height:1.55;}
.photo-card:hover .reveal,.photo-card:focus-within .reveal{opacity:1;}
.photo-card.has-reveal:hover > .photo-title{opacity:0;}
.photo-card > .photo-title{transition:opacity .3s ease;}
/* journey expand-on-hover */
.pathways{display:flex;gap:1.8rem;}
.pathcard{flex:1;min-width:0;transition:flex .55s cubic-bezier(.25,.8,.25,1);}
.pathcard:hover,.pathcard:focus-within{flex:2.1;}
.pathcard .reveal{opacity:0;background:linear-gradient(180deg,rgba(17,29,36,0) 0%,rgba(17,29,36,.94) 52%);justify-content:flex-end;padding-bottom:2rem;transition:opacity .4s ease .12s;}
.pathcard .reveal h3{font-family:var(--font-tagline);}
.pathcard .reveal p{font-size:.9rem;}
.pathcard:hover .reveal,.pathcard:focus-within .reveal{opacity:1;}
.pathcard .pathcard-caption{transition:opacity .3s ease;}
.pathcard:hover .pathcard-caption,.pathcard:focus-within .pathcard-caption{opacity:0;}
/* full-width menu panels like the original */
.dropdown{position:fixed;left:0;right:0;top:62px;transform:translateY(10px);width:100%;min-width:0;max-width:none;border-top:1px solid var(--frame-line);box-shadow:0 26px 44px rgba(13,20,24,.28);padding:0;}
.dropdown.mega{display:block;min-width:0;max-width:none;}
.nav-links>div:hover .dropdown,.nav-links>div:focus-within .dropdown{transform:translateY(0);}
.dropdown-in{max-width:1000px;margin:0 auto;display:grid;grid-template-columns:repeat(3,1fr);}
/* bio popup — split card matched to the design comp */
.modal .modal-box{padding:0;overflow:hidden;border-radius:18px;max-width:940px;display:grid;grid-template-columns:1fr 1.15fr;background:#F4F5F7;}
.modal .mphoto{min-height:460px;height:100%;}
.modal .mphoto img{width:100%;height:100%;object-fit:cover;object-position:center top;filter:grayscale(100%);display:block;}
.modal .mbody{padding:3rem 3rem 2.6rem 2.6rem;overflow:auto;max-height:86vh;}
.modal .mbody h2{font-family:var(--font-tagline);font-size:2.1rem;font-weight:600;color:#213340;border-bottom:1px solid #9AA3A9;padding-bottom:.7rem;margin-bottom:.7rem;line-height:1.1;}
.modal .mbody .member-role{color:#39434B;font-size:1.1rem;font-weight:400;margin-bottom:1.8rem;}
.modal .bio-text p{color:#39434B;}
.modal .bio-text p:first-child{font-weight:600;color:#213340;}
.modal .close{background:var(--mvx-sky);color:#0D1418;width:40px;height:40px;border-radius:50%;font-size:1.25rem;top:16px;right:16px;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 14px rgba(13,20,24,.25);transition:transform .2s ease;}
.modal .close:hover{transform:scale(1.08);}
/* rounded product imagery */
.pd-img,.serpex-two .prod img,.altrow .img{border-radius:18px;overflow:hidden;}
.pd-img img{border-radius:18px;}
@media(max-width:920px){
 .pathways{flex-direction:column;}
 .pathcard:hover,.pathcard:focus-within{flex:1;}
 .pathcard .reveal{opacity:1;background:linear-gradient(180deg,rgba(17,29,36,0) 30%,rgba(17,29,36,.94) 70%);}
 .pathcard .pathcard-caption{opacity:0;}
 .modal .modal-box{grid-template-columns:1fr;}
 .modal .mphoto{min-height:280px;max-height:320px;}
 .dropdown{position:static;}
 .dropdown-in,.dropdown-in.slim{display:block;padding:0;}
}

/* v12: diagnostics expand cards, dropdown spacing, reveal typography */
.photo-cards.expand{display:flex;gap:1.8rem;}
.photo-cards.expand .photo-card{flex:1;min-width:0;min-height:410px;transition:flex .55s cubic-bezier(.25,.8,.25,1),box-shadow .3s ease;}
.photo-cards.expand .photo-card:hover,.photo-cards.expand .photo-card:focus-within{flex:2.1;}
.photo-cards.expand .reveal{opacity:0;background:linear-gradient(180deg,rgba(17,29,36,0) 0%,rgba(17,29,36,.94) 52%);justify-content:flex-end;padding-bottom:2rem;transition:opacity .4s ease .12s;}
.photo-cards.expand .photo-card:hover .reveal,.photo-cards.expand .photo-card:focus-within .reveal{opacity:1;}
.photo-card .reveal .photo-title-reveal{font-family:var(--font-tagline);font-weight:600;}
.photo-card .reveal p.lead{color:var(--mvx-sky);font-style:italic;font-size:1.02rem;line-height:1.5;}
.photo-card .reveal p.photo-subtitle{color:#C9D2D8;font-style:italic;font-size:.85rem;line-height:1.55;}
@media(max-width:920px){
 .photo-cards.expand{flex-direction:column;}
 .photo-cards.expand .photo-card:hover,.photo-cards.expand .photo-card:focus-within{flex:1;}
 .photo-cards.expand .reveal{opacity:1;background:linear-gradient(180deg,rgba(17,29,36,0) 30%,rgba(17,29,36,.94) 70%);}
 .photo-cards.expand .photo-card .photo-title{opacity:0;}
}
/* dropdown mega: align to page container, even spacing, no dividers */
.dropdown-in{max-width:1000px;padding:2.2rem 24px 2.4rem;gap:3rem;align-items:start;}
.dropdown .mcol{padding:0;border-right:none;}
.dropdown .mcol h4{font-family:var(--font-tagline);font-size:1.15rem;color:var(--teal);margin-bottom:.7rem;}
.dropdown .mcol p{font-size:.88rem;line-height:1.6;margin-bottom:1.2rem;}
@media(max-width:560px){
 .dropdown-in{padding:0 0 .4rem .8rem;gap:0;}
 .dropdown .mcol{padding:.4rem 0;}
}

/* v13: mobile & tablet optimization */
@media(max-width:1080px){
 section.band>.container{padding:4.2rem 40px;}
 footer.site .container{padding:3.4rem 40px 2rem;}
}
@media(max-width:920px){
 /* in-menu dropdowns: flat, dark, compact (re-assert over later desktop rules) */
 .dropdown,.dropdown.mega{position:static;opacity:1;visibility:visible;transform:none;border:none;box-shadow:none;background:transparent;padding:0 0 .5rem .8rem;min-width:0;max-width:none;display:block;}
 .dropdown-in,.dropdown-in.slim{display:block;max-width:none;padding:0;gap:0;}
 .dropdown .mcol{padding:.35rem 0;border:none;display:block;min-height:0;}
 .dropdown .mcol p{display:none;}
 .dropdown .mcol h4{color:var(--mvx-sky);font-size:1rem;margin-bottom:.25rem;}
 .dropdown a{color:#C9D2D8;padding:.3rem 0;}
 .dropdown .mcol .btn{color:#fff;font-size:.82rem;}
 .dropdown .mcol .btn .circ{width:22px;height:22px;flex:0 0 22px;}
 .dropdown-in.slim a{padding:.3rem 0;font-size:.95rem;color:#C9D2D8;}
 /* wide tables scroll on tablet too */
 .spec{display:block;overflow-x:auto;-webkit-overflow-scrolling:touch;}
 .spec th,.spec td{min-width:150px;}
 /* comfortable card heights on touch */
 .photo-cards.expand .photo-card{min-height:340px;}
 .pathcard{min-height:360px;}
}
@media(max-width:760px){
 /* bio modal: stacked card scrolls as one unit */
 .modal{padding:14px;}
 .modal .modal-box{overflow-y:auto;max-height:90vh;}
 .modal .mphoto{min-height:0;max-height:34vh;}
 .modal .mbody{max-height:none;overflow:visible;padding:1.6rem 1.5rem 2rem;}
 .modal .mbody h2{font-size:1.55rem;padding-right:2.4rem;}
 .modal .mbody .member-role{margin-bottom:1.1rem;}
 /* compact cookie bar */
}
@media(max-width:560px){
 section.band>.container{padding:3.2rem 20px;}
 footer.site .container{padding:2.8rem 20px 1.6rem;}
 .hero-thin h1{font-size:2.9rem;}
 h2.section-title{font-size:2rem;}
 .modal .mbody h2{font-size:1.4rem;}
}

/* v14: original-style mega dropdowns */
.dropdown{position:fixed;left:0;right:0;top:62px;background:#fff;border-top:1px solid var(--frame-line);box-shadow:0 30px 50px rgba(13,20,24,.2);padding:0;min-width:0;max-width:none;}
.dropdown.mega{display:block;}
.dropdown-in{max-width:1160px;margin:0 auto;display:grid;grid-template-columns:repeat(3,1fr);gap:0;padding:0 24px;align-items:stretch;}
.dropdown .mcol{padding:2.4rem 2.2rem 2.6rem;border-right:1px solid var(--frame-line);}
.dropdown .mcol:first-child{border-left:1px solid var(--frame-line);}
.dropdown .mcol h4{font-family:var(--font-tagline);font-weight:600;font-size:1.75rem;color:var(--heading);margin-bottom:.8rem;transition:color .2s ease;}
.dropdown .mcol:hover h4{color:var(--mvx-blue);}
.dropdown .mcol p{display:block;font-size:.95rem;line-height:1.6;color:#39434B;margin-bottom:1.7rem;}
.dropdown .mcol .btn{font-style:italic;font-weight:400;font-size:.95rem;color:var(--ink);}
.dropdown .mcol .btn .circ{width:34px;height:34px;flex:0 0 34px;background:var(--header-dark);}
.dropdown .mcol .btn .circ svg{stroke:#fff;width:15px;height:15px;}
.dropdown .mcol:hover .btn .circ{background:var(--mvx-blue);}
/* news dropdown */
.dropdown-in.newsdd{grid-template-columns:1.35fr 1fr;}
.newsdd .ncol{padding:2rem 2.2rem 2.4rem;border-right:1px solid var(--frame-line);}
.newsdd .ncol:first-child{border-left:1px solid var(--frame-line);}
.newsdd .most-recent-article{font-style:italic;font-size:1.1rem;color:#39434B;border-bottom:1px solid var(--frame-line);padding-bottom:.9rem;margin-bottom:1.3rem;}
.newsdd .news-source{color:var(--mvx-blue);letter-spacing:.14em;text-transform:uppercase;font-size:.78rem;font-weight:500;}
.newsdd .date{color:#6A737B;letter-spacing:.14em;text-transform:uppercase;font-size:.78rem;margin-bottom:.9rem;}
.newsdd h4{font-family:var(--font-tagline);font-weight:600;font-size:1.85rem;line-height:1.15;margin-bottom:1.3rem;}
.newsdd h4 a{color:var(--mvx-blue);}
.newsdd h4 a:hover{color:var(--mvx-teal);}
.newsdd h5{font-family:var(--font-tagline);font-weight:600;font-size:1.2rem;line-height:1.3;margin-bottom:1rem;}
.newsdd h5 a{color:var(--mvx-blue);}
.newsdd h5 a:hover{color:var(--mvx-teal);}
.newsdd .read-more{display:inline-block;border:1px solid var(--heading);padding:.55rem 1.3rem;font-style:italic;font-size:.9rem;color:var(--ink);transition:background .2s ease;}
.newsdd .read-more:hover{background:var(--mvx-mist);}
.newsdd .cell{padding-bottom:1.5rem;}
.newsdd .cell.view-all{border-top:1px solid var(--frame-line);border-bottom:none;padding:1.5rem 0 0;margin-top:.2rem;}
.newsdd .cell.view-all a{font-style:italic;display:inline-flex;align-items:center;gap:.8rem;color:var(--ink);}
.newsdd .cell.view-all .circ{width:44px;height:44px;flex:0 0 44px;border-radius:50%;background:var(--header-dark);display:inline-flex;align-items:center;justify-content:center;}
.newsdd .cell.view-all .circ svg{stroke:#fff;width:17px;height:17px;}
.newsdd .cell.view-all a:hover .circ{background:var(--mvx-blue);}
/* dropdown link fixes */
.dropdown .mcol .btn{display:inline-flex;align-items:center;gap:.7rem;padding:0;}
.newsdd a{display:inline;padding:0;}
.newsdd .read-more{display:inline-block;padding:.55rem 1.3rem;}
.newsdd .cell.view-all a{display:inline-flex;padding:0;}

/* v15: dropdown bottom-aligned links + original type scale */
.dropdown .mcol{display:flex;flex-direction:column;align-items:flex-start;min-height:300px;}
.dropdown .mcol .btn{margin-top:auto;}
.dropdown .mcol h4{font-size:1.9rem;letter-spacing:-.01em;}
.dropdown .mcol p{font-size:1.05rem;line-height:1.65;color:#39434B;margin-bottom:2rem;}
.dropdown .mcol .btn{font-size:1.02rem;}
.dropdown .mcol .btn .circ{width:42px;height:42px;flex:0 0 42px;}
.dropdown .mcol .btn .circ svg{width:17px;height:17px;}
.newsdd .most-recent-article{font-size:1.2rem;}
.newsdd .news-source,.newsdd .date{font-size:.85rem;}
.newsdd h4{font-size:2.2rem;}
.newsdd h5{font-size:1.35rem;}
.newsdd .read-more{font-size:1rem;padding:.65rem 1.5rem;}
.newsdd .cell.view-all a{font-size:1.02rem;}

/* mobile re-assert (must stay last) */
@media(max-width:920px){
 .dropdown,.dropdown.mega{position:static;opacity:1;visibility:visible;transform:none;border:none;box-shadow:none;background:transparent;padding:0 0 .5rem .8rem;min-width:0;max-width:none;display:block;}
 .dropdown.newsmega{display:none;}
 .dropdown-in,.dropdown-in.newsdd{display:block;max-width:none;padding:0;gap:0;}
 .dropdown .mcol{padding:.35rem 0;border:none;display:block;min-height:0;}
 .dropdown .mcol p{display:none;}
 .dropdown .mcol h4{color:var(--mvx-sky);font-size:1rem;margin-bottom:.25rem;}
 .dropdown .mcol:hover h4{color:var(--mvx-sky);}
 .dropdown a{color:#C9D2D8;padding:.3rem 0;}
 .dropdown .mcol .btn{color:#fff;font-size:.82rem;font-style:normal;}
 .dropdown .mcol .btn .circ{width:22px;height:22px;flex:0 0 22px;background:var(--cyan);}
 .dropdown .mcol .btn .circ svg{stroke:currentColor;}
}

/* v16: homepage refinements */
.hero .kicker{font-size:2rem;}
.band.dark .bgimg{opacity:.55;}
.band.dark.goal .bgimg{object-position:center 22%;}
.band.dark .fullrule{height:1px;background:rgba(255,255,255,.65);margin:1.5rem calc(50% - 50vw) 2.4rem;}
.band.dark .stackcol h2{max-width:640px;}
.band.dark .stackcol .lede{max-width:620px;margin-top:1.5rem;}
.bigstat{display:grid;grid-template-columns:minmax(96px,auto) 1fr;gap:0 1.5rem;align-items:center;margin-top:2rem;}
.bigstat .stat-number{color:#4FC4E8;}
.bigstat .stat-label{font-style:italic;border-left:1px solid #B9C0C6;padding:.7rem 0 .7rem 1.5rem;font-size:1rem;max-width:240px;}
.statgrid .stat-number{color:#4FC4E8;white-space:nowrap;}
.statgrid .cell:hover .stat-number{color:var(--mvx-blue);}
.jpanel{background:#fff;border:1px solid var(--frame-line);padding:3.2rem 2.6rem 14rem;margin-top:3.4rem;}
.jpanel .journey:first-child{margin-top:0;}
.jpanel .journey{margin-top:3rem;}
.pathways{margin-top:-11.5rem;position:relative;z-index:2;padding:0 2.6rem;}
/* footer: linkedin square in Contact us */
.fcontact .frow{display:flex;align-items:center;gap:1.2rem;margin-top:.2rem;}
.fcontact .frow a.mail{color:var(--mvx-blue);}
.fcontact .frow a.mail:hover{color:var(--mvx-teal);}
.li-sq{display:inline-flex;width:38px;height:38px;border-radius:7px;background:var(--mvx-blue);color:#fff;align-items:center;justify-content:center;flex:0 0 38px;transition:background .2s ease;}
.li-sq:hover{background:var(--mvx-teal);}
.li-sq svg{width:20px;height:20px;}
@media(max-width:920px){
 .jpanel{padding:2rem 1.4rem 2.4rem;}
 .pathways{margin-top:2rem;padding:0;}
 .band.dark .fullrule{margin:1rem 0 1.6rem;}
 .hero .kicker{font-size:1.4rem;}
}

/* v17: goal band tuning */
.band.dark.goal{padding:7.5rem 0;}
.band.dark.goal .bgimg{opacity:.75;object-position:center 32%;}

/* v18: mission overlay clarity, aligned stat divider lines, full-width journey panel */
.band.dark .bgimg{opacity:.7;}
.band.dark.goal .bgimg{opacity:.75;}
.bigstat{grid-template-columns:132px 1fr;}
.jpanel{margin-left:-72px;margin-right:-72px;}
@media(max-width:1080px){.jpanel{margin-left:-40px;margin-right:-40px;}}
@media(max-width:560px){.jpanel{margin-left:-20px;margin-right:-20px;}}

/* v19: products dropdown — three blues, header font matches homepage h1, circles match headers */
.dropdown .mcol h4{font-family:var(--font-tagline);font-weight:600;}
.dropdown .mcol.cat-risk h4,.dropdown .mcol.cat-risk:hover h4{color:#213340;}
.dropdown .mcol.cat-diagnosis h4,.dropdown .mcol.cat-diagnosis:hover h4{color:#276F8B;}
.dropdown .mcol.cat-intervention h4,.dropdown .mcol.cat-intervention:hover h4{color:#2BA9D4;}
.dropdown .mcol.cat-risk .btn .circ,.dropdown .mcol.cat-risk:hover .btn .circ{background:#213340;}
.dropdown .mcol.cat-diagnosis .btn .circ,.dropdown .mcol.cat-diagnosis:hover .btn .circ{background:#276F8B;}
.dropdown .mcol.cat-intervention .btn .circ,.dropdown .mcol.cat-intervention:hover .btn .circ{background:#2BA9D4;}
.dropdown.mega{position:fixed;}
.dropdown.mega:not(.newsmega)::after{content:"";position:absolute;right:0;top:52%;width:calc((100% - 1160px)/2 + 24px);height:1px;background:var(--frame-line);}
@media(max-width:1200px){.dropdown.mega:not(.newsmega)::after{display:none;}}
@media(max-width:920px){
 .dropdown .mcol.cat-risk h4,.dropdown .mcol.cat-diagnosis h4,.dropdown .mcol.cat-intervention h4{color:var(--mvx-sky);}
 .dropdown .mcol.cat-risk .btn .circ,.dropdown .mcol.cat-diagnosis .btn .circ,.dropdown .mcol.cat-intervention .btn .circ{background:var(--cyan);}
 .dropdown.mega::after{display:none;}
 .dropdown,.dropdown.mega{position:static;}
}

/* v20: vertical right rule on mega dropdowns, two-column team dropdown */
.dropdown.mega:not(.newsmega)::after{content:none;}
.dropdown .mcol:last-child{border-right:1px solid var(--frame-line);}
.dropdown-in.cols2{grid-template-columns:repeat(2,1fr);max-width:790px;}
@media(max-width:920px){
 .dropdown-in.cols2{display:block;max-width:none;}
 .dropdown .mcol:last-child{border:none;}
}

/* v21: news dropdown conformed to original — Clash Display scale/colors, gray panel */
.dropdown.newsmega{background:var(--page-bg);}
.newsdd .ncol{border-color:#C7CCD2;}
.newsdd .ncol:first-child{border-color:#C7CCD2;}
.newsdd .most-recent-article{color:#39434B;border-color:#B9C0C6;}
.newsdd .news-source{color:#1E9CD0;}
.newsdd h4{font-family:var(--font-tagline);font-weight:600;font-size:1.7rem;line-height:1.18;letter-spacing:.01em;}
.newsdd h4 a{color:#1E9CD0;}
.newsdd h5{font-family:var(--font-tagline);font-weight:600;font-size:1.2rem;line-height:1.3;letter-spacing:.01em;}
.newsdd h5 a{color:#1E9CD0;}
.newsdd h4 a:hover,.newsdd h5 a:hover{color:var(--mvx-teal);}
.newsdd .read-more{border-color:#39434B;background:transparent;}
.newsdd .cell.view-all{border-color:#C7CCD2;}

/* v22: products overview — dropdown-style family boxes + Distributed by */
.famrow{display:grid;grid-template-columns:repeat(3,1fr);background:#fff;margin-top:1.5rem;}
.famrow .family-cell{padding:2.6rem 2.2rem 2.8rem;border-right:1px solid var(--frame-line);display:flex;flex-direction:column;align-items:flex-start;min-height:300px;}
.famrow .family-cell:first-child{border-left:1px solid var(--frame-line);}
.famrow h4{font-family:var(--font-tagline);font-weight:600;font-size:1.9rem;letter-spacing:-.01em;margin-bottom:.8rem;}
.famrow p{font-size:1.02rem;line-height:1.65;color:#39434B;margin-bottom:2rem;}
.famrow .btn{margin-top:auto;font-style:italic;font-weight:400;font-size:1.02rem;}
.famrow .btn .circ{width:42px;height:42px;flex:0 0 42px;}
.famrow .btn .circ svg{stroke:#fff;width:17px;height:17px;}
.famrow .family-cell.cat-risk h4{color:#213340;}.famrow .family-cell.cat-risk .btn .circ{background:#213340;}
.famrow .family-cell.cat-diagnosis h4{color:#276F8B;}.famrow .family-cell.cat-diagnosis .btn .circ{background:#276F8B;}
.famrow .family-cell.cat-intervention h4{color:#2BA9D4;}.famrow .family-cell.cat-intervention .btn .circ{background:#2BA9D4;}
.distby{margin-top:3.6rem;}
.distby img{height:58px;width:auto;mix-blend-mode:multiply;margin-top:1.2rem;}
@media(max-width:920px){
 .famrow{grid-template-columns:1fr;}
 .famrow .family-cell{border:none;border-bottom:1px solid var(--frame-line);min-height:0;}
 .famrow .family-cell:first-child{border-left:none;}
}

/* v23: news hero position, smaller grid Read More, team hero via photo 059 */
.newshero .hero-img{object-position:center 65%;}
.newsgrid .readmore{padding:.4rem 1.1rem;font-size:.85rem;}

/* v25: form honeypot + 404 page */
.honeypot{position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden;}
.form-msg{border-left:4px solid currentColor;}
button[type=submit][disabled]{opacity:.6;cursor:progress;}
.not-found .not-found-code{font-family:var(--font-tagline);font-weight:600;font-size:clamp(5rem,14vw,10rem);line-height:.9;color:var(--mvx-cloud);letter-spacing:-.02em;margin-bottom:.6rem;}
.not-found .section-title{margin-bottom:1rem;}
.not-found .lede{max-width:640px;}
.not-found .famrow{background:#fff;}

/* ============ v27: mobile menu, journey bar, tap-cards, modal, scrims ============ */

/* darker scrims so overlaid text stays legible (desktop + mobile) */
.hero .shade{background:linear-gradient(90deg,rgba(9,15,19,.84) 0%,rgba(9,15,19,.62) 45%,rgba(9,15,19,.40) 100%);}
.hero-thin .overlay{background:linear-gradient(90deg,rgba(11,17,22,.86) 0%,rgba(11,17,22,.60) 48%,rgba(11,17,22,.34) 100%);}
.band.dark::after{content:"";position:absolute;inset:0;pointer-events:none;
 background:linear-gradient(90deg,rgba(8,13,17,.80) 0%,rgba(8,13,17,.58) 50%,rgba(8,13,17,.34) 100%);}
.band.dark>.container{position:relative;z-index:2;}
.band.dark .bgimg{z-index:0;}

/* news source logos: MassDevice now matches the rest */
.newsgrid .srclogo,.featured .srclogo{mix-blend-mode:multiply;}

/* ---------------- mobile / tablet nav ---------------- */
@media(max-width:920px){
 /* stray divider beside the logo */
 .nav .logo{border-right:none;}
 /* menu becomes a scrollable panel so nothing is stranded below the fold */
 .nav-links{position:fixed;top:62px;left:0;right:0;
  max-height:calc(100vh - 62px);max-height:calc(100dvh - 62px);
  overflow-y:auto;-webkit-overflow-scrolling:touch;padding-bottom:2rem;}
 /* sub-menus collapsed until tapped */
 .nav-links>div>.dropdown{display:none;}
 .nav-links>div.sub-open>.dropdown{display:block;}
 .nav-links>div>a.nav-top-link .plus{transition:transform .2s ease;display:inline-block;}
 .nav-links>div.sub-open>a.nav-top-link{color:var(--mvx-sky);}
 .nav-links>div.sub-open>a.nav-top-link .plus{transform:rotate(45deg);}
 .nav-links a.nav-top-link{width:100%;}
 .nav-links>div.mobile-extra{display:block;width:100%;border-top:1px solid rgba(255,255,255,.16);
  margin-top:.8rem;padding-top:.8rem;}
 .nav-links>div.mobile-extra a{display:block;color:#fff;font-family:var(--font-tagline);
  text-transform:uppercase;letter-spacing:.12em;font-size:.95rem;padding:.7rem 0;}
}

/* ---------------- patient-journey bars stay on one line ---------------- */
@media(max-width:920px){
 .jbar{flex-wrap:nowrap;gap:5px;align-items:stretch;}
 .jseg{min-width:0;white-space:normal;font-size:.66rem;padding:.55rem .35rem;line-height:1.2;
  display:flex;align-items:center;justify-content:center;hyphens:auto;}
 .jseg.end-marker{flex:0 0 5px;padding:0;}
 .journey .jtitle{font-size:.72rem;letter-spacing:.16em;}
 .journey .jnote,.jarrow{font-size:.78rem;}
 .journey .jnote::before,.journey .jnote::after,.jarrow::before{max-width:36px;}
}
@media(max-width:560px){
 .jseg{font-size:.55rem;padding:.5rem .2rem;letter-spacing:-.01em;}
 .journey .jtitle{font-size:.62rem;letter-spacing:.1em;}
 .journey .jnote,.jarrow{font-size:.7rem;}
}

/* ---------------- tap-to-expand cards on mobile ---------------- */
@media(max-width:920px){
 .pathcard,.photo-cards.expand .photo-card{cursor:pointer;}
 /* collapsed: image + title only */
 .pathcard .reveal,.photo-cards.expand .photo-card .reveal{opacity:0;pointer-events:none;}
 .pathcard .pathcard-caption,.photo-cards.expand .photo-card .photo-title{opacity:1;}
 /* affordance */
 .pathcard::before,.photo-cards.expand .photo-card::before{content:"+";position:absolute;top:14px;right:14px;
  z-index:4;width:34px;height:34px;border-radius:50%;background:rgba(255,255,255,.92);color:#12333D;
  font-family:var(--font-tagline);font-weight:600;font-size:1.35rem;line-height:34px;text-align:center;
  transition:transform .25s ease;}
 .pathcard.open::before,.photo-cards.expand .photo-card.open::before{transform:rotate(45deg);}
 /* expanded: reveal flows inline so the card grows and the text is fully readable */
 .pathcard.open,.photo-cards.expand .photo-card.open{min-height:0;}
 .pathcard.open .reveal,.photo-cards.expand .photo-card.open .reveal{
  position:relative;opacity:1;pointer-events:auto;background:rgba(13,21,27,.94);
  padding:1.5rem 1.4rem 1.8rem;}
 .pathcard.open .pathcard-caption,.photo-cards.expand .photo-card.open .photo-title{display:none;}
 .pathcard.open .reveal p,.photo-cards.expand .photo-card.open .reveal p{font-size:.92rem;line-height:1.6;}
 .photo-cards.expand .photo-card.open .reveal p.photo-subtitle{font-size:.86rem;}
}
@media(max-width:760px){
 .modal .mphoto img{object-fit:contain;object-position:center;background:#E9ECEF;}
 .modal .mphoto{max-height:38vh;background:#E9ECEF;}
 /* × stays put while the bio scrolls */
 .modal .close{position:fixed;top:12px;right:12px;width:54px;height:54px;font-size:1.7rem;
  background:var(--mvx-sky);color:#0D1418;box-shadow:0 6px 20px rgba(8,13,17,.45);z-index:6;}
 /* plus an unmissable labelled button at the end of the bio */
 .modal .close-b{display:block;position:static;width:100%;height:auto;border-radius:6px;
  margin-top:1.8rem;padding:.95rem 1rem;font-family:var(--font-tagline);font-weight:600;
  font-size:1rem;letter-spacing:.06em;text-transform:uppercase;background:var(--header-dark);
  color:#fff;box-shadow:none;}
}
/* desktop: show a bit more of each headshot */
.modal .mphoto img{object-position:center 18%;}

/* v27b: let narrow journey labels wrap rather than spill */
@media(max-width:920px){
 .jseg{overflow-wrap:anywhere;word-break:break-word;overflow:hidden;}
}

/* ============ v28 ============ */
/* challenge stats: keep two columns on phones so the block stays compact */
@media(max-width:560px){
 .statgrid{grid-template-columns:1fr 1fr;}
 .statgrid .cell{padding:1.1rem .9rem 1.5rem;}
 .statgrid .stat-number{font-size:1.5rem;}
 .statgrid .stat-label{font-size:.78rem;line-height:1.45;}
}
/* bio photo panel: gray matched to the studio backdrop so the letterbox is invisible */
.modal .mphoto{background:#A3A3A3;}
@media(max-width:760px){
 .modal .mphoto{background:#A3A3A3;}
 .modal .close-b{display:none;}
}

/* ============ v29: Maverix brand lockup + inline "Distributed by" ============ */
.sechead{justify-content:flex-start;gap:3.2rem;}
.distby.inline{margin-top:0;display:flex;flex-direction:column;align-items:flex-start;gap:.65rem;}
.distby.inline .seclabel{margin:0;gap:0;font-size:.78rem;letter-spacing:.28em;color:var(--mvx-slate);}
.distby.inline .seclabel::after{content:none;}
.distby.inline img{height:46px;width:auto;margin-top:0;object-fit:contain;background:transparent;padding:0;}
.sechead .contact-block{margin-left:auto;}
@media(max-width:920px){
 .sechead{gap:2rem;}
 .brandlock .bl-mark{height:42px;}
 .brandlock .bl-tag{font-size:1.15rem;}
 .distby.inline img{height:38px;}
 .sechead .contact-block{margin-left:0;}
}
@media(max-width:560px){
 .brandlock{align-items:flex-start;}
 .brandlock .bl-tag{white-space:normal;}
}

/* ============ v30: news dropdown conformed to the original ============ */
.dropdown-in.newsdd{grid-template-columns:1.25fr 1fr;max-width:1010px;}
.newsdd .ncol{padding:1.6rem 2rem 1.9rem;}
.newsdd .most-recent-article{font-size:1.05rem;max-width:470px;padding-bottom:.7rem;margin-bottom:1rem;}
.newsdd .news-source{font-size:.8rem;letter-spacing:.14em;}
.newsdd .date{font-size:.8rem;letter-spacing:.14em;margin-bottom:.7rem;}
.newsdd h4{font-size:2rem;line-height:1.14;max-width:480px;margin-bottom:1.1rem;}
.newsdd h5{font-size:1.3rem;line-height:1.2;max-width:355px;margin-bottom:.9rem;}
.newsdd .read-more{font-size:.92rem;padding:.5rem 1.15rem;}
.newsdd .cell{padding-bottom:1.2rem;}
.newsdd .cell.view-all{padding-top:1.2rem;margin-top:0;}
.newsdd .cell.view-all a{font-size:1rem;gap:.7rem;}
.newsdd .cell.view-all .circ{width:40px;height:40px;flex:0 0 40px;}
.newsdd .cell.view-all .circ svg{width:15px;height:15px;}

/* v30b: headline anchors must inherit their heading's type, not the generic dropdown link style */
.newsdd h4 a,.newsdd h5 a{font-size:inherit;font-weight:inherit;font-family:inherit;
 line-height:inherit;letter-spacing:inherit;}

/* ---------- v31: static product groups, Rx note, pd-side "Distributed by" ---------- */
.pgroup{margin-top:2.4rem;}
.pgroup:first-of-type{margin-top:1.6rem;}
.pgroup .pglabel{font-family:var(--font-tagline);font-weight:600;font-size:.9rem;
 letter-spacing:.26em;text-transform:uppercase;color:var(--mvx-teal);
 padding-bottom:.7rem;margin-bottom:1.3rem;border-bottom:1px solid var(--frame-line);}
.pgrid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1.3rem;align-items:stretch;}
.pgrid .pcard{scroll-snap-align:none;}
.seclabel + .pgrid{margin-top:1.5rem;}
p.rxnote{margin-top:2.6rem;font-size:.86rem;line-height:1.6;color:#5B6670;
 max-width:920px;border-top:1px solid var(--frame-line);padding-top:1.2rem;}
p.mfg-note{margin-top:1.6rem;font-size:.85rem;font-style:italic;color:#5B6670;}
.pd-side .pd-brand{display:flex;flex-direction:column;align-items:flex-start;gap:.55rem;}
.pd-side .pd-brand .seclabel{margin:0;gap:0;font-size:.72rem;letter-spacing:.26em;color:var(--mvx-slate);}
.pd-side .pd-brand .seclabel::after{content:none;}
.pd-side .pd-brand img{max-width:210px;width:100%;height:auto;}
a.reglink{display:inline-flex;align-items:center;gap:.45rem;font-weight:500;color:var(--mvx-teal);}
/* zoomed-out hero: taller frame reveals more of a portrait source image */
.hero-thin.zoomout .inner{padding-top:16.5rem;padding-bottom:3rem;}
@media(max-width:900px){.pgrid{grid-template-columns:repeat(2,minmax(0,1fr));}}
@media(max-width:640px){
 .pgrid{grid-template-columns:1fr;}
 .hero-thin.zoomout .inner{padding-top:10rem;}
}

/* ---------- v32: whole product card is one click target ---------- */
.pcard{position:relative;}
.pcard .card-info .btn::after{content:"";position:absolute;inset:0;z-index:1;}
.pcard .card-info .btn{position:static;}
.pcard:focus-within{outline:2px solid var(--mvx-blue);outline-offset:3px;}
.pcard,.pcard .card-photo,.pcard .card-photo img{cursor:pointer;}
/* uniform white product photography */
.pcard .card-photo{background:#fff;}
.pcard .card-photo img{object-fit:contain;background:#fff;}

/* ---------- v33: dropdown links get an animated underline, not a gray box ---------- */
.dropdown a:hover{background:transparent;}
.btn .btn-label{position:relative;display:inline-block;}
.dropdown .mcol .btn .btn-label::after,
.famrow .btn .btn-label::after{content:"";position:absolute;left:0;right:0;bottom:-4px;height:1.5px;
 background:currentColor;transform:scaleX(0);transform-origin:left center;
 transition:transform .38s cubic-bezier(.22,.61,.36,1);}
.dropdown .mcol .btn:hover .btn-label::after,
.dropdown .mcol:hover .btn .btn-label::after,
.famrow .btn:hover .btn-label::after,
.famrow .family-cell:hover .btn .btn-label::after{transform:scaleX(1);}
@media(prefers-reduced-motion:reduce){
 .dropdown .mcol .btn .btn-label::after,.famrow .btn .btn-label::after{transition:none;}
}

/* ---------- v34: careers job feeds ---------- */
.jobs-split{gap:3.5rem;}
.jobs-col{display:flex;flex-direction:column;}
.jobs-embed{min-height:120px;margin-bottom:1.6rem;}
.jobs-embed .sk-ww-linkedin-page-jobs:not(:empty) + .jobs-empty{display:none;}
.jobs-empty{font-size:.95rem;color:#5B6670;font-style:italic;margin:0;}
.btn.joblink{margin-top:auto;font-style:italic;font-weight:400;align-self:flex-start;}
.btn.joblink .circ{width:38px;height:38px;flex:0 0 38px;background:var(--mvx-teal);}
.btn.joblink .circ svg{stroke:#fff;}
.btn.joblink .btn-label::after{content:"";position:absolute;left:0;right:0;bottom:-4px;height:1.5px;
 background:currentColor;transform:scaleX(0);transform-origin:left center;
 transition:transform .38s cubic-bezier(.22,.61,.36,1);}
.btn.joblink:hover .btn-label::after{transform:scaleX(1);}
@media(max-width:820px){.jobs-split{gap:2.6rem;}}
@media(prefers-reduced-motion:reduce){.btn.joblink .btn-label::after{transition:none;}}

/* ---------- v35: one lockup treatment across all three product families ---------- */
.sechead .famlogo{height:74px;width:auto;object-fit:contain;background:transparent;padding:0;
 align-self:flex-start;}
@media(max-width:920px){.sechead .famlogo{height:58px;}}
@media(max-width:560px){.sechead .famlogo{height:48px;}}

/* ---------- v37: brighter homepage imagery, top-aligned lockups, CTA above header ---------- */
/* hero video + still: more of the footage shows through, scrim eased on the right */
.hero video,.hero .hero-img{opacity:.74;}
.hero .shade{background:linear-gradient(90deg,rgba(9,15,19,.72) 0%,rgba(9,15,19,.44) 45%,rgba(9,15,19,.20) 100%);}
/* dark bands (Our Mission, Our Goal, About You, Join Us) */
.band.dark .bgimg{opacity:.88;}
.band.dark.goal .bgimg{opacity:.92;}
.band.dark::after{background:linear-gradient(90deg,rgba(8,13,17,.66) 0%,rgba(8,13,17,.42) 50%,rgba(8,13,17,.20) 100%);}
/* section head: lockup and "Distributed by" hang from the same top line */
.sechead{align-items:flex-start;}
.sechead .famlogo,.sechead .distby.inline,.sechead .contact-block{margin-top:0;}

/* ---------- v38: heroes pulled back a further 50%, gray fill either side ---------- */
.hero-thin.zoomout{background:#AEB4BA;}
.hero-thin.zoomout .hero-img{left:16.65%;right:auto;width:66.7%;}
@media(max-width:900px){
 .hero-thin.zoomout .hero-img{left:8%;width:84%;}
}
@media(max-width:600px){
 .hero-thin.zoomout .hero-img{left:0;width:100%;}
}

/* ---------- v39: zoomed-out heroes fade into the gray instead of hard-edging ---------- */
.hero-thin.zoomout .hero-img{
 -webkit-mask-image:linear-gradient(90deg,rgba(0,0,0,0) 0%,rgba(0,0,0,.55) 5%,#000 14%,#000 86%,rgba(0,0,0,.55) 95%,rgba(0,0,0,0) 100%);
 mask-image:linear-gradient(90deg,rgba(0,0,0,0) 0%,rgba(0,0,0,.55) 5%,#000 14%,#000 86%,rgba(0,0,0,.55) 95%,rgba(0,0,0,0) 100%);
 -webkit-mask-repeat:no-repeat;mask-repeat:no-repeat;
 -webkit-mask-size:100% 100%;mask-size:100% 100%;}
/* the image is wider than the visible band, so widen it to keep the same amount of picture showing */
.hero-thin.zoomout .hero-img{left:12.9%;width:74.2%;}
@media(max-width:900px){.hero-thin.zoomout .hero-img{left:5.5%;width:89%;}}
@media(max-width:600px){
 .hero-thin.zoomout .hero-img{left:0;width:100%;
  -webkit-mask-image:none;mask-image:none;}
}

/* ---------- v40: Narwhal Cryo System featured section (Diagnosis page) ---------- */
.nwfeature{margin:3.2rem 0 3.6rem;border:1px solid var(--frame-line);background:#fff;overflow:hidden;}
/* teal masthead, echoing the brochure cover */
.nw-top{display:grid;grid-template-columns:1.15fr .85fr;gap:3rem;align-items:center;
 padding:3.2rem 3rem;color:#fff;
 background:linear-gradient(115deg,#0F3D50 0%,#1A4A5D 30%,#276F8B 68%,#3494BA 100%);}
.nw-badge{display:inline-flex;align-items:center;gap:.5rem;border:1px solid rgba(255,255,255,.45);
 border-radius:999px;padding:.35rem 1rem;font-family:var(--font-tagline);font-weight:600;
 font-size:.7rem;letter-spacing:.24em;text-transform:uppercase;color:#fff;margin-bottom:1.6rem;}
.nw-badge::before{content:"";width:7px;height:7px;border-radius:50%;background:#F26A3D;}
.nw-kicker{font-family:var(--font-tagline);font-weight:600;font-size:.8rem;letter-spacing:.26em;
 text-transform:uppercase;color:var(--mvx-sky);margin-bottom:1rem;
 display:flex;align-items:center;gap:.9rem;}
.nw-kicker::before{content:"";width:26px;height:1px;background:var(--mvx-sky);flex:0 0 26px;}
.nw-title{font-family:var(--font-tagline);font-weight:700;font-size:clamp(2.4rem,4vw,3.5rem);
 line-height:1.04;letter-spacing:-.015em;color:#fff;margin:0 0 1.2rem;}
.nw-dot{color:#F26A3D;}
.nw-lede{font-size:1.05rem;line-height:1.65;color:rgba(255,255,255,.9);max-width:34rem;margin-bottom:1.9rem;}
.nw-cta{color:#fff;font-weight:600;}
.nw-cta .circ{background:#fff;}
.nw-cta .circ svg{stroke:var(--mvx-deep);}
.nw-cta .btn-label::after{content:"";position:absolute;left:0;right:0;bottom:-4px;height:1.5px;background:#fff;
 transform:scaleX(0);transform-origin:left center;transition:transform .38s cubic-bezier(.22,.61,.36,1);}
.nw-cta:hover{color:#fff;}
.nw-cta:hover .btn-label::after{transform:scaleX(1);}
.nw-shot{aspect-ratio:4/5;border-radius:14px;}
.nw-body{padding:2.8rem 3rem 3rem;}
.nw-seclabel{font-family:var(--font-tagline);font-weight:600;font-size:.78rem;letter-spacing:.26em;
 text-transform:uppercase;color:var(--mvx-teal);padding-bottom:.7rem;margin-bottom:1.6rem;
 border-bottom:1px solid var(--frame-line);}
.nw-seclabel.evidence{color:#C2632F;margin-top:3rem;}
.nw-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:1.4rem;}
.nw-card{border:1px solid var(--frame-line);border-radius:10px;padding:1.5rem;background:#FCFDFD;}
.nw-card h3{font-family:var(--font-tagline);font-weight:700;font-size:1.08rem;color:var(--heading);
 margin:0 0 1rem;line-height:1.3;}
.nw-why{font-family:var(--font-tagline);font-weight:600;font-size:.68rem;letter-spacing:.2em;
 text-transform:uppercase;color:#C2632F;padding-bottom:.5rem;margin-bottom:.7rem;
 border-bottom:1px solid var(--frame-line);}
.nw-card p{font-size:.9rem;line-height:1.6;color:#39434B;margin:0;}
.nw-evtitle{font-family:var(--font-tagline);font-weight:700;font-size:1.9rem;color:var(--heading);
 margin:0 0 1rem;line-height:1.2;}
.nw-evlede{font-size:1rem;line-height:1.68;color:#39434B;max-width:56rem;margin-bottom:1.8rem;}
.nw-n{display:block;margin-top:.5rem;font-size:.9rem;color:#5B6670;}
.nw-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:1.2rem;margin-bottom:1.4rem;}
.nw-stat{border-radius:10px;padding:1.6rem 1.4rem;text-align:center;
 background:linear-gradient(160deg,#EAF4F8 0%,#DCEBF2 100%);border:1px solid #CBDEE7;}
.nw-fig{font-family:var(--font-tagline);font-weight:300;font-size:3rem;line-height:1;
 color:var(--mvx-teal);margin-bottom:.8rem;}
.nw-fig.split-figure{display:flex;align-items:center;justify-content:center;gap:1.1rem;font-size:2.2rem;}
.nw-fig.split-figure span{display:inline-flex;align-items:baseline;gap:.2rem;position:relative;}
.nw-fig.split-figure em{font-style:normal;font-size:.9rem;color:var(--mvx-slate);}
.nw-fig.split-figure small{position:absolute;left:0;top:100%;margin-top:.3rem;font-size:.68rem;
 letter-spacing:.1em;color:#C2632F;white-space:nowrap;}
.nw-fig.split-figure i{width:1px;height:38px;background:#B4C9D4;display:inline-block;}
.nw-stat p{font-size:.86rem;line-height:1.5;color:#39434B;margin:.9rem 0 0;}
.nw-foot{font-size:.72rem;line-height:1.55;color:#6B747C;margin:0 0 .9rem;}
@media(max-width:1000px){
 .nw-top{grid-template-columns:1fr;gap:2rem;padding:2.4rem 1.8rem;}
 .nw-shot{aspect-ratio:16/9;}
 .nw-body{padding:2rem 1.8rem 2.4rem;}
 .nw-cards,.nw-stats{grid-template-columns:1fr;}
 .nw-evtitle{font-size:1.5rem;}
}
@media(prefers-reduced-motion:reduce){.nw-cta .btn-label::after{transition:none;}}
/* v40a: masthead type must win over the generic band heading colour */
.nwfeature .nw-top .nw-title,.nwfeature .nw-top h2{color:#fff;}
.nwfeature .nw-top .nw-title .nw-dot{color:#F26A3D;}
/* room for the sampling-length labels under the split figure */
.nw-fig.split-figure{margin-bottom:1.9rem;}
.nw-stat p{margin-top:.6rem;}
/* v40b: real Narwhal photography replaces the placeholders */
.nw-shot{overflow:hidden;}
.nw-shot img{width:100%;height:100%;object-fit:cover;display:block;border-radius:14px;}
.nw-cardimg{aspect-ratio:16/10;border-radius:8px;overflow:hidden;margin-bottom:1.1rem;
 background:#fff;border:1px solid var(--frame-line);}
.nw-cardimg img{width:100%;height:100%;object-fit:contain;display:block;background:#fff;}
/* v41: card headings reserve two lines so the three photos align across the row */
.nw-card{display:flex;flex-direction:column;}
.nw-card h3{min-height:2.6em;}
@media(max-width:1000px){.nw-card h3{min-height:0;}}

/* ---------- v42: journey cards advertise themselves — CTA always on top ---------- */
.pathcard .pcta{position:absolute;left:0;right:0;bottom:0;z-index:4;
 padding:0 1.5rem 1.4rem;display:flex;justify-content:center;pointer-events:auto;}
.pathcard .pcta .btn{color:#fff;font-style:italic;font-weight:400;font-size:.8rem;
 line-height:1.3;text-align:left;gap:.5rem;align-items:center;}
.pathcard .pcta .btn .circ{width:30px;height:30px;flex:0 0 30px;background:rgba(255,255,255,.16);
 border:1px solid rgba(255,255,255,.55);backdrop-filter:blur(2px);}
.pathcard .pcta .btn .circ svg{stroke:#fff;width:13px;height:13px;}
.pathcard .pcta .btn .btn-label{position:relative;}
.pathcard .pcta .btn .btn-label::after{content:"";position:absolute;left:0;right:0;bottom:-3px;height:1px;
 background:rgba(255,255,255,.55);transform:scaleX(0);transform-origin:left center;
 transition:transform .38s cubic-bezier(.22,.61,.36,1);}
.pathcard:hover .pcta .btn .btn-label::after,.pathcard:focus-within .pcta .btn .btn-label::after{transform:scaleX(1);}
.pathcard:hover .pcta .btn .circ,.pathcard:focus-within .pcta .btn .circ{background:var(--mvx-blue);
 border-color:var(--mvx-blue);}
/* clear the CTA so nothing sits on top of it */
.pathcard .pathcard-caption{padding-bottom:5.4rem;}
.pathcard .reveal{padding-bottom:5.4rem;}
@media(prefers-reduced-motion:reduce){.pathcard .pcta .btn .btn-label::after{transition:none;}}

/* --- v43: consent -------------------------------------------------------- */
/* Footer legal row now carries a 4th link (CookieYes revisit). Keep each label
   intact so the row wraps between links rather than inside "Privacy Policy". */
.fbottom a{white-space:nowrap;}
.fbottom>div:first-child{display:flex;flex-wrap:wrap;gap:0 1.4rem;}
.fbottom>div:first-child a{margin-right:0;}

/* --- v44: linked stat citations -------------------------------------------
   Footnote markers on the homepage statistics link to their sources (matching
   the original site). They must not inherit ordinary link styling, which would
   put a blue underline mid-sentence on the dark band. */
sup.cite{font-size:.62em;line-height:0;vertical-align:super;margin-left:.12em;}
sup.cite a{color:inherit;text-decoration:none;opacity:.72;border-bottom:1px dotted currentColor;}
sup.cite a:hover,sup.cite a:focus-visible{opacity:1;}
sup.cite .csep{opacity:.72;}

/* --- v45: traditional journey life-expectancy bar --------------------------
   The red end-of-journey marker now cuts the Life Expectancy block while the
   gradient is still visibly blue, rather than after it has washed out to white.
   `.tail` is an invisible spacer that absorbs the width freed by shortening the
   fade, so the three solid segments keep their original proportions instead of
   growing to fill the gap. */
.jseg.fade.truncated{background:linear-gradient(90deg,#C9E8F2,#D5EDF6);}
.jseg.tail{background:none;padding:0;pointer-events:none;}

/* --- v46: journey end-marker flush against Life Expectancy -----------------
   The bar's inter-segment gap is now a custom property so the red end-marker can
   cancel exactly one gap's worth of space and butt up against the Life Expectancy
   block. Declared here (after the responsive block above) so the mobile value
   feeds the same calc rather than drifting from a second hard-coded number. */
.jbar{--journey-gap:8px;gap:var(--journey-gap);}
.jseg.end-marker{margin-left:calc(var(--journey-gap) * -1);}
@media(max-width:920px){.jbar{--journey-gap:5px;}}

/* --- v47: journey rules span their own bar ---------------------------------
   On the original diagram each rule is exactly as wide as the bar it annotates:
   the one above matches the inset traditional bar, the one below runs the full
   width of the Maverix bar and ends in an arrowhead. The 150/170px caps that
   used to size these made them text-width-driven instead. */
.journey .jnote{width:81.5%;margin-left:auto;margin-right:auto;}
.journey .jnote::before,.journey .jnote::after{max-width:none;}
.jarrow::before{max-width:none;}
/* right-hand run of the lower rule: 1px line finishing in the arrowhead */
.jarrow::after{content:"";flex:1;height:9px;font-size:0;
 background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='9' height='9'%3E%3Cpath d='M0 0l9 4.5L0 9z' fill='%233A3A3B'/%3E%3C/svg%3E") right 50%/9px 9px no-repeat,
            linear-gradient(var(--mvx-graphite),var(--mvx-graphite)) left 50%/100% 1px no-repeat;}

/* --- v48: journey-card CTA never overlaps the body copy ---------------------
   The CTA is pinned to the bottom of the card, so whatever holds the text has to
   reserve room for it. That clearance was written as a literal 5.4rem in two
   places, and the mobile open-state padding shorthand (added earlier, higher
   specificity) silently overrode it — the CTA then sat on the last line of text.
   One variable now defines the clearance and every state that needs it uses it. */
.pathcard{--pcta-clearance:5.4rem;}
.pathcard .pathcard-caption,.pathcard .reveal{padding-bottom:var(--pcta-clearance);}
@media(max-width:920px){
 .pathcard.open .reveal{padding-bottom:var(--pcta-clearance);}
}

/* --- v49: multi-column specification tables --------------------------------
   The original .spec table is a two-column key/value layout, so it pins the
   first cell to 24% and bolds it. The SKU tables added to Biopsy Forceps,
   EBUS Needles and Netis are ordinary column-labelled grids, where that rule
   makes the SKU column absurdly wide. .spec.cols keeps the dark header and the
   row rules but lets every column size to its content. */
.spec.cols th,.spec.cols td{width:1%;padding-left:.8rem;padding-right:.8rem;}
.spec.cols td{white-space:nowrap;}
.spec.cols tr td:first-child{width:1%;}
.spec.cols th:nth-child(2),.spec.cols tr td:nth-child(2){white-space:normal;width:auto;}
.spec-head{font-family:var(--font-tagline);color:var(--mvx-blue);font-size:1.5rem;
 margin-top:2.4rem;}
/* A grid item defaults to min-width:auto, so a wide table inside .pd-panel
   stretches the whole grid column instead of scrolling inside its own box —
   that pushed the entire page sideways on phones and tablets. min-width:0 lets
   the panel shrink to its track so .spec's overflow-x:auto does its job.
   (Also fixes the pre-existing 21px sideways scroll on the Hydro-Slide page.) */
.pd-wrap{min-width:0;}
.pd-panel{min-width:0;}
