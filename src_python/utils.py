from enum import Enum
import numpy as np

class HomographyType(Enum):
    UNKNOWUN = -1
    NORMAL = 0
    CONCAVE = 1
    TWIST = 2
    REFLECTION = 3

    def __str__(self) -> str:
        return str(self.name)

def classifyHomography(pts1: np.ndarray, pts2: np.ndarray) -> int:
    if len(pts1) != 4 or len(pts2) != 4: 
        return HomographyType.UNKNOWUN
    
    original_corners = np.cross((pts1 - np.roll(pts1, -1, axis=0)), pts1 - np.roll(pts1, 1, axis=0))
    
    check_corners = np.cross((pts2 - np.roll(pts2, -1, axis=0)), pts2 - np.roll(pts2, 1, axis=0))
    
    J = original_corners * check_corners
    negative_J = (J<0).sum()
    if negative_J == 4:
        return HomographyType.REFLECTION
    elif negative_J == 2:
        return HomographyType.TWIST
    elif negative_J in [1,3]:
        return HomographyType.CONCAVE
    return HomographyType.NORMAL

def polyArea(points):
    n = len(points) #점의 개수
    a = 0.0
    for i in range(n):
        j = (i+1) % n
        a += points[i][0] * points[j][1] - points[j][0] * points[i][1]
       
    area = abs(a) / 2.0
    return area
