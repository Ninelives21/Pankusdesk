#!/usr/bin/env python3
"""Independent symbolic checks of the newly imported calculus working.
Requires SymPy locally; the static site has no Python/SymPy runtime dependency.
These identities check algebra, not the accuracy/completeness of a source transcription.
"""
import sympy as s
x,y,z,t,a,b,c,r,h,theta,phi=s.symbols('x y z t a b c r h theta phi', positive=True)
checks=[]
def check(name,value,expected=0):
    assert s.simplify(s.trigsimp(value-expected))==0,(name,value,expected)
    checks.append(name)
def series(name,f,expected,n):check(name,s.series(f,x,0,n).removeO(),expected)
def E(f):return x*s.diff(f,x)+y*s.diff(f,y)
def lap(f):return sum(s.diff(f,v,2)for v in (x,y,z))
check('4.14 sine/exponential stationary point',s.diff(s.exp(-x)*s.sin(x),x).subs(x,s.pi/4))
f=(x-a)**3*(x-b)**4;check('4.14 polynomial-product formula',s.diff(f,x).subs(x,(3*b+4*a)/7))
f=x*(x-1)*(x-2);check('4.15 interior derivative',s.diff(f,x).subs(x,1-s.sqrt(21)/6),s.Rational(3,4))
check('4.16 inverse-tangent derivative',s.diff(s.atan(x),x),1/(1+x*x))
check('4.17 logarithm derivative',s.diff(s.log(1+x),x),1/(1+x))
check('4.18 Cauchy ratio',(s.exp(b)-s.exp(a))/(s.exp(-b)-s.exp(-a)),-s.exp(a+b))
check('4.19 cosine derivative cycle',s.diff(s.cos(x),x,4),s.cos(x))
check('4.20 logarithm third derivative',s.diff(s.log(1+x),x,3),2/(1+x)**3)
series('4.21 tan series',s.tan(x),x+x**3/3+2*x**5/15,6)
series('4.22 exp(sin x)',s.exp(s.sin(x)),1+x+x*x/2-x**4/8,5)
series('4.23 log(1+sin² x)',s.log(1+s.sin(x)**2),x*x-5*x**4/6+32*x**6/45,8)
f=s.exp(a*s.asin(x));check('4.24 differential equation',(1-x*x)*s.diff(f,x,2)-x*s.diff(f,x)-a*a*f)
assert abs(float(s.log(s.Rational(11,10)))-.0953)<.00005;checks.append('4.25 four-place rounding')
check('4.26 arctangent cubic derivative',s.diff(s.atan(x),x,3),2*(3*x*x-1)/(1+x*x)**3)
series('4.27 exp(atan x)',s.exp(s.atan(x)),1+x+x*x/2-x**3/6-7*x**4/24,5)
check('4.28(i) limit',s.limit((x*s.exp(x)-s.log(1+x))/x**2,x,0),s.Rational(3,2))
check('4.28(ii) limit',s.limit((x**x-x)/(x-1-s.log(x)),x,1),2)
check('4.29 coefficient choice',s.limit((x*(120+60*s.cos(x))-180*s.sin(x))/x**5,x,0),1)
check('4.30 logarithm/cotangent',s.limit(s.log(x)/s.cot(x),x,0,dir='+'))
check('4.31 third-order quotient',s.limit((s.exp(x)*s.sin(x)-x-x*x)/(x*x+x*s.log(1-x)),x,0),-s.Rational(2,3))
check('4.32 exponential power limit',s.limit(((1+x)**(1/x)-s.E)/x,x,0),-s.E/2)
check('4.33 tangent/log product',s.limit(s.tan(x)*s.log(x),x,0,dir='+'))
check('4.34 reciprocal sine difference',s.limit(1/s.sin(x)-1/x,x,0))
f=x**3+y**3-3*a*x*y;check('5.1 mixed partial',s.diff(f,x,y),-3*a)
f=x*x*s.atan(y/x)-y*y*s.atan(x/y);check('5.2 mixed derivative',s.diff(f,x,y),(x*x-y*y)/(x*x+y*y));check('5.2 mixed orders',s.diff(s.diff(f,x),y),s.diff(s.diff(f,y),x))
F=s.Function('F');G=s.Function('G');f=F(x+c*t)+G(x-c*t);check('5.3 wave equation',s.diff(f,t,2)-c*c*s.diff(f,x,2))
f=t**(-s.Rational(3,2))*s.exp(-r*r/(4*t));check('5.4 / 5.14 heat equation',s.diff(r*r*s.diff(f,r),r)/r**2-s.diff(f,t))
f=1/s.sqrt(x*x+y*y+z*z);check('5.5 harmonic inverse radius',lap(f))
f=s.log(x**3+y**3+z**3-3*x*y*z);df=sum(s.diff(f,v)for v in (x,y,z));check('5.6 repeated sum derivative',sum(s.diff(df,v)for v in (x,y,z)),-9/(x+y+z)**2)
u=s.symbols('u');v=x*x/(a*a+u)**2+y*y/(b*b+u)**2+z*z/(c*c+u)**2;partials=[2*x/((a*a+u)*v),2*y/((b*b+u)*v),2*z/((c*c+u)*v)];constraint=x*x/(a*a+u)+y*y/(b*b+u)+z*z/(c*c+u)-1
check('5.7 constrained identity',sum(q*q for q in partials)-2*sum(q*w for q,w in zip(partials,(x,y,z))),-4*constraint/v)
check('5.8 third mixed derivative',s.diff(x**y,x,x,y),x**(y-2)*(y*(y-1)*s.log(x)+2*y-1))
f=F(s.sqrt(x*x+y*y));rad=s.symbols('rad',positive=True);target=s.diff(F(rad),rad,2)+s.diff(F(rad),rad)/rad;check('5.9 radial Laplacian',s.diff(f,x,2)+s.diff(f,y,2),target.subs(rad,s.sqrt(x*x+y*y)))
# Implicit differentiation of x log x + y log y + z log z = constant.
zx=-(1+s.log(x))/(1+s.log(z));zy=-(1+s.log(y))/(1+s.log(z));zxy=s.diff(zx,z)*zy
check('5.10 implicit mixed at x=y=z',zxy.subs({y:x,z:x}),-1/(x*(1+s.log(x))))
f=(x**3+y**3)/(3*x+4*y);check('5.11 logarithmic homogeneous quotient',E(f),2*f)
f=(x+2*y+3*z)/(x**8+y**8+z**8);check('5.12 degree minus seven',sum(w*s.diff(f,w)for w in(x,y,z)),-7*f)
f=(x+y)**s.Rational(7,2);check('5.13 second Euler expression',E(E(f))-E(f),s.Rational(7,2)*s.Rational(5,2)*f)
f=(x+y)/(s.sqrt(x)+s.sqrt(y));check('5.15 homogeneous inner function',E(f),f/2)
f=(x**3+y**3)/(x-y);check('5.16 atan Euler inner degree',E(f),2*f)
f=s.sin(s.exp(t)/t**2);check('5.17 total derivative',s.diff(f,t),s.exp(t)*(t-2)*s.cos(s.exp(t)/t**2)/t**3)
f=2*x*y-3*x*x*y;check('5.18 zero rate',s.diff(f,x).subs({x:3,y:1})*2+s.diff(f,y).subs({x:3,y:1})*(-s.Rational(32,21)))
f=x*s.log(x*y);yp=-(x*x+y)/(y*y+x);check('5.19 constrained derivative',s.diff(f,x)+s.diff(f,y)*yp,1+s.log(x*y)-x*(x*x+y)/(y*(y*y+x)))
check('5.20 square-root identity',1-(3*t-4*t**3)**2,(1-t*t)*(1-4*t*t)**2)
for val,sign in [(s.Rational(1,4),1),(s.Rational(3,4),-1)]:check('5.20 principal arcsine branch '+str(val),s.diff(s.asin(3*t-4*t**3),t).subs(t,val),sign*3/s.sqrt(1-val*val))
fx,fy,gy,gz=s.symbols('fx fy gy gz',nonzero=True);check('5.21 composed implicit derivatives',fy*gz*(-fx/fy)*(-gy/gz),fx*gy)
f=F(x-y,y-z,z-x);check('5.22 sum of partials',sum(s.diff(f,w)for w in(x,y,z)))
u,v,dx,dy=s.symbols('u v dx dy',real=True);xx=s.exp(u)*s.cos(v);yy=s.exp(u)*s.sin(v);du=xx*dx+yy*dy;dv=-yy*dx+xx*dy
check('5.23 / 5.27 coordinate identity',xx*dv+yy*du,s.exp(2*u)*dy);check('5.23 gradient norm',du**2+dv**2,s.exp(2*u)*(dx*dx+dy*dy))
f=F(x,y);yp=-s.diff(f,x)/s.diff(f,y);check('5.24 implicit second derivative',s.diff(yp,x)+s.diff(yp,y)*yp,-(s.diff(f,x,2)*s.diff(f,y)**2-2*s.diff(f,x,y)*s.diff(f,x)*s.diff(f,y)+s.diff(f,y,2)*s.diff(f,x)**2)/s.diff(f,y)**3)
# Polar second-derivative identity via the inverse coordinate differential operators.
rr,tt=s.symbols('rr tt',positive=True);U=s.Function('U')(rr,tt)
def DX(f):return s.cos(tt)*s.diff(f,rr)-s.sin(tt)*s.diff(f,tt)/rr
def DY(f):return s.sin(tt)*s.diff(f,rr)+s.cos(tt)*s.diff(f,tt)/rr
check('5.25 / 5.26 polar Laplacian',DX(DX(U))+DY(DY(U)),s.diff(U,rr,2)+s.diff(U,rr)/rr+s.diff(U,tt,2)/rr**2)
f=F(x/y,y/z,z/x);check('5.28 degree-zero ratio composition',sum(w*s.diff(f,w)for w in(x,y,z)))
check('5.29(i) polar Jacobian',s.Matrix([r*s.cos(theta),r*s.sin(theta)]).jacobian([r,theta]).det(),r)
check('5.29(ii) cylindrical Jacobian',s.Matrix([r*s.cos(phi),r*s.sin(phi),z]).jacobian([r,phi,z]).det(),r)
check('5.29(iii) / 5.31 spherical Jacobian',s.Matrix([r*s.sin(theta)*s.cos(phi),r*s.sin(theta)*s.sin(phi),r*s.cos(theta)]).jacobian([r,theta,phi]).det(),r*r*s.sin(theta))
check('5.30 ratio Jacobian',s.Matrix([y*z/x,z*x/y,x*y/z]).jacobian([x,y,z]).det(),4)
check('5.32 inverse polar Jacobian',s.Matrix([[x/s.sqrt(x*x+y*y),y/s.sqrt(x*x+y*y)],[-y/(x*x+y*y),x/(x*x+y*y)]]).det(),1/s.sqrt(x*x+y*y))
check('5.33 relation',(x+y+z)**2-(x*x+y*y+z*z)-2*(x*y+y*z+z*x))
f=x*s.sqrt(1-y*y)+y*s.sqrt(1-x*x);g=s.asin(x)+s.asin(y);check('5.34 zero Jacobian',s.Matrix([f,g]).jacobian([x,y]).det())
for num,f,value,sign in [(46,x**4+y**4-2*x*x+4*x*y-2*y*y,-8,1),(48,2*(x-y)**2-x**4-y**4,8,-1)]:
 pt={x:s.sqrt(2),y:-s.sqrt(2)};check(f'5.{num} stationary x',s.diff(f,x).subs(pt));check(f'5.{num} stationary y',s.diff(f,y).subs(pt));check(f'5.{num} value',f.subs(pt),value);H=s.hessian(f,(x,y)).subs(pt);assert H.det()>0 and sign*H[0,0]>0
