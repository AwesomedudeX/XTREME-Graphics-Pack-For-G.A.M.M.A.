import streamlit as st
from io import StringIO

st.set_page_config(layout="wide", initial_sidebar_state="expanded")

page = st.sidebar.radio("**Navigation:**", ["Home", "Modlist Compatibility", "Load Atmospheric Preset"])
atmospreset = """
r__color_grading (0.35, 0.5, 0.6)

r__detail_density 0.34
r__detail_height 0.9
r__detail_radius 150
r__dtex_range 50.
r__enable_grass_shadow off

r__saturation 1.1
r__gamma 0.9
r__exposure 1
scope_factor 1

r2_sun_lumscale 3.
r2_gloss_factor 0.001
r2_gloss_min 0.56
r2_sun_lumscale_amb 1.05
r2_sun_lumscale_hemi 1.41
r2_tonemap_lowlum 0.55
r2_tonemap on
r2_tonemap_adaptation 3.0
r2_tonemap_amount 1
r2_tonemap_middlegray 1.4
rs_c_brightness 0.985
rs_c_contrast 0.92
rs_c_gamma 1.
r2_sun_depth_near_scale 0.9998
r2_sun_depth_far_scale 0.99988
ssfx_hud_hemi 0.3

shader_param_1 (1.000000, 1.000000, 1.000000, 0.100000)
shader_param_2 (0.000000, 0.000000, 0.000000, 0.000000)
shader_param_3 (0.838000, 0.847000, 0.852000, -0.005000)
shader_param_4 (1.120000, 1.120000, 1.130000, -0.420000)
shader_param_5 (0.000000, 0.000000, 0.000000, 0.000000)
shader_param_6 (8.016100, 10.000500, 0.800000, 0.120000)
shader_param_7 (100.000000, 0.500000, 0.000000, 0.000000)
shader_param_8 (0.000000, 0.000000, 0.000000, 0.000000)
"""
disabledmods = """
-304- Dark Signal Weather and Ambiance Audio - Shrike
-290- Atmospherics Shaders Weathers and Reshade Latest - Hippobot
-190- Screen Space Shaders 20 - Ascii1457
-188- Enhanced Shaders - KennShade
-36- Better Rain texture - Detron
-35- Wet Surfaces Fix - CryoManne
-26- High Res PDA Maps - Bazingarrey
-24- Skies Redux - d_nan
"""

if page == "Home":
    st.title("XTREME Graphics Pack For G.A.M.M.A.")

else:

    st.title(page)

    if page == "Modlist Compatibility":
        st.write("This will edit your MO2 modlist file to disable the mods that should be disabled, while keeping the rest of your modlist intact.")
        st.write("Upload your **`modlist.txt`** file - **located in your current profile's folder (`GAMMA/profiles/yourprofile/` - default GAMMA profile is the `GAMMA/profiles/G.A.M.M.A./` folder)**")
        st.write("Then, download the converted file, drag it into your **`GAMMA/profiles/yourprofile/`** folder and replace the existing file when prompted.")

        userfile = st.file_uploader("")
        
        if userfile != None:

            if userfile.name != "modlist.txt":
                st.subheader("This is not a valid modlist file. Please use a valid file.")

            else:

                strio = StringIO(userfile.getvalue().decode("utf-8"))
                userout = disabledmods + strio.read()
                download = st.download_button("Download Converted File", data=userout, file_name="modlist.txt")

    elif page == "Load Atmospheric Preset":

        st.write("This will load the settings from the **`AtmosXTREME`** atmospheric preset file into a copy of your game settings file, which you can download and use to replace your **`user.ltx`** file.")
        st.write("Upload your **`user.ltx`** file (**located in the `Anomaly/appdata/` folder**) below.")
        st.write("Then, download the converted file, drag it into your **`Anomaly/appdata/`** folder and replace the existing file when prompted.")

        userfile = st.file_uploader("")
        
        if userfile != None:

            if userfile.name != "user.ltx":
                st.subheader("This is not a valid game settings file. Please use a valid file.")

            else:

                strio = StringIO(userfile.getvalue().decode("utf-8"))
                userout = strio.read() + atmospreset
                download = st.download_button("Download Converted File", data=userout, file_name="user.ltx")
