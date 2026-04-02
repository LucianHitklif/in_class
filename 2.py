def is_valid_triangle(s1, s2, s3):
    return (s1+s2>s3) and (s2+s3>s1) and (s1+s3>s2)
print(is_valid_triangle(2,2,2))
print(is_valid_triangle(2,3,10))
print(is_valid_triangle(3,4,5))
