import streamlit as st
import streamlit.components.v1 as components
import html

st.set_page_config(
    page_title="THE LAST COMMIT | 12А",
    page_icon="💜",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------
# THE LAST COMMIT | 12А
# Един файл: Python + вграден HTML/CSS
# Можеш да сменяш загадките и кодовете в списъка MISSIONS.
# ---------------------------------------------------------

MISSIONS = [
    {
        "level": "LEVEL 01",
        "place": "При Борка / охраната",
        "title": "Първата следа",
        "riddle": """
        Всяка голяма мисия започва с човек, който знае
        кой влиза, кой излиза и кой пак е закъснял.
        Потърси мястото, където редът в училище има
        своето най-бдително око.
        """,
        "hint": "Помисли за човека, който посреща всички на входа.",
        "code": "BORKA",
        "success": "Добре дошла в мисията. Досега никой не е успял да избяга от погледа на Борка.",
    },
    {
        "level": "LEVEL 02",
        "place": "Мостът на Кольо Фичето",
        "title": "Майсторът на мостовете",
        "riddle": """
        Следващата спирка е дело на човек, който е свързвал
        брегове, а не хора в общ чат.
        Там, където конструкцията говори повече от думите,
        те чака следващата следа.
        """,
        "hint": "Търси известния мост, свързан с името на Кольо Фичето.",
        "code": "MOST",
        "success": "Премина успешно. Поне този мост издържа на напрежението в 12А.",
    },
    {
        "level": "LEVEL 03",
        "place": "Стадион „Локомотив“",
        "title": "На стартова позиция",
        "riddle": """
        Тук има терен, голове и хора, които понякога тичат
        повече, отколкото в час по физическо.
        Следващата следа е на място, където се играе
        за победа, а не за срочна оценка.
        """,
        "hint": "Името му звучи като транспорт, но тук не се качваш на влак.",
        "code": "LOKOMOTIV",
        "success": "Гол! Продължаваме, преди някой да поиска VAR за отговора.",
    },
    {
        "level": "LEVEL 04",
        "place": "Пощата",
        "title": "Съобщение за получателя",
        "riddle": """
        Следващата следа не идва в Messenger,
        няма синя отметка и няма нужда от интернет.
        Потърси мястото, през което минават писма,
        пратки и понякога новини, които всички вече знаят.
        """,
        "hint": "Там се изпращат писма и се получават пратки.",
        "code": "POSHTA",
        "success": "Съобщението е доставено. Няма върната пратка — продължавай!",
    },
    {
        "level": "LEVEL 05",
        "place": "Аптеката на Милка",
        "title": "Лекарство за любопитство",
        "riddle": """
        След толкова загадки май вече ти трябва нещо успокоително.
        Потърси мястото, където Милка може да ти предложи
        нещо за нервите, а червената коса се помни по-лесно
        от всяка рецепта.
        Само не се опитвай да лекуваш любопитството — то е неизлечимо.
        """,
        "hint": "Името на човека е Милка. Спомни си и за ментата и валерианата.",
        "code": "MILKA",
        "success": "Диагнозата е ясна: тежък случай на любопитство. Лечението продължава!",
    },
    {
        "level": "LEVEL 06",
        "place": "Opel Corsa на Криса",
        "title": "Паркинг легенда",
        "riddle": """
        Време е за автомобилна спирка.
        Намери колата на Криса — малка, но с голямо присъствие.
        Има само един проблем: заключването явно е
        допълнителна екстра, която още не е активирана.
        Така че не се чуди, ако колата ти се струва гостоприемна.
        Следата е при нея!
        """,
        "hint": "Търсиш Opel Corsa-та на Криса. Да, онази, която не може да се заключва.",
        "code": "CORSA",
        "success": "Отключи следващото ниво. За разлика от колата на Криса — тази мисия поне има заключване!",
    },
    {
        "level": "FINAL LEVEL",
        "place": "Дворът на училището",
        "title": "Последният commit",
        "riddle": """
        Стигна почти до края. Всички следи, кодове и закачки
        те доведоха обратно там, откъдето започва всичко.
        Потърси мястото, където 12А оставя ежедневните си
        приключения зад гърба си.
        Този път няма звънец, няма контролно и няма поправка.
        В двора те чака нещо специално — от целия клас,
        с много обич и една голяма покана.
        """,
        "hint": "Върни се в училищния двор. Там те очаква голямата изненада.",
        "code": "12A",
        "success": "Последната следа е намерена. Време е за голямата изненада!",
    },
]

def normalize(value: str) -> str:
    return "".join(value.upper().strip().split())

if "unlocked" not in st.session_state:
    st.session_state.unlocked = 0
if "started" not in st.session_state:
    st.session_state.started = False
if "show_hint" not in st.session_state:
    st.session_state.show_hint = False
if "wrong" not in st.session_state:
    st.session_state.wrong = False

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap');
:root { color-scheme: dark; }
.stApp {
    background:
      radial-gradient(ellipse at 12% 5%, rgba(150,75,255,.24), transparent 34%),
      radial-gradient(ellipse at 90% 25%, rgba(91,42,160,.22), transparent 32%),
      linear-gradient(145deg, #100b1d 0%, #171027 48%, #0d0a17 100%);
    color: #f7f1ff;
    font-family: 'DM Sans', sans-serif;
}
.block-container { max-width: 760px; padding-top: 2.1rem; padding-bottom: 4rem; }
header, footer, #MainMenu { visibility: hidden; }
.hero {
    text-align:center; padding: 2rem 1.2rem 1.6rem;
    border: 1px solid rgba(205,164,255,.24);
    border-radius: 28px;
    background: linear-gradient(145deg, rgba(91,49,145,.30), rgba(35,22,54,.58));
    box-shadow: 0 18px 70px rgba(0,0,0,.25), inset 0 1px rgba(255,255,255,.08);
}
.kicker { color:#c9a4ff; letter-spacing:.28em; font-size:.72rem; font-weight:800; }
.hero h1 {
    font-family:'Space Grotesk',sans-serif; font-size:clamp(2.1rem,7vw,3.8rem);
    line-height:1.02; margin:.65rem 0 .35rem; color:#fff;
}
.hero h1 span { color:#c99cff; }
.subtitle { color:#c9bfd8; font-size:.98rem; }
.pill {
    display:inline-block; margin-top:1rem; padding:.45rem .9rem;
    border-radius:999px; border:1px solid rgba(205,164,255,.3);
    color:#e5d3ff; background:rgba(173,111,255,.12); font-size:.78rem;
}
.panel {
    margin-top:1.25rem; padding:1.35rem;
    border:1px solid rgba(205,164,255,.20); border-radius:22px;
    background:rgba(28,19,43,.78);
    box-shadow:0 12px 40px rgba(0,0,0,.18);
}
.level { color:#c99cff; font-size:.72rem; letter-spacing:.22em; font-weight:800; }
.place { color:#fff; font-family:'Space Grotesk',sans-serif; font-size:1.55rem; font-weight:700; margin:.35rem 0 .2rem; }
.riddle { color:#ded4e9; line-height:1.8; white-space:pre-line; font-size:1rem; }
.small { color:#a99bb9; font-size:.82rem; }
.success {
    padding: .9rem 1rem; border-radius:14px; background:rgba(127,76,190,.18);
    border:1px solid rgba(194,151,255,.28); color:#eadcff; margin-top:.8rem;
}
.stTextInput label { color:#d9c7ef !important; font-weight:700 !important; }
.stTextInput input {
    background:#21172f !important; color:white !important;
    border:1px solid #684b88 !important; border-radius:13px !important;
}
.stButton button {
    border-radius:13px !important; border:1px solid #a875e5 !important;
    background:linear-gradient(100deg,#8950c7,#6536a0) !important;
    color:white !important; font-weight:800 !important; min-height:3rem;
    box-shadow:0 8px 22px rgba(111,57,170,.25);
}
.stButton button:hover { border-color:#e0c2ff !important; transform:translateY(-1px); }
hr { border-color:rgba(205,164,255,.16); }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <div class="kicker">12А • SYSTEM PROGRAMMING</div>
  <h1>THE LAST <span>COMMIT</span></h1>
  <div class="subtitle">Една мисия. Седем нива. Една незабравима покана.</div>
  <div class="pill">✦ ACCESS GRANTED: CLASS 12A ✦</div>
</div>
""", unsafe_allow_html=True)

if not st.session_state.started:
    st.markdown("""
    <div class="panel">
      <div class="level">MISSION BRIEFING</div>
      <div class="place">Готова ли си за последния commit?</div>
      <p class="riddle">Това не е обикновен учебен ден. Няма домашно, няма тест и няма нужда да търсиш правилния отговор в учебника.
      Пред теб има поредица от следи. Всяка вярна парола отключва следващото ниво.
      Следвай загадките внимателно — финалът си заслужава.</p>
      <p class="small">Съвет: въвеждай кодовете с латински букви, когато е необходимо.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("▶ ЗАПОЧНИ МИСИЯТА", use_container_width=True):
        st.session_state.started = True
        st.rerun()
else:
    current = st.session_state.unlocked

    if current >= len(MISSIONS):
        st.markdown("""
        <div class="panel" style="text-align:center;padding:2.2rem 1.4rem;">
          <div class="level">MISSION COMPLETE</div>
          <div style="font-size:3rem;margin:.6rem 0;">💜🎓✨</div>
          <div class="place" style="font-size:2rem;">THE LAST COMMIT</div>
          <h2 style="color:#d7b5ff;">12А ви кани на бала!</h2>
          <p class="riddle">Успяхте да преминете през всички нива.<br>
          Благодарим Ви за търпението, подкрепата и всички спомени.<br>
          Това е нашият последен commit като клас —<br>
          но не и последният ни общ спомен.</p>
          <div class="pill">WITH LOVE • CLASS 12A</div>
        </div>
        """, unsafe_allow_html=True)
        st.balloons()
    else:
        mission = MISSIONS[current]
        st.markdown(f"""
        <div class="panel">
          <div class="level">{html.escape(mission['level'])} &nbsp; / &nbsp; {current+1:02d} OF {len(MISSIONS):02d}</div>
          <div class="place">{html.escape(mission['title'])}</div>
          <div class="small">DESTINATION: {html.escape(mission['place'])}</div>
          <hr>
          <div class="riddle">{html.escape(mission['riddle'].strip())}</div>
        </div>
        """, unsafe_allow_html=True)

        st.progress((current) / len(MISSIONS), text=f"Прогрес на мисията: {current} / {len(MISSIONS)}")

        with st.form(key=f"answer_form_{current}"):
            answer = st.text_input("ВЪВЕДИ КОДА ЗА СЛЕДВАЩОТО НИВО", placeholder="Твоята парола...")
            submitted = st.form_submit_button("UNLOCK NEXT LEVEL", use_container_width=True)
        if submitted:
            if normalize(answer) == normalize(mission["code"]):
                st.session_state.unlocked += 1
                st.session_state.wrong = False
                st.session_state.show_hint = False
                st.session_state["last_success"] = mission["success"]
                st.rerun()
            else:
                st.session_state.wrong = True

        if st.session_state.wrong:
            st.error("ACCESS DENIED. Това не е правилният код. Опитай отново!")
        if st.session_state.get("last_success") and st.session_state.unlocked == current:
            st.markdown(f"<div class='success'>✓ {html.escape(st.session_state.last_success)}</div>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("💡 ПОКАЖИ ПОДСКАЗКА", use_container_width=True):
                st.session_state.show_hint = not st.session_state.show_hint
        with col2:
            st.markdown(f"<div style='text-align:right;padding-top:1rem;color:#a99bb9;font-size:.8rem;'>LEVEL {current+1} / {len(MISSIONS)}</div>", unsafe_allow_html=True)

        if st.session_state.show_hint:
            st.info(mission["hint"])

st.markdown("<hr><div style='text-align:center;color:#8f819f;font-size:.75rem;letter-spacing:.12em;'>BUILT WITH ♥ BY 12А • THE LAST COMMIT</div>", unsafe_allow_html=True)
