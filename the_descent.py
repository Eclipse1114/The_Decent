import random
import streamlit as st

# ---------------------------------------------------------
# STREAMLIT PAGE CONFIG & CUSTOM STYLING
# ---------------------------------------------------------
st.set_page_config(
    page_title="The Descent",
    page_icon="🕯️",
    layout="centered"
)

# Custom CSS for dark/eerie aesthetics
st.markdown("""
    <style>
    .stApp {
        background-color: #0F0F12;
        color: #DCDCDC;
    }
    .story-card {
        background-color: #1C1C23;
        border: 2px solid #B43232;
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 24px;
    }
    h1, h2, h3 {
        color: #B43232 !important;
        font-family: 'Georgia', serif;
    }
    p, div {
        font-family: 'Georgia', serif;
        font-size: 18px;
    }
    /* Button custom styling */
    div.stButton > button {
        background-color: #282A36;
        color: #FFFFFF;
        border: 1px solid #B43232;
        border-radius: 8px;
        padding: 12px 20px;
        font-size: 16px;
        width: 100%;
        transition: all 0.2s ease;
    }
    div.stButton > button:hover {
        background-color: #464B5F;
        color: #FFFFFF;
        border-color: #FF4444;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SESSION STATE INITIALIZATION
# ---------------------------------------------------------
if "current_scene" not in st.session_state:
    st.session_state.current_scene = "start_game"
if "has_locket" not in st.session_state:
    st.session_state.has_locket = False
if "knows_salt_weakness" not in st.session_state:
    st.session_state.knows_salt_weakness = False
if "player_name" not in st.session_state:
    st.session_state.player_name = "Player"

def navigate_to(scene_name):
    """Callback helper to switch scenes on button clicks."""
    st.session_state.current_scene = scene_name

# ---------------------------------------------------------
# SCENE LOGIC & RENDERING
# ---------------------------------------------------------
scene = st.session_state.current_scene

st.title("🕯️ THE DESCENT")

# 1. START GAME
if scene == "start_game":
    st.session_state.has_locket = False
    st.session_state.knows_salt_weakness = False

    st.markdown("""
        <div class="story-card">
            <p>It's been a full year since anyone in the family heard from Grandpa.</p>
            <p>Today though, he invited me over, so of course I came out of pure goodwill.</p>
            <p>The house looks older than I remember. Darker.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(1)[0], None, None
    st.button("1. Knock on the door", on_click=navigate_to, args=("door_click",))
    st.button("2. Try the doorknob", on_click=navigate_to, args=("door_click",))
    st.button("3. Hesitate on the porch", on_click=navigate_to, args=("death_porch",))

# 2. DOOR CLICK
elif scene == "door_click":
    st.markdown(f"""
        <div class="story-card">
            <p>Before I can make a sound, the door clicks and swings inward.</p>
            <p>Grandpa stands in the dim hallway, smiling. His eyes are bloodshot.</p>
            <p><em>'Oh, it's you. What's your name again?'</em> he asks.</p>
            <p><em>'It's {st.session_state.player_name}, Grandpa.'</em> You say. The family was right—he's gone senile.</p>
        </div>
    """, unsafe_allow_html=True)

    st.button("Continue into the living room", on_click=navigate_to, args=("living_room",))

# 3. LIVING ROOM
elif scene == "living_room":
    st.markdown("""
        <div class="story-card">
            <p>Grandpa shuffles off into the kitchen to make tea, leaving me alone.</p>
            <p>The house smells like old paper and copper. I have a terrible feeling in my stomach.</p>
        </div>
    """, unsafe_allow_html=True)

    st.button("1. Explore the hallway", on_click=navigate_to, args=("explore_hallway",))
    st.button("2. Sit on the couch and wait", on_click=navigate_to, args=("forced_basement",))
    st.button("3. Go upstairs to sleep", on_click=navigate_to, args=("dream_world",))

# 4. EXPLORE HALLWAY
elif scene == "explore_hallway":
    st.markdown("""
        <div class="story-card">
            <p>I stand in the dim hallway. Two things catch my eye.</p>
        </div>
    """, unsafe_allow_html=True)

    st.button("1. Check the ticking clock", on_click=navigate_to, args=("check_clock",))
    st.button("2. Sneak into Grandpa's bedroom", on_click=navigate_to, args=("grandpas_room",))
    st.button("3. Wander into the pitch-black closet", on_click=navigate_to, args=("death_closet",))

# 5. CHECK CLOCK
elif scene == "check_clock":
    h, m = random.randint(0, 23), random.randint(10, 59)
    st.markdown(f"""
        <div class="story-card">
            <p>The clock numbers spin wildly before stopping at <strong>{h:02d}:{m:02d}</strong>.</p>
            <p>A second later, they spin again. Time doesn't work here.</p>
            <p>Chills run down my spine. I head into Grandpa's room.</p>
        </div>
    """, unsafe_allow_html=True)

    st.button("Enter Grandpa's room", on_click=navigate_to, args=("grandpas_room",))

# 6. GRANDPA'S ROOM
elif scene == "grandpas_room":
    st.markdown("""
        <div class="story-card">
            <p>Grandpa's room is freezing. The walls are covered in carved symbols.</p>
            <p>On his nightstand sits an old brass locket and a handwritten journal.</p>
        </div>
    """, unsafe_allow_html=True)

    st.button("1. Take the locket", on_click=navigate_to, args=("take_locket",))
    st.button("2. Read the journal", on_click=navigate_to, args=("read_journal",))
    st.button("3. Take and read both", on_click=navigate_to, args=("take_both",))

# ITEM INTERACTION SCENES
elif scene == "take_locket":
    st.session_state.has_locket = True
    st.markdown("""
        <div class="story-card">
            <p>I slip the warm brass locket into my pocket. Heavy footsteps approach!</p>
        </div>
    """, unsafe_allow_html=True)
    st.button("Run back to living room", on_click=navigate_to, args=("forced_basement",))

elif scene == "read_journal":
    st.session_state.knows_salt_weakness = True
    st.markdown("""
        <div class="story-card">
            <p>The journal describes an entity. Underlined in red: <em>'Salt stuns the beast.'</em> Heavy footsteps approach!</p>
        </div>
    """, unsafe_allow_html=True)
    st.button("Run back to living room", on_click=navigate_to, args=("forced_basement",))

elif scene == "take_both":
    st.session_state.has_locket = True
    st.session_state.knows_salt_weakness = True
    st.markdown("""
        <div class="story-card">
            <p>I grab the warm locket and read <em>'Salt stuns the beast'</em> in the journal. Heavy footsteps approach!</p>
        </div>
    """, unsafe_allow_html=True)
    st.button("Run back to living room", on_click=navigate_to, args=("forced_basement",))

# 7. FORCED BASEMENT
elif scene == "forced_basement":
    st.markdown("""
        <div class="story-card">
            <p>Grandpa returns, but he isn't carrying tea.</p>
            <p>His eyes are glassy and unblinking. He grabs my wrist with terrifying strength.</p>
            <p><em>'It is time,'</em> he chants. <em>'The blood of the lineage.'</em></p>
            <p>He drags me down into the pitch-black basement.</p>
        </div>
    """, unsafe_allow_html=True)

    st.button("Face the basement rift...", on_click=navigate_to, args=("basement_climax",))

# 8. BASEMENT CLIMAX
elif scene == "basement_climax":
    st.markdown("""
        <div class="story-card">
            <p>A tear in reality opens in the basement. Purple light spills out.</p>
            <p>A towering mass of shadows and tentacles crawls into the room.</p>
            <p>Grandpa drops to his knees praying. What do I do?!</p>
        </div>
    """, unsafe_allow_html=True)

    st.button("1. Run for the stairs", on_click=navigate_to, args=("death_stairs",))
    
    # Conditional inventory options
    if st.session_state.has_locket:
        st.button("Throw Grandpa's locket at it", on_click=navigate_to, args=("ending_locket",))
    if st.session_state.knows_salt_weakness:
        st.button("Throw rock salt from the floor", on_click=navigate_to, args=("ending_salt",))
        
    st.button("Freeze in panic", on_click=navigate_to, args=("death_freeze",))

# DREAM WORLD PATH
elif scene == "dream_world":
    st.markdown("""
        <div class="story-card">
            <p>I collapse into sleep and wake up in a shifting landscape of black sand.</p>
        </div>
    """, unsafe_allow_html=True)
    st.button("1. Try to find an exit", on_click=navigate_to, args=("dream_exit",))
    st.button("2. Accept your fate", on_click=navigate_to, args=("death_sand",))

elif scene == "dream_exit":
    st.markdown("""
        <div class="story-card">
            <p>I sink knee-deep into the sand near a distant platform.</p>
        </div>
    """, unsafe_allow_html=True)
    st.button("1. Climb onto platform", on_click=navigate_to, args=("dream_porch",))
    st.button("2. Walk to tree", on_click=navigate_to, args=("death_sand",))

elif scene == "dream_porch":
    st.markdown("""
        <div class="story-card">
            <p>I wake up outside on Grandpa's freezing porch. The doorknob is gone—a solid wall blocks the entryway.</p>
        </div>
    """, unsafe_allow_html=True)
    st.button("1. Walk down the dark road", on_click=navigate_to, args=("ending_road",))

# ---------------------------------------------------------
# ENDINGS & DEATH SCENES
# ---------------------------------------------------------
elif scene in ["death_porch", "death_closet", "death_stairs", "death_freeze", "death_sand"]:
    death_messages = {
        "death_porch": "Strange shadows pulled me off the steps before I could move.",
        "death_closet": "I walked into a closet and the door locked behind me forever.",
        "death_stairs": "Tentacles lashed out, dragging me backward into the void.",
        "death_freeze": "The entity consumed the room, and everything went black.",
        "death_sand": "Hands reached up from the black sand and dragged you below."
    }
    st.error(f"**GAME OVER:** {death_messages[scene]}")
    st.button("Restart", on_click=navigate_to, args=("start_game",))

elif scene in ["ending_locket", "ending_salt", "ending_road"]:
    ending_messages = {
        "ending_locket": ("ENDING: Solo Survivor", "The entity was hypnotized by the locket. You escaped, but leaving Grandpa behind will haunt you forever."),
        "ending_salt": ("ENDING: Heroes Escape", "The salt dissolved the shadow mass! Grandpa regained sanity and you both escaped safely!"),
        "ending_road": ("ENDING: The Road Alone", "You sprint down the dark road, leaving your past and home behind forever.")
    }
    title, desc = ending_messages[scene]
    st.balloons()
    st.success(f"**{title}**\n\n{desc}")
    st.button("Play Again", on_click=navigate_to, args=("start_game",))
