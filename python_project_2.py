import math

# Öklid Mesafesi Hesaplama Fonksiyonu
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Noktaları Kullanıcıdan Alma Fonksiyonu
def getPoints():
    points = []
    num_points = int(input("Kaç tane nokta gireceksiniz? "))
    for i in range(num_points):
        x = float(input(f"{i+1}. noktanın x koordinatını girin: "))
        y = float(input(f"{i+1}. noktanın y koordinatını girin: "))
        points.append((x, y))
    return points

# Ana Program
points = getPoints()

# Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)
        print(f"Mesafe {points[i]} ile {points[j]} arasında: {distance}")

# Minimum Mesafenin Bulunması
if distances:
    min_distance = min(distances)
    print(f"Minimum mesafe: {min_distance}")
else:
    print("Yeterli nokta girilmedi.")
