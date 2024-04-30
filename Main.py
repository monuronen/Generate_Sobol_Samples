from generate_sobol_samples import generate_sobol_samples

# what are the group titles of the decision variables in glm3.nml file (must be a list and order is important!)
params_section = ['mixing', 'mixing', 'mixing', 'mixing', 'mixing', 'mixing']
# what are the names of the decision variables in glm3.nml file (must be a list and order is important!)
params_name = ['coef_mix_KH', 'coef_mix_hyp', 'coef_mix_conv', 'coef_mix_turb', 'coef_wind_stir', 'coef_mix_shear']
# In glm3.nml file some of the parameters may have multiple values (i.e. light_extc = 1.0, 0.5, 2.0, 4.0  ! Comma-separated list of light extinction coefficients for each waveband)
# So, what are the indexes of the decision variables in glm3.nml file (must be a list and order is important!)
params_id = [0, 0, 0, 0, 0, 0]
bounds = [[0.18, 0.36], [0.4, 0.6], [0.14, 0.24], [0.408, 0.612], [0.184, 0.276], [0.2, 0.4]]
num_samples = 64

result_df = generate_sobol_samples(params_section, params_name, params_id, bounds, num_samples)
