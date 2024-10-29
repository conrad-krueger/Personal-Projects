import random
import math

def modular_inverse(a, m):
    # Extended Euclidean Algorithm to find the modular inverse
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def exists_perfect_square(r_a, B, r_c):

    # Check if A is coprime with B
    gcd = math.gcd(r_a, B)
    if r_c % gcd != 0:
        return False, None  # No solutions possible

    # Reduce A, B, C
    r_a //= gcd
    B //= gcd
    r_c //= gcd

    # Find modular inverse of A mod B
    inv_A = modular_inverse(r_a, B)

    # Calculate z as C * inv_A mod B
    z = (r_c * inv_A) % B

    # Now check if z is a perfect square
    z_value = (z * r_a) // gcd
    if int(z_value**0.5) ** 2 == z_value:  # Check if z_value is a perfect square
        return True, z_value
    
    return False, None  # No perfect square found

def opt(a,b,c):
  r_a = a%b
  r_c = c%b

  tf,val = exists_perfect_square(r_a,b,r_c)

  if not tf:
    return False

  if c - val*a/b <= 0:
    return False
  
  return True
