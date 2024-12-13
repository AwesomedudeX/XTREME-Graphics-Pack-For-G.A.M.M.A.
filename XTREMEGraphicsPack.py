import streamlit as st
from io import StringIO

st.set_page_config(layout="wide", initial_sidebar_state="expanded")

page = st.sidebar.radio("**Navigation:**", ["Home", "Modlist Compatibility", "Load Atmospheric Preset", "MCM Settings For SSS"])
atmospreset = """
r__color_grading (0.300000, 0.500000, 0.600000)

r__enable_grass_shadow off

r__saturation 1.2
r__gamma 1
r__exposure 0.65
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
disabledmods = {

":green[**G.A.M.M.A.**]": {

    "shaders": """-G.A.M.M.A. No Masks Textures
-G.A.M.M.A. Weathers
-304- Dark Signal Weather and Ambiance Audio - Shrike
-290- Atmospherics Shaders Weathers and Reshade Latest - Hippobot
-190- Screen Space Shaders 20 - Ascii1457
189- Beef's NVG - theRealBeef
188- Enhanced Shaders - KennShade
-129- Mask Reflections - shader fix - Grokitach
-36- Better Rain texture - Detron
-35- Wet Surfaces Fix - CryoManne
-26- High Res PDA Maps - Bazingarrey
-24- Skies Redux - d_nan
""",

    "textures": """-388- Aydins Grass Tweaks SSS Terrain LOD Compatibility - aytabag
357- Grey Tree Barks Begone - Joe325
-289- Grass Tweaks (reinstall for different options) - Aydin
242- Gardener of the Zone Textures - YuriVernadsky
241- Simple Autumn Retexture No leaves - Daedalus-Prime
""",

    "maps": """-26- High Res PDA Maps - Bazingarrey
