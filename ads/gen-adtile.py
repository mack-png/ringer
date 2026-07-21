import base64
IMG = "data:image/png;base64," + base64.b64encode(
    open('/Users/mackflavelle/games/ringer/levels/spotted_title.png','rb').read()).decode()
html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1024px;height:1024px;overflow:hidden;background:#08110f}}
.b{{position:relative;width:1024px;height:1024px;overflow:hidden;font-family:"Helvetica Neue",Arial,sans-serif}}
.bg{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 45%}}
.scrim{{position:absolute;top:0;left:0;right:0;height:420px;background:linear-gradient(180deg,rgba(6,17,15,.95),rgba(6,17,15,.45) 62%,rgba(6,17,15,0))}}
.vig{{position:absolute;inset:0;box-shadow:inset 0 0 180px 40px rgba(6,17,15,.7)}}
.ret{{position:absolute;left:50%;top:45%;width:168px;height:168px;transform:translate(-50%,-50%);
  border:3px solid rgba(255,214,120,.95);border-radius:50%;box-shadow:0 0 0 2px rgba(0,0,0,.35),0 0 34px rgba(255,206,92,.55)}}
.ret::before,.ret::after{{content:"";position:absolute;left:50%;width:2px;height:22px;background:rgba(255,214,120,.95);transform:translateX(-50%)}}
.ret::before{{top:-18px}}.ret::after{{bottom:-18px}}
.tk{{position:absolute;top:50%;width:22px;height:2px;background:rgba(255,214,120,.95);transform:translateY(-50%)}}
.tk.l{{left:-18px}}.tk.r{{right:-18px}}
.top{{position:absolute;top:0;left:0;right:0;padding:70px 60px;text-align:center}}
.w{{font-size:132px;font-weight:900;letter-spacing:-3px;color:#fff;line-height:.92;text-shadow:0 0 48px rgba(255,204,96,.6),0 3px 18px rgba(0,0,0,.7)}}
.t{{margin-top:14px;font-size:42px;font-weight:700;color:#ffd67a;text-shadow:0 2px 12px rgba(0,0,0,.85)}}
</style></head><body><div class="b">
  <img class="bg" src="{IMG}"><div class="scrim"></div><div class="vig"></div>
  <div class="ret"><span class="tk l"></span><span class="tk r"></span></div>
  <div class="top"><div class="w">SPOTTED</div><div class="t">Find the one in the crowd.</div></div>
</div></body></html>"""
open('adtile.html','w').write(html)
print("adtile.html built")
