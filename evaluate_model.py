from modeller import *
from modeller.scripts import complete_pdb

log.verbose()    # request verbose output
env = Environ()
env.libs.topology.read(file='$(LIB)/top_heav.lib') # read topology
env.libs.parameters.read(file='$(LIB)/par.lib') # read parameters

# read model file
# mdl1 = complete_pdb(env, 'Q99ZW2.B99990001.pdb')
# mdl2 = complete_pdb(env, 'Q99ZW2.B99990002.pdb')
# mdl3 = complete_pdb(env, 'Q99ZW2.B99990003.pdb')
# mdl4 = complete_pdb(env, 'Q99ZW2_M.B99990001.pdb')
# mdl5 = complete_pdb(env, 'Q99ZW2_M.B99990002.pdb')
# mdl6 = complete_pdb(env, 'Q99ZW2_M.B99990003.pdb')

temp1 = complete_pdb(env, 'Q99ZW2.B99990003.pdb')
temp2 = complete_pdb(env, 'Q99ZW2_M.B99990002.pdb')
temp3 = complete_pdb(env, '4cmp_fit.pdb')
temp4 = complete_pdb(env, '6ifo_fit.pdb')
temp5 = complete_pdb(env, '7s37_fit.pdb')

# tem1 = complete_pdb(env, 'P11413.B99990003.pdb')
# tem2 = complete_pdb(env, 'P11413M.B99990002.pdb')
# tem3 = complete_pdb(env, '4cmp_fit.pdb')
# tem4 = complete_pdb(env, '_fit.pdb')
# tem5 = complete_pdb(env, '7snf_fit.pdb')
# tem6 = complete_pdb(env, '7sni_fit.pdb')

# Assess all atoms with DOPE:
# s1 = Selection(mdl1)
# s1.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='dope_shope_Q99ZW2_1.profile',
#               normalize_profile=True, smoothing_window=15)
# s2 = Selection(mdl2)
# s2.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='dope_shope_Q99ZW2_2.profile',
#               normalize_profile=True, smoothing_window=15)
# s3 = Selection(mdl3)
# s3.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='dope_shope_Q99ZW2_3.profile',
#               normalize_profile=True, smoothing_window=15)
# s4 = Selection(mdl4)
# s4.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='dope_shope_Q99ZW2_M_1.profile',
#               normalize_profile=True, smoothing_window=15)
# s5 = Selection(mdl5)
# s5.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='dope_shope_Q99ZW2_M_2.profile',
#               normalize_profile=True, smoothing_window=15)
# s6 = Selection(mdl6)
# s6.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='dope_shope_Q99ZW2_M_3.profile',
#               normalize_profile=True, smoothing_window=15)

s1 = Selection(temp1)
s1.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='dope_shope_Q99ZW2.profile',
              normalize_profile=True, smoothing_window=15)
s2 = Selection(temp2)
s2.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='dope_shope_Q99ZW2_M.profile',
              normalize_profile=True, smoothing_window=15)
s3 = Selection(temp3)
s3.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='dope_shope_4CMP.profile',
              normalize_profile=True, smoothing_window=15)
s4 = Selection(temp4)
s4.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='dope_shope_6IFO.profile',
              normalize_profile=True, smoothing_window=15)
s5 = Selection(temp5)
s5.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='dope_shope_7S37.profile',
              normalize_profile=True, smoothing_window=15)
# s6 = Selection(tem6)
# s6.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='dope_shope_7SNI.profile',
#               normalize_profile=True, smoothing_window=15)

