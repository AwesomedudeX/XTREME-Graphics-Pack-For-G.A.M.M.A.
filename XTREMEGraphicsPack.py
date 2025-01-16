import streamlit as st
from io import StringIO

st.set_page_config(layout="wide", initial_sidebar_state="expanded")

page = st.sidebar.radio("**Navigation:**", ["Home", "Modlist Compatibility", "Load Atmospheric Preset", "MCM Settings For SSS", "Awesomedude's Graphics Settings", "**STALKER XTREME** Modlist Compatibility"])
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
r2_sun_lumscale 1.5
r2_sun_lumscale_hemi 1.41
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
r2_sun_tsm_bias 0.5
ssfx_hud_hemi 0

shader_param_1 (0.99, 1, 0.97, -0.1)
shader_param_2 (0, 0, 0, 0.1)
shader_param_3 (0.838, 0.847, 0.852, 0)
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
        ssfx_module/ao/blur_mcm          = 0.1
        ssfx_module/ao/distance_mcm      = 300
        ssfx_module/ao/flora_int_mcm     = 0.4
        ssfx_module/ao/global_int_mcm    = 2
        ssfx_module/ao/hud_int_mcm       = 1
        ssfx_module/ao/max_occ_mcm       = 0.06
        ssfx_module/ao/quality_mcm       = 8
        ssfx_module/ao/radius_mcm        = 1
        ssfx_module/ao/res_mcm           = 0.5
        ssfx_module/florafixes/grass_specular_mcm = 0.15
        ssfx_module/florafixes/grass_specular_wet_mcm = 0.18
        ssfx_module/florafixes/sss_color_mcm = 0.38
        ssfx_module/florafixes/sss_int_mcm = 4.6
        ssfx_module/florafixes/trees_specular_mcm = 0.14
        ssfx_module/florafixes/trees_specular_wet_mcm = 0.15
        ssfx_module/general/shaderscope_patch_mcm = false
        ssfx_module/il/blur_mcm          = 0.1
        ssfx_module/il/distance_mcm      = 150
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
        ssfx_module/parallax/quality_mcm = 36
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
        ssfx_module/ssfx_pp/ssfx_bloom/sky_mcm = 0.6
        ssfx_module/ssfx_pp/ssfx_bloom/threshold_mcm = 10
        ssfx_module/ssfx_pp/ssfx_bloom/use_weather_mcm = false
        ssfx_module/ssfx_pp/ssfx_bloom/vibrance_mcm = 1.35
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
r2_detail_bump on
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
r2_mblur 0.02816
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
r2_steep_parallax on
r2_sun on
r2_sun_depth_far_bias -0.00002
r2_sun_depth_far_scale 0.99988
r2_sun_depth_near_bias 0.00007
r2_sun_depth_near_scale 0.9998
r2_sun_details on
r2_sun_far 100.
r2_sun_focus on
r2_sun_lumscale 1.5
r2_sun_lumscale_amb 1.35
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
r2_tonemap_lowlum 0.25
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
r4_enable_tessellation on
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
r__detail_density 0.68
r__detail_height 0.7
r__detail_radius 150
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
r__optimize_dynamic_geom 1
r__optimize_shadow_geom off
r__optimize_static_geom 2
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
rs_vis_distance 1.
s3ds_param_1 (4.000000, 4.000000, 0.300000, 0.000000)
s3ds_param_2 (0.000000, 0.000000, 0.000000, 1.500000)
s3ds_param_3 (0.000000, 0.000000, 0.000000, 0.020000)
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
shader_param_1 (0.990000, 1.000000, 0.970000, -0.100000)
shader_param_2 (0.000000, 0.000000, 0.000000, 0.100000)
shader_param_3 (0.838000, 0.847000, 0.852000, 0.00000)
shader_param_4 (1.120000, 1.120000, 1.130000, -0.400000)
shader_param_5 (0.000000, 0.000000, 0.000000, 0.000000)
shader_param_6 (0.000000, 1.000000, 0.000000, 0.000000)
shader_param_7 (1.000000, 0.550000, 0.000000, 0.000000)
shader_param_8 (0.000000, 10.300000, 100.000000, 10.000000)
ssfx_ao (2.000000, 10.000000, 0.100000, 1.000000)
ssfx_ao_quality 8
ssfx_ao_setup1 (300.000000, 1.000000, 0.400000, 0.060000)
ssfx_blood_decals (0.600000, 0.600000, 0.000000, 0.000000)
ssfx_bloom_1 (10.000000, 1.000000, 0.000000, 0.600000)
ssfx_bloom_2 (1.000000, 1.350000, 1.500000, 0.800000)
ssfx_bloom_use_presets 0
ssfx_florafixes_1 (0.150000, 0.180000, 0.140000, 0.150000)
ssfx_florafixes_2 (4.600000, 0.380000, 0.000000, 0.000000)
ssfx_gloss_factor 0.89822
ssfx_gloss_method 1
ssfx_gloss_minmax (0.700000, 0.950000, 0.000000)
ssfx_grass_interactive (1.000000, 8.000000, 2000.000000, 1.000000)
ssfx_grass_shadows (1.000000, 1.000000, 50.000000, 0.000000)
ssfx_hud_drops_1 (0.000000, 0.000000, 30.000000, 0.050000)
ssfx_hud_drops_2 (0.225000, 1.500000, 0.400000, 2.000000)
ssfx_hud_hemi 0.
ssfx_il (6.666667, 4.000000, 0.600000, 0.500000)
ssfx_il_quality 16
ssfx_il_setup1 (150.000000, 1.000000, 1.000000, 0.000000)
ssfx_int_grass_params_1 (1.400000, 2.000000, 2.000000, 30.000000)
ssfx_int_grass_params_2 (1.000000, 5.000000, 0.300000, 2.000000)
ssfx_is_underground 0
ssfx_lightsetup_1 (0.600000, 0.600000, 0.000000, 0.000000)
ssfx_lut (1.000000, 9.000000, 0.000000, 0.000000)
ssfx_pom (16.000000, 40.000000, 0.035000, 0.600000)
ssfx_pom_refine 0
ssfx_rain_1 (1.100000, 0.030000, 0.700000, 2.000000)
ssfx_rain_2 (1.000000, 0.000000, 2.500000, 1.000000)
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
ssfx_terrain_offset (-0.100000, -0.050000, -0.100000, 0.000000)
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
Download these modded exes: https://github.com/themrdemonized/xray-monolith/releases/download/2024.12.9/STALKER-Anomaly-modded-exes_2024.12.9.zip. Then, open the downloaded file in 7Zip, and just drag and drop everything in the file into your Anomaly folder; replace the existing files when prompted.

