import numpy as np

def norm_vec(p1, p2):
  h =  np.cross(p1, p2)
  return h/np.linalg.norm(h)

def get_theta(h1, h2):
  return np.arccos(np.dot(h1,h2) / (np.linalg.norm(h1)*np.linalg.norm(h2)))

def rotation_matrix(vec1, vec2):

  #회전축 = h1, h2에 모두 수직인 단위벡터
  u = norm_vec(vec1, vec2)
  u /= np.linalg.norm(u)
  theta = get_theta(vec1, vec2)
  
  cos = np.cos(theta)
  sin = np.sin(theta)

  ux, uy, uz = u

  R =  np.array([(cos+(ux**2)*(1-cos), ux*uy*(1-cos)-uz*sin, ux*uz*(1-cos)+uy*sin),
                    (uy*ux*(1-cos) + uz*sin, cos+(uy**2)*(1-cos), uy*uz*(1-cos)-ux*sin),
                    (uz*ux*(1-cos)-uy*sin, uz*uy*(1-cos)+ux*sin, cos+(uz**2)*(1-cos))])
  return R

def get_target(vec, original, target, R1, R2=None):

  original_vec = vec - original 
  rotation = R2 @ R1 @ original_vec if R2 is not None else R1 @ original_vec

  return rotation + target



### 실행
original = np.array([(-0.500000,	0.000000,	2.121320),
                (0.500000,	0.000000,	2.121320),
                (0.500000,	-0.707107,	2.828427)
])
                
target = np.array([
    (1.363005,	-0.427130,	2.339082),
    (1.748084,	0.437983,	2.017688),
    (2.636461,	0.184843,	2.400710)
])

original_h = np.cross((original[1]-original[0]),(original[2]-original[0]))
target_h = np.cross((target[1]-target[0]), (target[2]-target[0]))

R1 = rotation_matrix(original_h,target_h)

R1_original = R1@(original[2]-original[0])
target13 = target[2]-target[0]

R2 = rotation_matrix(R1_original, target13)

p4o = np.array(
    (0.500000,	0.707107,	2.828427)
)

p4t = np.array(
    (1.498100,	0.871000,	2.883700)
)

p4o_r = get_target(p4o, original[0], target[0],R1, R2)
print(p4o_r)
#소수점 다섯번째자리에서 반올림하면 같음

p5o = np.array(
    (1.000000,	1.000000,	1.000000)
)

p5t = get_target(p5o, original[0], target[0],R1, R2)
print(p5t)