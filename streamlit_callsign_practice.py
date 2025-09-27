import streamlit as st
import streamlit.components.v1 as components
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

def speak_text_browser(text):
    """Use browser's built-in speech synthesis"""
    html_code = f"""
    <script>
    if ('speechSynthesis' in window) {{
        const utterance = new SpeechSynthesisUtterance('{text}');
        utterance.rate = 0.7;
        utterance.pitch = 1;
        speechSynthesis.speak(utterance);
    }}
    </script>
    """
    components.html(html_code, height=0)

def speak_text_local(text):
    """Local text-to-speech for development"""
    if os.name == "posix":    # macOS/Linux
        os.system(f'say "{text}"')
    else:                     # Windows
        os.system(
            f'powershell -c "Add-Type -AssemblyName System.Speech; '
            f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')"'
        )

def speak_text(text):
    """Cross-platform speech function"""
    try:
        # Try browser-based speech first (works on Streamlit Cloud)
        speak_text_browser(text)
    except:
        # Fallback to local TTS for development
        speak_text_local(text)

# ---------- Streamlit UI ----------
st.title("📻 Amateur Radio Call-Sign Practice")
st.markdown("*Note: Click anywhere on the page first to enable audio*")

if "running" not in st.session_state:
    st.session_state.running = False

delay = st.slider("Seconds between call signs", 2, 10, 5)
audio_delay = st.slider("Seconds delay before audio starts", 0, 5, 2)

col1, col2 = st.columns(2)
start = col1.button("▶️ Start", type="primary")
stop  = col2.button("⏹️ Stop")

if start:
    st.session_state.running = True
if stop:
    st.session_state.running = False

placeholder = st.empty()

# Status
if st.session_state.running:
    st.success("🔊 Practice session running...")
else:
    st.info("⏸️ Practice session stopped")

# ---------- Main loop ----------
while st.session_state.running:
    cs = random_callsign()
    
    # Display the call sign first
    with placeholder.container():
        st.markdown(f"### 📡 {cs}")
        st.markdown(f"**Phonetic:** {' - '.join(phonetic[ch] for ch in cs)}")
    
    # Wait before playing audio
    time.sleep(audio_delay)
    
    # Check if still running after the delay
    if st.session_state.running:
        spoken = " ".join(phonetic[ch] for ch in cs)
        speak_text(spoken)
    
    # Wait for the remaining time
    time.sleep(delay)
