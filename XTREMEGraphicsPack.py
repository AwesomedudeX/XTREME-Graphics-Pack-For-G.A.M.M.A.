import streamlit as st
from io import StringIO

st.set_page_config(layout="wide", initial_sidebar_state="expanded")

@st.cache_data()
def showScreenshots(screenshots, ext):
    for img in screenshots:
        st.image(img+ext, img)

page = st.sidebar.radio("**Navigation:**", ["Home", "STALKER XTREME", "Modlist Compatibility", "Load Atmospheric Preset", "MCM Settings For SSS", "Awesomedude's Graphics Settings", "ReShade File Finder", "Atmospheric Preset Editor", "Arrival Anomalies"])
atmospresets = {

"XTREME": """
r__color_grading (0, 0, 0)

r__enable_grass_shadow off

r__saturation 1.15
r__gamma 1.2
r__exposure 1
scope_factor 1

r2_sun_lumscale 3.
r2_gloss_factor 0.001
r2_gloss_min 0.56
r2_sun_lumscale 3.
r2_sun_lumscale_amb 2.5
r2_sun_lumscale_hemi 0.97063
r2_tonemap on
r2_tonemap_adaptation 3.0
r2_tonemap_amount 1
r2_tonemap_lowlum 0.55
r2_tonemap_middlegray 1.4
rs_c_brightness 1
rs_c_contrast 1
rs_c_gamma 1.
r2_sun_depth_near_scale 0.9998
r2_sun_depth_far_scale 0.99988
r2_sun_tsm_bias 0
ssfx_hud_hemi 0

shader_param_1 (0.99, 1, 0.97, -0.2)
shader_param_2 (0, 0, 0, 0)
shader_param_3 (0.838, 0.847, 0.852, -0.15)
shader_param_4 (1.12, 1.12, 1.13, -0.4)
""",

"XTREMEDull": """
r__color_grading (0, 0, 0)

r__enable_grass_shadow off

r__saturation 0.8
r__gamma 1
r__exposure 1
scope_factor 1

r2_sun_lumscale 3.
r2_gloss_factor 0.001
r2_gloss_min 0.56
r2_sun_lumscale 3.
r2_sun_lumscale_amb 2.5
r2_sun_lumscale_hemi 0.97063
r2_tonemap on
r2_tonemap_adaptation 3.0
r2_tonemap_amount 1
r2_tonemap_lowlum 0.55
r2_tonemap_middlegray 1.4
rs_c_brightness 1
rs_c_contrast 1
rs_c_gamma 1.
r2_sun_depth_near_scale 0.9998
r2_sun_depth_far_scale 0.99988
r2_sun_tsm_bias 0
ssfx_hud_hemi 0

shader_param_1 (0.99, 1, 0.97, -0.3)
shader_param_2 (0, 0, 0, 0)
shader_param_3 (0.9, 0.9, 0.9, -0.3)
shader_param_4 (1.12, 1.12, 1.13, -0.4)
""",

"XTREMEGloomy": """
r__color_grading (0, 0, 0)

r__enable_grass_shadow off

r__saturation 0.8
r__gamma 1
r__exposure 1
scope_factor 1

r2_sun_lumscale 3.
r2_gloss_factor 0.001
r2_gloss_min 0.56
r2_sun_lumscale 3.
r2_sun_lumscale_amb 2.5
r2_sun_lumscale_hemi 0.97063
r2_tonemap on
r2_tonemap_adaptation 3.0
r2_tonemap_amount 1
r2_tonemap_lowlum 0.55
r2_tonemap_middlegray 1.4
rs_c_brightness 1
rs_c_contrast 1
rs_c_gamma 1.
r2_sun_depth_near_scale 0.9998
r2_sun_depth_far_scale 0.99988
r2_sun_tsm_bias 0
ssfx_hud_hemi 0

shader_param_1 (0.99, 1, 0.97, -0.3)
shader_param_2 (0, 0, 0, 0)
shader_param_3 (0.9, 0.87, 0.82, -0.3)
shader_param_4 (1.12, 1.12, 1.13, -0.4)
""",

"XTREMERealistic": """
r__color_grading (0, 0, 0)

r__enable_grass_shadow off

r__saturation 1
r__gamma 1
r__exposure 1
scope_factor 1

r2_sun_lumscale 3.
r2_gloss_factor 0.001
r2_gloss_min 0.56
r2_sun_lumscale 3.
r2_sun_lumscale_amb 2.5
r2_sun_lumscale_hemi 0.97063
r2_tonemap on
r2_tonemap_adaptation 3.0
r2_tonemap_amount 1
r2_tonemap_lowlum 0.55
r2_tonemap_middlegray 1.4
rs_c_brightness 1
rs_c_contrast 1
rs_c_gamma 1.
r2_sun_depth_near_scale 0.9998
r2_sun_depth_far_scale 0.99988
r2_sun_tsm_bias 0
ssfx_hud_hemi 0

shader_param_1 (0.9, 1, 0.97, 0.1)
shader_param_2 (0, 0, 0, 0)
shader_param_3 (0.838, 0.92, 0.95, 0)
shader_param_4 (1.12, 1.12, 1.13, -0.4)
""",

"XTREMENature": """
r__color_grading (0, 0, 0)

r__enable_grass_shadow off

r__saturation 1.15
r__gamma 1
r__exposure 1
scope_factor 1

r2_sun_lumscale 3.
r2_gloss_factor 0.001
r2_gloss_min 0.56
r2_sun_lumscale 3.
r2_sun_lumscale_amb 2.5
r2_sun_lumscale_hemi 0.97063
r2_tonemap on
r2_tonemap_adaptation 3.0
r2_tonemap_amount 1
r2_tonemap_lowlum 0.55
r2_tonemap_middlegray 1.4
rs_c_brightness 1
rs_c_contrast 1
rs_c_gamma 1.
r2_sun_depth_near_scale 0.9998
r2_sun_depth_far_scale 0.99988
r2_sun_tsm_bias 0
ssfx_hud_hemi 0

shader_param_1 (0.99, 1, 0.97, -0.2)
shader_param_2 (0, 0, 0, 0)
shader_param_3 (0.85, 0.835, 0.82, -0.15)
shader_param_4 (1.12, 1.12, 1.13, -0.4)
""",

"XTREMENight": """
r__color_grading (0, 0, 0)

r__enable_grass_shadow off

r__saturation 0.8
r__gamma 1
r__exposure 1
scope_factor 1

r2_sun_lumscale 3.
r2_gloss_factor 0.001
r2_gloss_min 0.56
r2_sun_lumscale 3.
r2_sun_lumscale_amb 2.5
r2_sun_lumscale_hemi 0.97063
r2_tonemap on
r2_tonemap_adaptation 3.0
r2_tonemap_amount 1
r2_tonemap_lowlum 0.55
r2_tonemap_middlegray 1.4
rs_c_brightness 1
rs_c_contrast 1
rs_c_gamma 1.
r2_sun_depth_near_scale 0.9998
r2_sun_depth_far_scale 0.99988
r2_sun_tsm_bias 0
ssfx_hud_hemi 0

shader_param_1 (0.9, 1, 0.97, 0.5)
shader_param_2 (0, 0, 0, 0)
shader_param_3 (0.838, 0.9, 0.9, -0.1)
shader_param_4 (1.12, 1.12, 1.13, -0.4)
""",

"XTREMEVivid": """
r__color_grading (0, 0, 0)

r__enable_grass_shadow off

r__saturation 1.1
r__gamma 1
r__exposure 1
scope_factor 1

r2_sun_lumscale 3.
r2_gloss_factor 0.001
r2_gloss_min 0.56
r2_sun_lumscale 3.
r2_sun_lumscale_amb 2.5
r2_sun_lumscale_hemi 0.97063
r2_tonemap on
r2_tonemap_adaptation 3.0
r2_tonemap_amount 1
r2_tonemap_lowlum 0.55
r2_tonemap_middlegray 1.4
rs_c_brightness 1
rs_c_contrast 1
rs_c_gamma 1.
r2_sun_depth_near_scale 0.9998
r2_sun_depth_far_scale 0.99988
r2_sun_tsm_bias 0
ssfx_hud_hemi 0

shader_param_1 (0.95, 1, 0.97, 0.5)
shader_param_2 (0, 0, 0, 0)
shader_param_3 (0.838, 0.847, 0.852, 0)
shader_param_4 (1.12, 1.12, 1.13, -0.4)
""",

"XTREMEVibrant": """
r__color_grading (0, 0, 0)

r__enable_grass_shadow off

r__saturation 1.3
r__gamma 1
r__exposure 1
scope_factor 1

r2_sun_lumscale 3.
r2_gloss_factor 0.001
r2_gloss_min 0.56
r2_sun_lumscale 3.
r2_sun_lumscale_amb 2.5
r2_sun_lumscale_hemi 0.97063
r2_tonemap on
r2_tonemap_adaptation 3.0
r2_tonemap_amount 1
r2_tonemap_lowlum 0.55
r2_tonemap_middlegray 1.4
rs_c_brightness 1
rs_c_contrast 1
rs_c_gamma 1.
r2_sun_depth_near_scale 0.9998
r2_sun_depth_far_scale 0.99988
r2_sun_tsm_bias 0
ssfx_hud_hemi 0

shader_param_1 (0.99, 1, 0.97, -0.2)
shader_param_2 (0, 0, 0, 0)
shader_param_3 (0.838, 0.847, 0.86, -0.25)
shader_param_4 (1.12, 1.12, 1.13, -0.4)
""",

"XTREMEMysterious": """
r__color_grading (0, 0, 0)

r__enable_grass_shadow off

r__saturation 1.15
r__gamma 1
r__exposure 1
scope_factor 1

r2_sun_lumscale 3.
r2_gloss_factor 0.001
r2_gloss_min 0.56
r2_sun_lumscale 3.
r2_sun_lumscale_amb 1.49685
r2_sun_lumscale_hemi 0.97063
r2_tonemap on
r2_tonemap_adaptation 3.0
r2_tonemap_amount 1
r2_tonemap_lowlum 0.55
r2_tonemap_middlegray 1.4
rs_c_brightness 1
rs_c_contrast 1
rs_c_gamma 1.
r2_sun_depth_near_scale 0.9998
r2_sun_depth_far_scale 0.99988
r2_sun_tsm_bias 0
ssfx_hud_hemi 0

shader_param_1 (0.99, 1, 0.97, -0.3)
shader_param_2 (0, 0, 0, 0)
shader_param_3 (0.88, 0.85, 0.81, -0.3)
shader_param_4 (1.12, 1.12, 1.13, -0.4)
""",

"XTREMEApocalypse": """
r__color_grading (0, 0, 0)

r__enable_grass_shadow off

r__saturation 1.15
r__gamma 1
r__exposure 1
scope_factor 1

r2_sun_lumscale 3.
r2_gloss_factor 0.001
r2_gloss_min 0.56
r2_sun_lumscale 3.
r2_sun_lumscale_amb 1.49685
r2_sun_lumscale_hemi 0.97063
r2_tonemap on
r2_tonemap_adaptation 3.0
r2_tonemap_amount 1
r2_tonemap_lowlum 0.55
r2_tonemap_middlegray 1.4
rs_c_brightness 1
rs_c_contrast 1
rs_c_gamma 1.
r2_sun_depth_near_scale 0.9998
r2_sun_depth_far_scale 0.99988
r2_sun_tsm_bias 0
ssfx_hud_hemi 0

shader_param_1 (0.99, 1, 0.97, -0.3)
shader_param_2 (0, 0, 0, 0)
shader_param_3 (0.88, 0.85, 0.9, -0.3)
shader_param_4 (1.12, 1.12, 1.13, -0.4)
""",

}
disabledmods = {

":green[**G.A.M.M.A.**]": {

    "base shaders": """-190- Screen Space Shaders 20 - Ascii1457
-188- Enhanced Shaders - KennShade
-189- Beef's NVG - theRealBeef
""",

    "mask textures": """-G.A.M.M.A. No Masks Textures
-129- Mask Reflections - shader fix - Grokitach
""",

    "shaders": """-G.A.M.M.A. Weathers
-304- Dark Signal Weather and Ambiance Audio - Shrike
-290- Atmospherics Shaders Weathers and Reshade Latest - Hippobot
-36- Better Rain texture - Detron
-35- Wet Surfaces Fix - CryoManne
-24- Skies Redux - d_nan
""",

    "textures": """-388- Aydins Grass Tweaks SSS Terrain LOD Compatibility - aytabag
-357- Grey Tree Barks Begone - Joe325
-289- Grass Tweaks (reinstall for different options) - Aydin
-242- Gardener of the Zone Textures - YuriVernadsky
-241- Simple Autumn Retexture No leaves - Daedalus-Prime
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
        ssfx_module/ao/flora_int_mcm     = 1
        ssfx_module/ao/global_int_mcm    = 1
        ssfx_module/ao/hud_int_mcm       = 1
        ssfx_module/ao/max_occ_mcm       = 0.115
        ssfx_module/ao/quality_mcm       = 4
        ssfx_module/ao/radius_mcm        = 2
        ssfx_module/ao/res_mcm           = 1
        ssfx_module/florafixes/grass_specular_mcm = 0.15
        ssfx_module/florafixes/grass_specular_wet_mcm = 0.18
        ssfx_module/florafixes/sss_color_mcm = 0.38
        ssfx_module/florafixes/sss_int_mcm = 4.6
        ssfx_module/florafixes/trees_specular_mcm = 0.14
        ssfx_module/florafixes/trees_specular_wet_mcm = 0.15
        ssfx_module/general/shaderscope_patch_mcm = true
        ssfx_module/il/blur_mcm          = 0.1
        ssfx_module/il/distance_mcm      = 200
        ssfx_module/il/flora_int_mcm     = 1
        ssfx_module/il/global_int_mcm    = 4
        ssfx_module/il/hud_int_mcm       = 1
        ssfx_module/il/quality_mcm       = 16
        ssfx_module/il/res_mcm           = 0.15
        ssfx_module/il/vibrance_mcm      = 0.6
        ssfx_module/inter_grass/anomalies_distance_mcm = 25
        ssfx_module/inter_grass/enable_anomalies_mcm = true
        ssfx_module/inter_grass/enable_mcm = true
        ssfx_module/inter_grass/enable_mutants_mcm = true
        ssfx_module/inter_grass/enable_player_mcm = true
        ssfx_module/inter_grass/explosions_speed_mcm = 5
        ssfx_module/inter_grass/explosions_str_mcm = 1
        ssfx_module/inter_grass/horizontal_str_mcm = 2
        ssfx_module/inter_grass/max_distance_mcm = 1500
        ssfx_module/inter_grass/max_entities_mcm = 8
        ssfx_module/inter_grass/radius_mcm = 1.4
        ssfx_module/inter_grass/shooting_range_mcm = 2
        ssfx_module/inter_grass/shooting_str_mcm = 0.3
        ssfx_module/inter_grass/vertical_str_mcm = 2
        ssfx_module/parallax/ao_mcm      = 0.5
        ssfx_module/parallax/height_mcm  = 0.035
        ssfx_module/parallax/quality_mcm = 16
        ssfx_module/parallax/range_mcm   = 16.5
        ssfx_module/parallax/refine_mcm  = false
        ssfx_module/shadows/lod_max_mcm  = 0
        ssfx_module/shadows/lod_min_mcm  = 3
        ssfx_module/shadows/lod_quality_mcm = 3
        ssfx_module/shadows/volumetric_force_mcm = true
        ssfx_module/shadows/volumetric_int_mcm = 0.5
        ssfx_module/shadows/volumetric_quality_mcm = 3
        ssfx_module/shw_cascades/grass_shw_distance_mcm = 50
        ssfx_module/shw_cascades/grass_shw_nondir_maxdistance_mcm = 50
        ssfx_module/shw_cascades/grass_shw_quality_mcm = 0
        ssfx_module/shw_cascades/size_1_mcm = 14
        ssfx_module/shw_cascades/size_2_mcm = 40
        ssfx_module/shw_cascades/size_3_mcm = 126
        ssfx_module/ssfx_pp/ssfx_bloom/blur_mcm = 1
        ssfx_module/ssfx_pp/ssfx_bloom/dirt_mcm = 0.5
        ssfx_module/ssfx_pp/ssfx_bloom/exposure_mcm = 1
        ssfx_module/ssfx_pp/ssfx_bloom/lens_mcm = 5
        ssfx_module/ssfx_pp/ssfx_bloom/sky_mcm = 0.3
        ssfx_module/ssfx_pp/ssfx_bloom/threshold_mcm = 5
        ssfx_module/ssfx_pp/ssfx_bloom/use_weather_mcm = false
        ssfx_module/ssfx_pp/ssfx_bloom/vibrance_mcm = 1
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
        ssfx_module/ssfx_rain_module/ssfx_rain_main/alpha_mcm = 0.8
        ssfx_module/ssfx_rain_module/ssfx_rain_main/brightness_mcm = 0.05
        ssfx_module/ssfx_rain_module/ssfx_rain_main/len_mcm = 1.5
        ssfx_module/ssfx_rain_module/ssfx_rain_main/max_drops_mcm = 2500
        ssfx_module/ssfx_rain_module/ssfx_rain_main/quality_mcm = 1
        ssfx_module/ssfx_rain_module/ssfx_rain_main/radius_mcm = 15
        ssfx_module/ssfx_rain_module/ssfx_rain_main/reflection_mcm = 1
        ssfx_module/ssfx_rain_module/ssfx_rain_main/refraction_mcm = 2.5
        ssfx_module/ssfx_rain_module/ssfx_rain_main/speed_mcm = 1
        ssfx_module/ssfx_rain_module/ssfx_rain_main/splash_alpha_mcm = 0.2
        ssfx_module/ssfx_rain_module/ssfx_rain_main/splash_refraction_mcm = 3
        ssfx_module/ssfx_rain_module/ssfx_rain_main/width_mcm = 0.07
        ssfx_module/ssfx_wetness/ssfx_gloss/auto_gloss_max_mcm = 0.96
        ssfx_module/ssfx_wetness/ssfx_gloss/auto_gloss_mcm = true
        ssfx_module/ssfx_wetness/ssfx_gloss/max_gloss_mcm = 0.95
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
        ssfx_module/ssr/blur_mcm         = 0.25
        ssfx_module/ssr/general_int_mcm  = 1.15
        ssfx_module/ssr/quality_mcm      = 0
        ssfx_module/ssr/render_scale_mcm = 1
        ssfx_module/ssr/sky_int_mcm      = 1.3
        ssfx_module/ssr/use_noise_mcm    = false
        ssfx_module/ssr/weapon_int_max_mcm = 0.05
        ssfx_module/ssr/weapon_int_mcm   = 0.45
        ssfx_module/sss/enable_dir_mcm   = true
        ssfx_module/sss/enable_point_mcm = true
        ssfx_module/sss/len_dir_mcm      = 1
        ssfx_module/sss/len_point_mcm    = 1
        ssfx_module/sss/quality_dir_mcm  = 12
        ssfx_module/sss/quality_point_mcm = 4
        ssfx_module/terrain/distance_mcm = 20
        ssfx_module/terrain/grass_align_mcm = true
        ssfx_module/terrain/grass_slope_mcm = 76
        ssfx_module/terrain/pom_height_mcm = 0.04
        ssfx_module/terrain/pom_quality_mcm = 24
        ssfx_module/terrain/pom_range_mcm = 31.5
        ssfx_module/terrain/pom_refine_mcm = true
        ssfx_module/terrain/pom_water_level_mcm = 1
        ssfx_module/water/blur_mcm       = 0.45
        ssfx_module/water/blur_pattern_mcm = 1
        ssfx_module/water/caustics_int_mcm = 0.3
        ssfx_module/water/distortion_mcm = 0.6
        ssfx_module/water/parallax_height_mcm = 0.05
        ssfx_module/water/parallax_quality_mcm = 2
        ssfx_module/water/reflection_int_mcm = 0.86
        ssfx_module/water/ripples_int_mcm = 0.5
        ssfx_module/water/softborder_mcm = 0.3
        ssfx_module/water/specular_int_mcm = 1
        ssfx_module/water/ssr_quality_mcm = 2
        ssfx_module/water/ssr_res_mcm    = 2
        ssfx_module/water/turbidity_mcm  = 0.3
        ssfx_module/wind/grass_push_mcm  = 1.6
        ssfx_module/wind/grass_speed_mcm = 9.7
        ssfx_module/wind/grass_turbulence_mcm = 1.5
        ssfx_module/wind/grass_wave_mcm  = 0.5
        ssfx_module/wind/min_speed_mcm   = 0.1
        ssfx_module/wind/trees_bend_mcm  = 0.9
        ssfx_module/wind/trees_speed_mcm = 9.1
        ssfx_module/wind/trees_trunk_mcm = 0.17
        ssfx_module/wpn_dof/aim_blur_mcm = 0
        ssfx_module/wpn_dof/aim_edgeblur_mcm = 0
        ssfx_module/wpn_dof/aim_fadelen_mcm = 0
        ssfx_module/wpn_dof/aim_fadestart_mcm = 0
        ssfx_module/wpn_dof/blur_mcm     = 1.1
        ssfx_module/wpn_dof/edgeblur_mcm = 0.3
        ssfx_module/wpn_dof/fadelen_mcm  = 0.25
        ssfx_module/wpn_dof/fadestart_mcm = 0.15
        ssfx_module/wpn_dof/fdda_mcm     = false
        ssfx_module/wpn_dof/inventory_mcm = false
        ssfx_module/wpn_dof/looting_mutant_mcm = false
        ssfx_module/wpn_dof/pda_mcm      = false
        ssfx_module/wpn_dof/reloading_mcm = false

        dynamic_tonemap_extended/adaptation = 3
        dynamic_tonemap_extended/enable_dynamic_tonemap = true
        dynamic_tonemap_extended/k_amount = 0.05
        dynamic_tonemap_extended/k_lowlum = 0.1
        dynamic_tonemap_extended/k_lumscale_amb = 0.05
        dynamic_tonemap_extended/k_lumscale_amb_addition = 0.07
        dynamic_tonemap_extended/k_lumscale_hemi = 0.01
        dynamic_tonemap_extended/k_lumscale_hemi_addition = 0.05
        dynamic_tonemap_extended/k_middle = 0.05
        dynamic_tonemap_extended/max_amount = 0.6
        dynamic_tonemap_extended/max_lowlum = 0.55
        dynamic_tonemap_extended/max_lumscale_amb = 1.5
        dynamic_tonemap_extended/max_lumscale_hemi = 1.4
        dynamic_tonemap_extended/max_middle_gray = 1.4
        dynamic_tonemap_extended/min_amount = 0.3
        dynamic_tonemap_extended/min_clear_lowlum = 0.5
        dynamic_tonemap_extended/min_lumscale_amb = 0.35
        dynamic_tonemap_extended/min_lumscale_hemi = 0.95
        dynamic_tonemap_extended/min_middle_gray = 1.3
        dynamic_tonemap_extended/min_not_clear_lowlum = 0.25
        dynamic_tonemap_extended/not_clear_amb_reduction_coeff = 0.9
        dynamic_tonemap_extended/not_clear_hemi_reduction_coeff = 1
        dynamic_tonemap_extended/rain_amb_reduction_coeff = 0.8
        dynamic_tonemap_extended/rain_amount_addition = 0.25
        dynamic_tonemap_extended/rain_hemi_reduction_coeff = 0.9
        dynamic_tonemap_extended/rain_lowlum_reduction_coeff = 0.8
        dynamic_tonemap_extended/storm_amb_reduction_coeff = 0.75
        dynamic_tonemap_extended/storm_amount_addition = 0.3
        dynamic_tonemap_extended/storm_hemi_reduction_coeff = 0.9
        dynamic_tonemap_extended/storm_lowlum_reduction_coeff = 0.8
"""
graphicssettings = """
r1_detail_textures on
r1_dlights on
r1_dlights_clip 40.
r1_fog_luminance 1.
r1_glows_per_frame 16
r1_lmodel_lerp 0.1
r1_pps_u 0.
r1_pps_v 0.
r1_software_skinning 0
r1_ssa_lod_a 16.
r1_ssa_lod_b 16.
r2_aa off
r2_aa_break (0.800000, 0.100000, 0.000000)
r2_aa_kernel 0.5
r2_aa_weight (0.250000, 0.250000, 0.000000)
r2_allow_r1_lights off
r2_detail_bump off
r2_dof -1.000000,0.000000,800.000000
r2_dof_enable on
r2_dof_radius 0.25
r2_dof_sky 30.
r2_drops_control (0.000000, 0.000000, 0.000000)
r2_exp_donttest_shad off
r2_gi off
r2_gi_clip 0.001
r2_gi_depth 1
r2_gi_photons 16
r2_gi_refl 0.9
r2_gloss_factor 0.001
r2_gloss_min 0.56
r2_ls_bloom_fast off
r2_ls_bloom_kernel_b 0.1
r2_ls_bloom_kernel_g 1.
r2_ls_bloom_kernel_scale 0.05
r2_ls_bloom_speed 100.
r2_ls_bloom_threshold 0.
r2_ls_depth_bias -0.00005
r2_ls_depth_scale 1.00001
r2_ls_dsm_kernel 0.7
r2_ls_psm_kernel 0.7
r2_ls_squality 3.
r2_ls_ssm_kernel 0.7
r2_mask_control (1.000000, 1.000000, 1.000000, 1.000000)
r2_mblur 0.04054
r2_mblur_enabled on
r2_parallax_h 0.
r2_qsync 0
r2_shadow_cascede_old off
r2_slight_fade 1.
r2_smaa off
r2_soft_particles on
r2_soft_water on
r2_ss_sunshafts_length 1.
r2_ss_sunshafts_radius 1.
r2_ssa_lod_a 16.
r2_ssa_lod_b 32.
r2_ssao st_opt_off
r2_ssao_blur off
r2_ssao_half_data off
r2_ssao_hbao off
r2_ssao_hdao off
r2_ssao_mode disabled
r2_ssao_opt_data on
r2_steep_parallax off
r2_sun on
r2_sun_depth_far_bias -0.00002
r2_sun_depth_far_scale 0.99988
r2_sun_depth_near_bias 0.00007
r2_sun_depth_near_scale 0.9998
r2_sun_details on
r2_sun_far 100.
r2_sun_focus on
r2_sun_lumscale 3.
r2_sun_lumscale_amb 1.34663
r2_sun_lumscale_hemi 0.9706
r2_sun_near 15.
r2_sun_near_border 0.75
r2_sun_quality st_opt_medium
r2_sun_tsm on
r2_sun_tsm_bias 0.
r2_sun_tsm_proj 0.3
r2_sunshafts_min 0.01
r2_sunshafts_mode volumetric
r2_sunshafts_quality st_opt_low
r2_sunshafts_value 0.5
r2_terrain_z_prepass off
r2_tnmp_a 0.15
r2_tnmp_b 0.5
r2_tnmp_c 0.1
r2_tnmp_d 0.2
r2_tnmp_e 0.2
r2_tnmp_exposure 0.16033
r2_tnmp_f 0.3
r2_tnmp_gamma 0.76667
r2_tnmp_onoff 0.
r2_tnmp_w 1.12
r2_tonemap on
r2_tonemap_adaptation 3.
r2_tonemap_amount 0.50599
r2_tonemap_lowlum 0.45599
r2_tonemap_middlegray 1.4
r2_volumetric_lights on
r2_wait_sleep 0
r2_water_reflections on
r2_zfill off
r2_zfill_depth 0.25
r2em 0.
r3_dynamic_wet_surfaces on
r3_dynamic_wet_surfaces_far 30.
r3_dynamic_wet_surfaces_near 70.
r3_dynamic_wet_surfaces_sm_res 128
r3_minmax_sm off
r3_msaa st_opt_off
r3_msaa_alphatest st_opt_atest_msaa_dx10_1
r3_use_dx10_1 on
r3_volumetric_smoke on
r4_enable_tessellation off
r4_hdr10_bloom_blur_passes 20
r4_hdr10_bloom_blur_scale 1.
r4_hdr10_bloom_intensity 0.06
r4_hdr10_bloom_on 0
r4_hdr10_brightness 0.
r4_hdr10_colorspace 2
r4_hdr10_contrast 0.
r4_hdr10_contrast_middle_gray 0.5
r4_hdr10_exposure 2.
r4_hdr10_flare_blur_passes 12
r4_hdr10_flare_blur_scale 1.
r4_hdr10_flare_center_falloff 1.1
r4_hdr10_flare_ghost_ca 3.
r4_hdr10_flare_ghost_dispersal 0.6
r4_hdr10_flare_ghost_intensity 0.04
r4_hdr10_flare_ghosts 1
r4_hdr10_flare_halo_ca 10.
r4_hdr10_flare_halo_intensity 0.04
r4_hdr10_flare_halo_scale 0.47
r4_hdr10_flare_lens_color (1.000000, 0.700000, 1.000000)
r4_hdr10_flare_on 0
r4_hdr10_flare_power 0.04
r4_hdr10_flare_threshold 0.
r4_hdr10_gamma 1.1
r4_hdr10_on 0
r4_hdr10_pda_intensity 1.
r4_hdr10_saturation 0.
r4_hdr10_sun_dawn_begin 4.5
r4_hdr10_sun_dawn_end 6.
r4_hdr10_sun_dusk_begin 18.5
r4_hdr10_sun_dusk_end 21.
r4_hdr10_sun_inner_radius 0.2
r4_hdr10_sun_intensity 80.
r4_hdr10_sun_on 0
r4_hdr10_sun_outer_radius 0.4
r4_hdr10_tonemap_mode 1
r4_hdr10_tonemapper 0
r4_hdr10_ui_nits 400.
r4_hdr10_ui_saturation 0.5
r4_hdr10_whitepoint_nits 400.
r4_wireframe off
r__3Dfakescope 1
r__actor_shadow on
r__bloom_thresh (0.700000, 0.800000, 0.900000, 0.000000)
r__bloom_weight (0.330000, 0.330000, 0.330000, 0.000000)
r__clear_models_on_unload off
r__color_grading (0.000000, 0.000000, 0.000000)
r__detail_density 0.5
r__detail_height 0.8
r__detail_radius 110
r__dtex_range 50.
r__enable_grass_shadow off
r__exposure 1.
r__fakescope 1
r__framelimit 0
r__gamma 1.
r__geometry_lod 1.5
r__heatvision 0
r__lens_flares on
r__nightvision 0
r__no_ram_textures on
r__no_scale_on_fade off
r__optimize_dynamic_geom 2
r__optimize_shadow_geom off
r__optimize_static_geom 3
r__saturation 1.
r__supersample 1
r__tf_aniso 16
r__tf_mipbias -0.5
r__use_precompiled_shaders on
r__wallmark_ttl 50.
r_screenshot_mode png
render_short_tracers 1
renderer renderer_r4
rs_c_brightness 1.
rs_c_contrast 1.
rs_c_gamma 1.
rs_cam_pos off
rs_refresh_60hz off
rs_screenmode borderless
rs_skeleton_update 32
rs_stats off
rs_v_sync off
rs_vis_distance 0.8
s3ds_param_1 (4.000000, 4.000000, 0.300000, 0.000000)
s3ds_param_2 (0.550000, 0.000000, 0.000000, 1.500000)
s3ds_param_3 (0.000000, 0.000000, 0.200000, 0.030000)
s3ds_param_4 (1.000000, 1.000000, 1.000000, 1.000000)
scope_2dtexactive 0
scope_blur_inner 0.1
scope_blur_outer 1.
scope_brightness 1.
scope_ca 0.003
scope_factor 1.
scope_fog_interp 0.15
scope_fog_radius 1.25
scope_fog_sharp 4.
scope_fog_swayAim 0.66
scope_fog_swayMove 0.25
scope_fog_travel 0.25
scope_radius 0.
sds_enable on
sds_speed_enable on
sds_zoom_enable on
shader_param_1 (0.900000, 1.000000, 0.970000, 0.100000)
shader_param_2 (0.000000, 0.000000, 0.000000, 0.000000)
shader_param_3 (0.838000, 0.920000, 0.950000, 0.000000)
shader_param_4 (1.120000, 1.120000, 1.130000, -0.400000)
shader_param_5 (1.000000, 0.000000, 0.000000, 0.000000)
shader_param_6 (0.000000, 1.000000, 0.000000, 0.000000)
shader_param_7 (1.000000, 0.550000, 0.000000, 0.000000)
shader_param_8 (0.000000, 10.300000, 100.000000, 10.000000)
sil_glow_color (1.000000, 0.000000, 0.000000)
sil_glow_cool_temp_rate 0.01
sil_glow_max_temp 0.15
sil_glow_shot_temp 0.004
smooth_ads_transition 0
snd_acceleration on
snd_cache_size 256
snd_doppler_power 1.8
snd_doppler_smoothing 15
snd_targets 256
ssfx_ao (1.000000, 5.000000, 1.000000, 2.000000)
ssfx_ao_quality 4
ssfx_ao_setup1 (150.000000, 1.000000, 1.000000, 0.115000)
ssfx_blood_decals (0.600000, 0.600000, 0.000000, 0.000000)
ssfx_bloom_1 (10.000000, 1.000000, 0.000000, 0.300000)
ssfx_bloom_2 (1.000000, 1.000000, 1.500000, 0.800000)
ssfx_bloom_use_presets 0
ssfx_florafixes_1 (0.150000, 0.180000, 0.140000, 0.150000)
ssfx_florafixes_2 (4.600000, 0.380000, 0.000000, 0.000000)
ssfx_gloss_factor 0.672
ssfx_gloss_method 1
ssfx_gloss_minmax (0.700000, 0.950000, 0.000000)
ssfx_grass_interactive (1.000000, 8.000000, 2000.000000, 1.000000)
ssfx_grass_shadows (1.000000, 1.000000, 50.000000, 0.000000)
ssfx_hud_drops_1 (0.000000, 0.000000, 30.000000, 0.050000)
ssfx_hud_drops_2 (0.225000, 1.500000, 0.400000, 2.000000)
ssfx_hud_hemi 0.
ssfx_il (6.666667, 4.000000, 0.600000, 0.500000)
ssfx_il_quality 16
ssfx_il_setup1 (300.000000, 1.000000, 1.000000, 0.000000)
ssfx_int_grass_params_1 (1.400000, 2.000000, 2.000000, 30.000000)
ssfx_int_grass_params_2 (1.000000, 5.000000, 0.300000, 2.000000)
ssfx_is_underground 0
ssfx_lightsetup_1 (0.600000, 0.600000, 0.000000, 0.000000)
ssfx_lut (1.000000, 2.000000, 0.000000, 0.000000)
ssfx_pom (16.000000, 40.000000, 0.035000, 0.600000)
ssfx_pom_refine 0
ssfx_rain_1 (1.500000, 0.070000, 1.000000, 2.000000)
ssfx_rain_2 (0.800000, 0.050000, 2.500000, 1.000000)
ssfx_rain_3 (0.200000, 3.000000, 0.000000, 0.000000)
ssfx_rain_drops_setup (2500.000000, 15.000000, 0.000000, 0.000000)
ssfx_shadow_bias (0.400000, 0.030000, 0.000000)
ssfx_shadow_cascades (14.000000, 40.000000, 126.000000)
ssfx_shadows (256.000000, 1536.000000, 0.000000)
ssfx_ssr (1.000000, 0.250000, 0.000000, 0.000000)
ssfx_ssr_2 (1.150000, 1.300000, 0.450000, 0.050000)
ssfx_ssr_quality 0
ssfx_sss (1.000000, 1.000000, 0.000000, 0.000000)
ssfx_sss_quality (24.000000, 8.000000, 1.000000, 1.000000)
ssfx_terrain_grass_align 1
ssfx_terrain_grass_slope 0.84444
ssfx_terrain_offset (-0.090000, -0.050000, -0.080000, 0.000000)
ssfx_terrain_pom (36.000000, 40.000000, 0.040000, 1.000000)
ssfx_terrain_pom_refine 1
ssfx_terrain_quality (20.000000, 0.000000, 0.000000, 0.000000)
ssfx_volumetric (1.000000, 0.500000, 3.000000, 1.000000)
ssfx_water (1.000000, 0.800000, 1.000000, 0.000000)
ssfx_water_quality (1.000000, 2.000000, 0.000000)
ssfx_water_setup1 (0.600000, 3.000000, 0.300000, 0.050000)
ssfx_water_setup2 (0.860000, 6.000000, 0.300000, 0.500000)
ssfx_wetness_multiplier (1.400000, 0.500000, 0.000000)
ssfx_wetsurfaces_1 (0.500000, 1.400000, 0.700000, 1.250000)
ssfx_wetsurfaces_2 (0.800000, 1.500000, 0.200000, 0.350000)
ssfx_wind_grass (9.700000, 1.500000, 1.600000, 0.500000)
ssfx_wind_trees (11.100000, 0.170000, 0.900000, 0.100000)
ssfx_wpn_dof_1 (0.150000, 0.400000, 0.000000, 1.100000)
ssfx_wpn_dof_2 0.15
"""
caminert = """
cam_inert 0.55
cam_slide_inert 0.25"""
fov = """
fov 100.
hud_fov 0.7
hud_fov_aim_factor 0."""
installation = """
Download these modded exes: https://github.com/themrdemonized/xray-monolith/releases/download/2025.3.9/STALKER-Anomaly-modded-exes_2025.3.9.zip, open the file in 7Zip, and extract ALL the files into your Anomaly folder.

Then, download and install these files **in the order shown** using the links below; install them through MO2, placing them at the bottom of your modlist. Because of the size of the mod, MO2 may freeze during the installation; just wait for a bit for the mod to be installed and MO2 will be functional again.

**XTREME GRAPHICS PACK MAIN FILE: https://drive.google.com/uc?export=download&id=1BfzX8lDHcVq3SWconCI3MdcfQDjlftVK**

**XTREME GRAPHICS OPTIONALS: https://drive.google.com/uc?export=download&id=1OVRrutTfFfJ2of3_iASgHLhKhkwO3uKx**

**RESHADE: https://drive.google.com/file/d/1XiLQLt8_BdfBLbGyobAYtzebaDATjvIy/view?usp=drive_link**

You can also get **STALKER XTREME**, which is a modpack full of mods to greatly enhance the realism and immersiveness of the zone. Certain mods that are disabled may be re-enabled, but they might cause issues. I'll offer as much support for them as I can.

**STALKER XTREME BETA (REQUIRES A NEW GAME): https://www.mediafire.com/file/boax17zc1bthj3v/STALKER+XTREME.7z/file**

Head to the **STALKER XTREME** page for instructions on how to install it - I highly recommend using it with **XTREME Graphics Pack**.

From there, if you are not going to get **STALKER XTREME**, follow the instructions on the **Modlist Compatibility** and **MCM Settings For SSS** pages on this site to modify your settings and mod list files to work with this pack.

Finally, you can either use the **Load Atmospheric Preset** page or just open the game and type `cfg_load xtreme` to load the atmospheric settings. If you are using **STALKER XTREME**, I recommend getting ALL of my graphics settings to ensure everything works properly.
"""
stalkerxtreme = {
    "part1": """
STALKER XTREME is a modpack designed around making STALKER as realistic as possible, featuring a Cold System, constant psy drain, modified item effects, a realistic body health system, HUD changes, reanimations, and so much more.

To get **STALKER XTREME**, first, make sure MO2 is CLOSED. Then, just download the file and open it in 7Zip. Next, drag and drop EVERYTHING inside the file into your `GAMMA` folder.

You can download it here if you haven't already: https://www.mediafire.com/file/uf6tiegzwrkmyv2/STALKER+XTREME+BETA.7z/file

After that, you will need **Arrival Anomalies**. The author of this mod says that this is still a WIP, so it cannot be included in the pack. However, it can still be used; you'll just need to download and install it yourself.

To do that, head to https://www.moddb.com/mods/stalker-anomaly/addons/arrival-anomalies and download it. Next, open MO2, and install it with your preferred settings in MO2 DIRECTLY under **XTREME Visuals & Actor Animations**. You won't need to do anything else, since **STALKER XTREME** comes with all the necessary settings and disabled mods. It should look like this in the MO2 load order:
    """,
    "part2": """
    You may also need to move the **XTREME Graphics Pack** and **XTREME Graphics Pack Optionals** mods to be placed under the **XTREME Graphics** separator if you renamed any of them. The same applies with the ReShade 6.3.3 DX11 mod, but that should be placed in **XTREME High-Priority** instead. Make sure that they look like this in the load order:
    """,
    "part3": """
    Once that's done, you should be good to go! If you have any issues, feel free to reach out to me, and I'll help you the best I can. Enjoy!
    """
}
important = "If the ReShade preset doesn't load, go to the **ReShade File Finder** page to locate it. Also, if you want to use **Arrival Anomalies** with **STALKER XTREME**, go to the **Arrival Anomalies** page."
mainlist = {

    "shaders": """
**Atmospherics GAMMA 2.67:** Completely revamps shaders and weather, as well as color grading and LUTs to give the game a realistic and immersive look.

**HollywoodFX V3.1.5:** Adds cinematic VFX for gunshots, explosions, and other effects, as well as better sounds for them.

**Shaders Look Better (Motion Blur & Shaders Improvements) V1.2.0:** Improves shaders and motion blur to be smoother and more realistic.

**Dark Signal Weather and Ambiance Audio - Shrike:** G.A.M.M.A.'s version of this mod, included for compatibility purposes.

    """,

    "main textures": """
**Anomaly Texture Overhaul 5 - PAUL_8558:** A complete texture overhaul that adds detailed 4K and 8K textures, which add to the depressing realism and immersion of the game.

**Re.Pack Texture Pack Series - Hades@DK:** Adds high-res textures - ranging from 4K to 16K - to many different surfaces around the Zone. It includes high-res textures for glass, barbed wire, pseudodogs, lurkers, doors, and so much more.
    """,

    "mask textures": """
**Grok's Masks and Reflections 2.1.0:** Redone mask lighting effects with reflections and refractions, using blurred versions of Nav's 4K Mask Textures.

**Drunk's 4K Mask Textures:** Adds realistic 4K mask textures, complete with droplets and a somewhat blurred overlay.
    """,

    "maps": """
    **Re.Pack PDA Package V1.3**: Adds 16K PDA maps that add even more detail and zooming capability to your PDA.
    """

}
optionalslist = {

    "seasonal": """
**Graupel's Winter Mod v1.0.2:** A mod that turns the Zone into a bright Winter wonderland, or an accurate representation of the early stages of Winter.

**Aydin's Grass Tweaks 4.0:** A recolored version of the Golden Autumn Retexture mod, made to fit different seasons.

**Re\:Pack Foliage Package 1.2:** Adds 16K textures to leaves.

**C-Consciousness Grass Overhaul v0.55:** Adds 8K foliage, with recolors and resizing to fit each season. Made by **Huh?**, with help from **Hoddminir** and poppy textures from **https://pngimg.com**.

**Rotten Life Ground Textures:** Adds 4K realistic terrain textures, available in Summer, Fall and Late Fall.
    """,

    "summer": """
**Aydin's Grass Tweaks 4.0**

**Re\:Pack Foliage Package**

**C-Consciousness Grass Overhaul v0.55**

**Rotten Life Ground Textures**

**ATO 5 Foliage Textures (Trees & Bushes - not grass)**
    """,

    "late fall": """
**Aydin's Grass Tweaks 4.0**

**Re\:Pack Foliage Package**

**C-Consciousness Grass Overhaul v0.55**

**Rotten Life Ground Textures**
    """,

    "early winter": """
**Graupel's Winter Mod v1.0.2**

**Aydin's Grass Tweaks 4.0**

**Re\:Pack Foliage Package**

**C-Consciousness Grass Overhaul v0.55**
    """,

    "winter": """
**Graupel's Winter Mod v1.0.2**
    """,

    "weather": """
**Weather Expansion for Atmospherics 1.66b:** Adds a wide variety of weathers to the game, all of which look realistic, yet cinematic.

**Apocalyptic Blowout Overhaul 4.0.1:** Revamps blowouts to look incredibly beautiful.

**A.D.E.G.A. Upscaled Sky Textures:** Adds upscaled sky textures from the A.D.E.G.A. texture multipack.

**Awesomedude's Weather Edits For Weather Expansion:** My own edits to the sunshafts during sunsets and sunrise to make them more cinematic.
    """,

    "luts": """
    **Atmospherics Pre-SSS 22 LUTs:** The LUTs from Atmospherics before the Screen Space Shaders 22 update. Courtesy of Shahryar.
""",

    "othermods": """
**Misery-Based Terrain 2.8:** Adds muddy terrain textures.
    """

}
screenshots = [
    "Army Warehouses Sunrise 1",
    "Army Warehouses Sunrise 2",
    "Army Warehouses Sunrise 3",
    "Cordon Sunrise 1",
    "Cordon Sunrise 2",
    "Cordon Sunrise Closeup 1",
    "Cordon Sunrise Closeup 2",
    "Cordon Sunset",
    "Rookie Village Campfire",
    "Winter Wonderland"
]

if page == "Home":

    st.title("XTREME Graphics Pack")
    st.write("This graphics pack is a nice and easy way to make your game look so much better. It features a series of mods to improve shaders, VFX, textures and overall visual fidelity.")

    st.write("---")

    with st.expander("**Preview Screenshots**"):

        st.header("Preview Screenshots:")

        showScreenshots(screenshots, ".png")

    st.write("---")

    st.header("Installation:")
    st.write(installation)

    st.subheader("IMPORTANT:")
    st.write(important)

    st.write("---")

    st.header("Mods Included With The Pack:")
    st.write(":grey[Textures are shown in the order in which they are loaded]")

    c1, c2 = st.columns(2)
    ex1, ex2 = c1.expander("**Main Pack**"), c2.expander("**Optionals Pack**")

    with ex1:

        st.header("Main Textures:")
        st.write(mainlist["main textures"])

        st.header("Shaders & VFX:")
        st.write(mainlist["shaders"])

        st.header("Mask Textures:")
        st.write(mainlist["mask textures"])

        st.header("16K PDA Maps:")
        st.write(mainlist["maps"])

    with ex2:
        st.header("Seasonal Mods:")
        st.write(optionalslist["seasonal"])

        st.subheader("Summer/Autumn:")
        st.write(optionalslist["summer"])

        st.subheader("Late Fall:")
        st.write(optionalslist["late fall"])

        st.subheader("Early Winter:")
        st.write(optionalslist["early winter"])

        st.subheader("Winter:")
        st.write(optionalslist["winter"])

        st.header("XTREME Weather:")
        st.write(optionalslist["weather"])

        st.header("XTREME LUTs:")
        st.write(optionalslist["luts"])

        st.header("Other Mods:")
        st.write(optionalslist["othermods"])

else:

    st.title(page)

    if page == "STALKER XTREME":

        st.write(stalkerxtreme['part1'])
        st.image("ArrivalLoadOrder.png")
        st.write(stalkerxtreme['part2'])

        c1, c2 = st.columns(2)
        c1.subheader("XGP Load Order")
        c1.image("XGPLoadOrder.png")
        c2.subheader("ReShade Load Order")
        c2.image("ReShadeLoadOrder.png")
        
        st.write(stalkerxtreme['part3'])

    elif page == "Modlist Compatibility":

        st.write("This will edit your MO2 modlist file to disable the mods that should be disabled, while keeping the rest of your modlist intact.")
        st.write("**Keep in mind that this will disable mods that GAMMA has enabled by default, so you will need to revert back to a previous GAMMA modlist or the default GAMMA modlist if you want to uninstall this pack. Make sure to keep a backup of your modlist if you plan on doing so.**")
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
                    shaders = st.checkbox("Shaders and VFX")
                    textures = st.checkbox("Main Textures")
                    masks = st.checkbox("Mask Textures and VFX")
                    maps = st.checkbox("Re\:Pack 16K PDA Maps")
                    seasonal = st.checkbox("Any Seasonal Pack (Summer, Autumn, Winter or Late Fall)")

                    userout = userfile

                    if baseshaders:
                        userout = disabledmods[version]["base shaders"] + userout

                    if shaders:
                        userout = disabledmods[version]["shaders"] + userout

                    if textures or seasonal:
                        userout = disabledmods[version]["textures"] + userout

                    if masks:
                        userout = disabledmods[version]["mask textures"] + userout

                    if maps:
                        userout = disabledmods[version]["maps"] + userout

                download = st.download_button("Download Converted File", data=userout, file_name="modlist.txt")

    elif page == "Load Atmospheric Preset":

        st.write("This will load the settings from the selected atmospheric preset (default is **`XTREME`**) into a copy of your game settings file, which you can download and use to replace your **`user.ltx`** (game settings) file.")

        atmospreset = atmospresets[st.radio("**Select a preset below:**", atmospresets)]
        userfile = st.file_uploader("**After that, upload your **`user.ltx`** file (**located in the `Anomaly/appdata/` folder**) here:**")

        st.write("Then, download the converted file, drag it into your **`Anomaly/appdata/`** folder and replace the existing file when prompted.")

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

    elif page == "Awesomedude's Graphics Settings":

        st.write("This will load my own graphics settings into your **`user.ltx`** (game settings) file, which you can download and use to replace your current **`user.ltx`** file.")
        st.write("Upload your **`user.ltx`** file (**located in the `Anomaly/appdata/` folder**) below.")
        st.write("Then, download the converted file, drag it into your **`Anomaly/appdata/`** folder and replace the existing file when prompted.")

        userfile = st.file_uploader("")

        if userfile != None:

            if userfile.name != "user.ltx":
                st.subheader("This is not a valid game settings file. Please use a valid file.")

            else:

                write = ""

                if st.checkbox("Graphics Settings", True):
                    write += graphicssettings

                if st.checkbox("Camera Inertia Settings"):
                    write += caminert

                if st.checkbox("Field of View Settings"):
                    write += fov

                strio = StringIO(userfile.getvalue().decode("utf-8"))
                userout = strio.read() + write
                download = st.download_button("Download Converted File", data=userout, file_name="user.ltx")

    elif page == "ReShade File Finder":

        st.write("This page will give you the path to your ReShade file. Just enter the information below (highlight a folder in File Explorer and use `Ctrl+Shift+C` to copy its path), and hit **Locate**. Then, the path of the ReShade presets folder will show below. Copy it and paste it in the ReShade menu, and select the ReShade preset that you want (I recommend XTREME RTGI).")

        gammapath = st.text_input("Enter the file path of your **GAMMA** folder:")
        rename = st.checkbox("Did you rename the **XTREME Graphics Pack** mod?")
        name = "XTREME Graphics Pack"
        separator = "/"

        if gammapath != "":

            if rename:
                name = st.text_input("What did you rename it to?")

            if gammapath[2] == "\\":
                separator = "\\"

            if gammapath[-1] == separator:
                gammapath = gammapath[:-1]

            if st.button("Locate"):
                st.write(f"**Preset Folder Path: `{gammapath}{separator}mods{separator}{name}{separator}bin{separator}`**")

    elif page == "Atmospheric Preset Editor":

        st.write("This page will allow you to create your **own** atmospheric preset.")
        st.write("On the sidebar to the left, select the settings that you want to add to your preset. Then, fill out the fields that appear below.")

        preset = ""
        settings = {}

        with st.sidebar.expander("**Settings**"):

            startfrom = st.radio("**How do you want to start creating your preset?**", ["Start From Scratch", "Start From an XTREME Preset", "Start From an Existing Preset"])

            if startfrom == "Start From an XTREME Preset":
                atmospreset = atmospresets[st.radio("**Select an XTREME Preset to Start From:**", atmospresets)]

            elif startfrom == "Start From an Existing Preset":

                existingpreset = st.file_uploader("**Upload your preset here:**")

                if existingpreset != None:

                    if existingpreset.name[-4:] == ".ltx":
                        strio = StringIO(existingpreset.getvalue().decode("utf-8"))
                        preset = strio.read()+"\n\n\n"

                    else:
                        st.write("This is not a valid preset. Make sure to upload one that has a \"`.ltx`\" file extension - they can be found in the `appdata` folder in a mod, or the base `Anomaly` folder.")

            st.header("Preset Settings")

            selectall = st.checkbox("Select All", True)

            st.subheader("Main Shader Settings")

            selectallss = st.checkbox("Select All Shader Settings", selectall)
            shader1 = st.checkbox("Bright Colors", selectallss)
            shader2 = st.checkbox("Dark Colors", selectallss)
            shader3 = st.checkbox("Shader Gamma (mid-range colors)", selectallss)
            shader4 = st.checkbox("Contrast", selectallss)

            st.subheader("Post-Processing")

            selectallpp = st.checkbox("Select All Post-Process Settings", selectall)
            exposure = st.checkbox("Camera Exposure", selectallpp)
            gamma = st.checkbox("Display Gamma", selectallpp)
            saturation = st.checkbox("Color Saturation/Strength", selectallpp)
            cgrading = st.checkbox("Color Grading", selectallpp)

            st.subheader("Grass Settings")

            selectallgs = st.checkbox("Select All Grass Settings", selectall)
            grassheight = st.checkbox("Grass Size", selectallgs)
            grassdensity = st.checkbox("Grass Density", selectallgs)
            grassrender = st.checkbox("Grass Render Distance", selectallgs)

            st.subheader("Advanced Options")

            selectallao = st.checkbox("Select All Advanced Options", selectall)
            mblur = st.checkbox("Motion Blur Intensity", selectallao)
            sunlum = st.checkbox("Sun Brightness", selectallao)
            sunlumamb = st.checkbox("Ambient Sunlight Brightness", selectallao)
            tonemapamt = st.checkbox("Tonemapping Amount", selectallao)
            tonemapadapt = st.checkbox("Tonemapping Adaptation", selectallao)

            st.subheader("Screen Space FX Settings")

            selectallssfx = st.checkbox("Select All SSFX Settings", selectall)
            hudhemi = st.checkbox("Additional HUD Brightness", selectallssfx)

        if exposure or gamma or saturation or cgrading:

            st.write("---")
            st.header("Post-Processing")

            cols = st.columns(3)

            colindex = 0

            if exposure:
                settings['r__exposure'] = cols[colindex].slider("**Camera Exposure (`r__exposure`)**", min_value=0.5, max_value=4.0, value=1.0, step=0.01)
                colindex += 1

            if gamma:
                settings['r__gamma'] = cols[colindex].slider("**Display Gamma (`r__gamma`)**", min_value=0.5, max_value=2.2, value=1.0, step=0.01)
                colindex += 1

            if saturation:
                settings['r__saturation'] = cols[colindex].slider("**Color Saturation (`r__saturation`)**", min_value=0.0, max_value=2.0, value=1.0, step=0.01)

            st.header("")
            st.subheader("**Color Grading**")
            st.write("**(`r__color_grading`)**")

            cols = st.columns(3)

            if cgrading:
                settings["r__color_grading"] = [cols[0].number_input("**Red**", min_value=0.0, max_value=1.0, value=0.0, step=0.01), cols[1].number_input("**Green**", min_value=0.0, max_value=1.0, value=0.0, step=0.01), cols[2].number_input("**Blue**", min_value=0.0, max_value=1.0, value=0.0, step=0.01)]

        if grassheight or grassdensity or grassrender:

            st.write("---")
            st.header("Grass Settings (SAVE RELOAD REQUIRED)")

            cols = st.columns(3)

            colindex = 0

            if grassheight:
                settings['r__detail_height'] = cols[colindex].slider("**Grass Size (`r__detail_height`)**", min_value=0.5, max_value=2.0, value=0.8, step=0.01)
                colindex += 1

            if grassdensity:
                settings['r__detail_density'] = 1 - ( cols[colindex].slider("**Grass Density (`r__detail_density`)**", min_value=0.0, max_value=1.0, value=0.5, step=0.01) * (0.96) )
                colindex += 1

            if grassrender:
                settings['r__detail_radius'] = cols[colindex].slider("**Grass Render Distance (`r__detail_radius`)**", min_value=0, max_value=250, value=150, step=5)


        if sunlum or sunlumamb or tonemapamt or tonemapadapt:

            st.write("---")
            st.header("Advanced Options")

            if mblur:
                mblurintensity = st.slider("**Motion Blur Intensity (set to 0 to turn off) (`r2_mblur_enabled` & `r2_mblur`)**", min_value=0.0, max_value=1.0, value=0.0, step=0.01)

                if mblurintensity == 0:
                    settings["r2_mblur_enabled"] = "off"
                else:
                    settings["r2_mblur_enabled"] = "on"

                settings['r2_mblur'] = mblurintensity

            if sunlum:
                settings['r2_sun_lumscale'] = st.slider("**Sun Brightness (`r2_sun_lumscale`)**", min_value=-1.0, max_value=3.0, value=3.0, step=0.01)

            if sunlumamb:
                settings['r2_sun_lumscale_amb'] = st.slider("**Ambient Sunlight Brightness (`r2_sun_lumscale_amb`)**", min_value=0.0, max_value=3.0, value=2.0, step=0.01)

            if tonemapamt:

                tonemapamtinput = st.slider("**Tonemapping Amount - Set to 0 to turn off tonemapping (`r2_tonemap` & `r2_tonemap_amount`)**", min_value=0.0, max_value=1.0, value=0.5, step=0.01)

                if tonemapamtinput == 0:
                    settings['r2_tonemap'] = "off"

                else:
                    settings['r2_tonemap'] = "on"

                settings['r2_tonemap_amount'] = tonemapamtinput

            if tonemapadapt:
                settings['r2_tonemap_adaptation'] = st.slider("**Tonemapping Adaptation (`r2_sun_lumscale_amb`)**", min_value=0.01, max_value=10.0, value=3.0, step=0.01)

        if hudhemi:

            st.write("---")
            st.header("Screen Space FX Settings")

            settings['ssfx_hud_hemi'] = st.number_input("**Additional HUD Brightness (`ssfx_hud_hemi`)**", min_value=0.0, max_value=1.0, value=0.0, step=0.01)

        if shader1 or shader2 or shader3 or shader4:

            st.write("---")
            st.header("Main Shader Settings")

            cols = st.columns(5)

            cols[0].write("**Setting (Parameter)**")
            cols[1].write("**Red Intensity**")
            cols[2].write("**Green Intensity**")
            cols[3].write("**Blue Intensity**")
            cols[4].write("**Overall Intensity**")

            cols[0].write("")

            if shader1:
                cols[0].write("**Bright Colors (0 to 1)**")
                cols[0].write("**`shader_param_1`**")
                settings['shader_param_1'] = [cols[1].number_input("Red1", min_value=0.0, max_value=1.0, value=1.0, step=0.01, label_visibility="hidden"), cols[2].number_input("Green1", min_value=0.0, max_value=1.0, value=1.0, step=0.01, label_visibility="hidden"), cols[3].number_input("Blue1", min_value=0.0, max_value=1.0, value=1.0, step=0.01, label_visibility="hidden"), cols[4].number_input("**Overall Intensity Offset 1**", min_value=0.0, max_value=1.0, value=0.0, step=0.01, label_visibility="hidden")]

            if shader2:
                cols[0].write("**Dark Colors (0 to 1)**")
                cols[0].write("**`shader_param_2`**")
                settings['shader_param_2'] = [cols[1].number_input("Red2", min_value=0.0, max_value=1.0, value=0.0, step=0.01, label_visibility="hidden"), cols[2].number_input("Green2", min_value=0.0, max_value=1.0, value=0.0, step=0.01, label_visibility="hidden"), cols[3].number_input("Blue2", min_value=0.0, max_value=1.0, value=0.0, step=0.01, label_visibility="hidden"), cols[4].number_input("**Overall Intensity Offset 2**", min_value=0.0, max_value=1.0, value=0.0, step=0.01, label_visibility="hidden")]

            if shader3:
                cols[0].write("**Shader Gamma (-1 to 1)**")
                cols[0].write("**`shader_param_3`**")
                settings['shader_param_3'] = [cols[1].number_input("Red3", min_value=-1.0, max_value=1.0, value=1.0, step=0.01, label_visibility="hidden"), cols[2].number_input("Green3", min_value=-1.0, max_value=1.0, value=1.0, step=0.01, label_visibility="hidden"), cols[3].number_input("Blue3", min_value=-1.0, max_value=1.0, value=1.0, step=0.01, label_visibility="hidden"), cols[4].number_input("**Overall Intensity Offset 3**", min_value=0.0, max_value=1.0, value=0.0, step=0.01, label_visibility="hidden")]

            if shader4:
                cols[0].write("**Contrast (-1 to 1)**")
                cols[0].write("**`shader_param_4`**")
                settings['shader_param_4'] = [cols[1].number_input("Red4", min_value=-1.0, max_value=1.0, value=1.0, step=0.01, label_visibility="hidden"), cols[2].number_input("Green4", min_value=-1.0, max_value=1.0, value=1.0, step=0.01, label_visibility="hidden"), cols[3].number_input("Blue4", min_value=-1.0, max_value=1.0, value=1.0, step=0.01, label_visibility="hidden"), cols[4].number_input("**Overall Intensity Offset 4**", min_value=-1.0, max_value=1.0, value=0.0, step=0.01, label_visibility="hidden")]

        for param, val in zip(settings, settings.values()):

            if type(val) == list:

                preset += f"{param} ("

                for v in val:
                    if type(v) != str:
                        preset += f"{round(v, 2)}, "
                    else:
                        preset += f"{v}, "

                preset = preset[:-2]+")\n"

            else:

                if type(val) != str:
                    preset += f"{param} {round(val, 2)}\n"
                else:
                    preset += f"{param} {val}\n"


        if preset != None:

            st.header("Final Steps")

            preset = preset.split("\n")

            rnewline = True
            rcgnewline = True
            r2newline = True
            ssfxnewline = True
            shadernewline = True

            for line in range(len(preset)):

                if "r__" in preset[line] and rnewline:
                    preset[line] = "\n"+str(preset[line])
                    rnewline = False

                if "r__color_grading" in preset[line] and rcgnewline:
                    preset[line] = "\n"+str(preset[line])
                    rcgnewline = False

                if "r2_" in preset[line] and r2newline:
                    preset[line] = "\n"+str(preset[line])
                    r2newline = False

                if "ssfx" in preset[line] and ssfxnewline:
                    preset[line] = "\n"+str(preset[line])
                    ssfxnewline = False

                if "shader_param" in preset[line] and shadernewline:
                    preset[line] = "\n"+str(preset[line])
                    shadernewline = False

            preset = "\n".join(preset)

            if startfrom == "Start From an XTREME Preset":
                preset = atmospreset+"\n\n"+preset

            presetname = st.text_input("What do you want to name your preset?", "MyPreset.ltx").strip()

            if presetname[-4:] != ".ltx":
                presetname = presetname + ".ltx"

            with st.expander("**Preset Preview**", expanded=True):

                st.header(presetname)
                st.write(f"```{preset}\n```")

            st.download_button(f"**Download Your Preset (:blue[{presetname}])**", data=preset, file_name=presetname)

    elif page == "Arrival Anomalies":

        st.write("Download **Arrival Anomalies** and install it using the instructions on here: **https://www.moddb.com/mods/stalker-anomaly/addons/arrival-anomalies**")
        st.write("Then, go to your `GAMMA/profiles/XTREME/` folder and upload your `modlist.txt` file below (ONLY IF YOU ARE USING **STALKER XTREME**). After that, enter the name of the mod when you installed it below. Finally, download the converted file, and replace your `modlist.txt` file with it (close and reopen MO2 if it was open).")

        userfile = st.file_uploader("")

        if userfile != None:

            if userfile.name != "modlist.txt":
                st.subheader("This is not a valid modlist file. Please use a valid file.")

            else:

                strio = StringIO(userfile.getvalue().decode("utf-8"))
                userfile = strio.read()

                mods = userfile.split("\n")
                userout = []

                name = st.text_input("What did you name the mod while installing it?")

                for mod in mods:

                    if userout == []:
                        userout = [mod]

                    else:

                        if "XTREME Visuals and Actor Animations" in mod:
                            userout.append(f"+{name}")
                            print(userout)

                        userout.append(mod)

                userout = "\n".join(userout)
                download = st.download_button("Download Converted File", data=userout, file_name="modlist.txt")
