import streamlit as st
import random, time, os

# ---------- ITU phonetic alphabet ----------
phonetic = {
    "A":"Alpha","B":"Bravo","C":"Charlie","D":"Delta","E":"Echo",
    "F":"Foxtrot","G":"Golf","H":"Hotel","I":"India","J":"Juliett",
    "K":"Kilo","L":"Lima","M":"Mike","N":"November","O":"Oscar",
    "P":"Papa","Q":"Quebec","R":"Romeo","S":"Sierra","T":"Tango",
    "U":"Uniform","V":"Victor","W":"Whiskey","X":"X-ray","Y":"Yankee","Z":"Zulu",
    "0":"Zero","1":"One","2":"Two","3":"Three","4":"Four",
    "5":"Five","6":"Six","7":"Seven","8":"Eight","9":"Nine"
}

prefixes = ["K","N","W","AA","AB","AC","AD","AE"]
letters  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def random_callsign():
    prefix = random.choice(prefixes)
    digit  = str(random.randint(0,9))
    suffix = "".join(random.choices(letters, k=random.choice([2,3])))
    return prefix + digit + suffix

# ---------- Streamlit UI ----------
st.title("Amateur Radio Call-Sign Practice")

if "running" not in st.session_state:
    st.session_state.running = False

delay = st.slider("Seconds between call signs", 2, 10, 5)

col1, col2 = st.columns(2)
start = col1.button("Start")
stop  = col2.button("Stop")

if start:
    st.session_state.running = True
if stop:
    st.session_state.running = False

placeholder = st.empty()

# ---------- Main loop ----------
while st.session_state.running:
    cs = random_callsign()
    placeholder.markdown(f"### {cs}")
    spoken = " ".join(phonetic[ch] for ch in cs)

    # Speak the call sign
    if os.name == "posix":    # macOS/Linux
        os.system(f'say "{spoken}"')
    else:                     # Windows
        os.system(
            f'powershell -c "Add-Type –AssemblyName System.Speech; '
            f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{spoken}\')"'
        )
    time.sleep(delay)

