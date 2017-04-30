# -*- coding: utf-8 -*-
#------------------------------------------------------------

# https://www.youtube.com/user/teamkosuke
# https://www.youtube.com/user/promediatajdid1
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.MyZonKuliah'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')



YOUTUBE_CHANNEL_ID1 = "teamkosuke"
YOUTUBE_CHANNEL_ID2 = "promediatajdid1"
YOUTUBE_CHANNEL_ID3 = "UCaYgJKdiHVm_S-AoSV3QcIw"
YOUTUBE_CHANNEL_ID4 = "UCaYgJKdiHVm_S-AoSV3QcIw"
YOUTUBE_CHANNEL_ID5 = "thexfactoraustralia"
YOUTUBE_CHANNEL_ID6 = "BGXFactor"

# Entry point
def run():
    plugintools.log("myzonkuliah.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("myzonkuliah.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="[COLOR yellow]MYZon[/COLOR] [COLOR red]KULIAH (MIX)[/COLOR]",
		url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID1+"/",
        thumbnail=icon,
		fanart="https://s-media-cache-ak0.pinimg.com/originals/29/82/ed/2982ed4cd7b37ba92df10d4489c8d009.jpg",
		folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR yellow]MYPROmedia[/COLOR] [COLOR red]TAJDID (MIX)[/COLOR]",
		url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID2+"/",
        thumbnail="https://yt3.ggpht.com/-9Gz4W0AVpqg/AAAAAAAAAAI/AAAAAAAAAAA/ou6Kth2tjo8/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="https://s-media-cache-ak0.pinimg.com/originals/29/82/ed/2982ed4cd7b37ba92df10d4489c8d009.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR yellow]MYDigital[/COLOR] [COLOR red]ALQURAN (MIX)[/COLOR]",
		url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID3+"/",
        thumbnail="https://lh3.googleusercontent.com/-5PYn_Mawh6I/AAAAAAAAAAI/AAAAAAAAC4E/sCayz6Tlr7M/photo.jpg",
		fanart="https://s-media-cache-ak0.pinimg.com/originals/29/82/ed/2982ed4cd7b37ba92df10d4489c8d009.jpg",
        folder=True ) 
    
	
    
	
run()