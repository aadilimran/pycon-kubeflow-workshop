import kfp
from kfp.v2.dsl import component, Output, Input, Artifact

@component(base_image='python:3.8')
def b_square_minus_4ac(a: int, b: int, c: int) -> str:
    import cmath
    discriminant = b**2 - 4*a*c
    result = cmath.sqrt(discriminant)
    return str(result)

@component(base_image='python:3.8')
def minus_b_plus_minus_squared(b: int, square_root: str, roots: Output[Artifact]):
    import cmath
    data = complex(square_root)
    results = ((-1 * b) + data, (-1 * b) - data)
    with open(roots.path, 'w') as f:
        f.write(','.join(map(str, results)))

@component(base_image='python:3.8')
def divide_by_2a(a: int, roots: Input[Artifact], final_roots: Output[Artifact]):
    with open(roots.path, 'r') as f:
        root_strs = f.read().split(',')
        root1, root2 = complex(root_strs[0]), complex(root_strs[1])
    results = (root1 / (2 * a), root2 / (2 * a))
    with open(final_roots.path, 'w') as f:
        f.write(','.join(map(str, results)))

@component(base_image='python:3.8')
def print_results(roots: Input[Artifact]):
    with open(roots.path, 'r') as f:
        print(f"The roots are: {f.read()}")

@kfp.dsl.pipeline(
    name="Quadratic Equation v2",
    description="Solving quadratic equation using Kubeflow with complex number support."
)
def quadratic_eq_pipeline(a: int = 1, b: int = 2, c: int = 1):
    square_root = b_square_minus_4ac(a=a, b=b, c=c)
    roots = minus_b_plus_minus_squared(b=b, square_root=square_root.output)
    final_roots = divide_by_2a(a=a, roots=roots.output)
    print_results(roots=final_roots.output)
