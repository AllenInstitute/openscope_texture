import numpy as np
import matplotlib.pyplot as plt
import os

change_flashes_min = 4
change_flashes_max = 12

def get_next_change(change_time_scale = 0.3, depth = 0):
    t = np.random.geometric(change_time_scale)
    #logging.debug("Change picked for flash: {}".format(t))
    if (change_flashes_min > t) or (t >= change_flashes_max):
        # pick a diff one
        return get_next_change(change_time_scale, depth + 1)
    else:
        return t, depth
    
if __name__ == "__main__":

    all_proposed_values = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3]
    plt.figure()
    ax1=plt.subplot(2, 1, 1)
    ax2=plt.subplot(2, 1, 2)

    for proposed_value in all_proposed_values:
        color = np.random.rand(3,)
        all_values = []
        all_depths = []
        total_count = 5000
        for i in range(5000):
            new_value, depth = get_next_change(proposed_value)
            all_values.append(new_value)
            all_depths.append(depth)

        plt.sca(ax1)
        # We first get the arrays behind the historgram 
        # and then plot them
        x = np.arange(0, 20, 1)
        y = np.histogram(all_values, bins=range(0, 20))[0]
        plt.plot(x[1:]+x[0:-1]/2, y/total_count, color=color, alpha=0.5, label="time scale: {}".format(proposed_value))

        plt.sca(ax2)
        x = np.arange(0, 20, 1)
        y = np.histogram(all_depths, bins=range(0, 20))[0]
        plt.plot(x[1:]+x[0:-1]/2, y/total_count, color=color, alpha=0.5)
        # plt.hist(all_depths, bins=range(0, 20), color=color, alpha=0.5)
        
    plt.sca(ax1)
    plt.xlabel("Time to next change (flashes)") 
    plt.ylabel("Probability")
    plt.legend()
    plt.sca(ax2)
    plt.xlabel("Nb of attempts to get a valid change time")
    plt.ylabel("Probability")    
    local_script_path = os.path.dirname(os.path.realpath(__file__))
    plt.savefig(os.path.join(local_script_path, "change_time_distribution.png"))

    plt.show()
