import base64
IMG = "data:image/png;base64," + base64.b64encode(
    open('/Users/mackflavelle/games/ringer/levels/spotted_title.png','rb').read()).decode()

COMMON = """
  *{margin:0;padding:0;box-sizing:border-box}
  .banner{position:relative;overflow:hidden;font-family:"Helvetica Neue",Arial,system-ui,sans-serif}
  .bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
  .reticle{position:absolute;transform:translate(-50%,-50%);border:3px solid rgba(255,214,120,.95);
    border-radius:50%;box-shadow:0 0 0 2px rgba(0,0,0,.35),0 0 34px rgba(255,206,92,.55)}
  .reticle::before,.reticle::after{content:"";position:absolute;left:50%;width:2px;height:20px;
    background:rgba(255,214,120,.95);transform:translateX(-50%)}
  .reticle::before{top:-16px}.reticle::after{bottom:-16px}
  .tick{position:absolute;top:50%;width:20px;height:2px;background:rgba(255,214,120,.95);transform:translateY(-50%)}
  .tick.l{left:-16px}.tick.r{right:-16px}
  .word{font-weight:900;color:#fff;line-height:.92;
    text-shadow:0 0 46px rgba(255,204,96,.55),0 3px 18px rgba(0,0,0,.7)}
  .tag{font-weight:700;color:#ffd67a;text-shadow:0 2px 12px rgba(0,0,0,.8)}
  .hook{color:#e7f1ee;font-weight:600;line-height:1.3;text-shadow:0 2px 12px rgba(0,0,0,.9)}
  .hook b{color:#fff}
  .cta{background:#ffcf5c;color:#0f1f1c;font-weight:900;white-space:nowrap;border-radius:999px;
    box-shadow:0 10px 34px rgba(255,200,90,.4)}
"""

def page(w,h,css,body):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
    html,body{{width:{w}px;height:{h}px;overflow:hidden;background:#08110f}}
    .banner{{width:{w}px;height:{h}px}}{COMMON}{css}
    </style></head><body><div class="banner"><img class="bg" src="{IMG}">{body}</div></body></html>"""

# ---- 16:9 (1280x720) ----
wide_css = """
  .bg{object-position:50% 46%}
  .top-scrim{position:absolute;top:0;left:0;right:0;height:300px;background:linear-gradient(180deg,rgba(6,17,15,.92),rgba(6,17,15,.5) 55%,rgba(6,17,15,0))}
  .bot-scrim{position:absolute;bottom:0;left:0;right:0;height:340px;background:linear-gradient(0deg,rgba(6,17,15,.95),rgba(6,17,15,.55) 45%,rgba(6,17,15,0))}
  .reticle{left:45.5%;top:46.5%;width:150px;height:150px}
  .top{position:absolute;top:0;left:0;right:0;padding:44px 60px}
  .word{font-size:104px;letter-spacing:-3px}
  .tag{margin-top:10px;font-size:32px}
  .bottom{position:absolute;bottom:0;left:0;right:0;padding:0 60px 46px;display:flex;justify-content:space-between;align-items:flex-end;gap:24px}
  .hook{max-width:560px;font-size:25px}
  .cta{flex:none;font-size:26px;padding:18px 34px}
"""
wide_body = """<div class="top-scrim"></div><div class="bot-scrim"></div>
  <div class="reticle"><span class="tick l"></span><span class="tick r"></span></div>
  <div class="top"><div class="word">SPOTTED</div><div class="tag">Find the one in the crowd.</div></div>
  <div class="bottom"><div class="hook">Hundreds of faces. <b>One is the match.</b> You've got 20 seconds.</div>
  <div class="cta">▶ Play free on Telegram</div></div>"""
open('banner-16x9.html','w').write(page(1280,720,wide_css,wide_body))

# ---- 1:1 (1080x1080) ----
sq_css = """
  .bg{object-position:50% 44%}
  .top-scrim{position:absolute;top:0;left:0;right:0;height:360px;background:linear-gradient(180deg,rgba(6,17,15,.94),rgba(6,17,15,.5) 60%,rgba(6,17,15,0))}
  .bot-scrim{position:absolute;bottom:0;left:0;right:0;height:440px;background:linear-gradient(0deg,rgba(6,17,15,.96),rgba(6,17,15,.6) 50%,rgba(6,17,15,0))}
  .reticle{left:50%;top:45%;width:170px;height:170px}
  .top{position:absolute;top:0;left:0;right:0;padding:56px 60px;text-align:center}
  .word{font-size:120px;letter-spacing:-3px}
  .tag{margin-top:12px;font-size:38px}
  .bottom{position:absolute;bottom:0;left:0;right:0;padding:0 60px 60px;display:flex;flex-direction:column;align-items:center;gap:26px;text-align:center}
  .hook{max-width:840px;font-size:32px}
  .cta{font-size:34px;padding:22px 46px}
"""
sq_body = """<div class="top-scrim"></div><div class="bot-scrim"></div>
  <div class="reticle"><span class="tick l"></span><span class="tick r"></span></div>
  <div class="top"><div class="word">SPOTTED</div><div class="tag">Find the one in the crowd.</div></div>
  <div class="bottom"><div class="hook">Hundreds of faces. <b>One is the match.</b><br>You've got 20 seconds.</div>
  <div class="cta">▶ Play free on Telegram</div></div>"""
open('banner-1x1.html','w').write(page(1080,1080,sq_css,sq_body))
print("built banner-16x9.html + banner-1x1.html")
