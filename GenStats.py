from GenerateImage import GenerateImage
from RateImage import rate_image

generate = GenerateImage()
stats = open("stats.txt", "a")

for i in range(100):
    generate.set_random()
    values = generate.param_get()

    percentage = rate_image(values)

    stats.write("\n")

    for j in values:
        stats.write(" " + str(j) + " ")

    stats.write(" " + str(percentage))

    print(i)
