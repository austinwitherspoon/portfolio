Title: How TimeWarp works in AAF Files
Date: 2024-02-19
Modified: 2024-02-19
Category: Programming
Tags: python, programming, aaf, avid, video-editing, opentimelineio
Slug: how-timewarp-works-in-aaf-files
Authors: Austin Witherspoon


<!-- PELICAN_END_SUMMARY -->


Notes:
PARAM_OFFSET_MAP_U
- Position mode
  - Primary field in this mode
- Speed mode
 - Filled in, but inert

PARAM_SPEED_MAP_U 
- Map of speed changes relative to start frame on element
- Appears when using avid time warp in speed AND position mode.
  - In position mode, single keyframe.

PARAM_SPEED_OFFSET_MAP_U
- Map of source/destination frames, including decimal frames? 
- Only in speed mode


interpolations:
Linear
Cubic
Bezier
Constant

Summary:
In Speed mode, you can reference the 