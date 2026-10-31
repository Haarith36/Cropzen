import streamlit as st
import pandas as pd
from datetime import datetime, date

st.set_page_config(page_title="CROPZEN | Plant Care", page_icon="🌿", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');
.stApp{color:#effff4;font-family:'DM Sans',sans-serif;background:radial-gradient(ellipse at 12% 10%,rgba(32,135,74,.32),transparent 38%),radial-gradient(ellipse at 88% 78%,rgba(24,102,58,.28),transparent 40%),linear-gradient(135deg,#06140f 0%,#0a281b 48%,#071910 100%);background-attachment:fixed}
[data-testid="stHeader"]{background:rgba(3,16,10,.58)}
.block-container{padding-top:1.5rem;padding-bottom:3rem;max-width:1450px}
h1,h2,h3{font-family:'Manrope',sans-serif!important;color:#f3fff7!important}
p,label,li,.stMarkdown,[data-testid="stCaptionContainer"]{color:#e4f5e9}
section[data-testid="stSidebar"]{min-width:300px;width:300px;background:linear-gradient(180deg,rgba(4,25,16,.98),rgba(8,45,27,.97));border-right:1px solid rgba(101,230,160,.35)}
section[data-testid="stSidebar"]>div{width:300px}
section[data-testid="stSidebar"] *{color:#effff4}
.brand{font-family:'Manrope',sans-serif;font-size:2rem;font-weight:800;color:#65e6a0;letter-spacing:.04em}
.hero{background:linear-gradient(115deg,rgba(4,23,15,.94),rgba(15,82,45,.88),rgba(27,112,61,.82));padding:30px 34px;border-radius:22px;margin-bottom:22px;border:1px solid rgba(116,242,165,.32);box-shadow:0 18px 50px rgba(0,0,0,.22)}
.hero h1{font-size:2.45rem!important;margin:0 0 8px}
.hero p{color:#d9f7e3!important;margin:0}
.eyebrow{color:#7cf0aa;text-transform:uppercase;letter-spacing:.15em;font-weight:800;font-size:.75rem;margin-bottom:9px}
.panel{background:linear-gradient(145deg,rgba(9,43,27,.92),rgba(5,26,17,.88));border:1px solid rgba(137,232,168,.27);border-radius:17px;padding:19px;box-shadow:0 12px 34px rgba(0,0,0,.18)}
div[data-testid="stMetric"]{background:rgba(7,37,23,.88);border:1px solid rgba(137,232,168,.27);padding:16px;border-radius:15px}
div[data-testid="stMetricLabel"],div[data-testid="stMetricLabel"] *{color:#c7e8d1!important}
div[data-testid="stMetricValue"]{color:#75efaa!important;font-family:'Manrope',sans-serif}
.stButton>button,.stDownloadButton>button{border-radius:10px;font-weight:800;min-height:2.7rem;border:1px solid #65e6a0;color:#06170e;background:#65e6a0}
div[data-baseweb="select"]>div,div[data-baseweb="input"]>div,.stTextInput input,.stTextArea textarea,.stDateInput input{background:#f8fff9!important;color:#10251a!important;border-radius:9px!important}
.stTextInput label,.stSelectbox label,.stMultiSelect label,.stDateInput label,.stFileUploader label,.stTextArea label{color:#f1fff6!important;font-weight:700!important}
[data-testid="stFileUploader"]{background:rgba(4,25,16,.58);border:1px dashed rgba(130,236,166,.45);border-radius:13px;padding:9px}
hr{border-color:rgba(171,238,195,.24)}
footer{visibility:hidden}
</style>
""", unsafe_allow_html=True)

if "activity_log" not in st.session_state:
    st.session_state.activity_log = []
if "last_check" not in st.session_state:
    st.session_state.last_check = None

def add_activity(plant, issue):
    now = datetime.now()
    st.session_state.activity_log.insert(0, {
        "Date": now.strftime("%d %b %Y"),
        "Time": now.strftime("%I:%M:%S %p"),
        "Plant": plant,
        "Problem": issue,
    })
    st.session_state.activity_log = st.session_state.activity_log[:50]

with st.sidebar:
    st.markdown('<div style="font-size:2.4rem">🌿</div><div class="brand">CROPZEN</div><div style="color:#b7d8c2">PLANT CARE MADE SIMPLE</div>', unsafe_allow_html=True)
    st.markdown("---")
    page = st.radio("MAIN MENU", ["Dashboard", "Plant Problem Checker", "History"])
    st.markdown("---")
    st.caption("A simple plant-care helper for home gardeners and everyday plant owners.")
    st.caption("Guidance is general. A photo is saved for reference but is not automatically diagnosed.")

if page == "Dashboard":
    st.markdown('<div class="hero"><div class="eyebrow">WELCOME TO CROPZEN</div><h1>Keep your plants happy and healthy.</h1><p>Record a plant problem, get a structured care plan, and keep track of your checks.</p></div>', unsafe_allow_html=True)
    latest = st.session_state.activity_log[0] if st.session_state.activity_log else None
    c1,c2,c3 = st.columns(3)
    c1.metric("Plant checks saved", len(st.session_state.activity_log))
    c2.metric("Last plant checked", latest["Plant"] if latest else "—")
    c3.metric("Today", date.today().strftime("%d %b %Y"))
    st.markdown("### How to use CROPZEN")
    a,b,c = st.columns(3)
    with a:
        st.markdown('<div class="panel"><h3>01 · Describe</h3><p>Enter your plant name and choose the problem you can see.</p></div>', unsafe_allow_html=True)
    with b:
        st.markdown('<div class="panel"><h3>02 · Get care tips</h3><p>Get possible causes to investigate and practical care steps.</p></div>', unsafe_allow_html=True)
    with c:
        st.markdown('<div class="panel"><h3>03 · Track</h3><p>Save your checks and review them later in your history.</p></div>', unsafe_allow_html=True)
    st.info("Tip: Check the soil with your finger before watering. The top layer being dry does not always mean the whole pot is dry.")
    st.caption("CROPZEN is an educational plant-care helper. It does not identify diseases from images or replace advice from a qualified gardening or plant-health expert.")

elif page == "Plant Problem Checker":
    st.markdown('<div class="hero"><div class="eyebrow">PLANT CARE / QUICK CHECK</div><h1>Plant Problem Checker</h1><p>Share a few details to get practical first-step care suggestions.</p></div>', unsafe_allow_html=True)
    with st.form("plant_check_form"):
        left,right = st.columns(2)
        with left:
            plant = st.text_input("Plant name", placeholder="e.g. money plant, rose, tomato")
            category = st.selectbox("Plant type", ["Indoor plant","Outdoor plant","Flower","Vegetable","Fruit plant","Herb","Tree","Other"])
            problem = st.selectbox("What is the problem?", ["Yellow leaves","Brown or black spots","Wilting or drooping","Leaves curling","White powder or coating","Holes in leaves","Slow growth","No flowers or fruits","No obvious problem / routine care","Other / not sure"])
            affected = st.multiselect("Where do you see the problem?", ["Leaves","Stem","Roots / soil","Flowers","Fruits","Whole plant"])
        with right:
            sunlight = st.selectbox("Sunlight", ["Direct sunlight","Bright indirect light","Low light","Mostly shade","Not sure"])
            watering = st.selectbox("Watering routine", ["Daily","Every 2–3 days","About once a week","Only when soil feels dry","Irregular","Not sure"])
            soil = st.selectbox("Soil condition", ["Drains well","Stays wet for a long time","Dries very quickly","Hard / compacted","Potting mix","Not sure"])
            noticed = st.date_input("When did you first notice it?", value=date.today(), max_value=date.today())
        photo = st.file_uploader("Add a plant photo (optional)", type=["jpg","jpeg","png","webp"])
        details = st.text_area("Anything else? (optional)", placeholder="For example: Is it getting worse? Did you recently move or repot the plant?")
        submitted = st.form_submit_button("Generate care plan and save", type="primary", use_container_width=True)

    if photo is not None:
        st.markdown("#### Photo preview")
        st.image(photo, caption=f"Reference photo: {photo.name}", use_container_width=True)

    if submitted:
        if not plant.strip():
            st.error("Please enter the plant name.")
        else:
            saved_at = datetime.now().strftime("%d %b %Y, %I:%M:%S %p")
            st.session_state.last_check = {
                "plant":plant.strip(),"category":category,"problem":problem,"affected":affected,
                "sunlight":sunlight,"watering":watering,"soil":soil,"noticed":str(noticed),
                "photo_name":photo.name if photo else "No photo uploaded",
                "details":details.strip(),"saved_at":saved_at,
            }
            add_activity(plant.strip(), problem)
            st.success("Your plant check has been saved!")

    check = st.session_state.last_check
    if check:
        st.markdown("### Your plant-care suggestions")
        x,y,z = st.columns(3)
        x.metric("Plant", check["plant"])
        y.metric("Problem selected", check["problem"])
        z.metric("First noticed", check["noticed"])
        st.warning("Photo saved for reference only: this version does not use a trained image-recognition model. The possible causes below are based on the symptoms and care details you entered, not a visual diagnosis.")

        guidance = {
            "Yellow leaves": {
                "causes": "Overwatering or poor drainage; underwatering; natural ageing of older leaves; or a light or nutrient issue.",
                "actions": ["Check moisture 2–3 cm below the soil surface before watering again.", "Make sure excess water can drain freely; empty any water collected in the saucer.", "Notice whether yellowing starts on older leaves or new growth and monitor whether it spreads."],
                "water": "Water when the upper soil begins to dry, then water thoroughly until a little drains out. Do not follow a fixed calendar if the soil is still wet.",
                "soil": "Use a loose, well-draining growing mix suited to this plant. If the soil stays wet for a long time, improve drainage and check the pot holes.",
                "nutrition": "Do not add fertiliser immediately. If growth is active and the plant has been in the same potting mix for a long time, use a balanced fertiliser at the label's lowest recommended rate.",
                "prevention": "Keep a consistent watering routine based on soil moisture, light, and season; remove only fully dead leaves."
            },
            "Brown or black spots": {
                "causes": "Possible fungal or bacterial leaf spot, water sitting on leaves, sun scorch, or physical damage. The appearance alone cannot confirm which one.",
                "actions": ["Avoid wetting the leaves; water near the soil instead.", "Keep the plant airy and avoid crowding leaves together.", "Remove fallen or fully damaged leaves with clean tools and monitor whether new spots appear.", "If spots spread quickly, isolate a potted plant and ask a local horticulture expert to inspect it."],
                "water": "Water the soil rather than the foliage. Check moisture first; do not increase watering just because spots are present.",
                "soil": "Choose a free-draining mix and a pot with drainage holes. Avoid leaving roots in standing water.",
                "nutrition": "Avoid strong fertiliser while the plant is stressed. Resume normal, plant-appropriate feeding only after growth stabilises.",
                "prevention": "Provide airflow, avoid splashing soil onto leaves, and clean tools between plants."
            },
            "Wilting or drooping": {
                "causes": "Dry soil, waterlogged roots, heat stress, transplant stress, or root damage can all cause wilting.",
                "actions": ["Feel the soil before watering: if it is dry, water slowly and thoroughly; if it is wet, do not add more water.", "Check that the pot drains and is not sitting in collected water.", "Temporarily protect the plant from harsh midday conditions while it recovers."],
                "water": "Base watering on soil moisture. A dry root zone needs a thorough drink; persistently wet soil needs better drainage and time to dry.",
                "soil": "Use an airy, well-draining mix. Compacted or waterlogged soil can reduce oxygen around roots.",
                "nutrition": "Do not fertilise a wilted or stressed plant until it has recovered.",
                "prevention": "Avoid sudden changes in watering and protect recently repotted plants from extreme heat."
            },
            "Leaves curling": {
                "causes": "Possible heat or water stress, sap-feeding insects, or a recent change in light or location.",
                "actions": ["Inspect both sides of leaves and tender shoots for small insects or sticky residue.", "Check soil moisture and note whether curling is on new leaves, old leaves, or both.", "Keep conditions steady and avoid applying pesticides until the cause is identified."],
                "water": "Keep moisture even without keeping the soil constantly soggy; adjust based on the plant and how quickly its soil dries.",
                "soil": "A loose, well-draining mix helps roots take up water properly.",
                "nutrition": "Avoid extra feeding until pests and environmental stress have been checked.",
                "prevention": "Check leaf undersides weekly and avoid abrupt changes in light or watering."
            },
            "White powder or coating": {
                "causes": "Could be powdery mildew, mineral residue, dust, or pest-related material. A closer inspection is needed to distinguish them.",
                "actions": ["Check whether the coating returns after a small area is gently wiped.", "Improve spacing and airflow around the plant.", "Avoid overhead watering and seek expert help if the coating spreads."],
                "water": "Water at soil level and avoid keeping foliage wet for long periods.",
                "soil": "Use a well-draining mix; do not keep the pot constantly damp.",
                "nutrition": "Avoid excessive fertiliser, especially high-nitrogen feeding, until the issue is understood.",
                "prevention": "Give leaves room to dry and inspect new plants before placing them near others."
            },
            "Holes in leaves": {
                "causes": "Chewing insects, caterpillars, snails or slugs, or physical damage are possible causes.",
                "actions": ["Inspect leaves, stems, and the soil surface for insects or other signs of feeding.", "Check at different times of day because some pests hide during daylight.", "Identify the pest before choosing a control method; avoid spraying unknown chemicals."],
                "water": "Continue the plant's normal moisture-based watering routine; holes do not by themselves indicate a water problem.",
                "soil": "Keep the growing area tidy and use a mix suited to the plant with good drainage.",
                "nutrition": "No extra fertiliser is needed solely because leaves have holes.",
                "prevention": "Inspect new growth regularly and remove plant debris where pests may hide."
            },
            "Slow growth": {
                "causes": "Insufficient or unsuitable light, seasonal dormancy, root crowding, poor drainage, or lack of nutrients may contribute.",
                "actions": ["Check whether the plant receives the light it normally needs.", "Check drainage and whether roots are crowded in the pot.", "Compare growth over several weeks; some plants naturally grow slowly in certain seasons."],
                "water": "Water according to soil moisture and plant type; slow growth often means the plant uses water more slowly.",
                "soil": "Use a fresh, airy, well-draining mix when repotting is genuinely needed.",
                "nutrition": "Feed only during the plant's active growing period, following the product label. More fertiliser is not always better.",
                "prevention": "Match light, pot size, and feeding to the plant's needs and season."
            },
            "No flowers or fruits": {
                "causes": "The plant may be immature, receive unsuitable light, be outside its flowering season, or have a pollination or care issue.",
                "actions": ["Check the plant's age and normal flowering season.", "Confirm it gets suitable light for its species.", "For fruiting plants, consider whether pollination is needed and whether pollinators can reach the flowers."],
                "water": "Keep watering consistent and avoid both prolonged dryness and waterlogging during flowering.",
                "soil": "Use a fertile but well-draining growing medium suitable for the plant.",
                "nutrition": "Avoid excess nitrogen, which can encourage leafy growth at the expense of flowers. Use plant-appropriate fertiliser only as directed.",
                "prevention": "Provide suitable light, seasonal care, and pollination conditions; allow the plant time to mature."
            },
        }
        result = guidance.get(check["problem"])
        if result:
            st.markdown("#### Possible causes to investigate")
            st.write(result["causes"])
            st.markdown("#### Recommended action plan")
            for item in result["actions"]:
                st.markdown(f"- {item}")
            st.markdown("#### Watering plan")
            st.write(result["water"])
            st.markdown("#### Soil requirements")
            st.write(result["soil"])
            st.markdown("#### Nutrition and fertiliser")
            st.write(result["nutrition"])
            st.markdown("#### Prevention")
            st.write(result["prevention"])
        else:
            st.markdown("#### Routine care plan")
            st.write("Observe new growth, inspect both sides of leaves, and check soil moisture before watering. Match light and soil to the plant species. Avoid adding fertiliser or treatments until a specific need is identified.")

        st.markdown("#### What to monitor next")
        st.write("Take another photo from a similar angle in 3–5 days. Compare the number of affected leaves, whether spots or curling have spread, and whether new growth looks healthy. If the plant deteriorates quickly, consult a local nursery or horticulture specialist with the photo.")
        st.markdown("#### Your care details")
        st.write(f"**Plant type:** {check['category']}  ·  **Sunlight:** {check['sunlight']}")
        st.write(f"**Watering:** {check['watering']}  ·  **Soil:** {check['soil']}")
        st.write(f"**Affected parts:** {', '.join(check['affected']) if check['affected'] else 'Not specified'}")
        st.write(f"**Photo:** {check['photo_name']}")
        if check["details"]:
            st.write(f"**Extra details:** {check['details']}")
        st.caption(f"Saved on {check['saved_at']}")
        report = "\n".join([
            "CROPZEN — PLANT CARE CHECK",
            f"Plant: {check['plant']}",
            f"Plant type: {check['category']}",
            f"Problem selected: {check['problem']}",
            f"Affected parts: {', '.join(check['affected']) if check['affected'] else 'Not specified'}",
            f"Sunlight: {check['sunlight']}",
            f"Watering: {check['watering']}",
            f"Soil: {check['soil']}",
            f"First noticed: {check['noticed']}",
            f"Photo: {check['photo_name']}",
            f"Extra details: {check['details'] or 'None'}",
            f"Saved: {check['saved_at']}",
            "",
            "Note: General educational guidance only. This is not a confirmed diagnosis."
        ])
        st.download_button("Download plant-care report", report, "CROPZEN_Plant_Care_Report.txt", "text/plain")

else:
    st.markdown('<div class="hero"><div class="eyebrow">CROPZEN / YOUR RECORDS</div><h1>History</h1><p>See the plant checks you have saved during this app session.</p></div>', unsafe_allow_html=True)
    if st.session_state.activity_log:
        history = pd.DataFrame(st.session_state.activity_log)
        st.dataframe(history, use_container_width=True, hide_index=True)
        st.download_button("Export history as CSV", history.to_csv(index=False).encode("utf-8"), "CROPZEN_History.csv", "text/csv")
        if st.session_state.last_check:
            check = st.session_state.last_check
            st.markdown("### Latest saved check")
            st.write(f"**Plant:** {check['plant']}  ·  **Problem:** {check['problem']}")
            st.write(f"**Sunlight:** {check['sunlight']}  ·  **Watering:** {check['watering']}  ·  **Soil:** {check['soil']}")
    else:
        st.markdown('<div class="panel"><h3>No checks saved yet</h3><p>Open Plant Problem Checker, enter a plant name, and save your first check. It will appear here.</p></div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown('<p style="text-align:center;color:#b8d8c3;font-size:.82rem">CROPZEN • Simple Plant Care • Educational prototype</p>', unsafe_allow_html=True)
