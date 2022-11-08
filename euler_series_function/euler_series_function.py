# Biophysics Project.
import numpy as np

# A Function for calculate derivative, using euler recurrent sequence

# Main formula: v_n+1 = v_n + total_time/step_number*(-v_n + I)


# for i in range(0, ):

def euler_series(I, initial_speed, total_time, step_number):

    delta_t = total_time/step_number
    all_step = np.zeros(step_number)
    all_step[0] = initial_speed

    for step in range(0, len(all_step)-1):
        all_step[step + 1] = all_step[step] + delta_t*(-all_step[step] + I)

    return all_step

