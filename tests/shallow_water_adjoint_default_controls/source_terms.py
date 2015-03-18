# This file was *autogenerated* from the file source_terms.sage.
from sage.all_cmdline import *   # import sage library
_sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0)
t = var('t')
h = var('h')
g = var('g')
H = var('H')

# --------------------------------------------------

u = (t+_sage_const_1 )*h*sin(_sage_const_2 *pi*x)
eta = (t+_sage_const_1 )*h*cos(_sage_const_2 *pi*x)

u_src = diff(u, t) + g*diff(eta, x)
eta_src = diff(eta, t) + diff(H*u, x)

print "u: ", u
print "eta: ", eta

print "u_src: ", u_src
print "eta_src: ", eta_src

J = integrate((eta.subs(t=_sage_const_1 ))**_sage_const_2 , x, _sage_const_0 , _sage_const_1 )
print "J(t=1): ", J.subs(h=_sage_const_1 )
print "diff(J(t=1), h).subs(h=1): ", diff(J, h).subs(h=_sage_const_1 )
J = integrate((eta.subs(t=_sage_const_0 ))**_sage_const_2 , x, _sage_const_0 , _sage_const_1 )
print "J(t=0): ", J.subs(h=_sage_const_1 )
print "diff(J(t=0), h).subs(h=1): ", diff(J, h).subs(h=_sage_const_1 )