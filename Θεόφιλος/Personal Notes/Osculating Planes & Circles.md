For reading simplicity I will refer to a vector by making it bold:
- ${\bf r}=\vec{r}$ 
- $r=\Vert{} \vec{r} \Vert{}$
And the derivative in respect to $dt$ is going to be written as: 
- $\dot{{\bf r}} = d {\bf r} / dt$

Let a continuous parametric scalar vector function $\vec{r}(t)$:

$$\vec{r}(t)=r_x(t) \hat{i} + r_y(t) \hat{j} + r_z(t) \hat{k}$$
## Geometric
#### The Tangential Vector is:

$$ {\bf T}(s) = \frac{d {\bf r}}{ds}$$
> [!info] 
> The reason that ${\bf T}$ specifically is a Unit Vector is because we can deconstruct $d{\bf r}$ and $ds$ as infitesmally small vectors of $\Delta {\bf r}$ and $\Delta s$ respectively. And $\Delta {\bf r}$ is just a vector pointing from $s_1$ to $s_2$ and $\Delta s$ is just the distance from $s_1$ to $s_2$. Meaning that at the infitesmally small scale, they are equal in magnitude, so we get a Unit Vector.

> [!warning] 
> Remember that $s$ is the Arc-length. The Actual distance travelled on top of the curvilinear path.


#### The Normal Vector is:
$$\mathbf{N}(s) = \frac{\frac{d\mathbf{T}}{ds}}{\left\Vert{} \frac{d\mathbf{T}}{ds} \right\Vert{}} = \frac{1}{\kappa} \frac{d\mathbf{T}}{ds}$$

The variable $\kappa$ is the curvature of our curvilinear path, we can also say that it is the magnitude of the direction of change in the point Tangent. We can find it like so:
$$\kappa = \left\Vert{} \frac{d\mathbf{T}}{ds} \right\Vert{} $$

Though $\kappa$ is inversely proportional to the radius of curvature:
$$\kappa = \frac{1}{\rho} \iff \rho = \frac{1}{\kappa}$$

> Can be proved by taking a circle of radius $R$ parameterized by arc length $s$.

The variable $\rho$ is the radius of the osculating circle at that point. Meaning at tight turns the circle gets really tight, but at shallower turns the variable becomes higher.

#### The Binormal Vector is:
$${\bf B}(s) = {\bf T}(s) \times {\bf N}(s)$$
This vector is orthogonal to both ${\bf T}(s)$ and ${\bf N}(s)$, which is the result of a cross product.

### Derivatives:
#### Of the Tangent Vector:
$$ \frac{d{\bf T}}{ds} = \kappa {\bf N}$$
The rate of change in direction is proportional to the curvature and orthogonal to ${\bf T}$.

#### Of the Normal Vector:
$$ \frac{d{\bf N}}{ds} = -\kappa \mathbf{T} + \tau \mathbf{B}$$
> Can be proved by ...

#### Of the Binormal Vector:
$$ \frac{d{\bf B}}{ds} = - \tau \mathbf{N}$$

## Kinematics
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

Now that we are working in respect to time, we can use a new formula to find $\kappa$:
$$\kappa = \frac{\left\Vert{} {\bf v} \times {\bf a} \right\Vert{}}{v^3}$$
> Can be proven by solving for $\kappa$ from this cross-product: ${\bf v} \times {\bf a}$

Also, now we can use a new formila to find $\tau$:
$$\tau(t) = \frac{(\mathbf{v} \times \mathbf{a}) \cdot \dddot{\mathbf{r}}} {\Vert{}\mathbf{v} \times \mathbf{a}\Vert{}^2}$$
