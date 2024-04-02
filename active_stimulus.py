###############################################################################
# Change Detection with different samples of each texture
# @author: justink, jeromel
# Apr 2, 2024
###############################################################################

import argparse
import yaml
from six import iteritems
from camstim.change import DoCTask, DoCTrialGenerator
from camstim import Window, Warp
import logging

# Configure logging level
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def load_params():
    parser = argparse.ArgumentParser()
    parser.add_argument("json_path", nargs="?", type=str, default="")

    args, _ = parser.parse_known_args() # <- this ensures that we ignore other arguments that might be needed by camstim
    print(args)
    with open(args.json_path, 'r') as f:
        # we use the yaml package here because the json package loads as unicode, which prevents using the keys as parameters later
        params = yaml.load(f)
    return params

def load_stimulus_class(class_name):

    if class_name=='grating':
        from camstim.change import DoCGratingStimulus as DoCStimulus
    elif class_name=='images':
        from camstim.change import DoCImageStimulus as DoCStimulus
    else:
        raise Exception('no idea what Stimulus class to use for `{}`'.format(class_name))

    return DoCStimulus

def set_stimulus_groups(groups, stimulus_object):
    for group_name, group_params in iteritems(groups):
        for param, values in iteritems(group_params):
            stimulus_object.add_stimulus_group(group_name, param, values)

json_params = load_params()
stimulus = json_params['stimulus']

# Set up display window (This may become unnecessary in future release)
window = Window(fullscr=True, screen=1, monitor='Gamma1.Luminance50', warp=Warp.Spherical)

# Set up Task
params = {}
f = DoCTask(window=window,
            auto_update=True,
            params=params)
t = DoCTrialGenerator(cfg=f.params) # This also subject to change
f.set_trial_generator(t)

# Set up our DoC stimulus
DoCStimulus = load_stimulus_class(stimulus['class'])
stimulus_object = DoCStimulus(window, **stimulus['params'])

if stimulus['class']=='images':
    # This is what should allow many samples of each texture to be shown.
    stimulus_object.tweak_on_flash = True

if "groups" in stimulus:
    set_stimulus_groups(stimulus['groups'],stimulus_object)

# Add our DoC stimulus to the Task
f.set_stimulus(stimulus_object, stimulus['class'])

# Run it
f.start()