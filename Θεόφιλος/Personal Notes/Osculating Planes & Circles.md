For reading simplicity I will refer to a vector by making it bold:
- ${\bf r}=\vec{r}$ 
- $r=\Vert{} \vec{r} \Vert{}$
And the derivative in respect to $dt$ is going to be written as: 
- $\dot{{\bf r}} = d {\bf r} / dt$

Let a continuous parametric scalar vector function $\vec{r}(t)$:

$$\vec{r}(t)=r_x(t) \hat{i} + r_y(t) \hat{j} + r_z(t) \hat{k}$$
## Geometric
___
___
#### The Tangential Unit Vector is:
Definition:

$$ {\bf T}(s) = \frac{d {\bf r}}{ds}$$
> [!info] 
> The reason that ${\bf T}$ specifically is a Unit Vector is because we can deconstruct $d{\bf r}$ and $ds$ as infitesmally small vectors of $\Delta {\bf r}$ and $\Delta s$ respectively. And $\Delta {\bf r}$ is just a vector pointing from $s_1$ to $s_2$ and $\Delta s$ is just the distance from $s_1$ to $s_2$. Meaning that at the infitesmally small scale, they are equal in magnitude, so we get a Unit Vector.

> [!warning] 
> Remember that $s$ is the Arc-length. The Actual distance travelled on top of the curvilinear path.


#### The Principal Normal Unit Vector is:
The definition and then the result:
$$\mathbf{N}(s) = \frac{\frac{d\mathbf{T}}{ds}}{\left\Vert{} \frac{d\mathbf{T}}{ds} \right\Vert{}} = \frac{1}{\kappa} \frac{d\mathbf{T}}{ds}$$

The variable $\kappa$ is the curvature of our curvilinear path. 


The variable $\rho$ is the radius of the osculating circle at that point. Meaning at tight turns the circle gets really tight, but at shallower turns the variable becomes higher.

#### The Binormal Unit Vector is:
Definition:
$${\bf B}(s) = {\bf T}(s) \times {\bf N}(s)$$
This vector is orthogonal to both ${\bf T}(s)$ and ${\bf N}(s)$, which is the result of a cross product.

### Variables:
___
#### The variable $\kappa$ of curvature:
We can also say that it is the magnitude of the direction of change in the point Tangent. We can find it like so:
$$\kappa = \left\Vert{} \frac{d\mathbf{T}}{ds} \right\Vert{} $$

Though $\kappa$ is inversely proportional to the radius of curvature:
$$\kappa = \frac{1}{\rho} \iff \rho = \frac{1}{\kappa}$$

> [!info]- Can be proved by taking a circle of radius $R$ parameterized by arc length $s$.

#### The variable $\tau$ of torsion:
Torsion is the rate at which the direction of the Binormal Unit Vector changes. We can define it as so:
$$\left\Vert{} \frac{d\mathbf{B}}{ds} \right\Vert{} = \tau$$

Which we can also derive the above formula by taking the derivative of the Unit Vector: $\mathbf{B}$ and just take the magnitude of both sides. 

### Derivatives:
___
#### Of the Tangent Vector:
$$ \frac{d{\bf T}}{ds} = \kappa {\bf N}$$
The rate of change in direction is proportional to the curvature and orthogonal to ${\bf T}$.
> [!info]- Can be proved by the definition of the Principal Normal Unit Vector.
> $$\mathbf{N}(s) = \frac{1}{\kappa} \frac{d\mathbf{T}}{ds} \iff \kappa \, \mathbf{N}(s) = \frac{d\mathbf{T}}{ds} $$

#### Of the Binormal Vector:
$$ \frac{d{\bf B}}{ds} = - \tau \mathbf{N}$$
> [!info]- Can be proved by a vector property and an assumption.
> A property for Unit Vectors is that their derivatives are always perpendicular to themselves:
> $$ \mathbf{A} \cdot \frac{d \mathbf{A}}{ds} = 0 $$
> So in turn we create this equation, to see if the result of $\frac{d \mathbf{B}}{ds}$ is along $\mathbf{T}$:
> $$\mathbf{B} \cdot \mathbf{T} = 0 \implies \frac{d}{ds}(\mathbf{B} \cdot \mathbf{T}) = \frac{d\mathbf{B}}{ds} \cdot \mathbf{T} + \mathbf{B} \cdot \frac{d\mathbf{T}}{ds} = 0$$
> Substituting:
> $$\frac{d\mathbf{B}}{ds} \cdot \mathbf{T} + \mathbf{B} \cdot (\kappa \mathbf{N}) = 0 \implies \frac{d\mathbf{B}}{ds} \cdot \mathbf{T} = 0$$
> So we now know that $\frac{d\mathbf{B}}{ds}$ is perpendicular to $\mathbf{T}$ meaning that the result is along the the Principal Normal Unit Vector $\mathbf{N}$. 
> Though $\mathbf{N}$ is a unit vector, we can name a "new" variable $\tau$ that represents torsion as the scalar.
> $$\frac{d\mathbf{B}}{ds} = -\tau \mathbf{N}$$
> As a convention we use the sign '$-$' before $\tau$.