f=x**3*y*y*(1-x-y);pt={x:s.Rational(1,2),y:s.Rational(1,3)};check('5.47 stationary value',f.subs(pt),s.Rational(1,432));check('5.47 Hessian determinant',s.hessian(f,(x,y)).subs(pt).det(),s.Rational(1,144));check('5.47 x-axis stationary x',s.diff(f,x).subs(y,0));check('5.47 y-axis stationary y',s.diff(f,y).subs(x,0))
check('5.49 / 5.53 equal-edge sphere constraint',3*(r/s.sqrt(3))**2,r*r)
f=x*y+64/x+64/y;check('5.50 area gradient x',s.diff(f,x).subs({x:4,y:4}));check('5.50 area gradient y',s.diff(f,y).subs({x:4,y:4}));check('5.50 minimum area',f.subs({x:4,y:4}),48)
# Weighted product: derivative of its logarithm, subject to the sum constraint.
m,n,p=s.symbols('m n p',positive=True);sol={x:a*m/(m+n+p),y:a*n/(m+n+p),z:a*p/(m+n+p)}
check('5.51 weighted product stationary ratios',(m/x-n/y).subs(sol));check('5.51 weighted product constraint',(x+y+z).subs(sol),a)
check('5.52 near distance',s.sqrt(sum((q-2*q/13)**2 for q in (3,4,12))),11);check('5.52 far distance',s.sqrt(sum((q+2*q/13)**2 for q in (3,4,12))),15)
V=x*x*(y+h/3);S=4*x*y+x*s.sqrt(x*x+4*h*h);lam=s.symbols('lam');L=S+lam*(V-s.symbols('V0'));pt={x:s.sqrt(5)*h,y:h/2}
for w in (x,y,h):check('5.54 stationary '+str(w),s.diff(L,w).subs(lam,-4/x).subs(pt))
check('5.55 reciprocal constraint',a/(a+b+c)+b/(a+b+c)+c/(a+b+c),1)
check('5.56 / 5.58 ellipsoid constraint',(x*x/a**2+y*y/b**2+z*z/c**2).subs({x:a/s.sqrt(3),y:b/s.sqrt(3),z:c/s.sqrt(3)}),1)
l,m,n=s.symbols('l m n',real=True);u=s.symbols('u');M=s.diag(1/a**4-u/a**2,1/b**4-u/b**2,1/c**4-u/c**2);B=M.row_join(s.Matrix([l,m,n])).col_join(s.Matrix([[l,m,n,0]]));pol=l*l*a**4*(1-b*b*u)*(1-c*c*u)+m*m*b**4*(1-a*a*u)*(1-c*c*u)+n*n*c**4*(1-a*a*u)*(1-b*b*u)
check('5.57 polynomial retains singular cases',-B.det()*a**4*b**4*c**4,pol)
check('5.59 near squared distance',sum((q-w)**2 for q,w in zip((2,4,-2),(1,2,-1))),6);check('5.59 far squared distance',sum((q-w)**2 for q,w in zip((-2,-4,2),(1,2,-1))),54)
series('Notebook inverse sine / root',s.asin(x)/s.sqrt(1-x*x),x+2*x**3/3,5)
check('Notebook denominator y² has limit zero bound',s.limit(x*y*y/(x*x+y*y),x,0),0)
check('Notebook denominator y⁴ path x=y²',s.cancel((x*y*y/(x*x+y**4)).subs(x,y*y)),s.Rational(1,2))
print(f'IMPORTED CALCULUS: PASS — {len(checks)} independent symbolic/numerical checks')