"""

},

":orange[**E.F.P.**]": """
-[Detron] Better Rain FX
-[Iretuerye] Golden Autumn Retexture - Autumn Grass Tress
-[Iretuerye] Golden Autumn Retexture - Green Grass
-[Ascii1457] Screen Space Shaders u16 - Volumetric Sun Rays Fixes (DX10-11 Only)
-[Ascii1457] Screen Space Shaders u16 - Fog (DX10-11 Only)
-[Ascii1457] Screen Space Shaders u16 - Flora Fixes and Improvements (DX10-11 Only)
-[Ascii1457] Screen Space Shaders u16 - Sky Debanding (DX10-11 Only)
-[Ascii1457] Screen Space Shaders u16 - Shadows Fixes (DX10-11 Only)
-[Ascii1457] Screen Space Shaders u16 - Interactive Grass (DX10-11 Only)
-[Ascii1457] Screen Space Shaders u16 - New Shadow Features (DX10-11 Only)
-[Ascii1457] Screen Space Shaders u16 - Indirect Light (DX10-11 Only)
-[Ascii1457] Screen Space Shaders u16 - Weapons DOF (DX10-11 Only)
-[Ascii1457] Screen Space Shaders u16 - Rain Puddles (DX10-11 Only)
-[Ascii1457] Screen Space Shaders u16 - SSR Water (DX10-11 Only)
-[Ascii1457] Screen Space Shaders u16 - SSR (DX10-11 Only)
-[Ascii1457] Screen Space Shaders u16 - SSS (DX10-11 Only)
-[Ascii1457] Screen Space Shaders u16 - SSDO (DX10-11 Only)
-[Ascii1457] Screen Space Shaders u16 - Main - ES Patch (DX10-11 Only)
-[Ascii1457] Screen Space Shaders u16 - Main - Beef NVGs Patch(DX10-11 Only)
-[Ascii1457] Screen Space Shaders u16 - Main (DX10-11 Only)
-[Beef] NVGS - ES (DX10-11 Only)
-[Joe325] Nicer Reflections
-[KennShade] ES PBR - Shader Params
-[KennShade] ES PBR - Fixed Bloom
-[KennShade] ES PBR - Cubemaps
-[KennShade] ES PBR - Color Grading
-[KennShade] ES PBR (DX10-11 Only)
-[Awene] Agressor - Custom Weather
"""

}
sssmcm = """
![mcm]
        ssfx_module/ao/blur_mcm          = 1
        ssfx_module/ao/distance_mcm      = 150
        ssfx_module/ao/flora_int_mcm     = 0.75
        ssfx_module/ao/global_int_mcm    = 0.8
        ssfx_module/ao/hud_int_mcm       = 1
        ssfx_module/ao/max_occ_mcm       = 0
        ssfx_module/ao/quality_mcm       = 4
        ssfx_module/ao/radius_mcm        = 2.5
        ssfx_module/ao/res_mcm           = 0.5
        ssfx_module/florafixes/grass_specular_mcm = 0.15
        ssfx_module/florafixes/grass_specular_wet_mcm = 0.18
        ssfx_module/florafixes/sss_color_mcm = 1
        ssfx_module/florafixes/sss_int_mcm = 2
        ssfx_module/florafixes/trees_specular_mcm = 0.14
        ssfx_module/florafixes/trees_specular_wet_mcm = 0.15
        ssfx_module/general/shaderscope_patch_mcm = true
        ssfx_module/il/blur_mcm          = 1
        ssfx_module/il/distance_mcm      = 150
        ssfx_module/il/flora_int_mcm     = 0.62
        ssfx_module/il/global_int_mcm    = 0.577
        ssfx_module/il/hud_int_mcm       = 0.95
        ssfx_module/il/quality_mcm       = 32
        ssfx_module/il/res_mcm           = 0.15
        ssfx_module/il/vibrance_mcm      = 0.55
        ssfx_module/inter_grass/anomalies_distance_mcm = 25
        ssfx_module/inter_grass/enable_anomalies_mcm = true
        ssfx_module/inter_grass/enable_mcm = true
        ssfx_module/inter_grass/enable_mutants_mcm = true
        ssfx_module/inter_grass/enable_player_mcm = true
        ssfx_module/inter_grass/explosions_speed_mcm = 5
        ssfx_module/inter_grass/explosions_str_mcm = 1.5
        ssfx_module/inter_grass/horizontal_str_mcm = 2.5
        ssfx_module/inter_grass/max_distance_mcm = 1000
        ssfx_module/inter_grass/max_entities_mcm = 7
        ssfx_module/inter_grass/radius_mcm = 1
        ssfx_module/inter_grass/shooting_range_mcm = 2
        ssfx_module/inter_grass/shooting_str_mcm = 0.3
        ssfx_module/inter_grass/vertical_str_mcm = 1
        ssfx_module/parallax/ao_mcm      = 0
        ssfx_module/parallax/height_mcm  = 0.05
        ssfx_module/parallax/quality_mcm = 36
        ssfx_module/parallax/range_mcm   = 40
        ssfx_module/parallax/refine_mcm  = true
        ssfx_module/shadows/lod_max_mcm  = 0
        ssfx_module/shadows/lod_min_mcm  = 0
        ssfx_module/shadows/lod_quality_mcm = 1
        ssfx_module/shadows/volumetric_force_mcm = true
        ssfx_module/shadows/volumetric_int_mcm = 3
        ssfx_module/shadows/volumetric_quality_mcm = 5
        ssfx_module/shadows/volumetric_resolution_mcm = 100
        ssfx_module/shw_cascades/grass_shw_distance_mcm = 35
        ssfx_module/shw_cascades/grass_shw_nondir_maxdistance_mcm = 30
        ssfx_module/shw_cascades/grass_shw_quality_mcm = 0
        ssfx_module/shw_cascades/size_1_mcm = 20
        ssfx_module/shw_cascades/size_2_mcm = 60
        ssfx_module/shw_cascades/size_3_mcm = 160
        ssfx_module/ssfx_pp/ssfx_bloom/blur_mcm = 2
        ssfx_module/ssfx_pp/ssfx_bloom/dirt_mcm = 1.8
        ssfx_module/ssfx_pp/ssfx_bloom/exposure_mcm = 1
        ssfx_module/ssfx_pp/ssfx_bloom/lens_mcm = 1.5
        ssfx_module/ssfx_pp/ssfx_bloom/sky_mcm = 0
        ssfx_module/ssfx_pp/ssfx_bloom/threshold_mcm = 6
        ssfx_module/ssfx_pp/ssfx_bloom/use_weather_mcm = false
        ssfx_module/ssfx_pp/ssfx_bloom/vibrance_mcm = 1.3
        ssfx_module/ssfx_rain_module/ssfx_rain_footsteps/jump_vol_mcm = 0.7
        ssfx_module/ssfx_rain_module/ssfx_rain_footsteps/land_vol_mcm = 0.7
        ssfx_module/ssfx_rain_module/ssfx_rain_footsteps/main_vol_mcm = 0.4
        ssfx_module/ssfx_rain_module/ssfx_rain_footsteps/multi_no_rain_mcm = 0.3
        ssfx_module/ssfx_rain_module/ssfx_rain_footsteps/multi_run_mcm = 1.4
        ssfx_module/ssfx_rain_module/ssfx_rain_footsteps/multi_walk_mcm = 0.33
        ssfx_module/ssfx_rain_module/ssfx_rain_footsteps/vol_rnd_mcm = 0.15
        ssfx_module/ssfx_rain_module/ssfx_rain_hud_raindrops/animation_speed_mcm = 1
        ssfx_module/ssfx_rain_module/ssfx_rain_hud_raindrops/buildup_mcm = 2
        ssfx_module/ssfx_rain_module/ssfx_rain_hud_raindrops/density_mcm = 2
        ssfx_module/ssfx_rain_module/ssfx_rain_hud_raindrops/drying_mcm = 1
        ssfx_module/ssfx_rain_module/ssfx_rain_hud_raindrops/extra_gloss_mcm = 0.4
        ssfx_module/ssfx_rain_module/ssfx_rain_hud_raindrops/gloss_mcm = 2
        ssfx_module/ssfx_rain_module/ssfx_rain_hud_raindrops/reflection_str_mcm = 1
        ssfx_module/ssfx_rain_module/ssfx_rain_hud_raindrops/refraction_str_mcm = 1
        ssfx_module/ssfx_rain_module/ssfx_rain_hud_raindrops/size_mcm = 0.5
        ssfx_module/ssfx_rain_module/ssfx_rain_main/alpha_mcm = 1
        ssfx_module/ssfx_rain_module/ssfx_rain_main/brightness_mcm = 0
        ssfx_module/ssfx_rain_module/ssfx_rain_main/len_mcm = 1.1
        ssfx_module/ssfx_rain_module/ssfx_rain_main/max_drops_mcm = 2500
        ssfx_module/ssfx_rain_module/ssfx_rain_main/quality_mcm = 2
        ssfx_module/ssfx_rain_module/ssfx_rain_main/radius_mcm = 15
        ssfx_module/ssfx_rain_module/ssfx_rain_main/reflection_mcm = 1
        ssfx_module/ssfx_rain_module/ssfx_rain_main/refraction_mcm = 2.5
        ssfx_module/ssfx_rain_module/ssfx_rain_main/speed_mcm = 0.7
        ssfx_module/ssfx_rain_module/ssfx_rain_main/splash_alpha_mcm = 0.2
        ssfx_module/ssfx_rain_module/ssfx_rain_main/splash_refraction_mcm = 3
        ssfx_module/ssfx_rain_module/ssfx_rain_main/width_mcm = 0.03
        ssfx_module/ssfx_wetness/ssfx_gloss/auto_gloss_max_mcm = 0.96
        ssfx_module/ssfx_wetness/ssfx_gloss/auto_gloss_mcm = true
        ssfx_module/ssfx_wetness/ssfx_gloss/max_gloss_mcm = 0.96
        ssfx_module/ssfx_wetness/ssfx_gloss/min_gloss_mcm = 0.7
        ssfx_module/ssfx_wetness/ssfx_gloss/specular_color_mcm = 0.6
        ssfx_module/ssfx_wetness/ssfx_gloss/specular_int_mcm = 0.6
        ssfx_module/ssfx_wetness/ssfx_wet_surf/buildup_speed_mcm = 1.4
        ssfx_module/ssfx_wetness/ssfx_wet_surf/cover_distance_mcm = 30
        ssfx_module/ssfx_wetness/ssfx_wet_surf/cover_res_mcm = 1
        ssfx_module/ssfx_wetness/ssfx_wet_surf/dry_speed_mcm = 0.5
        ssfx_module/ssfx_wetness/ssfx_wet_surf/ripples_intensity_mcm = 1.25
        ssfx_module/ssfx_wetness/ssfx_wet_surf/ripples_min_speed_mcm = 0.7
        ssfx_module/ssfx_wetness/ssfx_wet_surf/ripples_size_mcm = 1.5
        ssfx_module/ssfx_wetness/ssfx_wet_surf/ripples_speed_mcm = 1.4
        ssfx_module/ssfx_wetness/ssfx_wet_surf/waterfall_intensity_mcm = 0.35
        ssfx_module/ssfx_wetness/ssfx_wet_surf/waterfall_min_speed_mcm = 0.2
        ssfx_module/ssfx_wetness/ssfx_wet_surf/waterfall_size_mcm = 1.2
        ssfx_module/ssfx_wetness/ssfx_wet_surf/waterfall_speed_mcm = 1.5
        ssfx_module/ssr/blur_mcm         = 0.1
        ssfx_module/ssr/general_int_mcm  = 1.1
        ssfx_module/ssr/quality_mcm      = 0
        ssfx_module/ssr/render_scale_mcm = 1
        ssfx_module/ssr/sky_int_mcm      = 1.2
        ssfx_module/ssr/temporal_mcm     = 0.6
        ssfx_module/ssr/use_noise_mcm    = false
        ssfx_module/ssr/weapon_int_max_mcm = 0.1
        ssfx_module/ssr/weapon_int_mcm   = 1
        ssfx_module/sss/enable_dir_mcm   = true
        ssfx_module/sss/enable_point_mcm = true
        ssfx_module/sss/len_dir_mcm      = 1
        ssfx_module/sss/len_point_mcm    = 1
        ssfx_module/sss/quality_dir_mcm  = 24
        ssfx_module/sss/quality_point_mcm = 8
        ssfx_module/terrain/distance_mcm = 20
        ssfx_module/terrain/grass_align_mcm = true
        ssfx_module/terrain/grass_slope_mcm = 90
        ssfx_module/terrain/pom_height_mcm = 0.04
        ssfx_module/terrain/pom_quality_mcm = 36
        ssfx_module/terrain/pom_range_mcm = 20
        ssfx_module/terrain/pom_refine_mcm = true
        ssfx_module/terrain/pom_water_level_mcm = 1
        ssfx_module/water/blur_mcm       = 0.45
        ssfx_module/water/blur_pattern_mcm = 1
        ssfx_module/water/caustics_int_mcm = 0.3
        ssfx_module/water/distortion_mcm = 0.6
        ssfx_module/water/parallax_height_mcm = 0.05
        ssfx_module/water/parallax_quality_mcm = 2
        ssfx_module/water/reflection_int_mcm = 0.8
        ssfx_module/water/ripples_int_mcm = 0.5
        ssfx_module/water/softborder_mcm = 0.3
        ssfx_module/water/specular_int_mcm = 1
        ssfx_module/water/ssr_quality_mcm = 2
        ssfx_module/water/ssr_res_mcm    = 2
        ssfx_module/water/turbidity_mcm  = 0.3
        ssfx_module/wind/grass_push_mcm  = 3
        ssfx_module/wind/grass_speed_mcm = 10.000001
        ssfx_module/wind/grass_turbulence_mcm = 3
        ssfx_module/wind/grass_wave_mcm  = 1
        ssfx_module/wind/min_speed_mcm   = 0.45
        ssfx_module/wind/trees_bend_mcm  = 0.3
        ssfx_module/wind/trees_speed_mcm = 12.000001
        ssfx_module/wind/trees_trunk_mcm = 0.2
        ssfx_module/wpn_dof/aim_blur_mcm = 1.6
        ssfx_module/wpn_dof/aim_edgeblur_mcm = 1
        ssfx_module/wpn_dof/aim_fadelen_mcm = 0.25
        ssfx_module/wpn_dof/aim_fadestart_mcm = 0.1
        ssfx_module/wpn_dof/blur_mcm     = 1.1
        ssfx_module/wpn_dof/edgeblur_mcm = 0.3
        ssfx_module/wpn_dof/fadelen_mcm  = 0.25
        ssfx_module/wpn_dof/fadestart_mcm = 0.15
        ssfx_module/wpn_dof/fdda_mcm     = false
        ssfx_module/wpn_dof/inventory_mcm = true
        ssfx_module/wpn_dof/looting_mutant_mcm = true
        ssfx_module/wpn_dof/pda_mcm      = true
        ssfx_module/wpn_dof/reloading_mcm = false
