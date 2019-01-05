"""
Since it takes a while to find the right header lines in MKL,
this script copies just the ones we need into a new file called 'mkl_funcs.py'.
"""

def get_lines(fn): return [o.strip() for o in open(fn).readlines()]

fns = 'sm cblas vml ipps rng rngi'.split()
#fns = 'sm cblas vml ipps'.split()
sm_lines,cblas_lines,vml_lines,ipp_lines,rng_lines,rngi_lines = map(
#sm_lines,cblas_lines,vml_lines,ipp_lines = map(
    get_lines, [f'all_{o}.h' for o in fns])

f = open('mkl_funcs.py', 'w')
print('### AUTO-GENERATED BY get_headers.py ###\n', file=f)
for o in fns: print(f'{o}_lines={get_lines("all_"+o+".h")}', file=f)