Then, download and install these files **in the order shown** using the links below; install them like any other mod in MO2, placing them at the bottom of your modlist. Because of the size of the mod, MO2 may freeze during the installation; just wait for a bit for the mod to be installed and MO2 will be functional again.

**STALKER XTREME BETA 0.5: https://drive.google.com/uc?export=download&id=1yoPv5f8IESSiLe1u9TMbPFD28zcRUXXz**

**XTREME GRAPHICS PACK: https://drive.google.com/uc?export=download&id=1DwzwPiSmS22ylzvI6UdubwMh0LVcWP1h**

**XTREME GRAPHICS OPTIONALS: https://drive.google.com/uc?export=download&id=17LBuPvmTKmVjoZ12TnMC-OBE1Fu4b6c3**

**RESHADE: https://drive.google.com/uc?export=download&id=1k_nM1rgbatpw-FLxl3c4g90mx7I_6IOn**

From there, follow the instructions on the **Load Atmospheric Preset**, **Modlist Compatibility** and **MCM Settings For SSS** pages to modify your settings and mod list files to work with this pack.

You will need to use the **Awesomedude's Graphics Settings** and **STALKER XTREME Modlist Compatibility** pages as well if you are using **STALKER XTREME**.

Finally, I’d really appreciate if you could send a message in the forum regardless of whether you have issues or not, just so that you show up as a member of the forum. This way, I can keep track of how many people are using the pack.
"""
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

**Anomaly Texture Overhaul 4:** A complete texture overhaul that adds detailed 4K and 8K textures, which add to the depressing realism and immersion of the game.

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
**Apocalyptic Blowout Overhaul 4.0.1:** Revamps blowouts to look incredibly beautiful.

**Weather Expansion for Atmospherics 1.66b:** Adds a wide variety of weathers to the game, all of which look realistic, yet cinematic.

**Awesomedude's Weather Edits For Weather Expansion:** My own edits to the sunshafts during sunsets and sunrise to make them more cinematic - REQUIRES WEATHER EXPANSION.    
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
    "Summer Cordon Sunset"
    "Late Fall Cordon Sunrise 1",
    "Late Fall Cordon Sunrise 2",
    "Late Fall Cordon Sunrise 3",
    "Late Fall Army Warehouses Sunrise 1",
    "Late Fall Army Warehouses Sunrise 2",
    "Late Fall Army Warehouses Sunrise 3",
    "Winter Wonderland",
    "Rookie Village Campfire",
    ""
]

xtrememodlist = {

"audio": """
+Re.Tune Anomaly Footsteps V4
+Re.Tune Exoskeletons and Nosorogs
+Re.Tune Bullet Cracks and Impacts
+Re.Tune Grenade SFX V2
+Re.Tune Ambience Sounds V3.1
+Dynamic Zoom Click Sound V1.3
+Voiced Actor Expanded 2.1 RU - PICK ONE
-Voiced Actor Expanded 2.1 EN - PICK ONE
+[ ISFX ] Improved Special Sound Effects
+[Haruka] Mags Redux Sounds
+Anomaly Radios Extended
+Stalker Anomaly Radio Revamp - РАДИО ОБНОВЛЕНИЕ
-XTREME Audio_separator
""",

"mags": """
+Mags_Redux_Models_Update_
+MrBs_Extra_Mags_for_MagsRedux
+[Shinesparkler] GAMMA Mags Redux Fixes 1.2.4
-XTREME Weapons_separator
""",

"heatvision": """
+HeatVision V1.3 [DLTX]
""",

"graphics": """
+ReShade 6.3.3 DX11
+XTREME Graphics Pack Optionals
+XTREME Graphics Pack
-XTREME Graphics_separator""",

"gameplay0": """
-XTREME Gameplay & HUD_separator
""",

"ammocheck1": """
+261- Ammo Check - Ishmaeel
""",

"hud1": """
+[relax_68] Improved Main Menu 1.0.0 ALPHA
+UI Rework G.A.M.M.A. Style - Sota
""",

"gameplay1": """
+Wrist Watch Key
+ReadWatch v1.0
-[HarukaSai] Quick Action Wheel (BUGGY)
+DynaHUD 1.19
+BHSRO G.A.M.M.A. 0.9.3 Patch
+BHSRO Old Surgical Kit Animation
+[Maka] THAP Rework 2.3 FIXED EXO ANIMS
+BHS Realistic Overhaul 0.87 BETA
+[relax_68] Improved Main Menu 1.0.0 ALPHA
+UI Rework G.A.M.M.A. Style - Sota
""",

"ammocheck2": """
+OneKey Weapon Controls
""",

"gameplay2": """
+Draggable Hud Editor
+Awesomedude's Consumables Uses Adjustments (OPTIONAL - VERY USEFUL)
+Disassembly Animation Freedom - Krebou
+NPC Close Combat Enhanced - RavenAscendant
+Proper Jam Chance - Literally Faust
+Quick Melee Reworked V1.6A
+[Utjan] Immersive Skinning
+[Utjan] PDA Hacking v1.2
+NPC Wounds And Treatment
+Mugging Squads 1.4 - TheMrDemonized
+[Haruka] Laser and Torch MCM Keybinding
+[ZoraZ] Sprint Cancel Aim and Lean Toggle
+[ITsPorky] Toggle Auto Run V1.0.2
""",

"optionals": """
+G.A.M.M.A. MCM values
+Advanced Stamina System (ASS) 1.10 - TheMrDemonized
+Toxic Rain 0.74
+[livvan] Stressful Zone 1.06.03
+Awesomedude's Cold System Adjustments (REQUIRES COLD SYSTEM)
+Cold System 0.6
-310- Tactical Fonts for Anomaly 4k - CryoManne
-309- Tactical Fonts for Anomaly 2k - CryoManne
-[AlphaLion] Reworked Status Icons 1.5 - Alt Color
-[AlphaLion] Reworked Status Icons 1.5 - Alt
+[AlphaLion] Reworked Status Icons 1.5 - Default
-XTREME OPTIONAL_separator""",

"disabled": """
-95- Doom-like weapon inspection - Grokitach
-94- Tacticool scopes - jaymorrow
-G.A.M.M.A. Disable WPO Overheat
-G.A.M.M.A. Wepl Hit Effects Rework
-G.A.M.M.A. Vices are free
-G.A.M.M.A. Soundtrack
-G.A.M.M.A. Short Psi Storms
-G.A.M.M.A. Reliable Animation Settings
-G.A.M.M.A. No Copyrighted Music
-G.A.M.M.A. MCM values - Rename to keep your personal changes
-394- Return Menu Music - Mirrowel
-311- NPC Stop Looting Dead Bodies - DTTheGunslinger
-365- Boomsticks and Sharpsticks 2022 Guns - Mitch & Team
-314- Retrogue's Additional Weapons - Retrogue
-245- Hideout Furniture 1.2.0 - Aoldri
-76- Boomsticks and Sharpsticks New (keep disabled) - Mich
-302- Minimalist companion UI moddb - Kageeskl
-271- G.A.M.M.A. Large Files - GAMMA Team
-203- YACS Better Campfire Saves (forces campfire saves but they are better) - Ishmaeel
-108- Remove dropping weapons from damage - Great_Day
-50- Disable Burnt Fuzz - _STYX_
-20- EFT footsteps and tinnitus 1.1 - Souvlakii
-2- Main Menu Theme - Deathcard Cabin - Grokitach
-18- Ambient Music Pack - Wojach
-17- Inventory open close sound - HollidayW
-16- Hit Effects - Wepl
-15- Voiced Actor - DesmanMetzger
-13- Quieter Wood Boxes Breaking - cringeybabey
-G.A.M.M.A. No harmonica
-G.A.M.M.A. Minimalist HUD
-XTREME Disabled_separator""",

"hud2": """
-282- GAMMA Loading Screens - CS Eden
-25- High Res Loading Screens - Bazingarrey
"""

}

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

    elif page == "**STALKER XTREME** Modlist Compatibility":
        
        st.write("This will edit your MO2 modlist file to disable the mods that should be disabled, while keeping the rest of your modlist intact.")
        st.write("Before you start, open MO2, click on your profile at the top (by default, it's **`G.A.M.M.A.`**) and click **`<Manage...>`**. Then, select your profile, and click **`Copy`**. After that, just enter a name (maybe **`XTREME`**) and hit **`OK`**.")
        st.write("Once that's done, upload your **`modlist.txt`** file - **located in your current profile's folder (`GAMMA/profiles/yourprofile/`)**.")
        st.write("Finally, download the converted file, drag it into your **`GAMMA/profiles/yourprofile/`** folder and replace the existing file when prompted.")
        st.write("If you have **XTREME Graphics Pack** installed, and you haven't renamed it to anything other than the default, it will be automatically placed under the **XTREME Graphics** separator. If any part of XGP is disabled and at the bottom of the modlist, you will have to move it back into position and re-enable it for it to work.")

        userfile = st.file_uploader("")
        
        if userfile != None:

            if userfile.name != "modlist.txt":
                st.subheader("This is not a valid modlist file. Please use a valid file.")

            else:

                strio = StringIO(userfile.getvalue().decode("utf-8"))
                userfile = strio.read()
                userout = userfile

                st.subheader("What parts of STALKER XTREME do you want to use?")

                if st.checkbox("Select All"):
                    selectall = True

                else:
                    selectall = False

                audio = st.checkbox("XTREME Audio", selectall)
                graphics = st.checkbox("XTREME Graphics", selectall)
                hud = st.checkbox("XTREME HUD", selectall)
                gameplay = st.checkbox("XTREME Gameplay", selectall)
                optionals = st.checkbox("XTREME Optionals", selectall)
                disabled = st.checkbox("Recommended Disabled GAMMA Mods", selectall)

                heatvision = st.checkbox("Heat Vision Optics", selectall)
                ammocheck = st.checkbox("Ammo Check", selectall)

                if ammocheck:
                    mags = st.checkbox("Mags Redux", selectall)
                else:
                    mags = False

                if audio:
                    userout = xtrememodlist["audio"] + userout

                if mags:
                    userout = xtrememodlist["mags"] + userout
                
                if heatvision:
                    userout = xtrememodlist["heatvision"] + userout

                if graphics:
                    userout = xtrememodlist["graphics"] + userout

                if gameplay or hud or ammocheck:
                    userout = xtrememodlist["gameplay0"] + userout

                if ammocheck:
                    userout = xtrememodlist["ammocheck1"] + userout

                if hud:
                    userout = xtrememodlist["hud1"] + userout

                if gameplay:
                    userout = xtrememodlist["gameplay1"] + userout

                if ammocheck:
                    userout = xtrememodlist["ammocheck2"] + userout

                if gameplay:
                    userout = xtrememodlist["gameplay2"] + userout

                if optionals:
                    userout = xtrememodlist["optionals"] + userout

                if disabled:
                    userout = xtrememodlist["disabled"] + userout

                if hud:
                    userout = xtrememodlist["hud2"] + userout

                download = st.download_button("Download Converted File", data=userout, file_name="modlist.txt")