"""

if page == "Home":
    st.title("XTREME Graphics Pack For G.A.M.M.A.")

else:

    st.title(page)

    if page == "Modlist Compatibility":

        st.write("This will edit your MO2 modlist file to disable the mods that should be disabled, while keeping the rest of your modlist intact.")
        st.write("Upload your **`modlist.txt`** file - **located in your current profile's folder (`GAMMA/profiles/yourprofile/` - default GAMMA profile is the `GAMMA/profiles/G.A.M.M.A./` folder)**. Then, select whichever options you selected when installing the pack.")
        st.write("After that, download the converted file, drag it into your **`GAMMA/profiles/yourprofile/`** folder and replace the existing file when prompted.")

        version = st.radio("**What S.T.A.L.K.E.R. modpack do you use?**", [":green[**G.A.M.M.A.**]", ":orange[**E.F.P.**]"])
        userfile = st.file_uploader("")
        
        if userfile != None:

            if userfile.name != "modlist.txt":
                st.subheader("This is not a valid modlist file. Please use a valid file.")

            else:

                strio = StringIO(userfile.getvalue().decode("utf-8"))
                userfile = strio.read()

                if version == ":green[**G.A.M.M.A.**]":

                    st.subheader("What options did you select when installing the pack?")
                    
                    baseshaders = st.checkbox("Base Shaders (REGULAR OR WINTER)", value=True)
                    shaders = st.checkbox("Shaders & VFX")
                    textures = st.checkbox("ADEGAZR+ Texture Multipack")                    
                    maps = st.checkbox("Re\:Pack 16K PDA Maps")
                    winter = st.checkbox("Winter")
                    latefall = st.checkbox("Late Fall")

                    userout = userfile

                    if shaders or baseshaders:
                        userout = disabledmods[version]["shaders"] + userout

                    if textures or winter or latefall:
                        userout = disabledmods[version]["textures"] + userout
                        
                    if maps:
                        userout = disabledmods[version]["maps"] + userout

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

    elif page == "MCM Settings For SSS":
        
        st.write("This will edit your MCM settings file to change its settings to what they should be for this pack.")
        st.write("Upload your **`axr_options.ltx`** file from your G.A.M.M.A. MCM values mod in MO2 - to get it, open MO2, search for `G.A.M.M.A. MCM values`, right-click on the mod and hit `Reveal in Explorer`.**")
        st.write("After that, in the file explorer window that pops up, open the `gamedata` folder, open the `configs` folder inside of that, and drag and drop the `axr_options.ltx` file onto the website.")
        st.write("Then, download the converted file, drag it into the `configs` folder and replace the existing file when prompted.")

        userfile = st.file_uploader("")
        
        if userfile != None:

            if userfile.name != "axr_options.ltx":
                st.subheader("This is not a valid MCM values file. Please use a valid file.")

            else:

                strio = StringIO(userfile.getvalue().decode("utf-8"))
                userout = strio.read() + sssmcm
                download = st.download_button("Download Converted File", data=userout, file_name="axr_options.ltx")
