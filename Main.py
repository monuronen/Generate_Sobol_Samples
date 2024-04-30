from generate_sobol_samples import generate_sobol_samples

# what are the group titles of the decision variables in glm3.nml file (must be a list and order is important!)
params_section = ['mixing','mixing','mixing','mixing','mixing','mixing','light','meteorology','meteorology','meteorology']
# what are the names of the decision variables in glm3.nml file (must be a list and order is important!)
params_name = ['coef_mix_KH','coef_mix_hyp','coef_mix_conv','coef_mix_turb','coef_wind_stir','coef_mix_shear','Kw','ce','ch','cd']
# In glm3.nml file some of the parameters may have multiple values (i.e. light_extc = 1.0, 0.5, 2.0, 4.0  ! Comma-separated list of light extinction coefficients for each waveband)
# So, what are the indexes of the decision variables in glm3.nml file (must be a list and order is important!)
params_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bounds = [[0.15,0.45],[0.25,0.75],[0.1,0.3],[0.25,0.77],[0.11,0.35],[0.15,0.45],[0.2,0.9],[0.0007,0.0017],[0.0007,0.0020],[0.0006, 0.0034]]
num_samples = 32

result_df = generate_sobol_samples(params_section, params_name, params_id, bounds, num_samples)
