import streamlit as st
from io import StringIO

st.set_page_config(layout="wide", initial_sidebar_state="expanded")

page = st.sidebar.radio("**Navigation:**", ["Home", "Modlist Compatibility", "Load Atmospheric Preset", "MCM Settings For SSS", "Awesomedude's Graphics Settings", "ReShade File Finder", "Arrival Anomalies"])
atmospreset = """
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
shader_param_3 (0.838, 0.847, 0.852, -0.2)
shader_param_4 (1.12, 1.12, 1.13, -0.4)
"""
disabledmods = {

":green[**G.A.M.M.A.**]": {

    "mask textures": """-G.A.M.M.A. No Masks Textures
-129- Mask Reflections - shader fix - Grokitach
""",

    "base shaders": """-190- Screen Space Shaders 20 - Ascii1457
-189- Beef's NVG - theRealBeef
-188- Enhanced Shaders - KennShade
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
        ssfx_module/general/shaderscope_patch_mcm = false
        ssfx_module/il/blur_mcm          = 0.1
        ssfx_module/il/distance_mcm      = 300
        ssfx_module/il/flora_int_mcm     = 1
        ssfx_module/il/global_int_mcm    = 4
        ssfx_module/il/hud_int_mcm       = 1
        ssfx_module/il/quality_mcm       = 16
        ssfx_module/il/res_mcm           = 0.15
        ssfx_module/il/vibrance_mcm      = 0.6
        ssfx_module/inter_grass/anomalies_distance_mcm = 30
        ssfx_module/inter_grass/enable_anomalies_mcm = true
        ssfx_module/inter_grass/enable_mcm = true
        ssfx_module/inter_grass/enable_mutants_mcm = true
        ssfx_module/inter_grass/enable_player_mcm = true
        ssfx_module/inter_grass/explosions_speed_mcm = 5
        ssfx_module/inter_grass/explosions_str_mcm = 1
        ssfx_module/inter_grass/horizontal_str_mcm = 2
        ssfx_module/inter_grass/max_distance_mcm = 2000
        ssfx_module/inter_grass/max_entities_mcm = 8
        ssfx_module/inter_grass/radius_mcm = 1.4
        ssfx_module/inter_grass/shooting_range_mcm = 2
        ssfx_module/inter_grass/shooting_str_mcm = 0.3
        ssfx_module/inter_grass/vertical_str_mcm = 2
        ssfx_module/parallax/ao_mcm      = 0.6
        ssfx_module/parallax/height_mcm  = 0.035
        ssfx_module/parallax/quality_mcm = 16
        ssfx_module/parallax/range_mcm   = 40
        ssfx_module/parallax/refine_mcm  = false
        ssfx_module/shadows/lod_max_mcm  = 0
        ssfx_module/shadows/lod_min_mcm  = 1
        ssfx_module/shadows/lod_quality_mcm = 3
        ssfx_module/shadows/volumetric_force_mcm = true
        ssfx_module/shadows/volumetric_int_mcm = 0.5
        ssfx_module/shadows/volumetric_quality_mcm = 3
        ssfx_module/shw_cascades/grass_shw_distance_mcm = 100
        ssfx_module/shw_cascades/grass_shw_nondir_maxdistance_mcm = 50
        ssfx_module/shw_cascades/grass_shw_quality_mcm = 1
        ssfx_module/shw_cascades/size_1_mcm = 14
        ssfx_module/shw_cascades/size_2_mcm = 40
        ssfx_module/shw_cascades/size_3_mcm = 126
        ssfx_module/ssfx_pp/ssfx_bloom/blur_mcm = 1
        ssfx_module/ssfx_pp/ssfx_bloom/dirt_mcm = 0.8
        ssfx_module/ssfx_pp/ssfx_bloom/exposure_mcm = 1
        ssfx_module/ssfx_pp/ssfx_bloom/lens_mcm = 1.5
        ssfx_module/ssfx_pp/ssfx_bloom/sky_mcm = 0.3
        ssfx_module/ssfx_pp/ssfx_bloom/threshold_mcm = 10
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
        ssfx_module/ssfx_rain_module/ssfx_rain_main/quality_mcm = 2
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
        ssfx_module/sss/quality_dir_mcm  = 24
        ssfx_module/sss/quality_point_mcm = 8
        ssfx_module/terrain/distance_mcm = 20
        ssfx_module/terrain/grass_align_mcm = true
        ssfx_module/terrain/grass_slope_mcm = 76
        ssfx_module/terrain/pom_height_mcm = 0.04
        ssfx_module/terrain/pom_quality_mcm = 36
        ssfx_module/terrain/pom_range_mcm = 40
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
        ssfx_module/wind/trees_speed_mcm = 11.1
        ssfx_module/wind/trees_trunk_mcm = 0.17
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

        dynamic_tonemap_extended/adaptation = 3
        dynamic_tonemap_extended/enable_dynamic_tonemap = true
        dynamic_tonemap_extended/k_amount = 0.1
        dynamic_tonemap_extended/k_lowlum = 0.1
        dynamic_tonemap_extended/k_lumscale_amb = 0.05
        dynamic_tonemap_extended/k_lumscale_amb_addition = 0.07
        dynamic_tonemap_extended/k_lumscale_hemi = 0.01
        dynamic_tonemap_extended/k_lumscale_hemi_addition = 0.05
        dynamic_tonemap_extended/k_middle = 0.05
        dynamic_tonemap_extended/max_amount = 1
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
r1_ssa_lod_a 64.
r1_ssa_lod_b 48.
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
r2_mask_control (0.000000, 0.000000, 0.000000, 0.000000)
r2_mblur 0.02451
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
r2_ssa_lod_a 32.
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
r2_sun_lumscale_amb 1.19482
r2_sun_lumscale_hemi 0.95
r2_sun_near 15.
r2_sun_near_border 0.75
r2_sun_quality st_opt_medium
r2_sun_tsm on
r2_sun_tsm_bias 0.5
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
r2_tonemap_amount 0.3
r2_tonemap_lowlum 0.5
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
r4_hdr10_colorspace 0
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
r4_hdr10_ui_nits 140.
r4_hdr10_ui_saturation 0.5
r4_hdr10_whitepoint_nits 400.
r4_wireframe off
r__3Dfakescope 1
r__actor_shadow on
r__bloom_thresh (0.700000, 0.800000, 0.900000, 0.000000)
r__bloom_weight (0.330000, 0.330000, 0.330000, 0.000000)
r__clear_models_on_unload off
r__color_grading (0.000000, 0.000000, 0.000000)
r__detail_density 0.34
r__detail_height 1.
r__detail_radius 110
r__dtex_range 50.
r__enable_grass_shadow off
r__exposure 1.
r__fakescope 0
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
r__saturation 0.8
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
shader_param_1 (0.990000, 1.000000, 0.970000, -0.300000)
shader_param_2 (0.000000, 0.000000, 0.000000, 0.000000)
shader_param_3 (0.900000, 0.870000, 0.820000, -0.300000)
shader_param_4 (1.120000, 1.120000, 1.130000, -0.400000)
shader_param_5 (1.000000, 0.000000, 0.000000, 0.000000)
shader_param_6 (0.000000, 1.000000, 0.000000, 0.000000)
shader_param_7 (1.000000, 0.550000, 0.000000, 0.000000)
shader_param_8 (0.000000, 10.300000, 100.000000, 10.000000)
sil_glow_color (1.000000, 0.000000, 0.000000)
sil_glow_cool_temp_rate 0.01
sil_glow_max_temp 0.15
sil_glow_shot_temp 0.004
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
ssfx_hud_drops_1 (470.012909, 1.000000, 30.000000, 0.050000)
ssfx_hud_drops_2 (0.225000, 1.500000, 0.400000, 2.000000)
ssfx_hud_hemi 0.
ssfx_il (6.666667, 4.000000, 0.600000, 0.500000)
ssfx_il_quality 16
ssfx_il_setup1 (300.000000, 1.000000, 1.000000, 0.000000)
ssfx_int_grass_params_1 (1.400000, 2.000000, 2.000000, 30.000000)
ssfx_int_grass_params_2 (1.000000, 5.000000, 0.300000, 2.000000)
ssfx_is_underground 0
ssfx_lightsetup_1 (0.600000, 0.600000, 0.000000, 0.000000)
ssfx_lut (1.000000, 13.000000, 0.000000, 0.000000)
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
ssfx_terrain_grass_slope 1.
ssfx_terrain_offset (-0.120000, -0.050000, -0.150000, 0.000000)
ssfx_terrain_pom (12.000000, 20.000000, 0.040000, 1.000000)
ssfx_terrain_pom_refine 0
ssfx_terrain_quality (8.000000, 0.000000, 0.000000, 0.000000)
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
Download these modded exes: https://github.com/themrdemonized/xray-monolith/releases/download/2025.1.22/STALKER-Anomaly-modded-exes_2025.1.22.zip, open the file in 7Zip, and extract ALL the files into your Anomaly folder.

Then, download and install these files **in the order shown** using the links below; install them like any other mod in MO2, placing them at the bottom of your modlist. Because of the size of the mod, MO2 may freeze during the installation; just wait for a bit for the mod to be installed and MO2 will be functional again.

**XTREME GRAPHICS PACK MAIN FILE: https://drive.google.com/uc?export=download&id=1h0nS_IBgu8UVvR9MUtLur--97Nv5XUWe**

**XTREME GRAPHICS OPTIONALS: https://drive.google.com/uc?export=download&id=1JwDFXzc4x8Kk7NJcd95IJ-7HxUzB-szH**

**RESHADE: https://drive.google.com/uc?export=download&id=1k_nM1rgbatpw-FLxl3c4g90mx7I_6IOn**

You can also get **STALKER XTREME**, which is a modpack full of mods to greatly enhance the realism and immersiveness of the zone. Certain mods that are disabled may be re-enabled, but they might cause issues. I'll offer as much support for them as I can.

**STALKER XTREME BETA (REQUIRES A NEW GAME, INSTALL INSTRUCTIONS ARE INSIDE): https://www.mediafire.com/file/1q0pdiyapey25zs/STALKER+XTREME+BETA.7z/file**

From there, follow the instructions on the **Modlist Compatibility** and **MCM Settings For SSS** pages on this site to modify your settings and mod list files to work with this pack.

Finally, you can either use the **Load Atmospheric Preset** page or just open the game and type `cfg_load xtreme` to load the atmospheric settings. If you are using **STALKER XTREME**, I recommend getting ALL of my graphics settings to ensure everything works properly.
"""
important = "If the ReShade preset doesn't load, go to the **ReShade File Finder** page to locate it. Also, if you want to use **Arrival Anomalies** with **STALKER XTREME**, go to the **Arrival Anomalies** page."
mainlist = {

    "base shaders": """
**Enhanced Shaders & Colour Grading 1.10:** Improved shaders and color grading methods.

**Beef's NVGs Improved 1.5:** Improved night vision goggle overlays by TheRealBeef.

**Screen Space Shaders 22:** Screen space shaders with volumetric lighting and some post-processing effects.
    """,

    "shaders": """
**Atmospherics GAMMA 2.67:** Completely revamps shaders and weather, as well as color grading and LUTs to give the game a realistic and immersive look.

**HollywoodFX V3.1.5:** Adds cinematic VFX for gunshots, explosions, and other effects, as well as better sounds for them.

**Shaders Look Better (Motion Blur & Shaders Improvements) V1.2.0:** Improves shaders and motion blur to be smoother and more realistic.

**Dark Signal Weather and Ambiance Audio - Shrike:** G.A.M.M.A.'s version of this mod, included for compatibility purposes.

    """,

    "main textures": """
**Global Texture Rework BETA:** A full texture overhaul that adds 2K and 4K textures to the game, which give the Zone a lifeless and worn-out look.

**Rotten Life Texture Pack:** A texture pack that adds old-themed 4K and 8K textures, which give structures in the Zone a cozy, yet run-down and scrappy look.

**Anomaly Texture Overhaul 4 - PAUL_8558:** A complete texture overhaul that adds detailed 4K and 8K textures, which add to the depressing realism and immersion of the game.

**Re.Pack Doors V1.0:** Adds 4K textures to doors.

**Re.Pack Glass & Windows V1.5:** Adds 4K textures to glass and windows, complete with scratches, dust, dirt and cracks for added immersion.

**Re.Pack Barbed Wire V1.1:** Adds 4K textures to barbed wire.

**Re.Pack Signs V1.0:** Adds 4K textures for signs, with added details like bullet holes, moss or cracks.

**Re.Pack Pseudogiant 1.7:** Adds a new high-definition texture for pseudogiants.

**Re.Pack Crow 1.0:** Adds a new high-definition texture for crows.

**Vehicle Textures Redux V1.3.1:** Adds redone 4K textures for vehicles,
    """,

    "mask textures": """
**Grok's Masks and Reflections 2.1.0:** Redone mask lighting effects with reflections and refractions, using blurred versions of Nav's 4K Mask Textures.

**Drunk's 4K Mask Textures:** Adds realistic 4K mask textures, complete with droplets and a somewhat blurred overlay.
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
    "Cinematic Late Fall Cordon Sunrise",
    "Summer Cordon Sunset",
    "Late Fall Cordon Sunrise 1",
    "Late Fall Cordon Sunrise 2",
    "Late Fall Cordon Sunrise 3",
    "Late Fall Army Warehouses Sunrise 1",
    "Late Fall Army Warehouses Sunrise 2",
    "Late Fall Army Warehouses Sunrise 3",
    "Winter Wonderland",
    "Rookie Village Campfire"
]

if page == "Home":
    
    st.title("XTREME Graphics Pack For G.A.M.M.A.")
    st.write("This graphics pack is a nice and easy way to make your game look so much better. It features a series of mods to improve shaders, VFX, textures and overall visual fidelity.")

    st.write("---")

    with st.expander("**Preview Screenshots**"):

        st.header("Preview Screenshots:")

        for img in screenshots:
            st.image(img+".png", img)

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

        st.header("Base Shaders:")
        st.write(mainlist["base shaders"])

        st.header("Main Textures:")
        st.write(mainlist["main textures"])

        st.header("Shaders & VFX:")
        st.write(mainlist["shaders"])
        
        st.header("Mask Textures:")
        st.write(mainlist["mask textures"])

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

        st.write("This will load the settings from the **`XTREME`** atmospheric preset file into a copy of your game settings file, which you can download and use to replace your **`user.ltx`** (game settings) file.")
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
