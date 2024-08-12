"""
Stimulus to run passively viewing of images for an OpenScope project
"""

from psychopy import visual
import psychopy.visual
import camstim
from camstim import Stimulus, NaturalScenes, SweepStim, Foraging, Window, Warp, MovieStim
import os
import yaml
import numpy as np
from psychopy import monitors
import argparse
import logging


if __name__ == "__main__":
    parser = argparse.ArgumentParser("mtrain")
    parser.add_argument("json_path", nargs="?", type=str, default="")

    args, _ = parser.parse_known_args() # <- this ensures that we ignore other arguments that might be needed by camstim
    
    # print args
    if args.json_path == "":
        logging.warning("No json path provided, using default parameters. THIS IS NOT THE EXPECTED BEHAVIOR FOR PRODUCTION RUNS")
        json_params = {}
    else:
        with open(args.json_path, 'r') as f:
            # we use the yaml package here because the json package loads as unicode, which prevents using the keys as parameters later
            json_params = yaml.load(f)
            logging.info("Loaded json parameters from mtrain")
            # end of mtrain part

    # Copied monitor and window setup from:
    # https://github.com/AllenInstitute/openscope-glo-stim/blob/main/test-scripts/cohort-1-test-12min-drifting.py

    dist = 15.0
    wid = 52.0

    # mtrain should be providing : a path to a network folder or a local folder with the entire repo pulled
    SESSION_PARAMS_images_folder = json_params.get('images_folder', os.path.abspath(os.path.join("data", "passive")))
    
    # mtrain should be providing : Gamma1.Luminance50
    monitor_name = json_params.get('monitor_name', "testMonitor")
    
    # mtrain should be providing : Gamma1.Luminance50
    image_repeat = json_params.get('monitor_name', 1)
    
    # create a monitor
    if monitor_name == 'testMonitor':
        monitor = monitors.Monitor(monitor_name, distance=dist, width=wid)
    else:
        monitor = monitor_name

    # Create display window
    window = Window(fullscr=True, # Will return an error due to default size. Ignore.
                    monitor=monitor,  # Will be set to a gamma calibrated profile by MPE
                    screen=0,
                    warp=Warp.Spherical
                    )

    stimulus = NaturalScenes(image_path_list=SESSION_PARAMS_images_folder,
                            window=window,
                            sweep_length=0.25,
                            start_time=0.0,
                            stop_time=None,
                            blank_length=0.0,
                            blank_sweeps=100,
                            runs=image_repeat,
                            shuffle=True,)

    ss = SweepStim(window,
                pre_blank_sec=10.0,
                post_blank_sec=10.0)
    
    ss.add_stimulus(stimulus)

    ss.run()