#### Of the Normal Vector:
$$ \frac{d{\bf N}}{ds} = -\kappa \mathbf{T} + \tau \mathbf{B}$$
> [!info]- Can be proved by this cross product: $\mathbf{N} = \mathbf{B} \times \mathbf{T}$ and the previous proof.
> $$\frac{d\mathbf{N}}{ds} = \frac{d\left(\mathbf{B}\times\mathbf{T}\right)}{ds} = \left(\frac{d\mathbf{B}}{ds} \times \mathbf{T}\right) + \left(\mathbf{B} \times \frac{d\mathbf{T}}{ds}\right)$$
> Substituting for what we found previously, and applying the property from the corss products we get:
> $$\frac{d\mathbf{N}}{ds} = (-\tau \mathbf{N} \times \mathbf{T}) + (\mathbf{B} \times \kappa \mathbf{N}) = -\tau(-\mathbf{B}) + \kappa(-\mathbf{T}) = -\kappa \mathbf{T} + \tau \mathbf{B}$$
> > [!warning] Recall that the cross product is not commutative. 
> > You can test that out by using your left hand as the axis and applying the right hand rule to these axis.

## Kinematics
___
___
Before we continue, because we are working with time, we can define speed and accelaration. Previously we traversed the path in equal distances. But now we traverse the path in equal amount of time, meaning that we can accelarate, stop etc.

- ${\bf v}(t) = \dot{{\bf r}}(t)$
- ${\bf a}(t) = \dot{{\bf v}}(t) = \dot{\dot{{\bf r}}}(t)$

#### We can write out the Tangential Vector by saying:
$${\bf T} = \hat{{\bf u}}_t = \frac{{\bf v}}{v} $$

> [!info]- Can be proven easily with the chain rule:
> $${\bf T} = \frac{d {\bf r}}{ds} = \frac{d {\bf r}}{dt} \frac{dt}{ds} = \dot{{\bf r}} \frac{1}{v} = \frac{{\bf v}}{v}$$

#### We can write out the Normal Vector as follows:
$${\bf N} = \hat{{\bf u}}_n = \frac{\dot{{\bf T}}}{\dot{T}}$$

> [!info]- Can be proven easily with the chain rule:
> $${\bf N} = \frac{1}{\kappa} \frac{d\mathbf{T}}{ds} = \frac{1}{\kappa} \frac{d {\bf T}}{dt} \frac{dt}{ds} = \frac{\dot{{\bf T}}}{\kappa v} \implies \kappa v \, N = \dot{T} \implies {\bf N} = \frac{\dot{{\bf T}}}{\dot{T}}$$

#### The $\kappa$ variable of curvature:

Now that we are working in respect to time, we can use a new formula to find $\kappa$:
$$\kappa = \frac{\left\Vert{} {\bf v} \times {\bf a} \right\Vert{}}{v^3}$$
> [!info]- Can be proven by solving for $\kappa$ from this cross-product: ${\bf v} \times {\bf a}$

#### The $\tau$ variable of torsion:

Also, now we can use a new formila to find $\tau$:
$$\tau(t) = \frac{(\mathbf{v} \times \mathbf{a}) \cdot \dddot{\mathbf{r}}} {\Vert{}\mathbf{v} \times \mathbf{a}\Vert{}^2}$$

### Derivatives:
#### Of the Tangent Vector:
$$ \dot{{\bf T}} = \kappa v \, {\bf N}$$
The rate of change in direction is proportional to the curvature and orthogonal to ${\bf T}$.
> [!info]- Can be proved by the derivative Normal Unit Vector in respect to arc-length and the chain rule.
> $$\mathbf{N}(s) = \frac{1}{\kappa} \frac{d\mathbf{T}}{ds} \implies \kappa \, \mathbf{N}(t) = \frac{d\mathbf{T}}{dt} \frac{dt}{ds} \implies  \dot{{\bf T}} = \kappa v \, {\bf N} $$

#### Of the Binormal Vector:
$$ \dot{{\bf B}} = - v \tau \, \mathbf{N}$$
> [!info]- Can be proved by the derivative of the Binormal Unit Vector in respect to arc-length and the chain rule.
> $$-\tau \mathbf{N} = \frac{d\mathbf{B}}{ds} \implies -\tau \mathbf{N} =  \frac{d\mathbf{B}}{dt}\frac{dt}{ds} \iff  \dot{{\bf B}} = - v \tau \, \mathbf{N}$$


#### Of the Normal Vector:
$$ \dot{{\bf N}} =  v\left(\tau \mathbf{B} -\kappa \mathbf{T}\right)$$
> [!info]- Can be proved by the derivative of the Principal Normal Unit Vector in respect to arc-length and the chain rule.
> $$ -\kappa \mathbf{T} + \tau \mathbf{B} = \frac{d{\bf N}}{ds} \implies -\kappa \mathbf{T} + \tau \mathbf{B} = \frac{d{\bf N}}{dt}\frac{dt}{ds} \iff \dot{{\bf N}} =  v\left(\tau \mathbf{B} -\kappa \mathbf{T}\right)$$

### Expressing Accelaration: